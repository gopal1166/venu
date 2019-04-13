# if else elif
# count = 10

# if count < 10:
#     print("count is lessa than 10")
# elif count == 10:
#     print("count is equal to 10")
# else:
#     print("count is not less than 10")


# name = "Venu"
# switch(name){
#     case "Venu":
#         print("Venu");
#         break;
#     case "Gopal":
#         print("Gopal");
#         break;
#     default:
#         print("Not matched");
# }
# switch 

#For
# for i in range(10):
#     print(i)

# list = [1, 2, 3]
# for ele in list:
#     print(ele)

# Func
# def myFunc(name):
#     print("my name is ", name)

# myFunc("Venu")

# local variable
# def func2():
#     localVar = "I m local var"
#     print("This is func2")
#     print(localVar)

# func2()
# print(localVar)


#global var

# globalVar = "Gopal"

# def func3():
#     global globalVar
#     globalVar = "Ram"
#     print(globalVar)

# func3()

# print(globalVar)


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


















