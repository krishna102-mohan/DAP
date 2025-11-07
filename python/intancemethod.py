class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Hi', self.name)
        print('Your marks are:', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('You got first grade')
        elif self.marks >= 50:
            print('You got second grade')
        elif self.marks >= 35:
            print('You got third grade')
        else:
            print('You have failed')
            
n = int(input('Enter number of students: '))
for i in range(n):
    name = input('Enter name: ')
    marks = int(input('Enter marks: '))
    s = Student(name, marks)
    s.display()
    s.grade()
    print()
class Test:
    count = 0

    def __init__(self):
        Test.count += 1

    @classmethod
    def no_of_objects(cls):
        print('The number of objects created for Test class:', cls.count)



t1 = Test()
t2 = Test()
Test.no_of_objects()

t3 = Test()
t4 = Test()
t5 = Test()
Test.no_of_objects()

class ADITYA:
    @staticmethod
    def add(a, b):
        print("Addition:", a + b)

    @staticmethod
    def sub(a, b):
        print("Subtraction:", a - b)

    @staticmethod
    def avg(a, b):
        print("Average:", (a + b) / 2)

ADITYA.add(200,100)   
ADITYA.sub(200,100)       
ADITYA.avg(200,100)


