"""Remove any character from a string that is given by the user."""

print('This program helps you to remove any character from a given string.')

def input1():
    global string                                  # string need to be defined for other functions.
    string = input('Enter the string: ')          
    if string.isspace() or string.isdigit():       # condition to ensure that the input data is only string.
        print('Please enter a string!') 
        return input1()                            # repeat the input process.
    else: 
        input2()                                   

def input2():
    k = 0
    _lst = []
    global remove                                 # remove need to be defined for other functions. 
    remove = input('Enter the character: ')
    for z in remove:                              # loop to count the number of intered character in (remove).
        _lst.append(z)
        k +=1                                     # k represent the counter.       
    if remove.isspace() or remove.isdigit():      # condition to ensure that the input data is only characters.
        print('Please enter a character!')
        return input2()                           
    if k > 1:                                     # condition to check the number of entered characters.
        print('Please enter one character!')
        return input2()
    else:
        code()

def code():
    for x in string:                                # For loop to remove the selected character 
        if x == remove:
            continue 
        print(x, end='')                           # Print the character side by side to return the intered string without the removed character.

input1()