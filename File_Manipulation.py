import os
import shutil

#check if file exists
if os.path.exists('Python Automation Course.docx'):
    print("File Exists!!")
else:
    print("File do not exists")

#print(os.listdir('.'))

with open('example.txt','w') as f:
    f.write("Hello World!!")
    
with open('example.txt','r') as f:
    content = f.read()
print(content)

#Copy a file
shutil.copy('source.txt','example.txt')

#Move a file
shutil.move('c:/Work/My_Work/example.txt','c:/Work/My_Work/S_Hustle/example.txt')

#Rename a file
os.rename('example.txt','destination.txt')

#Delete a file
os.remove('destination.txt')

#Remove a empty directory
os.rmdir('test')

#Remove a directory with files
shutil.rmtree('test')