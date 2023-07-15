#!/usr/bin/env python3
#Budget Buddy (CLI Version)
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

print (bold + "MONTHLY INCOME AND EXPENSES\n\n" + end)
time.sleep (0.5)

name = input("Name: " )
print ()
time.sleep (0.5)

month = input("Month: " )
print ()
time.sleep (0.5)

#gather info
print ()
time.sleep (0.5)
print (bold + "\n-ANSWERS MUST BE IN DOLLAR AMOUNTS-" + end + "\n\n")
time.sleep (1)


income = input("What is your monthly income? $" )
income = int(income)
print ()
time.sleep (0.5)

rent = input("How much is your rent? $" )
rent = int(rent)
print ()
time.sleep (0.5)

cons = input("How much for consumers? $" )
cons = int(cons)
print ()
time.sleep (0.5)

cable = input("How much for cable? (tv/internet): $" )
cable = int(cable)
print ()
time.sleep (0.5)

car = input("How much for car insurance? $" )
car = int(car)
print ()
time.sleep (0.5)

food = input("How much for food/groceries? $" )
food = int(food)
print ()
time.sleep (0.5)

gas = input("How much for gas? $" )
gas = int(gas)
print ()
time.sleep (0.5)

person = input("Personal items, clothes, etc: $" )
person = int(person)
print ()
time.sleep (0.5)

other = input("Other expenses? $" )
other = int(other)
print ()
time.sleep (0.5)

cell = input("Cell phone bill? $" )
cell = int(cell)
print ()
time.sleep (1)


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
print (bold + " --RESULTS-- \n" + end)
time.sleep (1)

print (name, " | ", month, (x.strftime("%Y")) + "\n") #year

print ('Monthly Income:     $'+str(income) + "\n")
print ('  Monthly Costs      '+str() + "\n")
print ('  Rent:             $'+str(rent))
print ('  Consumers:        $'+str(cons))
print ('  Cable:            $'+str(cable))
print ('  Car Ins:          $'+str(car))
print ('  Food:             $'+str(food))
print ('  Gas:              $'+str(gas))
print ('  Personal:         $'+str(person))
print ('  Other:            $'+str(other))
print ('  Phone:            $'+str(cell) + "\n")
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
print (bold + ('    Total Costs:    $'+str(total)) + "\n" + end)
time.sleep (1)

remain = (income - total)
print (bold + ('    Remaining:      $'+str(remain)) + "\n" + end)
time.sleep (1)


#two more questions
print ()
sav = input(" How much into savings account? $" )
sav = int(sav)

print ()
left = (remain - sav)
print (bold + ('    Whats Left:     $'+str(left)) + end)
time.sleep (1)

print ()
earn = input(" Additional earned income? $" )
earn = int(earn)

print ()
newt = (remain - sav + earn)
print (bold + ('    New Total:      $'+str(newt)) + end)


#Save file as
print ("\n")
saveas = input('Save File as: ')
print ()

#save to text file (w=writeOver, a=append)
#save to: files/filename
saveFile = open(saveas, 'w')

#write to text file
saveFile.write( str( ' --RESULTS--' ) + "\n\n" )
saveFile.write( str(name + ' | ' + str(month) + (x.strftime(" %Y")) + "\n\n" ))

saveFile.write( 'Monthly Income:    $' + str(income) + "\n\n" )
saveFile.write( '  Monthly Costs     ' + str() + "\n\n" )
saveFile.write( '  Rent:            $' + str(rent) + "\n" )
saveFile.write( '  Consumers:       $' + str(cons) + "\n" )
saveFile.write( '  Cable:           $' + str(cable) + "\n" )
saveFile.write( '  Car Ins:         $' + str(car) + "\n" )
saveFile.write( '  Food:            $' + str(food) + "\n" )
saveFile.write( '  Gas:             $' + str(gas) + "\n" )
saveFile.write( '  Personal:        $' + str(person) + "\n" )
saveFile.write( '  Other:           $' + str(other) + "\n" )
saveFile.write( '  Phone:           $' + str(cell) + "\n\n" )
saveFile.write( '    Total Costs:   $' + str(total) + "\n\n" )
saveFile.write( '    Remaining:     $' + str(remain) + "\n\n\n\n" )
#two questions
saveFile.write( ' How much into savings account? $' + str(sav) + "\n\n" )
saveFile.write( '    Whats Left:    $' + str(left) + "\n\n\n" )
saveFile.write( ' Additional earned income? $' + str(earn) + "\n\n" )
saveFile.write( '    New Total:     $' + str(newt) + "\n\n" )

saveFile.close()

print ()
