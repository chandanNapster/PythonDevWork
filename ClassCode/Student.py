class Student:
    def check_pass_dail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Chandan", 39)
student2 = Student("Harry", 90)

print(student1.name)
print(student1.marks)

print(student1.check_pass_dail())
