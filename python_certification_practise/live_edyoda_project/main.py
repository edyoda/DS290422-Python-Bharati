from admin_panel import *

class Main:
    def __init__(self,admin):
        self.admin = admin

    def execute(self,choice):
        
        if choice == 1:
            print("******************Admin Login******************")
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            flag = self.admin.admin_login(username,password)
            if flag:
                print("Logged In Successfully!")
                while True : 

                    choice = int(input("Enter \n1.Add Module \n2.Add Trainer \n3.Add Students \n4.Add Batch \n5.View Modules \n6.View Trainer \n7.View Students \n8.View Batch \n9.Remove Module \n10.Edit Trainer Profile \n"))

                    if choice == 1:
                        print("Add Module".center(50, '*'))
                        module_name = input("Enter the module name : ")
                        duration = input("Enter the duration required for this module : ")
                        flag = self.admin.add_module(module_name,duration)
                        if flag:
                            print("Module Successfully Added!!!")
                        else:
                            print("Something went wrong!!!")

                    elif choice == 2:
                        print("Add Trainer".center(50, '*'))
                        name = input("Enter trainer name : ")
                        gender = input("Enter trainer gender : ")
                        qualification = input("Enter trainer qualification : ")
                        experience = input("Enter trainer experience : ")
                        mobile_no = input("Enter trainer mobile_no : ")
                        email_ID = input("Enter trainer email_ID : ")
                        password = input("Enter trainer password : ")
                        flag = self.admin.add_trainer(name,gender,qualification,experience,mobile_no,email_ID,password)
                        if flag:
                            print("Trainer Successfully Added!!!")
                        else:
                            print("Something went wrong!!!")

                    elif choice == 3:
                        print("Add Students".center(50, '*'))
                        flag = self.admin.add_student()
                        if flag:
                            print("Students Successfully Added!!!")
                        else:
                            print("Something went wrong!!!")

                    elif choice == 4:
                        print("Add Batch".center(50, '*'))
                        module_key = input("Enter module code : ")
                        trainer_key = input("Enter trainer code : ")
                        student_key = input("Enter student code : ")
                        flag = self.admin.add_batch(module_key,trainer_key,student_key)
                        if flag:
                            print("Batch Successfully Added!!!")
                        else:
                            print("Something went wrong!!!")

                    elif choice == 5:
                        module = self.admin.get_module()
                        print(module)

                    elif choice == 6:
                        trainer = self.admin.get_trainer()
                        
                    elif choice == 7:
                        student = self.admin.get_student()

                    elif choice == 8:
                        batch = self.admin.get_batch()
                        print(batch)

                    elif choice == 9:
                        self.admin.remove_module()

                    elif choice == 10:
                        self.admin.edit_trainer()

            else:
                print("Invalid Credentials!!!")
        elif choice == 2:
            print("******************Trainer Login******************")
        elif choice == 3:
            print("******************Student Login******************")
        

if __name__ == "__main__":
    admin = Admin_Panel()
    main = Main(admin)

    while True:
        choice = int(input("Login as : \n1.Admin Login \n2.Trainer Login \n3.Student Login \n"))
        main.execute(choice=choice)