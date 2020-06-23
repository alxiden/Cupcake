import os
from PIL import ImageChops, ImageDraw
import PIL.Image
import shutil
from tkinter import *
from zipfile import ZipFile

root = Tk()

root.title("Cupcake 4.0")

p = " "

paths = Entry(root, width = 50, borderwidth = 5)
paths.grid(row = 2, column =2, columnspan =3)
path = paths.get()

row = 11

def Zip():
     zips = os.listdir(paths.get())
     zips.sort()
     for z in zips:
          ofin,f_e = (os.path.splitext(z))
          if f_e == ".zip":
               os.makedirs(paths.get()+ "/" +ofin)
               location = paths.get() +"/" + ofin
               with ZipFile(paths.get()+ "/" + z, "r") as zipObj:
                    zipObj.extractall(location)
          
          else:
               pass


def wrong():
     global row
     wro = Lable(root, text = "Something went wrong, please tell the programer the error and he will fix it")
     wro.grid(row = row, column = 2, columnspan = 3)
     row = row + 1

def com():
     global row
     com = Label(root, text = "Job Complete")
     com.grid(row = row , column = 2)
     row = row +1

def folder():
     global p
     folders = os.listdir(paths.get())
     folders.sort()
     for folder in folders:
          if os.path.isdir(paths.get() + "/"+ folder):
               p = paths.get() + "/"+ folder
               if p == paths.get():
                    pass
               else:
                    if d.get() == 1:
                         add2()
                    else:
                         add()
          elif os.path.isfile(paths.get() + "/"+ folder):
               p = paths.get()
               add()
          else:
               wrong()

def add():
     files = os.listdir(p)
     files.sort()
     image1 =files[0]
     imagelast = files[-1]
     counter = 1
     im1 = " "
     for file in files:
          orfn, file_ext = (os.path.splitext(file))
          pa = p + "/" + file
          if os.path.isdir(pa):
               pass
          else:
               if file_ext == ".ini":
                    pass
               elif d.get() == 1:
                    ofn, fe = (os.path.splitext(image1))
                    if image1 == file:
                         pass
                    elif image1 != file:
                         if os.path.isdir(p+"/"+image1): #Checks to see if im1 is a directory
                              im1 = "adsfrg"
                              im2 = PIL.Image.open(p + "/" + file).histogram()
                         else:     
                              im1 = PIL.Image.open(p + "/" + image1).histogram() #the image to be compared too
                              im2 = PIL.Image.open(p + "/" + file).histogram()#file for comparison
                         if im1 == im2 and file == imagelast:
                              if os.path.isdir(p+"/"+image1) and os.path.isfile(pa):
                                   os.rename(pa, p + "/" + orfn + "_X" + str(counter) + fe)
                              else:
                                   counter = counter +1
                                   os.remove(pa)
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                         elif im1 == im2:
                              counter = counter +1
                              os.remove(pa)
                         elif im1 != im2 and file == imagelast:
                              if os.path.isdir(p+"/"+image1) and os.path.isfile(pa):
                                   os.rename(pa, p + "/" + orfn + "_X" + str(counter) + fe)
                              else:
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                                   counter = 1
                                   os.rename(pa, p + "/" + orfn + "_X" + str(counter) + fe)
                         elif im1 != im2:
                              if os.path.isdir(p+"/"+image1) and os.path.isfile(pa):
                                   os.rename(pa, p + "/" + orfn + "_X" + str(counter) + fe)
                              else:
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                                   image1 = file
                                   counter = 1
                         else:
                              wrong()
               else:
                    add2()


def add2():
     files = os.listdir(p)
     files.sort()
     for file in files:
          orfn, file_ext = (os.path.splitext(file))
          new_name = "{}{}{}".format(orfn, rem.get(), file_ext).strip()
          os.rename(p + "/" + file, p + "/" + new_name)
     
     

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
Radiobutton(root, text = "Auto", variable = d, value = 3,anchor = W).grid(row = 5, column = 2, sticky = W)
def_question = d.get()

l2 = Label (root, text = "Enter text you want added/removed (leave blank if n/a): ").grid(row = 6, column = 2)
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
     if fo.get() == 1: #multiple folders
          folder()
     elif d.get() ==1: #adding to the file name
          add2()
     elif d.get() == 2: #removing
          remove()
     else:
          wrong()
     com()

def remove():
     files = os.listdir(paths.get())
     files.sort()
     for file in files:
          original_file_name, file_ext = (os.path.splitext(file))
          new_name = original_file_name.replace(rem.get(), "").strip()
          os.rename(paths.get() + "/" + file, paths.get() + "/" + new_name)



submit = Button(root, text = "Run", command =lambda: run())
submit.grid(row = 10, column =2)

ziprun = Button(root, text = "Zip", command =lambda: Zip())
ziprun.grid(row = 10, column =3)


root.mainloop()

