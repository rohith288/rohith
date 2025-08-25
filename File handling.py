print("\t\t\t\t----->> File Handling <<-----\t\t\t\t\n\t\t\t\t=============================\t\t\t\t")

"""
To open a file we have python in built function open():
Syntax: open('file_name','mode','encoding')

we have different types of mode:
1.read() --> represented by 'r'
2.write()--> represented by 'w' if the existing file has data it will be over ride
3.append()--> represented by 'a' if the existing file has data it wont over ride
and  if the file doesn't exists in folder 
"""

# opening a file  -- initially the file is empty
f=open('sample.txt')
print(f.read())

#Various properties of file objects:
f=open('sample.txt','w')
print('File_Name:',f.name)
print('file_mode',f.mode)
print('file_encoding',f.encoding)
print('is file readable',f.readable())
print('is file writable',f.writable())
print('is file closed',f.closed)
f.close()
print('is file closed',f.closed)

#writing to the file:
print("========writing the file========")
f=open('sample.txt','w') # if the file exists it will override if not it will create
f.write("Name:Rohith\n") # \n indicates new line
f.write("job role:sql developer\n")
f.write("company:evergent technologies\n")
f.write("Hyderabad")
print("file written successfully")
f.close()
print("file closed")


#writing to the file using list :
print("========writing the file using list[]========")
f=open('sample1.txt','w') # if the file exists it will override if not it will create
l=["Rohith\n","Sql developer\n","Evergent technologies"]
print(f.writelines(l))
print("file written successfully")
f.close()
print("file closed")

"""
#writing to the file using list :
print("========writing the file using list[]========")
f=open('sample1.txt','w') # if the file exists it will override if not it will create
l=["Rohith","Sql developer","Evergent technologies"]
for i in range(len(l)):
    print(f.writelines(l))
    i+=1
print("file written successfully")
f.close()
print("file closed")
"""

#reading a file:
print("=====reading the file======")
f=open('sample.txt','r') #if file doesn't exist will get file not found error
print(f.read())
f.close() #closing the file


#appending the file:
print("=====appending the file======")
f=open('sample.txt','a')
f.write("\n5000612")
f.write("\nTelangana.")
f.close()

# read and write the file (r+): it wont over ride the existing file but it will write the new line at end
f=open('sample.txt','r+')
print(f.read())
print(f.write("\nIndia"))
print(f.write("\nAsia"))
f.close()

# write and read (w+): it will over ride the existing data
f=open('sample1.txt','w+')
print(f.read())
print(f.write("\nIndia"))
print(f.write("\nAsia"))
f.close()

#appending the file(a+):
print("=====appending the file======")
f=open('sample.txt','a')
f.write("\n5000612")
f.write("\n state:Telangana.")
f.close()









