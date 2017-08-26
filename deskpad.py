#coding: utf-8
try:
	from multiprocessing import Process
	from random import *
	from time import *
	import os
	from tkinter import *
except:
    print("Error in Import Packages...")
    exit()
   
from tkinter import filedialog

class main():
	def __init__(self):
		print("notepad(msg): Initialized a engine...")
		self.getversion()
		self.principalvm()
	
	def getversion(self):
		verfile1 = open('./.programs/conf.d/deskpad/version.txt')
		self.version = verfile1.read()
		verfile1.close()
		print("notepad(msg): Version:. "+ self.version)

	def principalvm(self):
		# Window definition
		self.root = Tk()
		self.root.geometry("500x500")
		self.root.title("Deskpad - ProEditor")
		# Widgets --- Scrollbar
		scrollbar = Scrollbar(self.root)
		scrollbar.pack(side=RIGHT, fill=Y)
		# Widgets --- Menu
		self.menu1 = Menu(self.root)
		filemenu = Menu(self.menu1, tearoff=0)
		filemenu.add_command(label="Save", command=self.event_save_file)
		filemenu.add_command(label="Open", command=self.event_open_file)
		self.menu1.add_cascade(label="Archive", menu=filemenu)
		helpmenu = Menu(self.menu1)
		helpmenu.add_command(label="About", command=self.event_about_file)
		self.menu1.add_cascade(label="Help", menu=helpmenu)
		self.root.config(menu=self.menu1)
		# Text área...
		self.text = Text(self.root)
		self.text.pack(expand=YES, fill=BOTH)
		# Setup a ScrollBar
		self.text.config(yscrollcommand=scrollbar.set)
		scrollbar.config(command=self.text.yview)
		# Mainloop
		self.root.mainloop()
			
	def event_save_file(self):
		fileName = filedialog.asksaveasfilename()
		try:
			file1 = open(fileName, 'w')
			textoutput = self.text.get(0.0, END)
			file1.write(textoutput)
		except:
			pass
		finally:
			file1.close()
	
	def event_open_file(self):
		fileName = filedialog.askopenfilename()
		try:
			file1 = open(fileName, 'r')
			contents = file1.read()
			self.text.delete(0.0, END)
			self.text.insert(0.0, contents)
		except:
			pass
	
	def event_about_file(self):
		root1 = Tk()
		root1.wm_title("Info")
		info1 = Label(root1, text=self.version)
		info1.pack()
		root1.mainloop()
		
		
main()
