session1: python getting started

date: 13/04/2019
--------------------------------------------

install: python

link: python.org

verify the installation: `python` type this on command line

variables:

syntax:
```
variableName = 'value'    value: int/string/array/dict
```

naming convension:
```
camelCase

should not start with digit, special char, 
no spaces

we can start with _
like _name, _sal

Data types:
```
1.Number
2.List
3.Tuple
4.Set
5.Dict

List:
```
mutable: we can update the values
duplicates allowed in lists
list = [1, 2, 3]

to deleted:
    del list['index']

Tuple:
tup = (1, 2, 3)
immutable: once defined we cant update the values

*interview question: difference b/n list and tuple


Set:
syntax:
set = {}
duplicates not allowed

To convert list to set
```
list = [1, 2, 2, 3]
set(list)   # {1, 2, 3}

*interview question: difference b/n list and set


Dict:
syntax:
dict = {}

to store data as key value pairs

ex:
dict = {
    'name': "Gopal",
    'sal': 10
}

to access value: use key

ex: dict['name']   # "Gopal'

to update the vlaue:
    dict['name'] = "Ram"   # {'name': "Ram"}

------------------------------------------------

conditions:
`if`
`if else`
`if elif else`
`switch`


if else elif else:
```
count = 10

if count < 10:
    print("count is lessa than 10")
elif count == 10:
    print("count is equal to 10")
else:
    print("count is not less than 10")
```

loops:
`for, while, dowhile`

for
```
for i in range(10):
    print(i)

list = [1, 2, 3]
for ele in list:
    print(ele)
```

functions:
syntax:
```
def funcName():
        #state ments
        #return 
```

ex:
```
def myFunc(name):
    print("my name is ", name)

myFunc("Venu")
```

local variables:
global varibless:

local:
defined inside the function
scope only inside the function
we cant acces out side of funcion

eg:
```
def func2():
    localVar = "I m local var"
    print("This is func2")
    print(localVar)

func2()
print(localVar)
```

global var:
defined outside of the class
scope both inside n outside of functions
we can access any where in the file

eg:
```
globalVar = "Gopal"

def func3():
    global globalVar
    globalVar = "Ram"
    print(globalVar)

func3()

print(globalVar)
```

```
we used global keyword to update the global variable from the function
```

* interview: local vs global variables


class:
syntax:
```
class ClassName:
    properties,
    functions

we'll create obj
using instacee we'll access
```


eg:
```
#class
class FirstClass:
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)
        return self.name

instance = FirstClass("Gopal")
print(instance.func())
# print(instance.)
```
























































