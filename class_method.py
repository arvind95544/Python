class Student:
    leav=10

    @classmethod
    def change_leav(self,newleav):
        self.leav=newleav

am=Student()
an=Student()
am.change_leav(8)
print(an.leav)
print(Student.leav)