import os
#task how many number 4 is in the list

l= [1,3,4,5,7,4]
print("#4 is repeated:",l.count(4),"times")

# task if a list contain vowels or not
l = ["a","e","i","o","u"]
st = input("Enter ur string: ")
count =0 
for ch in st:
    if ch.lower() in l:
       count+=1 
print("Ur string contain",count,"vowels")

#task program to access environment varaible
path = os.getcwd()
os_name = os.name
dir = os.path.expanduser("~")
print ("the current path is ",path)
print ("the current operating system is ",os_name)
print ("the home directory is  ",dir)