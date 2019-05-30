from enum import Enum

class colors(Enum):
    Red = 1
    Blue = 2
    Green = 3
print("-----")
ch = 3
if ch == colors.Red.value:
    print (colors.Red.name)
elif ch == colors.Blue.value:
    print (colors.Blue.name)
elif ch == colors.Green.value:
    print (colors.Green.name)
else:
    print ("Invalid Color")