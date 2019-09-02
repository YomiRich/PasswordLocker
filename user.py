

class User:

    '''
    Class that generates a new instance of a passlocker user
    
    __init__method that helps us to define properties for our objects

    Args:
        name:New user name
        password:New user password
    '''
    user_list=[]

    def __init__(self,name,password):
        
        self.name=name
        self.password=password

    def save_user(self):
        '''
        save user method that saves user obj into user list
        '''
        User.user_list.append(self)  

    @classmethod
    def display_users(cls):
        '''
        Method that returns users using the password locker app
        '''
        return cls.user_list

    @classmethod
    def user_verified(cls,name,password):
        '''
        Method that takes a user login info  & returns a boolean true if the details are correct

        Args:
            name:User name to search
            password:password to match

        Return:
            Boolean true if they both match to a user & false if it doesn't    
        '''
        for user in cls.user_list:
            if user.name==name and user.password==password:
                return True
        return False
    
            





