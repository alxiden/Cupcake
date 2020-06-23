import os
from PIL import ImageChops, ImageDraw
import PIL.Image
import shutil
from tkinter import *
from tkinter import messagebox
from zipfile import ZipFile

root = Tk()

root.title("Cupcake 4.4")

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
     messagebox.showerror("Error", "Something went wrong")

def com():
     messagebox.showinfo("Title", "Job Complete")

def folder():
     global p
     folders = os.listdir(paths.get())
     folders.sort()
     for folder in folders:
          if os.path.isdir(paths.get() + "/"+ folder):
               p = paths.get() + "/"+ folder
               if p == paths.get():
                    pass
               elif d.get() == 1:
                    add2()
               elif d.get() == 3:
                    add()
               elif d.get() == 2:
                    remove()
               else:
                    wrong()
          elif os.path.isfile(paths.get() + "/"+ folder):
               p = paths.get()
               if d.get() == 1:
                    add2()
               elif d.get() == 3:
                    add()
               elif d.get() == 2:
                    remove()
               else:
                    pass
          else:
               pass

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
               elif de.get() == 1 or de.get() == 0:
                    ofn, fe = (os.path.splitext(image1))
                    if image1 == file:
                         pass
                    elif image1 != file:
                         if os.path.isdir(p+"/"+image1): #Checks to see if im1 is a directory
                              #print("1")
                              im1 = "adsfrg"
                              im2 = PIL.Image.open(p + "/" + file).histogram()
                         else:
                              #print("2")
                              im1 = PIL.Image.open(p + "/" + image1).histogram() #the image to be compared too
                              im2 = PIL.Image.open(p + "/" + file).histogram()#file for comparison
                         if im1 == im2 and file == imagelast:
                              #print("3")
                              if os.path.isdir(p+"/"+image1) and os.path.isfile(pa):
                                   #print("4")
                                   os.rename(pa, p + "/" + orfn + "_X" + str(counter) + fe)
                              else:
                                   #print("5")
                                   counter = counter +1
                                   if de.get() == 1:
                                        #print("6")
                                        os.remove(pa)
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                         elif im1 == im2:
                              #print("7")
                              counter = counter +1
                              if de.get() == 1:
                                   #print("7")
                                   os.remove(pa)
                         elif im1 != im2 and file == imagelast:
                              #print("8")
                              if os.path.isdir(p+"/"+image1) and os.path.isfile(pa):
                                   #print("9")
                                   os.rename(pa, p + "/" + orfn + "_X" + str(counter) + fe)
                              else:
                                   #print("10")
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                                   counter = 1
                                   os.rename(pa, p + "/" + orfn + "_X" + str(counter) + fe)
                         elif im1 != im2:
                              #print("11")
                              if os.path.isdir(p+"/"+image1) and os.path.isfile(pa):
                                   #print("12")
                                   os.rename(pa, p + "/" + orfn + "_X" + str(counter) + fe)
                              else:
                                   #print("13")
                                   os.rename(p + "/" + image1, p + "/" + ofn + "_X" +str(counter)+ fe)
                                   image1 = file
                                   counter = 1
                         else:
                              pass
               else:
                    add2()


def add2():
     files = os.listdir(p)
     files.sort()
     for file in files:
          pa = p + "/" + file
          if os.path.isdir(pa):
               #print("13")
               pass
          else:
               #print("14")
               orfn, file_ext = (os.path.splitext(file))
               new_name = "{}{}{}".format(orfn, rem.get(), file_ext).strip()
               os.rename(pa, p + "/" + new_name)
     
     

welcome = Label(root, text = "Welcome to Cupcake 4.4")
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
c = Checkbutton(root, text = "Do you wish to delete duplicate files?(Only works in auto mode)", variable = de)
c.grid(row = 8, column =2,columnspan = 3, sticky = W)
delete = de.get()

#fo = IntVar()
#c = Checkbutton(root, text = "Are there Multiple folders?", variable = fo)
#c.grid(row = 9, column =2, sticky = W)
#mfolder = fo.get()

def run():
     if d.get() == 1 or d.get() == 2 or d.get() == 3:
          folder()
     else:
          wrong()
     com()

def remove():
     files = os.listdir(p)
     files.sort()
     for file in files:
          pa = p + "/" + file
          if os.path.isdir(pa):
               pass
          else:
               original_file_name, file_ext = (os.path.splitext(file))
               new_name = original_file_name.replace(rem.get(), "").strip()
               os.rename(pa, p + "/" + new_name)



submit = Button(root, text = "Run", command =lambda: run())
submit.grid(row = 10, column =2)

ziprun = Button(root, text = "Zip", command =lambda: Zip())
ziprun.grid(row = 10, column =3)


root.mainloop()

