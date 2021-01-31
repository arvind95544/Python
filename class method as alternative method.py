class Student:
    leav=10

    def __init__(self,aname,astd,asection,asubject):
        self.name=aname
        self.std=astd
        self.section=asection
        self.subject=asubject


    @classmethod
    def change_leav(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(string.split("-"))


am=Student.change_leav("Amit-9-A-[Hindi,English")
print(am.name)