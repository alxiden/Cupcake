import os
from PIL import ImageChops, ImageDraw
import PIL.Image
import shutil
#from send2trash import send2trash
from tkinter import *

root = Tk()

root.title("Cupcake 3.0")

paths = Entry(root, width = 50, borderwidth = 5)
paths.grid(row = 2, column =2, columnspan =3)
path = paths.get()

def folder():
     folders = os.listdir(paths.get())
     folders.sort()
     for folder in folders:
          original_file_name, file_ext = (os.path.splitext(folder))
          if file_ext != "":
               add()
          else:
               p = paths.get() + "/"+ folder
               end_image = PIL.Image.new(mode = "RGB",size = (200, 70), color = "red")
               end_image.save(path +"/zzz999.png")
               files = os.listdir(p)
               files.sort()
               image1 =files[0]
               counter = 1
               im1 = " "
          for file in files:
               original_file_name, file_ext = (os.path.splitext(file))
               if file_ext == ".ini":
                    pass
               elif delete == 0:
                    ofn, fe = (os.path.splitext(image1))
                    if image1 == file:
                         pass
                    elif image1 != file:
                         im1 = PIL.Image.open(p + "/" + image1).histogram() #the image to be compared too
                         im2 = PIL.Image.open(p + "/" + file).histogram()#file for comparison
                         if im1 == im2:
                              os.remove(p + "/" + file)
                              counter = counter +1
                         elif im1 != im2:
                               os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                               counter = 1
                               image1 = file
                         else:
                               print("something went wrong")
               else:
                    addd = input("Enter in the text you wish to be added/removed (can not contain blank spaces): ").strip()
                    new_name = "{}{}{}".format(original_file_name, addd, file_ext).strip()
                    os.rename(path + "/" + file, p + "/" + new_name)
          print("Job Complete")
          os.remove(p + "/zzz999.png")

def add():
     end_image = PIL.Image.new(mode = "RGB",size = (200, 70), color = "red")
     end_image.save(paths.get() +"/zzz999.png")
     files = os.listdir(paths.get())
     files.sort()
     image1 =files[0]
     counter = 1
     im1 = " "
     for file in files:
          original_file_name, file_ext = (os.path.splitext(file))
          if file_ext == ".ini":
               pass
          elif delete == 0:
               ofn, fe = (os.path.splitext(image1))
               if image1 == file:
                    pass
               elif image1 != file:
                    im1 = PIL.Image.open(paths.get() + "/" + image1).histogram() #the image to be compared too
                    im2 = PIL.Image.open(paths.get() + "/" + file).histogram()#file for comparison
                    if im1 == im2:
                         os.remove(paths.get() + "/" + file)
                         counter = counter +1
                    elif im1 != im2:
                          os.rename(paths.get() + "/" + image1, paths.get() + "/" + ofn + "_X" +str(counter)+ fe)
                          counter = 1
                          image1 = file
                    else:
                          print("something went wrong")
          else:
               addd = input("Enter in the text you wish to be added/removed (can not contain blank spaces): ").strip()
               new_name = "{}{}{}".format(original_file_name, addd, file_ext).strip()
               os.rename(path + "/" + file, path + "/" + new_name)
     print("Job Complete")
     os.remove(paths.get() + "/zzz999.png")
     

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

l2 = Label (root, text = "Enter text you want removed (leave blank if n/a): ").grid(row = 6, column = 2)
rem = Entry(root, width = 50, borderwidth = 5)
rem.grid(row = 7, column =2, columnspan =3)
remo=rem.get().strip()

de = IntVar()
c = Checkbutton(root, text = "Do you wish to delete duplicate files?", variable = de)
c.grid(row = 8, column =2, sticky = W)
delete = de.get()

fo = IntVar()
c = Checkbutton(root, text = "Are there Multiple folders?", variable = fo)
c.grid(row = 9, column =2, sticky = W)
mfolder = fo.get()

def run():
     #print(d.get())
     #print(def_question)
     if d.get() == 1 and fo.get() == 1:
          folder()
     elif d.get() ==1:
          add()
     elif d.get() == 2:
          remove()
     else:
          print("I don't understand your command")

def remove():
     files = os.listdir(paths.get())
     files.sort()
     for file in files:
          original_file_name, file_ext = (os.path.splitext(file))
          #print(remo)
          new_name = original_file_name.replace(rem.get(), "").strip()
          os.rename(paths.get() + "/" + file, paths.get() + "/" + new_name)
     print("Job Complete")

        
submit = Button(root, text = "Run", command =lambda: run())
submit.grid(row = 10, column =2)


root.mainloop()

