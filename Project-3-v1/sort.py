""" for making the names of boys and girls in lower case"""

with open('girls.txt','r') as b:

    names = b.readlines()

names = [ line.lower() for line in  names]

with open('girls.txt','w') as b:
    b.writelines(names)
