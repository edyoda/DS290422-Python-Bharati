class Trainer:
    def __init__(self,name,gender,qualification,experience,mobile_no,email_ID,password):
        self.name = name
        self.gender = gender
        self.qualification = qualification
        self.experience = experience
        self.mobile_no = mobile_no
        self.email_ID = email_ID
        self.password = password

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self,gender):
        self.gender = gender
    
    def get_qualification(self):
        return self.qualification

    def set_qualification(self,qualification):
        self.qualification = qualification

    def get_experience(self):
        return self.experience

    def set_experience(self,experience):
        self.experience = experience

    def __str__(self):
        return f"Name : {self.name} \nGender : {self.gender} \nQualification : {self.qualification} \nExperience : {self.experience} \nMobile No: {self.mobile_no} \nEmail ID : {self.email_ID}"
        
    