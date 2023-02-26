# amp

- In order to understand the decorators first understand the basic of function in python 
```python
def a1():
    print("Called a1")
a1()
```
- you can say that above code will run fine and print the output as `Called a1`.
- Now what if
```python
def a1():
    print("Called a1")
print(a1)
```
- This time we are only using the name of function not the complete function with `()` . Now what will be output of that
let me help you `<function a1 at 0x00000270EF1D2CB0>` this is the output at my end. <br>
This looks like this printing the location of my function 
- This meas a1 is an object and we can pass it as our parameter.See below code to see what i mean 
```python
def a1():
    print("Called a1")

def a2(a):
    a() # calling the passed argument a

a2(a1) # passing the previous function a1 as the paramenter
```
- As I said function can pass as object, we are passing func a1 to a2 and will work fine as expected output will be `Called a1`.

#### Wrapper Function 
- A function inside any function before the return statement of the first function.See below code
```python
def a1(func):
    def wrapper():
        print("Started")
        func() # calling the argument of func a1
        print("Ended")
    return wrapper # return the oobject from wrapper func
```
- the output and working will be simple as you expected
<br> Now I want to use this func for other func, in order to do that

```python
def a1(func):
    def wrapper():
        print("Started")
        func() # calling the argument of func a1
        print("Ended")
    return wrapper # return the oobject from wrapper func

def a2():
    print("Welcome")

a1(a2)
```
- see the last line of below code, we calling the func `a1` with argument of `a2`
- If you run above code, it will work strangenly by not giving any output. If you print it then you will get the address of the wrapper function 
`a1(a2): ... return wrapper` 
- Because thats what is happening, func `a1` is just writtening the `wrapper` function not calling it, this means we never end up calling function `a2`  
- Here is the trick, adding extra () will work fine, because it will call the `wrapper` func. See below code
```python
def a1(func):
    def wrapper():
        print("Started")
        func() # calling the argument of func a1
        print("Ended")
    return wrapper # return the oobject from wrapper func

def a2():
    print("Welcome")

a1(a2)() # added parenthesis
```
- This will work absolutely fine
<br><br>

- Now i want every time i call `a2` I want to call `a1` along with it
- See below code to get it better
```python
def a1(func):
    def wrapper():
        print("Started")
        func() # calling the argument of func a1
        print("Ended")
    return wrapper # return the oobject from wrapper func

def a2():
    print("Welcome")

x = a1(a2)
x()
```
- The last second line called the **Function aliasing**, changing the name of a function and changing its functionality 

---
##### Decorators
- And heres our decorator comes in 
- The last second line of above code can be replace with something nicer that is `@a1`, yes a decorator
- `@a2` This will write `x = a1(a2)` this line in python for us, means it will automatically gonaa run it 
--- 
- Now the issue is with parameters we are passing they may be incerease 
- the error code is below. See line  
```python
def a1(func):
    def wrapper():
        print("Started")
        func() # calling the argument of func a1
        print("Ended")
    return wrapper # return the oobject from wrapper func
@a1
def a2(a):
    print(a)

a2("hi")
``` 
- see func `a2` is having a parameter but `func()` don't it will generate an error.

#### *args, **kwargs
- `*args, **kwargs` are the solution to this 
```python 
def a1(func):
    def wrapper(*args,**kwargs):
        print("Started")
        func(*args,**kwargs) # calling the argument of func a1
        print("Ended")
    return wrapper # return the oobject from wrapper func

@a1
def a2(a,b):
    print(a,b)

a2("hi","Wolcome')
```
- this will take care of any arguments in any amount
