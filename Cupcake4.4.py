import os
from tkinter import *
from tkinter import messagebox
from PIL import Image
from zipfile import ZipFile

root = Tk()
root.title("Cupcake 4.4")

p = ""

row = 11

# Main frame for nicer layout
main_frame = Frame(root, padx=12, pady=12)
main_frame.grid(sticky="nsew")
root.columnconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(2, weight=1)

def Zip():
    dir_path = paths.get()
    zips = os.listdir(dir_path)
    zips.sort()
    for z in zips:
        ofin, f_e = os.path.splitext(z)
        if f_e.lower() == ".zip":
            location = os.path.join(dir_path, ofin)
            os.makedirs(location, exist_ok=True)
            with ZipFile(os.path.join(dir_path, z), "r") as zipObj:
                zipObj.extractall(location)


def show_help():
     guide = Toplevel(root)
     guide.title("Cupcake 4.4 — User Guide")
     guide.geometry("600x400")
     guide_frame = Frame(guide, padx=8, pady=8)
     guide_frame.pack(fill="both", expand=True)

     scrollbar = Scrollbar(guide_frame)
     scrollbar.pack(side="right", fill="y")

     text = Text(guide_frame, wrap="word", yscrollcommand=scrollbar.set)
     text.pack(fill="both", expand=True)
     scrollbar.config(command=text.yview)

     GUIDE_TEXT = (
          "Cupcake 4.4 - User Guide\n\n"
          "Overview:\n"
          "  Cupcake automates filename edits and simple duplicate removal for images.\n\n"
          "Fields and controls:\n"
          "  - Path: enter the folder path containing the files to process.\n"
          "  - Mode (Add / Remove / Auto):\n"
          "      Add: appends the text from the 'Enter text...' field to filenames.\n"
          "      Remove: removes occurrences of that text from filenames.\n"
          "      Auto: attempts to detect duplicate images and rename or remove accordingly.\n"
          "  - Delete duplicates checkbox: when enabled in Auto mode, duplicate files will be removed.\n\n"
          "Buttons:\n"
          "  - Run: performs the selected operation on the specified path.\n"
          "  - Zip: extracts any .zip files found inside the provided path into folders named after the zip.\n\n"
          "Examples:\n"
          "  - Rename files by adding '_v2': choose Add and enter '_v2' in the text field, set Path, then Run.\n"
          "  - Remove a suffix: choose Remove, enter the suffix text, set Path, then Run.\n\n"
          "Notes and warnings:\n"
          "  - Always double-check the selected folder. Operations will rename or delete files.\n"
          "  - The Auto mode uses image histograms to detect exact duplicates; it's conservative but may still rename files.\n"
          "  - Back up important files before running mass operations.\n\n"
          "Troubleshooting:\n"
          "  - If you see errors about paths, ensure the Path field points to an existing directory.\n"
          "  - For PIL errors, ensure Pillow is installed: `pip install pillow`.\n\n"
     )

     text.insert("1.0", GUIDE_TEXT)
     text.config(state="disabled")

     close = Button(guide_frame, text="Close", command=guide.destroy)
     close.pack(pady=6)


def wrong():
     messagebox.showerror("Error", "Something went wrong")

def com():
     messagebox.showinfo("Title", "Job Complete")

def folder():
     global p
     base = paths.get()
     folders = os.listdir(base)
     folders.sort()
     for folder in folders:
        folder_path = os.path.join(base, folder)
        if os.path.isdir(folder_path):
            p = folder_path
            if p == base:
                continue
            elif d.get() == 1:
                add2()
            elif d.get() == 3:
                add()
            elif d.get() == 2:
                remove()
            else:
                wrong()
        elif os.path.isfile(folder_path):
            p = base
            if d.get() == 1:
                add2()
            elif d.get() == 3:
                add()
            elif d.get() == 2:
                remove()
            else:
                pass

