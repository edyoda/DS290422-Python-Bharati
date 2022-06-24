import random
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
        # trainer_data = {
        #     "name" : name,
        #     "gender" : gender,
        #     "qualification" : qualification,
        #     "experience" : experience,
        #     "mobile_no" : mobile_no,
        #     "email_ID" : email_ID,
        #     "password" : password
        # }
        trainer_data = Trainer(name,gender,qualification,experience,mobile_no,email_ID,password)
        self.trainer_details[key] = trainer_data
        if self.trainer_details[key]:
            return True
        return False

    def add_student(self):
        key = random.randint(1,100)
        student_size = int(input("Enter the number of students you want to add : "))
        for i in range(student_size):
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
        
        self.student_details[key] = Admin_Panel.student_list
        if self.student_details[key]:
            return True
        return False

    def add_batch(self,module_key,trainer_key,student_key):
        key = random.randint(1,100)
        batch_data = {
            module_key : module_key,
            trainer_key : trainer_key,
            student_key : student_key
        }
        self.batch_details[key] = batch_data
        if self.batch_details[key]:
            return True
        return False

    def get_module(self):
        return self.module_details

    def get_trainer(self):
        return self.trainer_details

    def get_student(self):
        return self.student_details