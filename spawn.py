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

class main():
	def __init__(self):
		self.clear_cache_spkg()
		self.hostget()
		self.versionget()
		self.winprincipal()

	def error_win(self, errortype, code):
		error1 = Tk()
		error1.geometry("290x200")
		error1.title("Error, Code: "+ errortype)
		# Widgets
		label1 = Label(error1, text="Error type:.")
		label2 = Label(error1, text=code)
		button3 = Button(error1, text="Exit", command=self.end_spawn)
		# Packing things
		label1.pack()
		label2.pack()
		button3.pack()

	def end_spawn(self):
		exit()

	def winprincipal(self):
		# window definition
		self.root = Tk()
		print("spawn[msg]: defined win principal")
		self.root.geometry("250x250")
		self.root.title("(Spawn Package)@-@("+ str(self.hostname)+ "):")
		# Widgets
		self.label1 = Label(self.root, text="Spawn Package for System:. 1.1.000")
		self.entry1 = Entry(self.root)
		self.entry1.insert(0, "you program...")
		self.button1 = Button(self.root, text="[INSTALL]", command=self.event_get_entry)
		self.menu1 = Menu(self.root)
		appmenu = Menu(self.menu1, tearoff=0)
		appmenu.add_command(label="Install", command=self.event_get_entry)
		appmenu.add_command(label="Uninstall", command=self.event_get_entry_uninstall)
		appmenu.add_command(label="Clear (.spawnTmp)", command=self.clear_cache)
		appmenu.add_command(label="Clear Cache", command=self.clear_cache_spkg)
		appmenu.add_separator()
		appmenu.add_command(label="Exit", command=self.exitsys)
		self.menu1.add_cascade(label="Operations", menu=appmenu)
		helpmenu = Menu(appmenu, tearoff=0)
		helpmenu.add_command(label="About", command=self.infowin)
		self.menu1.add_cascade(label="Help", menu=helpmenu)
		# Button pack
		self.label1.pack(side=TOP)
		self.entry1.pack(side=LEFT)
		self.button1.pack(side=RIGHT)
		self.root.config(menu=self.menu1)
		# rootmainloop
		self.root.mainloop()

	def clear_cache_spkg(self):
		print("Clearing a All .spkg")
		os.system("rm ./*.spkg")

	def clear_cache(self):
		print("Clearing Cache...")
		os.system("rm -rf ./.spawnTmp/program1/*")

	def exitsys(self):
		exit()

	def infowin(self):
		self.infowin = Tk()
		self.infowin.title("Sobre")
		self.labelp = Label(self.infowin, text="Spawn Package Manager by: Andrew")
		self.labelp.pack()
		self.infowin.mainloop()

	def event_get_entry(self):
		self.program = self.entry1.get()
		self.spawn()

	def event_get_entry_uninstall(self):
		self.uninstall = self.entry1.get()
		if(self.uninstall=="main.py"):
			self.error_win("10", "Not Uninstall apps of System...")
		elif(self.uninstall=="desktop.py"):
			self.error_win("10", "Not Uninstall apps of System...")
		elif(self.uninstall=="spawn.py"):
			self.error_win("(1)", "Kernel Panic... Error in System (Logic)")
		elif(self.uninstall=="*.py"):
			self.error_win("10", "Spawn Package not have a perm for delete fs(1):")
		else:
			pass

		try:
			appexist = open('./.programs/conf.d/spawn/appexist-list/'+ self.uninstall)
			appexist.read()
			appexist.close()
			print("App Exist [!] Uninstalling...")
			uninstall1 = True
		except:
			print("App Not exist")
			uninstall1 = False
			self.error_win("8", "App Not Exist... not uninstalling")

		if(uninstall1==True):
			os.system("rm ./.programs/"+ self.uninstall)
			os.system("rm ./.programs/conf.d/spawn/appexist-list/"+ self.uninstall)
			os.system("rm ./"+ self.uninstall)
		else:
			pass

	def spawn(self):
		try:
			portfileversion = open('./.programs/ports/version.txt', 'r+')
			self.portversion = portfileversion.read()
			portfileversion.close()
			self.port_compiler()
		except:
			self.error_win("Error in Ports Version...")

	def port_compiler(self):
		try:
			print("debug:. Copying from ports the program...")
			command1 = "cp -r ./.programs/ports/" + self.program + "/setup.py ./spawn.spkg"
			command2 = "cp -r ./.programs/ports/"+ self.program + "/* ./.spawnTmp/program1/"
			command3 = "rm ./.spawnTmp/program1/setup.py" # Remove a unecessary files
			#print(command)
			#os.system("cp -r ./.programs/ports/"+ self.program+ "/* ./.spawnTmp/program1")
			os.system(command1)
			os.system(command2)
			os.system(command3)
			self.install_pkg()
		except:
			self.error_win("code 0", "File Missing or Program inexistent...")

	def install_pkg(self):
		try:
			os.system("pwd")
			os.system("python3 ./spawn.spkg")
		except:
			self.error_win("7", "Error in trigger a setup.py ...")

	def hostget(self):
		hostfile = open('./.config/hostname.cfg', 'r+')
		self.hostname = hostfile.read()
		hostfile.close()
		print("spawn[msg]: dectected hostname:. "+ self.hostname)

	def versionget(self):
		versionf = open('./.config/version.txt', 'r+')
		self.versionsys = versionf.read()
		versionf.close()
		print("spawn[msg]: dectected version:. "+ self.versionsys)

main()
