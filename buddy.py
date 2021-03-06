#!/usr/bin/python
#Budget Buddy
#Income/Expenses Program
#Written by David Lawson


import os
os.system('clear')
import time
import datetime
x = datetime.datetime.now()
import sys

print
print "###########################################"
print "#  Calculates income and expenses on      #"
print "#  a monthly basis. Prints results to     #"
print "#  screen w/option to save as text file.  #"
print "#  Whole numbers only, wont do decimals.  #"
print "###########################################"
print
time.sleep (0.5)

raw_input("Press [Enter] to continue... ")
os.system('clear')
print

class color:
   BOLD = '\033[1m'
   END = '\033[0m'
   RED = '\033[91m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'

print color.BOLD + "MONTHLY INCOME AND EXPENSES\n\n" + color.END
time.sleep (0.5)

name = raw_input("Name: " )
print
time.sleep (0.5)

month = raw_input("Month: " )
print
time.sleep (0.5)

#gather info
print
time.sleep (0.5)
print color.BOLD + "-ANSWERS MUST BE IN DOLLAR AMOUNTS-" + color.END + "\n\n"
time.sleep (1)


income = raw_input("What is your monthly income? $" )
income = int(income)
print
time.sleep (0.5)

rent = raw_input("How much is your rent? $" )
rent = int(rent)
print
time.sleep (0.5)

cons = raw_input("How much for consumers? $" )
cons = int(cons)
print
time.sleep (0.5)

cable = raw_input("How much for cable? (tv/internet): $" )
cable = int(cable)
print
time.sleep (0.5)

car = raw_input("How much for car insurance? $" )
car = int(car)
print
time.sleep (0.5)

food = raw_input("How much for food/groceries? $" )
food = int(food)
print
time.sleep (0.5)

gas = raw_input("How much for gas? $" )
gas = int(gas)
print
time.sleep (0.5)

person = raw_input("Personal items, clothes, etc: $" )
person = int(person)
print
time.sleep (0.5)

other = raw_input("Other expenses? $" )
other = int(other)
print
time.sleep (0.5)

cell = raw_input("Cell phone bill? $" )
cell = int(cell)
print "\n"
time.sleep (1)


#processing delay
import sys, time
string = 'Processing...\n'
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.08)


#print to screen
os.system('clear')
print
print color.BOLD + " --YOUR INFO-- \n" + color.END
time.sleep (1)

print name, " | ", month, (x.strftime("%Y")) + "\n" #year

print ('Monthly Income:     $'+str(income)) + "\n"
print ('  Monthly Costs      '+str()) + "\n"
print ('  Rent:             $'+str(rent))
print ('  Consumers:        $'+str(cons))
print ('  Cable:            $'+str(cable))
print ('  Car Ins:          $'+str(car))
print ('  Food:             $'+str(food))
print ('  Gas:              $'+str(gas))
print ('  Personal:         $'+str(person))
print ('  Other:            $'+str(other))
print ('  Phone:            $'+str(cell)) + "\n"
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
print color.BOLD + ('    Total Costs:    $'+str(total)) + "\n" + color.END
time.sleep (1)

remain = (income - total)
print color.BOLD + ('    Remaining:      $'+str(remain)) + "\n" + color.END
time.sleep (1)


#two more questions
print "\n"
sav = raw_input(" How much into savings account? $" )
sav = int(sav)

print
left = (remain - sav)
print color.BOLD + ('    Whats Left:     $'+str(left)) + color.END
time.sleep (1)

print "\n"
earn = raw_input(" Additional earned income? $" )
earn = int(earn)

print
newt = (remain - sav + earn)
print color.BOLD + ('    New Total:      $'+str(newt)) + color.END


#Save file as
print "\n"
saveas = raw_input('Save File as: ')
print

#save to text file (w=writeOver, a=append)
#save to: files/filename
saveFile = open(saveas, 'w')

#write to text file
saveFile.write( str( ' --YOUR INFO--' ) + "\n\n" )
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

print "\n"
