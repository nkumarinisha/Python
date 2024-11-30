
#6. WAP to print how many words of data we have in given file which r starting with 'h'

Fo =open('first.txt','r')
words=Fo.read().split()
count=0
for char in words:
    if char.startswith('h') or char.startswith('H'):
        count+=1
print(count)
