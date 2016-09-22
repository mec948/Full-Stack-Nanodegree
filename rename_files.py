import os

def rename_files():

    #1 get file names from folder
     file_list = os.listdir(r"/Users/melaniecummings/Desktop/prank")
     print(file_list)

     #2 changed the current directory to the prank directory to find files
     os.chdir(r"/Users/melaniecummings/Desktop/prank")
     saved_path = os.getcwd()

    #3 for each file rename file
     for file_name in file_list:
          print("Old File Name - " + file_name)
          print("New File Name - " + file_name.translate(None,"123456789"))
          os.rename(file_name, file_name.translate(None,"123456789"))
     #4 change the directory back to what it was
          os.chdir(saved_path)
rename_files()
