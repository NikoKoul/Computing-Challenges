# will explain later
diction = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}
code = []
for x in raw_input():
    code += [diction[x]]

def swap(str1,loc1,str2,loc2):
    #print x[loc1],str2+'****',
    #print x[loc2],str1
    x[loc1] = str2
    x[loc2] = str1

def encrypt():
    for y in range(len(x)):
        important = y + code[y%len(code)]
        #print important
        #print y,(important % len(x))
        swap(x[y],y,x[(important % len(x))],(important % len(x)))
        string = ''
    for a in x:
        string +=a
    print string
def decrypt():
    for m in range(len(x)):
        y = len(x)- m - 1
        important = y + code[y%len(code)]
        #print important
        #print y,(important % len(x))
        swap(x[y],y,x[(important % len(x))],(important % len(x)))
        string = ''
    for a in x:
        string +=a
    print string
while True:
    z = raw_input()
    #print z
    x = []
    for p in z:
        x +=[p]
    #print len(x)
    #print x
    #encrypt()
    decrypt()
