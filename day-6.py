Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\khush\OneDrive\Desktop\workshop python\module.py
>>> import module
>>> summ=module.add(2,3)
>>> summ
5
>>> import module as md
>>> 
>>> summ=md.add(2,6)
>>> summ
8
>>> subb=md.subtract(6,2)
>>> subb
4
>>> poww=md.power(3,2)
>>> poww
9
>>> divide=md.division(10/5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    divide=md.division(10/5)
TypeError: division() missing 1 required positional argument: 'b'
>>> divide=md.division(10,5)
>>> division
<function division at 0x000001F1AB484180>
>>> import module as ml
>>> divv=md.division(10,5)
>>> divv
2.0
