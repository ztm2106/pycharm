def run_length_encode(s):
    """

    Produce a run-length encoded string

    :param s: (str) a string with (hopefully) many repeated

    letters

    :return: a run-length encoded version of s

    """
    #create empty lift
    list = ""
    #starting i is 0
    i = 0
    #loop check each index from user input
    while i <= len(s) - 1:
        #set the count bacl to one for new letter
        count = 1
        #use string index for each character
        ch = s[i]
        #set i = to j
        j = i
        ##loop check each index from user input but compared to the user string - 1 to see compare before characters
        while j < len(s) - 1:
            #if the charchter of the current index to the one before in the list are equally
            if s[j] == s[j + 1]:
                #add one to the count
                count = count + 1
                #add one to j for next letter
                j = j + 1
            #if anything else
            else:
                #exit this loop
                break
        #add the single charachet and count for each letters into the empty list
        list = list + ch + str(count)
        #add one to the to j that is set to i to check next non reccurng number
        i = j + 1
    #return the list
    return list



#main prog.
print(run_length_encode("aabbbbccccdddaaa"))
print(run_length_encode("cccaagtaaa"))
print(run_length_encode("gggctttttttttcgacccaaa"))