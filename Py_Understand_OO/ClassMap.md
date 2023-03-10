# Class WalkThrough By Ukant Jadia

<script src="https://gist.github.com/ukantjadia/1ebc4e77b019242b0ccb2ebeca82a78b.js"></script>

- method -> a function that is associated with a class
- Class -> a class we can use to create a blueprint of each employee, So we don't have to create it from scratch for employee
- instance variable -> contains data that is created for each instance
- `__init__` -> this is a `class` way of creating the instance variable for
            <br> think of  `__init__` as an initializer and if you are with another language background take it as a constructor
- method -> adding a functionality
- Each method in a class automatically takes an instance as a first argument and always called that self
- calling a method -> calling the method in different ways `className.`methodName(instanceName)` and `instanceName.methodName()`
- class variable -> class variable is a variable that is shared among all of the instances of a class
  - class instances are variable that is unique to each instance
  - and class variables are the same for each instance
- the class variable can be accessed by both class and instance
- To get the namespace of an instance use `instanceName.__dict__`
  - when we see the namespace of any instance we don't have the class variable but
  - when we see it with the name of the class then it's available
- To change or access the class variable, do it with the class name or instance name (self)
  - doing it with the class name will change it for every instance
  - doing it with instance will only change it for that specific instances
- method -> don't have any instance or class in its working

- Inheritance
- For inheritance we need to create a another class and pass the parent(previous) class as it's argument.
- It will have all functionality of it's parent class.
- Now to see it use help() function like `help(new_class)`
- We can use the methods of parent class also and also we can create new methods also for our child class
- we can also called the parent `__init__`` method for our new class 
- We have something good in code side so refer that.
- We have this two very important method `isinstance(instance_name,class_name)` and `issubclass(subclass,class)`
## 

### Difference between a class and an instance of a class

class - class is a blueprint for creating instances for each employee
instance - creating a user of any class like employee


### Difference between class method, regualr method, static method

- class method automatticaly pass class(`cls`) as it's first argument, regular method automatically pass first argument instance(`self`) and static method don't have either class nither instance in it's argument list
