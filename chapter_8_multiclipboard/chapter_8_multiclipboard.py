# boring task: mutilple use content of clipboard
# store arg with the shelve module 
# new knowledge: .pyw()
# step 1: 
# step 2: 
# step 3: 

# .pyw : won’t show a Terminal window when it runs this program. 
# three function:
# 1. save : py mcb.pyw save spam 
# 2. running and copy content to clipboard : py mcb.pyw spam
# 3. copy keyword list to clipboard : py mcb.py list

# 业务逻辑：
# get command line args , like: c/cpp: int main(int argc, void ** argv)
# save/list/otherwise(copy to clpbd)

#TODO: read command line args from sys.argv
#TODO: read/write to the clipboard
#TODO: save clipboard to a shelf file
#@pyw.exe C:\Users\sr105\source\repos\automate_the_boring_stuff_with_python\chapter_8_multiclipboard %*
#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[argv[2]]= pyperclip.paste() # shelf is a list
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

