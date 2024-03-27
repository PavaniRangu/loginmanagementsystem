class login_management_system:
    def __init__(self):
        self.mydict={}
    def register(self,name,email,password,rollno):
        if rollno in self.mydict:
            print("Username already exists please choose a different username")
        else:
            self.mydict['rollno']={'name':name,'email':email,'password':password}
            print("You have successfully registered")
#class Login(login_management_system):
    def login(self,email,password):
        for rollno,details in self.mydict.items():
            if details['email']==email and details['password']==password:
                print("your login is successfull")
            else:
                print("you need to register in order to login")
                return
#        print("Invalid login")
#class details(Login):
    def display_details(self,rollno):
#      rollno=int(input("enter the roll number for which the details need to be displayed"))
        if rollno in self.mydict:
            print("name is ",self.mydict[rollno]['name'])
            print("rollno is",rollno)
            print("email is ",self.mydict[rollno]['email'])
        else:
            print("rollnumber not found")
class interfacee:
    def __init__(self):
        self.s1=login_management_system()
        self.loggedin_user=None
    def register(self):
        name=input("enter the name")
        rollno=input("enter the roll number")
        email=input("enter the email")
        password=input("enter the password")
        self.s1.register(name,email,password,rollno)
    def login(self):
        if self.loggedin_user:
            print("Already logged in ")
            return
        email=input("enter the email")
        password=input("enter the password")

        if self.s1.login(email,password):
            self.loggedin_user=email

    def display_details(self):
        if self.loggedin_user:
            self.s1.display_details(self.loggedin_user)
        else:
            print("Please login first.")
    
    def logout(self):
        if self.loggedin_user:
            print("Logging out", self.loggedin_user)
            self.loggedin_user = None
        else:
            print("Not logged in.")

obj=interfacee()
obj.register()
obj.login()
obj.display_details()
obj.logout()


