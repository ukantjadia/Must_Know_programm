# checking the give number is divisible by the another no if yes then print Foo
# > Trick check wheather it is divisible or not and also check that it is not divisible by another number 
# > if don't do this then any number you enter will never check for the condition where it is checking wheather it is divisible by both or not

num = int(input("Enter any number"))

if (num%31==0 and num%37!=0): # Checking for the not condition is important remove it and try it with number 1147
    print("FOO")
elif (num%37==0 and num%31!=0):
    print("BAR")
elif(num%31==0 and num%37==0):
    print("FOOBAR")
else:
    print("it is note divisible by 31 not either 37")
# 