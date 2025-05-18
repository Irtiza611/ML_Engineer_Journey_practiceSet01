f1 = open("first.txt", "w")
f1.write("heello this is my first program to write something in a file ")
f1.close()

f1 = open("first.txt","r")
print(f1.read())


f1 = open("first.txt", "a")
f1.write("so i am now appending a line in the previous file ")
f1.close()

f1 = open("first.txt")
print(f1.read())