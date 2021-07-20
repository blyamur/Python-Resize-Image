import os
import shutil
import random
import string
import webbrowser
from os import path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageEnhance

__author__ = "Mons (https://blog.mons.ws)"

# Settings start
factor = 2   # image enhancement rate
basewidth = 1920  #  the size to which we reduce the images
#  Settings end 

new = 1
url = "https://blog.mons.ws"
root = Tk()
root.title("Image\Resizer - "+str(basewidth)) #  Window title
root.configure(background='#E5E5E6') # Common window background

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 #  Mid-screen
h = h//2 
w = w - 200 # Offset from the middle
h = h - 200
root.geometry('460x230+{}+{}'.format(w, h)) # Search for center center and placement windows in the center

#root.wm_iconbitmap('icon.ico') # If you have the need to have an icon in an application, uncomment
#root.maxsize('460', '230') # Uncomment  if necessary, change the window size
#root.minsize('460', '230') # Uncomment if necessary, change the window size
root.resizable(False, False) # Disable sizes. Comment, if necessary, change the window size
def open_file():
	try:
		file_open = filedialog.askopenfilename(title='Please select an Image', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png'])])
		full_name = path.basename(file_open) #  Current image title
		file_dir = os.path.dirname(os.path.abspath(file_open)) # path to the source folder
		dir_name = path.splitext(full_name)[0] #   name
		new_name = ''.join(random.choice(string.ascii_letters) for _ in range(16))+'_'+dir_name+'_'+str(basewidth)# New name
		ext_name = path.splitext(full_name)[1] # extension
		fl = Label(text=str(full_name[:45])+'...', foreground="#36514A",background="#E5E5E6", # Current name 45 characters
			padx="2", pady="2", font="10").place(relx = 0.5, 
			rely = 0.65,
			anchor = 'center')
		if ext_name.lower().endswith(('.jpeg', '.jpg', '.png')):
			try:
				img = Image.open(file_open)
				wpercent = (basewidth/float(img.size[0]))
				hsize = int((float(img.size[1])*float(wpercent)))
				img = img.resize((basewidth,hsize), Image.ANTIALIAS)
				enhancer = ImageEnhance.Sharpness(img)
				img = enhancer.enhance(factor)
				img.save(file_dir + '/' + new_name + ext_name)
				messagebox.showinfo("Done"," The image is reduced!\n" ) #Image size change
				
			except:
				messagebox.showerror("Error", " Something went wrong!") #Something went wrong
		else:
			messagebox.showerror("Error", " This is not an Image! \n Please select another file!") #This is not an image! Select another file
	except:
		messagebox.showerror("Error", " Restart the program!") #Restart the program

def openweb():
	webbrowser. open(url, new=new)

Label(root, text = 'Select Image',font =('Verdana', 14),foreground=('#424242'),background=('#E5E5E6')).pack(side = TOP, pady = 10) # Select an image
errmsg = 'Error!'
select_button = Button(text="Select a file",background="#4B8CBF",foreground="#FFFFFF",padx="10",pady="8",border="0",font="16",command=open_file).place(relx = 0.5,rely = 0.45,anchor = 'center') # Select a file
copy_right = Button(text="© 2021 Mons", foreground="#36514A",background="#E5E5E6", activebackground="#E5E5E6",border="0",activeforeground="#7AB900",
				padx="15", pady="6", font=("Verdana", 8),cursor="hand2",relief=FLAT,command=openweb).pack(side=BOTTOM)
root.mainloop()
