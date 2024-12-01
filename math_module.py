#examples of using math modules

#tell python we want to use the math module
import math

#we use "dot" notation to access values amnd functions from a module
print(math.pi)

#compute a square root
print(2**0.5)

# or.. we can u8se sqrt from the math module
print(math.sqrt(2))



#Example of func. composition using funcs. in math module
result = math.cos(math.sqrt(math.pi / 3))
print("The result is", round(result, 3))

#lets break this up into multiple lines of code


#intermidiate results
result1 = math.pi / 3
result2 = math.sqrt(result1)
#result
result3 = math.cos(result2)
print("The result still is", round(result3, 3))

#we can also break up the code be we use variables when we dont need inter. results
result = math.pi / 3
result = math.sqrt(result)
result = math.cos(result)
print("Once again the result is", round(result, 3))
