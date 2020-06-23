import os
from PIL import ImageChops, Image

#input
path =input("Enter in the path of the folder you want to rename the files of: ").strip()
def_question = input("Do you wish to add or remove from the file(s) name? (a/r): ").strip().lower()
addd = input("Enter in the text you wish to be added/removed (can not contain blank spaces): ").strip()

#veriables
files = os.listdir(path)
count = 1


#print(files)


def add():
     for file in files:
          image = Image.open(os.path.join(path,file))
          if image.histogram() != image2.histogram():
               count = count + 1
               image = image2
               original_file_name, file_ext = (os.path.splitext(file))
               new_name = "{}_X{}{}".format(original_file_name, str(count)), file_ext).strip()

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


if def_question == "a":
    add()
elif def_question == "r":
    remove()
else:
    print("I don't understand your command")
#print(files)


