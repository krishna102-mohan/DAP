'''class student:

 def _init_(self,name,rollno):
    self.name=name
    self.rollno=rollno
    print("Inside constructor")
    print("Name:",self.name)
    print("rollno:",self.rollno)
 def update_marks(self,marks):
     self.marks=marks
     print("\n inside instance method")
     print(f"{self.name}'s updared to:",self.marks)

s1=student('arun',401)
s1.update_marks(85)'''
class student:

 def _init_(self,name,rollno):
    self.name=name
    self.rollno=rollno
    print("Inside constructor")
    print("Name:",self.name)
    print("rollno:",self.rollno)
    del self.name       

 def update_marks(self,marks):
     self.marks=marks
     print("\n inside instance method")
     print(f"{self.name}'s updared to:",self.marks)

     print("\n outside the class")
     print("name(befoer):",s1.name)
     s1.name='anil'
     print("marks(outside):",s1.marks)
     

s1=student('arun',401)
s1.update_marks(85)


t1=test()
t2=test()
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
t1.x=888
t1.y=999
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
