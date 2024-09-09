#learning economics and just using this for some documentation


#cost of the car
costofcar=float(input("How much is the car you want to buy? $"))

#selling price of the car after a year of use
sellcar= float(input("How much can the car be sold for after a year of use? $"))

#knowing how much distance the car can go with a single liter
kilometers=float(input("How many kilometers do you get per liter? "))

#total kilometers = number of kilometers * 2 trips per day * 5 days a week * 47 weeks
totalkilo= kilometers * 2 * 5 * 47

#the base price of gas
basecost=float(input("How much does gas cost per litre? "))

gascost= totalkilo/kilometers *basecost




