class Student:
    leav=10

    def __init__(self,aname,astd,asection,asubject):
        self.name=aname
        self.std=astd
        self.section=asection
        self.subject=asubject


    def printself(self):
        return f"Name is {self.name}.Standard is {self.std}.Section is {self.section}.Subject are {self.subject}"
#
# am = Student()
# an = Student()
# print(am,an)
# am.name="Amit"
# am.std=8
# an.name ="Ankit"
# an.std =7
# am.section = 'A'
# an.section ='M'
# an.subject = ["Math","Science"]
# am.subject = ["Hindi","English"]
# print(an.printself())
av=Student("Avnish",9,'A',["Hindi","English"])
print(av.name)
