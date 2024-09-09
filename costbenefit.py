#learning economics and just using this for some documentation


#cost of the car
costofcar=float(input("How much is the car you want to buy? $"))

#selling price of the car after a year of use
sellcar= float(input("How much can the car be sold for after a year of use? $"))
resale= costofcar-sellcar

#knowing how much distance the car can go with a single liter
kilometers=float(input("How many kilometers do you get per liter? "))

#total kilometers = number of kilometers * 2 trips per day * 5 days a week * 47 weeks
totalkilo= kilometers * 2 * 5 * 47

#the base price of gas
basecost=float(input("How much does gas cost per litre? "))

#total cost of gas for a year
gascost= totalkilo/kilometers *basecost

#cost for parking in a year
parkcost= float(input("How much does parking cost for a day? $"))

parkcost=parkcost * 5 * 47

#insurance and registration
insurance= float(input("What would be the cost of your parking and registration? $"))

#repairs for a year
repairs= float(input("How much do you think repairs of the car would cost for the year? $"))

#total amount that would be spent on the car over the course of a year
totalcar= repairs + insurance + parkcost + gascost + resale






