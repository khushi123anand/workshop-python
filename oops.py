Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
D[105] [0]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    D[105] [0]
NameError: name 'D' is not defined
D[105]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    D[105]
NameError: name 'D' is not defined
class Car:
    def_init_(self):
        
SyntaxError: invalid syntax
class Car:
    def__init__(self) :
    self.brand = "Suzuki"
    
SyntaxError: invalid syntax
class Car:
    def __init__(self):
        self.brand="Suzuki"
        self.color="Blue"
        self.top_speed=200

    
car=Car
(
car=Car()
car.brand
'Suzuki'
car.color
'Blue'
class Car:
    def __init__(self,b,cts):
        self.brand=b
        self.color=c
        self.top_speed=ts

        
car=Car("Maruti","Black",150)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    car=Car("Maruti","Black",150)
TypeError: Car.__init__() takes 3 positional arguments but 4 were given
>>> class Car:
...     def __init__(self,b,c,ts):
...         self.brand=b
...         self.color=c
...         self.top_speed=ts
... 
...         
>>> car=Car("Maruti","Black",150)
>>> car.brand
'Maruti'
>>> car=Car("Tata","Grey",225)
>>> car.brand
'Tata'
>>> class Car:
...     def __init__(self,b,c,ts):
...         self.brand=b
...         self.color=c
...         self.top_speed=ts
...     def accelerate(self):
...         print("Your car top speed is:" ,self.top_speed)
... 
...         
>>> c=car.Car("Tata","Grey",225)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c=car.Car("Tata","Grey",225)
AttributeError: 'Car' object has no attribute 'Car'
>>> car=Car("Tata","Grey",225)
>>> car.accelerate()
Your car top speed is: 225
>>> class College:
...     def __init__(self,n,loc):
...         self.name=n
...         self.location=loc
...     def msg(self):
...         print(self.name+" is present at "+self.loc)
... 
...         
>>> class Department(College):
...     def __init__(self,name,ids):
...         self.id=ids
... 
...         
