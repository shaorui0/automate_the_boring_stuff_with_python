# Project: mapIt.py with the webbrowser Module

#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import sys, webbrowser

if len(sys.argv) > 1:
    # get addr from command line
    addr = ' '.join(sys.argv[1:]) # argv[0] is filename
else:
    # get addr from clipboard
    addr = pyperclip.paste()

webbrowser.open('https://map.baidu.com/search/'+addr)
# if you want download thing from web , use ‘requests’



