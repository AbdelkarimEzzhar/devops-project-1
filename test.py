import unittest 
from app import greet
class TestApp (unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("EZZHAR"),"Hello EZZHAR!, welcome to our first small project in devops")
        self.assertEqual(greet(),"Hello world!, welcome to our first small project in devops")
if __name__=="__main__":
    unittest.main()
