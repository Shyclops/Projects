#10191523 Christopher Won

#This code will check if a two dimensional array passed in is rectangular or not
def rectangular(a):
    widthCheck = len(a[0])                          #sets a variable that will check the length of other arrays against it
    rect = True                                     #assumes that the array all arrays is rectangular untill proved otherwise
    for x in a:                                     #runs through the list of arrays
        if widthCheck != len(x):                    #if the width of the array is not equal to the width of the first array
            rect = False                            #if the two widths are not the same, the array is not rectangular
    return rect                                     #return the result of whether the array is rectangular

#This code will rotate a rectangular array and return it to the user
def rotate(a):                                  
    if rectangular(a) == True:                      #check if array is rectaungular, if rectangular, continue with program
        matrix = []                                 #make an empty matrix that the rotated matrix will be put into
        for j in range(len(a[0])):                  #cycle through the indexes of the arrays
            row=[]                                  #make an empty list that will hold one row of the array
            for i in reversed(a):                   #go through the arrays in reverse order
                row.append(i[j])                    #take the values of whatever row program is on and add them to the new list from bottom up
            matrix.append(row)                      #add the new list onto the matrix
        return matrix                               #return the matrix that has was made by appending the rotated rows
    else:                                           #if array is not rectangular
        return 'Cannot Rotate'                      #tell user that array is not rectangular

#This code will transform a string into a code by adding op after each string of consonants
def opish(a):                                       
    vowelPrevious = True                            #Assumes that the letter before the first is a vowel
    keyword = "op"                                  #The keyword that will be added to the code will be 'op'
    output = ""                                     #This is an empty string that the code will be put into 
    for i in a:                                     #cycle through the string index by index
        if i == 'a' or i == 'e' or i == 'i' \
            or i == 'o' or i == 'u':                #check if current letter is a vowel 
            if vowelPrevious == False:              #if the previous letter was a consonant
                output = output + keyword           #add the keyword to the string as a string of consonants just ended
                vowelPrevious = True                #when the program looks again, the last letter will have been a vowel
        else:                                       #if it is a consonant
            vowelPrevious = False                   #on the next loop the previous letter is not a vowel
        output = output + i                         #add the letter to the output
    if vowelPrevious == False:                      #if the previous letter was not a vowel
        output = output + keyword                   #add the keyword if the only letter in the string is a vowel
    return output                                   #return the coded string
