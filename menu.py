from tkinter import *

win=Tk()

# Create a parent menubar
menubar=Menu(win)
win.config(menu=menubar)



# Create a File menu

file_menu=Menu(menubar,tearoff=0)

# Add items to File menu

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_command(label="Close")

file_menu.add_separator()

file_menu.add_command(label="Exit",command=win.destroy)
# Cascade to the parent menubar
menubar.add_cascade(label="File", menu=file_menu)

# Create a Edit menu
edit_menu=Menu(menubar,tearoff=0)


# Add items to Edit menu
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Select All")


# Cascade edit menu to the parent menu bar

menubar.add_cascade(label="Edit", menu=edit_menu)


# Create a help menu
help_menu=Menu(menubar,tearoff=0)


# Add items to help menu
help_menu.add_command(label="About")
help_menu.add_command(label="Help")
help_menu.add_command(label="Training")


# Cascade helpmenu to parent menubar

menubar.add_cascade(label="Help", menu=help_menu)

win.mainloop()
