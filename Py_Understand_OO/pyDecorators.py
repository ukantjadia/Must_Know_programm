# def a1():
#     print("Called a1")

# def a2(a):
#     a() # calling the passed argument a

# a2(a1) # passing the previous function a1 as the paramenter

# print(a1k)
# def a1(func):
#     def wrapper():
#         print("Started")
#         func() # calling the argument of func a1
#         print("Ended")
#     return wrapper # return the oobject from wrapper func

# def a2():
#     print("Welcome")

# print(joa1(a2))
def a1(func):
    def wrapper(*args,**kwargs):
        print("Started")
        func(*args,**kwargs) # calling the argument of func a1
        print("Ended")
    return wrapper # return the oobject from wrapper func

@a1
def a2(a,b,c):
    print(a,c,b)

a2("hi",'Fuck you',0)

