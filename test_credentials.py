import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours

    Arg:
        unittest.TestCase:Test case class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        setUp method to run before each test case
        '''

        #create a credential obj
        self.new_credential=Credential("Cool","Yes","Win","Winwin")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        Credential.credential_list=[]


    def test_init(self):
        '''
        test init test case to test if the obj is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Cool")
        self.assertEqual(self.new_credential.user_password,"Yes") 
        self.assertEqual(self.new_credential.credential_name,"Win")
        self.assertEqual(self.new_credential.credential_password,"Winwin")


def test_save_credential(self):
        '''
        test_save_credential to test if the credential obj is saved into the credential list
        '''

        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)


    def test_save_multiple_credential(self):
        '''
        tesr save multiple credential to test if we can save multiple credentials to the credential list
        '''

        self.new_credential.save_credential()
        test_credential=Credential("Master","Soul","Winner","Maggie")

        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2) 
        
    def test_delete_credential(self):
        '''
        delete credential to test if we can remove a credential from the credential list
        '''
        self.new_credential.save_credential()

        test_credential=Credential("Cup","Green","Pinterest","1234")  
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

def test_display_credential(self):
        '''
        display credential that returns a list of a users credentials
        '''

        self.new_credential.save_credential()

        test_credential=Credential("Queen","Bee","Ig","Queen")
        test_credential.save_credential()

        test_credential=test_credential=Credential("Queen","Bee","Ig","Queen")
        test_credential.save_credential()

        self.assertEqual(len(Credential.display_credential("Queen","Bee")),2)
        
