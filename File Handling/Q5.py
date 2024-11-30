
#5. WAP to print how many words of data we have in given file with 5 characters in it 
Fo =open('first.txt','r')
words=Fo.read().split()
count=0
for char in words:
    if len(char)==5:
        count+=1
print(count)
