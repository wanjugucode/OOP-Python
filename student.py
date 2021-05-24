class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age):
        self.first_name= first_name
        self.last_name=last_name
        self.age=age
    def great(self):
        return f"Hello {self.first_name}welcome to {self.school}"
    def year_of_birth(self):
        return f"Hello you were born in{2021-self.age}"

    def initials(self):
        return f"Hello {self.first_name} {self.last_name} your initials are {self.first_name[0]}{self.last_name[0]} "
