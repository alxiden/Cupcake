import os
from PIL import ImageChops, Image
import shutil
from send2trash import send2trash

#input
path =input("Enter in the path of the folder you want to rename the files of: ").strip()
def_question = input("Do you wish to add or remove from the file(s) name? (a/r): ").strip().lower()
addd = input("Enter in the text you wish to be added/removed (can not contain blank spaces): ").strip()
delete = input("Would you like to delete every other file? (y/n): ").strip().lower()

#veriables
files = os.listdir(path)
files.sort()
number = 1



def add():
     global number
     for file in files:
          original_file_name, file_ext = (os.path.splitext(file))
          if delete == "y" and number%2 !=0:
               number += 1
               new_name = "{}{}{}".format(original_file_name, addd, file_ext).strip()
               os.rename(path + "/" + file, path + "/" + new_name)
          elif delete =="y" and number%2 == 0:
               send2trash(path + "/" +file)
               number += 1
          else:
               new_name = "{}{}{}".format(original_file_name, addd, file_ext).strip()
               os.rename(path + "/" + file, path + "/" + new_name)
     print("Job Complete")

def remove():
    for file in files:
        original_file_name, file_ext = (os.path.splitext(file))
        #print(original_file_name)
        if original_file_name.find(addd) != -1:
             new_name = original_file_name.replace(addd, "_").strip()
             os.rename(path + "/" + file, path + "/" + new_name)
        else:
             print("Nothing found")
        print("Job Complete")

def deleted():
     if delete == "y":
          number = {}

if def_question == "a":
    add()
elif def_question == "r":
    remove()
else:
    print("I don't understand your command")
#print(files)


