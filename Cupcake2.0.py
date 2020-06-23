import os
from PIL import ImageChops, ImageDraw
import shutil
from send2trash import send2trash

#input
path =input("Enter in the path of the folder you want to rename the files of: ").strip()
def_question = input("Do you wish to add or remove from the file(s) name? (a/r): ").strip().lower()
delete = input("Would you like to delete duplicate files? (y/n): ").strip().lower()

#veriables
end_image = Image.new(mode = "RGB",size = (200, 70), color = "red")
end_image.save(path +"/zzz999.png")
files = os.listdir(path)
files.sort()
image1 =files[0]
counter = 1
im1 = " "


def add():
     global im1
     global image1
     global counter
     for file in files:
          original_file_name, file_ext = (os.path.splitext(file))
          if delete == "y":
               if image1 == file:
                    pass
               elif image1 != file:
                    im1 = Image.open(path + "/" + image1).histogram() #the image to be compared too
                    im2 = Image.open(path + "/" + file).histogram()#file for comparison
                    if im1 == im2:
                          send2trash(path + "/" +file)
                          counter = counter +1
                    elif im1 != im2:
                          os.rename(path + "/" + image1, path + "/" + image1 + "_X" +str(counter))
                          counter = 1
                          image1 = file
                    else:
                         print("something went wrong")
          else:
               addd = input("Enter in the text you wish to be added/removed (can not contain blank spaces): ").strip()
               new_name = "{}{}{}".format(original_file_name, addd, file_ext).strip()
               os.rename(path + "/" + file, path + "/" + new_name)
     print("Job Complete")
     send2trash(path + "/zzz999.png")

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
     addd = input("Enter in the text you wish to be added/removed (can not contain blank spaces): ").strip()
     remove()
else:
     print("I don't understand your command")
#print(files)


