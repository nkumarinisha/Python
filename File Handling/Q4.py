
#4. WAP to print how many lines of data we have in given file with more than 80 characters in it 

Fo=open('first.txt','r')
data=Fo.readlines()
count=0
for lines in data:
    if len(lines)>=80:
        count+=1
print(count)
