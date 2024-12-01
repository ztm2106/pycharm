def unique_chars(s):
    """

    Return a string of all the unique characters from the

    given argument.

    If you happen to already know other Python data structures

    such as lists, dictionaries, or sets, you may not use them

    :param s: (str) a string

    :return: all of the unique characters in s

    """
    #create new string to write over
    less_characters = ""
    #loop to go to check each letter in string using index of string s
    for i in range(len(s)):
        #check if arguments are the same is not print letter
        if s[i] != s[i - 1]:
            #add to new reoccuring string
            less_characters += s[i]
    #return the new sring
    return less_characters



#main prog
print(unique_chars("class"))


