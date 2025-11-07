class a:
    def methoda(self):
        print("Method a")

class b:
    def methodb(self):
        print("methodb")

class c(a, b):
    print("c")  # This will print once when the class is created

c= c()  # instantiate c
c.methoda()  # call methoda from class a
c.methodb()  # call methodb from class b

class a:
    def methoda(self):
        print("Method a")

class b:
    def methodb(self):
        print("Method b")

class c(a, b):
    def methodc(self):
        print("Method c")

# class d inherits from both b and c
class d(c, b):
    pass

# Instantiate d
d = d()

# Call methods from a, b, c through d
d.methoda()  # From class a (inherited via c)
d.methodb()  # From class b (directly inherited and via c)
d.methodc()  # From class c
