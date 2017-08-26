#coding: utf-8
try:
    from tkinter import *
    from tkinter import filedialog
    import os
    from time import *
    from multiprocessing import Process
except:
    print("(!) Missing Modules:. tkinter...")
    exit()

# # # # # #
# Python Works
# Desktop Mix 1.1.000
# # # # # # # --- # Desktop Mix

class main():
    def __init__(self):
        # Window
        self.loadscreen = Tk()
        self.loadscreen.title("Mix Desktop --- Loading")
        self.loadscreen.geometry("500x500")
        # Widgets
        self.button1 = Button(self.loadscreen, text="Continue GUI Start?", command=self.event_continue)
        self.button2 = Button(self.loadscreen, text="Close GUI StartUp", command=exit)
        self.button1.pack(side=BOTTOM)
        self.button2.pack(side=BOTTOM)
        self.label1 = Label(self.loadscreen, text="Loading --- Mix System")
        self.label1.pack()
        self.loadscreen.mainloop()

    def event_deskpad(self):
        os.system("python3 ./deskpad.py")

    def event_spawn(self):
        self.event_login_root_ath()

    def event_login_root_ath(self):
        rootpass = open('./.config/rootpass.cfg', 'r+')
        self.truepass = rootpass.read()
        rootpass.close()
        # Window title...
        self.root2 = Tk()
        self.root2.title("Root Authentication")
        # Widgets
        label1 = Label(self.root2, text="-> Insert you Password:.")
        self.label9 = Label(self.root2, text="Password is Corretly")
        self.passentry = Entry(self.root2)
        self.passentry.insert(0, "Insert you root passwd...")
        self.button7 = Button(self.root2, text="[OK]", command=self.event_get_passentry)
        # pack
        label1.pack()
        self.passentry.pack()
        self.button7.pack()

    def event_get_passentry(self):
        userpass = self.passentry.get()
        rootfile = open('./.config/rootpass.cfg', 'r+')
        self.rootpass1 = rootfile.read()
        rootfile.close()
        if(userpass==self.rootpass1):
            print("desktop(msg): root pass is corretly")
            self.label9.pack()
            self.root2.destroy()
            os.system("python3 ./spawn.py")
        else:
            self.label0 = Label(self.root2, text="Error in pass")
            self.label0.pack()

    def event_continue(self):
        self.hostname_get()
        self.version_get()

    def hostname_get(self):
        hostfile = open('./.config/hostname.cfg', 'r+')
        self.hostname = hostfile.read()
        hostfile.close()
        self.label1 = Label(self.loadscreen, text="Hostname dectected:. "+ self.hostname)
        self.label1.pack()

    def version_get(self):
        versionfile = open('./.config/version.txt', 'r+')
        self.version = versionfile.read()
        versionfile.close()
        self.label1 = Label(self.loadscreen, text="Version for MixSystem:. "+ self.version)
        self.label1.pack()
        self.startdesktop()

    def startdesktop(self):
        # Desktop En
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Desktop Mix # ("+ self.hostname+ ")")
        # Widgets
        self.label4 = Label(self.root, text="[!] This a Mix Desktop :-D ")
        self.label5 = Label(self.root, text="[!] Version:. "+ self.version)
        self.button3 = Button(self.root, text="Deskpad", command=self.event_deskpad)
        #self.label6 = Button(self.root, text="Command Line", command=self.event_get_command)
        self.label7 = Label(self.root, text="Apps for You...")
        self.button4 = Button(self.root, text="Spawn Pkg", command=self.event_spawn)
#        self.menu2 = Menu(self.root)
 #        sysmenu = Menu(self.menu2, tearoff=0)
  #       sysmenu.add_command(label="Open Terminal")
   #      sysmenu.add_separator()
    #     self.menu2.add_cascade(label="System", menu=self.menu2)
     #    self.root.config(self.menu2)
        # Packwidgets
        self.label4.pack()
        self.label5.pack()
        self.label7.pack(side=TOP)
        self.button3.pack(side=LEFT)
        self.button4.pack(side=RIGHT)

main()

