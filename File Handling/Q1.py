#1. WAP to print how many lines of data we have in given file

Fo =open('first.txt','r')
data=Fo.readlines()
print(f'we have {len(data)} lines of data')
