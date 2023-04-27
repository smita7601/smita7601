# ELIGIBE FOR VOATING 

age = int(input("Enter age:"))

if age>=18:                               
    print("Eligible for voating!")        
else:
    print("Not eligible for voating")


# Default function to run if else condition  
def NumberCheck(a):   
    # Checking if the number is positive  
    if a > 0:   
        print("Number given by you is Positive")   
    # Checking if the number is negative   
    elif a < 0:   
        print("Number given by you is Negative")   
    # Else the number is zero  
    else:   
        print("Number given by you is zero")  
# Taking number from user  
a = float(input("Enter a number as input value: "))  
# Printing result  
NumberCheck(a) 


## FIND FACTORIAL 

num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    