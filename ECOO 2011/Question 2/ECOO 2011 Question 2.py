#braille
#the 6 letter values for each letter
letters = {'xooooo': 'a','xoxooo': 'b','xxoooo': 'c','xxoxoo': 'd','xooxoo': 'e',\
           'xxxooo': 'f','xxxxoo': 'g','xoxxoo': 'h','oxxooo': 'i','oxxxoo': 'j',\
           'xoooxo': 'k','xoxoxo': 'l','xxooxo': 'm','xxoxxo': 'n','xooxxo': 'o',\
           'xxxoxo': 'p','xxxxxo': 'q','xoxxxo': 'r','oxxoxo': 's','oxxxxo': 't',\
           'xoooxx': 'u','xoxoxx': 'v','oxxxox': 'w','xxooxx': 'x','xxoxxx': 'y',\
           'xooxxx': 'z','oooooo': ' '}
#collect and organize input into 2D list
whole = []
for i in range(5):
    group = []
    for f in range(3):
        line = raw_input()
        group.append(line)
    whole.append(group)


for i in range(5):
    #three lines for the three lines of braille
    allChars1 = []
    allChars2 = []
    allChars3 = []
    
    allChars1 = list(whole[i][0])
    allChars2 = list(whole[i][1])
    allChars3 = list(whole[i][2])
    line = []
    sent = []
    #create groups of the six digits of a letter 
    for i in range(0,(len(allChars1)),2):
        x = [allChars1[i], allChars1[i+1], allChars2[i], allChars2[i+1],\
                 allChars3[i], allChars3[i+1]]
        x = ''.join(x)
        line.append(x)
        
    #translate it (is there a faster way of doing this?)
    for lett in line:
        sent.append(letters[lett])
    #print the translated line
    print ''.join(sent)
