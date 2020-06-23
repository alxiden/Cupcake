import os
from PIL import ImageChops, Image, ImageDraw
import shutil
from send2trash import send2trash
from tkinter import *

root = Tk()

root.title("Cupcake 3.0")

paths = Entry(root, width = 50, borderwidth = 5)
paths.grid(row = 2, column =2, columnspan =3)
path = paths.get()

#end_image = Image.new(mode = "RGB",size = (200, 70), color = "red")
#end_image.save(paths.get() +"/zzz999.png")


def add():
     files = os.listdir(paths.get())
     files.sort()
     image1 =files[0]
     counter = 1
     im1 = " "
     for file in files:
          original_file_name, file_ext = (os.path.splitext(file))
          if delete == 0:
               if image1 == file:
                    pass
               elif image1 != file:
                    im1 = Image.open(paths.get() + "/" + image1).histogram() #the image to be compared too
                    im2 = Image.open(paths.get() + "/" + file).histogram()#file for comparison
                    if im1 == im2:
                          send2trash(paths.get() + "/" +file)
                          counter = counter +1
                    elif im1 != im2:
                          os.rename(paths.get() + "/" + image1, paths.get() + "/" + image1 + "_X" +str(counter))
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


welcome = Label(root, text = "Welcome to Cupcake 3.0")
welcome.grid(row = 0, column =2, columnspan =3)

l1 = Label (root, text = "Please enter the path to your folder: ")
l1.grid(row = 1, column =2, columnspan =3)

paths = Entry(root, width = 50, borderwidth = 5)
paths.grid(row = 2, column =2, columnspan =3)
path = paths.get()

d = IntVar()
Radiobutton(root, text = "Add", variable = d, value = 1, anchor = W).grid(row = 3, column = 2, sticky = W)
Radiobutton(root, text = "Remove", variable = d, value = 2,anchor = W).grid(row = 4, column = 2, sticky = W)
def_question = d.get()

de = IntVar()
c = Checkbutton(root, text = "Do you wish to delete duplicate files?", variable = de)
c.grid(row = 5, column =2, sticky = W)
delete = de.get()


def run():
     print(d.get())
     print(def_question)
     if d.get() == 1:
          add()
     elif d.get() == 2:
          addd = input("Enter in the text you wish to be added/removed (can not contain blank spaces): ").strip()
          remove()
     else:
          print("I don't understand your command")
submit = Button(root, text = "Run", command =lambda: run())
submit.grid(row = 6, column =2)


root.mainloop()



#veriables
#end_image = Image.new(mode = "RGB",size = (200, 70), color = "red")
#end_image.save(path +"/zzz999.png")
#files = os.listdir(path)
#files.sort()
#image1 =files[0]
#counter = 1
#im1 = " "


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
