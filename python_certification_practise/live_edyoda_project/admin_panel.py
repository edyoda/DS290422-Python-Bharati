import random
from wsgiref import validate
from student import *
from trainer import *


class Admin_Panel:
    student_list = []
    def __init__(self):
        self.module_details = {}
        self.trainer_details = {}
        self.student_details = {}
        self.batch_details = {}
        
    def admin_login(self,username,password):
        if username == "admin" and password == "admin":
            return True
        return False

    def add_module(self,module_name,duration):
        topic_list = []
        key = random.randint(1,100)

        topic_size = int(input("Enter the number of topics you want to add : "))
        for i in range(topic_size):
            topic =  input("Enter topic name : ")
            topic_list.append(topic)

        module_data = {
            "module_name" : module_name,
            "duration" : duration,
            "topics" : topic_list
        }
        self.module_details[key] = module_data
        if self.module_details[key]:
            return True
        return False

    def add_trainer(self,name,gender,qualification,experience,mobile_no,email_ID,password):
        key = random.randint(1,100)
        trainer_ID = random.randint(1,100)
        self.trainer_data = Trainer(trainer_ID,name,gender,qualification,experience,mobile_no,email_ID,password)
        self.trainer_details[key] = self.trainer_data
        if self.trainer_details[key]:
            return True
        return False

    def add_student(self):
        key = random.randint(1,100)
        student_size = int(input("Enter the number of students you want to add : "))
        for i in range(1,student_size+1):
            print(f"\n Enter the details for student {i} : \n")
            name = input("Enter student name : ")
            gender = input("Enter student gender : ")
            age = input("Enter student age : ")
            qualification = input("Enter student qualification : ")
            experience = input("Enter student experience : ")
            mobile_no = input("Enter student mobile_no : ")
            email_ID = input("Enter student email_ID : ")
            password = input("Enter student password : ")
            student = Student(i,name,gender,age,qualification,experience,mobile_no,email_ID,password)
            Admin_Panel.student_list.append(student)
            print()
        
        self.student_details[key] = Admin_Panel.student_list
        print(self.student_details)
        if self.student_details[key]:
            return True
        return False

    def add_batch(self,module_key,trainer_key,student_key):
        key = random.randint(1,100)
        batch_data = {
            "module_key" : module_key,
            "trainer_key" : trainer_key,
            "student_key" : student_key
        }
        self.batch_details[key] = batch_data
        if self.batch_details[key]:
            return True
        return False

    def get_module(self):
        return self.module_details

    def get_trainer(self):
        count = 0
        for k,v in self.trainer_details.items():
            count += 1
            print(f"Trainer {count} Details :\n")
            print(k," ",v,"\n")
        
    def get_student(self):
        count = 0
        for k,v in self.student_details.items():
            for i in v:
                count += 1
                print(f"Student {count} Details :\n")
                print(i,"\n")

    def get_batch(self):
        return self.batch_details
        
    def remove_module(self):
        for k,v in self.module_details.items():
            print(k,"----->",v,"\n")

        module_code = int(input("Enter the module code you want to delete : "))
        self.module_details.pop(module_code)
        print("Successfully deleted module!!! \n")

        for k,v in self.module_details.items():
            print(k,"----->",v,"\n")

    def edit_trainer(self):
        for k,v in self.trainer_details.items():
            print(v.get_ID(),"----->",v,"\n")

        trainer_code = int(input("Enter the trainer code you want to edit : "))

        for k,v in self.trainer_details.items():
            if v.get_ID() == trainer_code:
            
                name = input("Enter trainer name : ")
                gender = input("Enter trainer gender : ")
                qualification = input("Enter trainer qualification : ")
                experience = input("Enter trainer experience : ")
                mobile_no = input("Enter trainer mobile_no : ")
                email_ID = input("Enter trainer email_ID : ")
                
                v.set_name(name)
                v.set_gender(gender)
                v.set_qualification(qualification)
                v.set_experience(experience)
                v.set_mobile_no(mobile_no)
                v.set_email_ID(email_ID)
                
        print("Trainer Data Successfully Updated!!! \n")

        for k,v in self.trainer_details.items():
            print(v.get_ID(),"----->",v,"\n")




            

        
