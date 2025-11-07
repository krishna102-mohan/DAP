'''class student:
  '''class demo on student class'''
  def __init__(self):
      self.name='srinu'
      self.age=34
      self.marks=80
  def talk(self):
      print("hi",self.name)
      print("age",self.age)
      print("marks",self.marks)
s=student()
s.talk()
class student:
  '''class demo on student class'''
  def __init__(self,name,age,marks):
      self.name=name
      self.age=age
      self.marks=marks
  def talk(self):
      print("hi",self.name)
      print("age",self.age)
      print("marks",self.marks)
s=student('srinu',34,80)
s.talk()
class student:
    '''class demo on student class'''
    
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

    def talk(self):
        print("Hi", self.name)
        print("Age", self.age)

s = student()  # create an instance (call constructor)
s.talk()       # call talk method
class test:

    def m1(self):
        print("method execution")
t1=test()
t2=test()
t3=test()
t1.m1()'''
class student:
    '''this is student class requried data'''
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("student name:{}\nrollno:{}\nmarks:{}\n",format
