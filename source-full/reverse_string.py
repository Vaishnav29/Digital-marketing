str1 = 'string is immutable'
str2 = ''
l = []

def push(l, item):
    l.append(item)
    
for i in range(len(str1)):
    push(l, str1[i])
   
def pop(l):
    if(len(l)!=0):
        return l.pop()
    else:
        return

for i in range(0,len(l), 1):
    str2 += pop(l)