#coding: utf-8

try:
	import os
	from time import *
	from random import *
	import sys
except:
	print("[!] Try install module in you Python")
	exit()


os.system("clear")
os.system("echo System connection to host is stable")

try:
	reposfile = open('./.config/repos.conf', 'r+')
	repo_dectect = reposfile.read()
	reposfile.close()

	print("[!] Repository of Mix System is: "+ repo_dectect)
except:
	print("[!] Try gen a list of repos for Mix System...")

try:
	existuser = open('./Users/.exist')
	existuser.read()
	existuser.close()
except:
	print("[!] Users Folders not dectected... Making a folder")
	os.system("mkdir ./Users")
	print("[!] Criated Users folders with sucess!!!")

try:
	host = open('./.config/user.cfg', 'r+')
	host.read()
	host.close()
	passd = open('./.config/pass.cfg', 'r+')
	passd.read()
	passd.close()
	print("[!] Host dectect... continue boot...")
except:
	print("[!] This a new system... is time for configure!")
	main1 = 1
	while(main1<12):
		name = input("Insert you Name: ")
		passwd = input("Insert you passwd: ")
		filename = open('./.config/user.cfg', 'w+')
		filename.write(name)
		filename.close()
		filepasswd = open('./.config/pass.cfg', 'w+')
		filepasswd.write(passwd)
		filepasswd.close()
		print("User criated with sucess!!!")
		print("User criated is: "+ name)
		print("Password for user is: "+ passwd)
		print("Add more things... <UNDER CONSTRUCTION>")
		add = input("[Under Contruction]: Click to pass")
		break

	print("[!] Setup triggered with sucess...")

# Root get

try:
	rootfile = open('./.config/rootpass.cfg', 'r+')
	rootpass = rootfile.read()
	rootfile.close()
	print("[!] Dectected a root account,,, ")
except:
	print("[!] -----[ROOT PASSWD NEW]-------->")
	main12 = 1
	while(main12<100):
		rootpass = input("Please, define a new root pass:. ")
		arootpass = input("Please, insert again a pass:. ")
		if(rootpass==arootpass):
			break
		else:
			print("Retry a new password...")
			print("")
	
	rootfile = open('./.config/rootpass.cfg', 'w+')
	rootfile.write(rootpass)
	rootfile.close()
	print("Shutdown a computer...")


# Login Part...

versionfile = open('./.config/version.txt', 'r+')
version = versionfile.read()
versionfile.close()
print("[!] Version is: "+ version)
sleep(3)
os.system("clear")


main = 1
while(main<12):
	print("Welcome to Mix System "+ version)
	nome = input("Insert you Name for Entry: ")
	senha = input("Insert you Password for Entry: ")
	filenome = open('./.config/user.cfg', 'r+')
	nomereal = filenome.read()
	filenome.close()
	filesenha = open('./.config/pass.cfg', 'r+')
	senhareal = filesenha.read()
	filesenha.close()
	
	if(nome=="root"):
		if(senha==rootpass):
			print("Login(msg): You login with a root, use with caution...")	
			rootacess = True
			break
		else:
			print("root passwd is incorretly...")
	else:
		pass

	if(nome==nomereal):
		print("Name is corretly (!) ")
		if(senha==senhareal):
			print("Password is corretly (!) ")
			rootacess = False
			break
		else:
			print("Password is incorretly (!) ")
			main = main + 1
	else:
		print("Name is incorretly...")

# Computer Name get...

try:
	hostfile = open('./.config/hostname.cfg', 'r+')
	hostname = hostfile.read()
	hostfile.close()
	print("[!] Host defined for "+ hostname)
except:
	print("hostname not defined... Define now!!!")
	host1 = input("Hostname is: ")
	filehost = open('./.config/hostname.cfg', 'w+')
	filehost.write(host1)
	filehost.close()
	print("Hostname is defined!!!")
	exit()

# Shell área

print("[!] Initializing a Shell...")

