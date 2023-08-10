#!/usr/bin/env python3
#Buddy (CLI Version)
#Income/Expenses Program

import os
import sys
import time
import datetime

x = datetime.datetime.now()

os.system('clear')
print ()
print ("###########################################")
print ("#  Calculates income and expenses on      #")
print ("#  a monthly basis. Prints results to     #")
print ("#  screen w/option to save as text file.  #")
print ("#  Whole numbers only, wont do decimals.  #")
print ("###########################################")
print ()
time.sleep (0.5)

input("Press [Enter] to continue... ")
os.system('clear')
print ()

bold = '\033[1m'
end = '\033[0m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'

print (f"{bold}MONTHLY INCOME AND EXPENSES\n{end}")
time.sleep (0.5)

name = input("Name: " )
print ()
time.sleep (0.5)

month = input("Month: " )
print ()
time.sleep (0.5)

#gather info
print ()
print (f"{bold}-ANSWERS MUST BE IN DOLLAR AMOUNTS-\n\n{end}")
time.sleep (0.5)


income = input("What is your monthly income? $" )
income = int(income)
print ()
time.sleep (0.5)

rent = input("How much is your rent? $" )
rent = int(rent)
print ()

cons = input("How much for consumers? $" )
cons = int(cons)
print ()

cable = input("How much for internet? $" )
cable = int(cable)
print ()

car = input("How much for car insurance? $" )
car = int(car)
print ()

food = input("How much for food/groceries? $" )
food = int(food)
print ()

gas = input("How much for gas? $" )
gas = int(gas)
print ()

person = input("Personal items, clothes, etc: $" )
person = int(person)
print ()

other = input("Other expenses? $" )
other = int(other)
print ()

cell = input("Cell phone bill? $" )
cell = int(cell)
print ()


#processing delay
import sys, time
string = 'Processing...\n'
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.07)


#print to screen
os.system('clear')
print ()
print (f"{bold} --RESULTS-- \n{end}")
time.sleep (0.5)

print (name, " | ", month, (x.strftime("%Y")) + "\n") 

print ('Monthly Income:     $'f"{income}\n")
print ('  Expenses           'f"\n")
print ('  Rent:             $'f"{rent}")
print ('  Consumers:        $'f"{cons}")
print ('  Internet:         $'f"{cable}")
print ('  Car Ins:          $'f"{car}")
print ('  Food:             $'f"{food}")
print ('  Gas:              $'f"{gas}")
print ('  Personal:         $'f"{person}")
print ('  Other:            $'f"{other}")
print ('  Phone:            $'f"{cell}\n")
time.sleep (1)

a = rent
b = cons
c = cable
d = car 
e = food
f = gas
g = person
h = other
i = cell

total = (a + b + c + d + e + f + g + h + i)
print (f"{bold}    Total Costs:    ${total}\n{end}")
time.sleep (0.5)

remain = (income - total)
print (f"{bold}    Remaining:      ${remain}\n{end}")
time.sleep (0.5)


#two more questions
print ()
sav = input(" How much into savings account? $" )
sav = int(sav)

print ()
left = (remain - sav)
print (f"{bold}    Whats Left:     ${left}{end}")
time.sleep (0.5)

print ("\n")
earn = input(" Additional earned income? $" )
earn = int(earn)

print ()
newt = (remain - sav + earn)
print (f"{bold}    New Total:      ${newt}{end}")


#Save file as
print ("\n")
saveas = input('Save File as: ')
print ()

#save as text file (w=writeOver, a=append)
#save to: files/filename
saveFile = open(saveas, 'w')

#write to text file
saveFile.write(f" --RESULTS-- \n\n")
saveFile.write(f"{name}  |  {month}" + (x.strftime(" %Y")) + "\n\n")

saveFile.write('Monthly Income:    $'f"{income}\n\n")
saveFile.write('  Expenses          'f"\n\n")
saveFile.write('  Rent:            $'f"{rent}\n")
saveFile.write('  Consumers:       $'f"{cons}\n")
saveFile.write('  Internet:        $'f"{cable}\n")
saveFile.write('  Car Ins:         $'f"{car}\n")
saveFile.write('  Food:            $'f"{food}\n")
saveFile.write('  Gas:             $'f"{gas}\n")
saveFile.write('  Personal:        $'f"{person}\n")
saveFile.write('  Other:           $'f"{other}\n")
saveFile.write('  Phone:           $'f"{cell}\n\n")
saveFile.write('    Total Costs:   $'f"{total}\n\n")
saveFile.write('    Remaining:     $'f"{remain}\n\n\n\n")
#two questions
saveFile.write(' How much into savings account? $'f"{sav}\n\n")
saveFile.write('    Whats Left:    $'f"{left}\n\n\n")
saveFile.write(' Additional earned income? $'f"{earn}\n\n")
saveFile.write('    New Total:     $'f"{newt}\n\n")
saveFile.close()

print ()
