#braille
#the 6 letter values for each letter
A = 'xooooo'
B = 'xoxooo'
C = 'xxoooo'
D = 'xxoxoo'
E = 'xooxoo'
F = 'xxxooo'
G = 'xxxxoo'
H = 'xoxxoo'
I = 'oxxooo'
J = 'oxxxoo'
K = 'xoooxo'
L = 'xoxoxo'
M = 'xxooxo'
N = 'xxoxxo'
O = 'xooxxo'
P = 'xxxoxo'
Q = 'xxxxxo'
R = 'xoxxxo'
S = 'oxxoxo'
T = 'oxxxxo'
U = 'xoooxx'
V = 'xoxoxx'
W = 'oxxxox'
X = 'xxooxx'
Y = 'xxoxxx'
Z = 'xooxxx'
SPACE = 'oooooo'
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
        if lett == A:
            sent.append('a')
        elif lett == B:
            sent.append('b')
        elif lett == C:
            sent.append('c')
        elif lett == D:
            sent.append('d')
        elif lett == E:
            sent.append('e')
        elif lett == F:
            sent.append('f')
        elif lett == G:
            sent.append('g')
        elif lett == H:
            sent.append('h')
        elif lett == I:
            sent.append('i')
        elif lett == J:
            sent.append('j')
        elif lett == K:
            sent.append('k')
        elif lett == L:
            sent.append('l')
        elif lett == M:
            sent.append('m')
        elif lett == N:
            sent.append('n')
        elif lett == O:
            sent.append('o')
        elif lett == P:
            sent.append('p')
        elif lett == Q:
            sent.append('q')
        elif lett == R:
            sent.append('r')
        elif lett == S:
            sent.append('s')
        elif lett == T:
            sent.append('t')
        elif lett == U:
            sent.append('u')
        elif lett == V:
            sent.append('v')
        elif lett == W:
            sent.append('w')
        elif lett == X:
            sent.append('x')
        elif lett == Y:
            sent.append('y')
        elif lett == Z:
            sent.append('z')
        elif lett == SPACE:
            sent.append(' ')
    #print the translated line
    print ''.join(sent)
