from datetime import datetime


class User(object):
    '''holds user data'''
        
    user_details = {'derrick':["1234", 'admin'], 'obola': ["123", 'norm_user'], 'leslie':["123", 'moderator'], 'henry':["123", 'norm_user']}

    comments = []

    def __init__(self, username, password, role='norm_user'):
        '''initializes user class'''
        self.username = username
        self.password = password
        self.role = role

    def add_comment(self, username):
        comment = input("enter comment: ")
        comment_time = datetime.now().strftime("%d- %H:%M")
        comment_author = username

        comment_details = {username: [comment, comment_time]}

        User.comments.append(comment_details)

        print(comment_details)

        return comment_details

class Admin(User):
    '''holds admin functions:d'''
    
    def delete_comments(self):
        '''deletes any comment'''
        pass

    def edit_comments(self):
        '''edits any comment'''
        pass
        
    

def login():
    username = input("Input username: ")
    password = input("Input password: ")
    u_name = User.user_details[username]
    if password == u_name[0] and u_name[1] == 'norm_user':
        print('logged in as normal user')
        norm_user = User(username, password)
        norm_user.add_comment(username)
    
    elif u_name[0] == password and u_name[1] == 'moderator':
        print('logged in as moderator')
        mod_user = Moderator()

    elif u_name[0] == password and u_name[1] == 'admin':
        print('logged in as admin')
        admin_user = Admin()
    else:
        print('wrong username or password')


login()
