
#This grabs the input that we receive from the people
given_input = open('5_words.txt', 'r')

words = given_input.read()
words = words.split("\n")

given_input.close()
##

# Processes the words and outputs in desired square format
for word in words:
    #Prints first line (word going forward horizontally)
    print ("*"),
    for j in range(0, len(word)):
        print (word[j]),
    print ("*")
    #Prints all lines with word going vertically
    for i in range(0, len(word)):
        print (word[len(word)-(i+1)]),
        for h in range(0, len(word)):
            print ("*"),
        print (word[i])
    #Prints the last line (word going backwards horizontally)
    print "*",
    for k in range(0, len(word)):
        print (word[len(word)-(k+1)]),
    print "*"
    print " "
    
