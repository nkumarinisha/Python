#2. WAP to print how many words of data we have in given file

Fo =open('first.txt','r')
words=Fo.read().split()
print(len(words))
