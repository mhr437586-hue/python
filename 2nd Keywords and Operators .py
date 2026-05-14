# keywords are reserved in Python
# Python is a case-sensitive language
# In Python, small a  and capital A are different

#print sum
a=2
b=5
sum=a+b
print(sum)
a=6
b=2
diff=a-b
print(diff)

'''
Comments
 Multi line comment('''    ''')
 single line comment(#)
'''
 
 
  #Operators
     # 1 Arithmetic operators
a=5
b=2
sum=(a+b)
print(sum)
        #print(a+b)
print(a-b)
print(a*b)
print(a/b)
#answer of division is always in a float value if the number is int answer in float
print(a%b) #remainder
print(a**b) # a to the power b (a^b)

a=2
b=5
c=a+b
print(c)

  # 2 Relational operators & Comparison operators
a=50
b=20
print(a==b) #False
    # the answer of relational/comparison operator is in True or False
print(a!=b) #True   
print(a>=b) #True   
print(a>b) #True   
print(a<=b) #False  
print(a<b) #False 
           # always return a boolean

    # 3 Assignment operators
a=4-2 # assign 4-2 in a
print(a)
b=6
b+=3 # increment the value of b by 3 and then assign into b
print(b)

a=4-2 # assign 4-2 in a
print(a)
b=6
#b+=3 # increment the value of b by 3 and then assign into b
b-=3 # decrement the value of b by 3 and then assign into b
print(b)

num=10
 #num=num+10
num+=10
 #print(num)
print("num : ", num)

num=10
 #num=num-10
num-=10
 #print(num)
print("num : ", num)

num=10
 #num=num*10
num*=5
 #print(num)
print("num : ", num)

num=10
 #num=num/10
num/=5
 #print(num)
print("num : ", num)

num=10
 #num=num%10
num%=5
 #print(num)
print("num : ", num)

num=10
 #num=num**10
num**=5  # 10 to the power 5
 #print(num)
print("num : ", num)


    # 4 Logical operators
        # work on Boolean Values
    # not, and, or

#truth table of or
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("True or False is ", True or False)
print("False or False is ", False or False)

 output:
          True or False is  True
          True or True is  True
          False or True is  True
          True or False is  True
          False or False is  False         

#truth table of 'and'
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("True and False is ", True and False)
print("False and False is ", False and False)

   output:
          True and False is  False
          True and True is  True
          False and True is  False
          True and False is  False
          False and False is  False

print(not(False))  # answer in true
print(not(True))   # answer in false



a=20
b=30
print(not False)
print(not (a<b))
       # does not work with only single operands
       #and, or operator works on double values
   
val1 = True
val2 = True
print("and operator:", val1 and val2)
   # The AND operator gives a true result only when both values are true; otherwise, it returns false.

print("or operator:", val1 or val2)
    # or operator gives a result when one value is true answer is true if both are false, then answer is false

val1 = True
val2 = False
print("AND operator:", val1 and val2)  #False
print("OR operator:", val1 or val2)  #True
   
val1 = False
val2 = False
print("AND operator:", val1 and val2) #False
print("OR operator:", val1 or val2)  #False

a=20
b=30
print("AND operator:", (a!=b) and (a<b)) #True
print("OR operator:", (a==b) or (a>b))  #False

