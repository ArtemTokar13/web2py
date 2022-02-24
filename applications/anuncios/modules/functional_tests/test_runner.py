# -*- coding: utf-8 -*-

'''
Created on 23 sept. 2020

@author: nico

Ejecución:
    
    python web2py.py --no-banner -S h3o -R applications/h3o/private/run_functional_tests.py
'''

import unittest
import os
from os.path import join as pjoin, isdir, splitext
from gluon import current, DAL
from gluon.tools import Auth
from gluon.contrib.appconfig import AppConfig
from .mock_db_data import MockDbData, define_views
from db_conn import define_auth, define_all_tables, configure_mail_settings
from perm_manage import Perm
from constants import BRANDING_ID_FEDE



EN_LANG_ID = 1

def test_environment_setup(migrate_enabled=False):
    """ Esta función se llamará desde db.py para configurar las variables globales
    con los valores para ejecutar los tests.
    
    No debe llamarse a esta función en la propia ejecución de los tests. 
    """
    current.TESTING = True
    current.PYA_ambimetricsDEV = False
    current.BD_REMOTA_POR_TUNEL_DESDE_DEV = False
    current.use_tunel_to_PYA_ambimetricsFEDE = False
    current.USAR_BD = 'sqlite'
    current.LAZY_TABLES = True
    current.EXTRA_LAZY_TABLES = False
    current.MIGRATE_ENABLED = False
    current.FAKE_MIGRATE_ALL= False
    
    cfg_file = pjoin(current.request.folder, 'modules', 'functional_tests', 'appconfig_for_tests.ini')
    current.app_config = AppConfig(configfile=cfg_file)
    current.force_decimal_separator = False
    current.IS_POST = False
    current.session.user_is_betaTester = True
    current.session.Lang_id = EN_LANG_ID

    current.use_beta_db = True      # ha de ser True para que en sitios como la API no se intente conectar con la bd beta
    
#     current.db = db = DAL('sqlite:memory',
#                           #check_reserved=['postgres', 'postgres_nonreserved'],
#                           lazy_tables=True,
#                           migrate_enabled=migrate_enabled)
    test_db_path = pjoin(current.request.folder, 'test_db')
    current.db = db = DAL('sqlite://test_db.sqlite',
                          folder=test_db_path,
                          lazy_tables=True,
                          migrate_enabled=migrate_enabled)
    
    current.auth = define_auth(db, TESTING=True) 
    current.auth.settings.create_user_groups = False
    #current.auth.settings.everybody_group_id = False
    current.oPerm = Perm()
    current.request.branding_id = BRANDING_ID_FEDE
    current.session.branding_id = BRANDING_ID_FEDE 
    
    
    define_all_tables(db, 
                      MIGRATE_PREFIX='dev_functional_testing_',
                      auth=current.auth,
                      upload_folder_name='uploads_testing',
                      extra_lazy=False)

    


def run_tests(recreate_database=False):
    #test_environment_setup()
    test_db_path = pjoin(current.request.folder, 'test_db')
    uploads_testing_path = pjoin(current.request.folder, 'uploads_testing')
    
    if not isdir(test_db_path):
        os.mkdir(test_db_path)
    
    if recreate_database:
        files_to_delete = {'sql.log', 'test_db.sqlite', '.table'}
        for fname in os.listdir(test_db_path):
            k = fname
            if 'dev_functional_testing' in fname and splitext(fname)[1] == '.table':
                k = '.table'
            if k in files_to_delete:
                os.remove(pjoin(test_db_path, fname))
        for root, dirnames, fnames in os.walk(uploads_testing_path, topdown=False):
            for fname in fnames:
                os.remove(pjoin(root, fname))
            for dirname in dirnames:
                os.rmdir(pjoin(root, dirname)) 
        
    current.db = db = DAL('sqlite://test_db.sqlite',
             folder=test_db_path,
             lazy_tables=True,
             migrate_enabled=False)
    
    
    current.auth = Auth(current.db)
    
    define_all_tables(current.db, 
                      MIGRATE_PREFIX='dev_functional_testing_',
                      auth=current.auth,
                      upload_folder_name='uploads_testing',
                      extra_lazy=False)

    try:
        db_is_empty = db(db.auth_user.id>0).isempty()
    except:
        db_is_empty = True
         
    if db_is_empty:
        current.db = db = DAL('sqlite://test_db.sqlite',
             folder=test_db_path,
             lazy_tables=True,
             migrate_enabled=True)
    
    
        current.auth = Auth(current.db)
        
        define_all_tables(current.db, 
                          MIGRATE_PREFIX='dev_functional_testing_',
                          auth=current.auth,
                          upload_folder_name='uploads_testing',
                          extra_lazy=False)
        define_views(db)
        current.oMock_db_data = MockDbData(db) 
        current.oMock_db_data.fill_test_data()
    
