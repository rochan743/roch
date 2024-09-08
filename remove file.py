import os
print("Checking file exists or not ")

if os.path.exists("information.txt"):
   os.remove("information.txt")
   
else:
    print("File does not exist")