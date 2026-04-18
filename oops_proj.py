class chatbook:
    def __init__(self):
        self.user_name=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
         
         user_input=input("""Welcome to Chatbook! How would like to procced 
                        1.Press 1 to signup
                        2.Press 2 to signin
                        3.Press 3 to write a post
                        4. Press 4 to write a message to friend 
                        5.Press any key tto end""")
         user_input = int(input("Enter choice: "))

         if user_input ==1:
             self.signup()
         elif user_input ==2:
             self.signin()
         elif user_input ==3:
             self.my_Post()
         elif user_input ==4:
             self.send_message()
         else:
             exit()




    def signup(self):
        email =input("Enter the email")
        password=input("eneter the password ")
        self.user_name=email
        self.password=password
        print("you have signed up suceesfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.user_name=="" and self.password=="":
            print("First signup by pasin the in the main menu ")
        else:
            uname=input("eneter the username")
            pwd=input("eneter the password")

            if self.user_name==uname and self.password==pwd:
                print("you have signed i sucessfully ")
                self.loggedin= True
            else:
                print("enter true username and password ")   

    def my_Post(self):
        if self.loggedin==True:
            txt=input("enter the message -->") 
            print("Following content has been posted ")
        else:
            print("YOu need to sign in first ")    
            print("/n")
            self.menu()

    def send_message(self):
        if self.loggedin==True:
            txt=input("Enter the message ")
            frnd=input("for who ur sending the message ")
            print(f"YOur message has been sent to{frnd}")
        else:
            print("YOu need to sign in first ")    
            print("/n")
            self.menu()    

obj=chatbook()

       