#     suite = unittest.TestLoader().loadTestsFromModule(save_work_session)

    from .h3o_api import (save_work_session, cloud_check, check_sw_version, 
                          download_plots, download_sprayer_list, download_scg_list,
                          finish_ns_work_order, save_factory_data, 
                          change_work_session_state, register_user,
                          expert_alert)

    suite = unittest.TestSuite()

    for m in [save_work_session, cloud_check, check_sw_version, download_plots,
              download_sprayer_list, download_scg_list, 
              finish_ns_work_order, save_factory_data, 
              change_work_session_state, register_user,
              expert_alert]:

        suite.addTest(unittest.TestLoader().loadTestsFromModule(m))
     
#    """ --- Pruebas individuales --- """ 
# 
#     suite = unittest.TestSuite()
#     def add_t(name, mod):
#         suite.addTest(unittest.defaultTestLoader.loadTestsFromName(name, mod))
#                   
#                   
#     add_t('Test_cloud_check_v2.test_cloud_check_bad_pwd', cloud_check)
#     add_t('Test_api_save_work_session', save_work_session)
#     add_t('Test_api_save_work_session_api_v2', save_work_session)
#     add_t('Test_api_save_work_session_api_v1', save_work_session)
#     add_t('Test_api_save_work_session.test_without_workorder', save_work_session)
#     add_t('Test_api_save_work_session.test_scg_traceability', save_work_session)
#     add_t('Test_api_save_work_session.test_insert_treatment_equipment', save_work_session)
#     add_t('Test_api_save_work_session.test_treatment_equipment_search', save_work_session)
#     add_t('Test_api_save_work_session_api_v1.test_scg_traceability', save_work_session)
# 
#     add_t('Test_api_start_work_session.test_without_workorder', save_work_session)
#     add_t('Test_api_start_work_session.test_insert_treatment_equipment', save_work_session)
#     add_t('Test_api_start_work_session_api_v2.test_without_workorder', save_work_session)
#     add_t('Test_api_save_work_session_data', save_work_session)
#     add_t('Test_api_finish_work_session', save_work_session)
#       
#     add_t('Test_api_chk_sw_version', check_sw_version)
#     add_t('Test_api_change_work_session_state.test_change_work_session_state', change_work_session_state)
#     add_t('Test_api_download_scg_list', download_scg_list)
#     add_t('Test_api_download_sprayer_list', download_sprayer_list)
#     add_t('Test_api_finish_ns_work_order.test_finish_ns_work_order', finish_ns_work_order)
#     add_t('Test_api_finish_ns_work_order.test_finish_ns_work_order_fail_auth', finish_ns_work_order)
#     add_t('Test_api_register_user.test_register_user', register_user)
#     add_t('Test_api_save_factory_data.test_save_factory_data_update_currentUsageHours', save_factory_data)
#     add_t('Test_api_save_work_session.test_save_work_session_with_finished_work_order', save_work_session)
#     add_t('Test_api_save_work_session.test_save_work_session_with_work_order', save_work_session)
#     add_t('Test_api_save_work_session.test_without_workorder', save_work_session_fail_events1)       
#     
#     add_t('Test_expert_alert_subscription', expert_alert)
#     add_t('Test_expert_alert_subscription_v4', expert_alert)
    
            
#    """ --- Fin pruebas individuales --- """


    unittest.TextTestRunner(verbosity=1).run(suite)

    