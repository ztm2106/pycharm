def is_unique_chars(s):
    """

    Return True if all the characters in the string s are

    unique.

    If you happen to already know other Python data structures

    such as lists, dictionaries, or sets, you may not use them

    :param s: (str) a string

    :return: True if the characters in s are unique

    """
    #create new empty list to iterate over user input string
    chars = []
    #loop through the letters in string s
    for i in s:
        #if the letter is in the new list return false because there is a duplicate
        if i in chars:
            #return to mai prog
            return False
        #if i is not in the new list
        else:
            #add to the list
            chars.append(i)
    #if no duplicates return true
    return True


#main prog
print(is_unique_chars("abcdd"))