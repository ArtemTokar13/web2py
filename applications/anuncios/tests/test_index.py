import unittest
from applications.anuncios.controllers.default import index

from gluon.globals import Request

#execfile("applications/anuncios/controllers/default.py", globals())

db(db.anuncio.id>0).delete()  # Clear the database
db.commit()

class TestDB(unittest.TestCase):
#    def setUp(self):
#        request = Request()  # Use a clean Request object

    def testDB(self):
        # Set variables for the test function
        request.post_vars["anuncio.id"] = 1
        request.post_vars["title"] = "abracadabra"

        resp = index()
        db.commit()
        self.assertEquals(0, len(resp["anuncio"]))

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDB))
unittest.TextTestRunner(verbosity=2).run(suite)
