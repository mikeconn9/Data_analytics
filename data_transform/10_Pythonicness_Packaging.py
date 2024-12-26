#Zen of Python
import this

#PEP 8 suggestions
#PEP 20: The Zen of Python
#PEP 257: Style Conventions for Docstrings

#Function Arguments
#*args as a function parameter enables you to pass an arbitrary number of arguments to that function.

#Example1:
def function(named_arg, *args):
    print(named_arg)
    print(*args)

function(1,2,3,4,5)

#Example2: *args accessed inside a function as the tuple args
def adder(x, *args):
    print(x+sum(args))

adder(2, 3)
adder(2, 3, 4)
adder(1, 2, 3, 4, 5)

#Example3: Named parameters to a function can be made optional by giving them a default value. 
# Come after named parameters without a default value.

def function(x,y,food="spam"):
    print(food)

function(1,2)
function(1,2,"egg") 

#Example4: **kwargs: Keyword arguments. Allows you to handle named arguments that you have not defined in advance.
#The keyword arguments return a dictionary in which the keys are the argument names, amd the values are the argument values.

def my_func(x,y=7,*args,**kwargs):
    print(args)
    print(kwargs)

my_func(2,3,4,5,6,a=7,b=8)

#Results:
#(4, 5, 6)
#{'a': 7, 'b': 8}

#Tuple Unpacking:
#Example1:
numbers = (1,2,3)
a,b,c=numbers
print(a)
print(b)
print(c)

#Example2:
a,b,*c,d=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)

#Ternary Operator
#Example1:
a = 7
b = 1 if a>= 5 else 42
print(b)

#For and While with else:
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

#Results: Unbroken 1

# try/except/else

#main:
#If Python interpreter is running that module(The source file) as the main program, 
# it sets the special name variable to have a value "main". If this file is being imported
# from another module, name will be set to the module's name.

#Major 3rd-Party Libraries
# Django: The most frequently used web framework written in Python.
# Also CherryPy and Flask.
# BeautifulSoup: Scraping data from websites.
# matplotlib: Create graphs based on data in Python.
# NumPy: Allows for use of multidimensional arrays, mathematical operations.
# SciPy: Numous extensions to the functionality of NumPy.
# Panda3D: 3D games.
# pygame: 2D games.

#Packaging:
#Putting modules you have written in a standard format, so that other programmers can install and use them with ease.
#This involves setuptools and distutils.
#Step1:
# Organize existing files correctly. 
# Directory structure:
#Projects/
#    LICENSE.txt
#    README.txt
#    setup.py
#    project/
#       __init__.py #MUST have
#       proj1.py
#       proj2.py
#Step2: Write the setup.py file, containing info necessary to assemble the package so it can be uploaded to PyPI
# and installed with pip(name, version, etc.).
#Example:
from distutils.core import setup

setup(
    name='Projects',
    version='0.1dev',
    packages=['project',],
    license='MIT',
    long_description=open('README.txt').read(),
)
#Step3: upload setup.py to PyPI, or use the command line to create a binary distribution.
# Navigate to the directory containing setup.py, and run the command python setup.py sdist
# Run python setup.py bdist (or bdist_wininst for Windows), to build a binary distribution.
# Use "python setup.py register" followed by "python setup.py sdist upload" to upload a package.

#Step4: Install a package with python setup.py install.

# Converting scripts to executables: py2exe, PyInstaller, cx_Freeze