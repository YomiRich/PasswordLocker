import unittest
from user import User #importing the User class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours

    Args:
        unnitest.TestCase:TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_user=User("Mueni","nomnom")

    def test_init(self):
        '''
        test init test case to test if the obj is initialized correctly
        '''
        self.assertEqual(self.new_user.name,"Mueni")
        self.assertEqual(self.new_user.password,"nomnom")
        
        