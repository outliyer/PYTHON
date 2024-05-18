
f= open('alpha.txt','r')
content=f.read()
print(content)
f.close()

with open('alpha.txt') as f:#it will automatically closes the file
    pass
print(f.mode)#prints the mode
print(f.name)#prints the name of the file
print(len(content))#prints the length of the file
#the lines are converted in to the list from the below code
with open('alpha.txt')as f:
   lines=f.readlines
   print(lines)
   #method 2 for the printing out the conten in the from of list is 
   for line in lines:
    print(line,end=' ')
    ###########......work in progress....####