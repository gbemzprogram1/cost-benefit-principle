#cost benefit checker for if the value is worth it to you or not

cost=int(input("What is the price of what you want to buy?  "))
benefit=int(input("What is the benefit of this to you?, what is the maximum you would be willing to pay to fulfil the desire "))

if cost > benefit:
    print("think again before buying this")
    
else:
    print('You can go ahead with your purchase since they are of equal value to you or the benefiit seems greater to you')    