shell = 1
while(main<20):
	if(rootacess==False):
		command = input("("+ hostname+ ")-Shell: ")
		rootfile = open('./.config/root.lock', 'w')
		rootfile.write("false")
		rootfile.close()
	else:
		command = input("("+ hostname+ ")-Shell(root): ")
		rootfile = open('./.config/root.lock', 'w')
		rootfile.write("true")
		rootfile.close()

	if(command=="exit"):
		print("Exiting of System...")
		break
	elif(command==""):
		pass
	elif(command=="mix-desktop"):
		os.system("python3 ./desktop.py")
	elif(command=="edit"):
		main2 = 1
		while(main2<120):
			editer = input("Edit a file:. ")
			if(editer=="exit"):
				print("Exited of FileSystem...")
				break
			elif(editer=="ls"):
				os.system("ls ./Users/")
			else:
				os.system("nano ./Users/"+ editer)
	elif(command=="list"):
		print("""
	:: Commands Avaiable:. Exit, edit, list(this command),
			       mkdir, ls, delete, clear, rootacess,
			       support
		
	:: Commands Avaiable in root:. format, edit_account, filesys

		""")
	elif(command=="mkdir"):
		folder = input("folder to make:. ")
		os.system("mkdir ./Users/"+ folder)
	elif(command=="format"):
		if(rootacess==True):
			print("Are you sure you want to format your users folder?")
			escyn = input("[y/N] (Yes or [Not]): ")
			if(escyn=="yes"):
				os.system("rm -rf ./Users/*")
				print("formated... [Bye Bye Data]")
			elif(escyn=="no"):
				print("ok, exited of format users...")
			else:
				print("Command not exited")
		else:
			print("Passwd is null, require a rootpass")
	elif(command=="edit_account"):
		print("mixsys(debug): for edit account, require a root")
		ifrootpass = input("rootpass:. ")
		if(ifrootpass==rootpass):
			print("===@ Welcome with a Account editor...")
			main2 = 1
			while(main2<12):
				print("Edit a: name or password ???")
				edit = input("[name, passwd, exit]: ")
				if(edit=="name"):
					print("In new initialiazation, the system is start account manager")
					os.system("rm -rf ./.config/user.cfg")
					break
				if(edit=="passwd"):
					print("In new initialization, the system is start account manager!!!")
					os.system("rm -rf ./.config/pass.cfg")
					break
			
	elif(command=="ls"):
		folder1 = input("folder to ls: ")
		if(folder1=="Users"):
			os.system("ls ./Users/")
		else:
			os.system("ls ./Users/"+ folder1)
	elif(command=="delete"):
		ren = input("delete a file:. ")
		os.system("rm -rf ./Users/"+ ren)
	elif(command=="clear"):
		os.system("clear")
	elif(command=="support"):
		os.system("python3 ./.programs/support.py")
	elif(command=="made"):
		print("Mix System 1.1.000 Feito pelo Andrew... PyWorks!!!")
		print("Sign ME")
	elif(command=="rootacess"):
		print("[!] Caution, the root have a infinity acess")
		passw = input("passwd root: ")
		if(passw==rootpass):
			print("Rootacess is possible!!!")
			rootacess = True
		else:
			print("Password incorretly")
	elif(command=="spawn"):
		if(rootacess==True):
			os.system("python3 ./spawn.py")
		else:
			print("Root pass not disponible...")
	elif(command=="exitroot"):
		if(rootacess==True):
			rootacess = False
		else:
			print("root acess is null...")
	else:
		try:
			appexist = open('./.programs/conf.d/spawn/appexist-list/'+ command, 'r+')
			pythontype = appexist.read()
			appexist.close()

			if(pythontype=="python3"):
				pyexec = 3
			else:
				pyexec = 2

			print("[Shell]:. App really exist... Running a python:. ")

			if(pyexec==3):
				os.system("python3 ./.programs/"+ command+ ".py")
			else:
				os.system("python2 ./.programs/"+ command+ ".py")
		except:
			print("Command or Application:. "+ command+ " Not Exist (!)")



print("Kernel Halted... Press a key for Shutdown...")
main = input()
print("Shutdown a shell...")