def add():
     files = os.listdir(p)
     files.sort()
     image1 = files[0]
     imagelast = files[-1]
     counter = 1
     im1 = ""
     for file in files:
          orfn, file_ext = os.path.splitext(file)
          pa = os.path.join(p, file)
          if os.path.isdir(pa):
               continue
          else:
               if file_ext == ".ini":
                    continue
               elif de.get() == 1 or de.get() == 0:
                    ofn, fe = os.path.splitext(image1)
                    if image1 == file:
                         continue
                    elif image1 != file:
                         if os.path.isdir(os.path.join(p, image1)):
                              im1 = "dir"
                              im2 = Image.open(os.path.join(p, file)).histogram()
                         else:
                              im1 = Image.open(os.path.join(p, image1)).histogram()
                              im2 = Image.open(os.path.join(p, file)).histogram()
                         if im1 == im2 and file == imagelast:
                              if os.path.isdir(os.path.join(p, image1)) and os.path.isfile(pa):
                                   os.rename(pa, os.path.join(p, orfn + "_X" + str(counter) + fe))
                              else:
                                   counter += 1
                                   if de.get() == 1:
                                        os.remove(pa)
                                   os.rename(os.path.join(p, image1), os.path.join(p, ofn + "_X" + str(counter) + fe))
                         elif im1 == im2:
                              counter += 1
                              if de.get() == 1:
                                   os.remove(pa)
                         elif im1 != im2 and file == imagelast:
                              if os.path.isdir(os.path.join(p, image1)) and os.path.isfile(pa):
                                   os.rename(pa, os.path.join(p, orfn + "_X" + str(counter) + fe))
                              else:
                                   os.rename(os.path.join(p, image1), os.path.join(p, ofn + "_X" + str(counter) + fe))
                                   counter = 1
                                   os.rename(pa, os.path.join(p, orfn + "_X" + str(counter) + fe))
                         elif im1 != im2:
                              if os.path.isdir(os.path.join(p, image1)) and os.path.isfile(pa):
                                   os.rename(pa, os.path.join(p, orfn + "_X" + str(counter) + fe))
                              else:
                                   os.rename(os.path.join(p, image1), os.path.join(p, ofn + "_X" + str(counter) + fe))
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
          pa = os.path.join(p, file)
          if os.path.isdir(pa):
               continue
          else:
               orfn, file_ext = os.path.splitext(file)
               new_name = "{}{}{}".format(orfn, rem.get(), file_ext).strip()
               os.rename(pa, os.path.join(p, new_name))
     
     


welcome = Label(main_frame, text="Welcome to Cupcake 4.4")
welcome.grid(row=0, column=0, columnspan=2, pady=(0, 8), sticky="w")

# Help icon/button at top-right
help_btn = Button(main_frame, text="❓", command=show_help, width=3, relief="flat")
help_btn.grid(row=0, column=2, sticky="e")

l1 = Label(main_frame, text="Please enter the path to your folder:")
l1.grid(row=1, column=0, columnspan=3, sticky="w", pady=4)

paths = Entry(main_frame, width=60, borderwidth=5)
paths.grid(row=2, column=0, columnspan=3, sticky="ew", padx=2, pady=4)
path = paths.get()

d = IntVar()
Radiobutton(main_frame, text="Add", variable=d, value=1, anchor=W).grid(row=3, column=0, sticky=W, pady=2)
Radiobutton(main_frame, text="Remove", variable=d, value=2, anchor=W).grid(row=4, column=0, sticky=W, pady=2)
Radiobutton(main_frame, text="Auto", variable=d, value=3, anchor=W).grid(row=5, column=0, sticky=W, pady=2)
def_question = d.get()

l2 = Label(main_frame, text="Enter text you want added/removed (leave blank if n/a):")
l2.grid(row=6, column=0, sticky="w", pady=(8, 2))
rem = Entry(main_frame, width=60, borderwidth=5)
rem.grid(row=7, column=0, columnspan=3, sticky="ew", padx=2, pady=4)
remo = rem.get().strip()

de = IntVar()
c = Checkbutton(main_frame, text="Do you wish to delete duplicate files? (Only works in auto mode)", variable=de)
c.grid(row=8, column=0, columnspan=3, sticky=W, pady=4)
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
          pa = os.path.join(p, file)
          if os.path.isdir(pa):
               continue
          else:
               original_file_name, file_ext = os.path.splitext(file)
               new_name = original_file_name.replace(rem.get(), "").strip()
               os.rename(pa, os.path.join(p, new_name + file_ext))




# Centered larger buttons with standout style
button_container = Frame(main_frame, padx=6, pady=6)
button_container.grid(row=10, column=1)
submit = Button(
     button_container,
     text="Run",
     command=run,
     width=14,
     height=2,
     bg="#4CAF50",
     fg="white",
     activebackground="#45a049",
     font=("Segoe UI", 10, "bold"),
     relief="raised",
     bd=3,
)
ziprun = Button(
     button_container,
     text="Zip",
     command=Zip,
     width=14,
     height=2,
     bg="#2196F3",
     fg="white",
     activebackground="#1976D2",
     font=("Segoe UI", 10, "bold"),
     relief="raised",
     bd=3,
)
submit.pack(side="left", padx=10)
ziprun.pack(side="left", padx=10)


root.mainloop()

