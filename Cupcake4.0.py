import os
from PIL import ImageChops, ImageDraw
import PIL.Image
import shutil
from tkinter import *
from zipfile import ZipFile

root = Tk()

root.title("Cupcake 4.0")

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
     folders = os.listdir(paths.get())
     folders.sort()
     for folder in folders:
          original_file_name, file_ext = (os.path.splitext(folder))
          if file_ext != "":
               add()
          else:
               p = paths.get() + "/"+ folder
               files = os.listdir(p)
               files.sort()
               image1 =files[0]
               imagelast = files[-1]
               counter = 1
               im1 = " "
               for file in files:
                    orfn, file_ext = (os.path.splitext(file))
                    if "_X" in orfn:
                         break
                    if file_ext == ".ini":
                         pass
                    elif delete == 0:
                         ofn, fe = (os.path.splitext(image1))
                         if image1 == file:
                              pass
                         elif image1 != file:
                              im1 = PIL.Image.open(p + "/" + image1).histogram() #the image to be compared too
                              im2 = PIL.Image.open(p + "/" + file).histogram()#file for comparison
                              if im1 == im2 and file == imagelast:
                                   counter = counter +1
                                   os.remove(p + "/" + file)
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                              elif im1 == im2:
                                   counter = counter +1
                                   os.remove(p + "/" + file)
                              elif im1 != im2 and file == imagelast:
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                                   counter = 1
                                   os.rename(p+ "/" + file, p + "/" + orfn + "_X" + str(counter) + fe)
                              elif im1 != im2:
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                                   image1 = file
                                   counter = 1
                              else:
                                    wrong()
                    else:
                         new_name = "{}{}{}".format(original_file_name, addd, file_ext).strip()
                         os.rename(path + "/" + file, p + "/" + new_name)
               com()

def add():
     p = paths.get()
     files = os.listdir(p)
     files.sort()
     image1 =files[0]
     imagelast = files[-1]
     counter = 1
     im1 = " "
     for file in files:
          orfn, file_ext = (os.path.splitext(file))
          if file_ext == ".ini":
               pass
          elif delete == 0:
               ofn, fe = (os.path.splitext(image1))
               if image1 == file:
                    pass
               elif image1 != file:
                    im1 = PIL.Image.open(p + "/" + image1).histogram() #the image to be compared too
                    im2 = PIL.Image.open(p + "/" + file).histogram()#file for comparison
                    if im1 == im2 and file == imagelast:
                         counter = counter +1
                         os.remove(p + "/" + file)
                         os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                    elif im1 == im2:
                         counter = counter +1
                         os.remove(p + "/" + file)
                    elif im1 != im2 and file == imagelast:
                         os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                         counter = 1
                         os.rename(p+ "/" + file, p + "/" + orfn + "_X" + str(counter) + fe)
                    elif im1 != im2:
                         os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                         image1 = file
                         counter = 1
                    else:
                         wrong()
          else:
               new_name = "{}{}{}".format(original_file_name, addd, file_ext).strip()
               os.rename(path + "/" + file, p + "/" + new_name)
     com()
     

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
          new_name = original_file_name.replace(rem.get(), "").strip()
          os.rename(paths.get() + "/" + file, paths.get() + "/" + new_name)
     print("Job Complete")


submit = Button(root, text = "Run", command =lambda: run())
submit.grid(row = 10, column =2)

ziprun = Button(root, text = "Zip", command =lambda: Zip())
ziprun.grid(row = 10, column =3)


root.mainloop()

