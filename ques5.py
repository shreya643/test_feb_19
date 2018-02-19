'''5. Define an Student class and initialize it with name and section.
 Now, make a classmethod that takes in a string parameter "name-A" which creates an instance and
 returns the instance based on parameter.
 [Hint: use @classmethod decorator]'''

class Student:
    def __init__(self,name,sem):
        self.name=name
        self.sem=sem

    @classmethod
    def get_from_string(cls,inp):
        name,sem=inp.split("-")
        return cls(name,sem)


student1=Student.get_from_string("Shreya-A")
print (student1)
print (student1.__dict__)
