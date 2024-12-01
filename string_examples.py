import util
#examples of what we can do with strings and string processing

s = "antidisestablishmentarianism"

#how long is the string? how many charcters are in the string
#strings can also use the len() func.
print(len(s))

#we can access individual characters from a string the same way we access data in list

print(s[0], s[27])

#self check: what does the following print out?
print(s[5], s[15])

#be careful about "off by one" error
#to get last character of any string, we would need len(s) - 1
#(-1 so that we dont go outside the bounds of the string
print(s[len(s)-1])

#we can loop over the string using a for loop
#EX: count the number of i's in the string s

i_count = 0
#loop through all charcters of s and check if the character is i
#if so add to running count for i's
for ch in s:
    if ch == "i":
        i_count += 1
print("There are", i_count, "i's in the string", s)


#instead of looping through characters, we can also lopp through the indicies of the string

d_count = 0
for i in range(len(s)):
    #check if the character at the index is d
    if s[i] == "d":
        d_count += 1
print("There are", d_count, "d's in the string", s)

#we combine strings
str1 = "CS"
str2 = "140"
str3 = str1 + str2
print(str3)



#use the reverse function in util to reverse string and string constants
print(util.reverse(s))
print(util.reverse("zakiy"))


#search a string for a sequence of characters
print(s.find("ta"))
#have a starting point in the string
print(s.find("ta", 10), "this")
#kevin is not in string s and cannot be found so it returns -1
print(s.find("kevin"), "this")

#substring
print(s[0:4])
print(s[7:16])


#ask user to type t2 number and seperate by comma and take the average of these 2 number
data = input("Input two numbers sperated by a comma: ")
#search for the comma

comma = data.find(",")
num1 = float(data[:comma])
num2 = float(data[comma + 1:])

print((num1 + num2) / 2)



print(util.scramble(s))

