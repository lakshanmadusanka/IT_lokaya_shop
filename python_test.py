# from audiooop import avg

price=float(input("Enter number of items :"))

priceOne=int(input("Enter price of item1 RS:"))
priceTwo=int(input("Enter price of item2 RS:"))
priceThree=int(input("Enter price of item3 RS:"))
priceFour=int(input("Enter price of item4 RS:"))
priceFive=int(input("Enter price of item5 RS:"))

total = priceOne+priceTwo+priceThree+priceFour+priceFive
print("Total is:",total)

average=total/5
print("The five item average is RS:"+str(round(average,2)))

largest_number=max(priceOne,priceTwo,priceThree,priceFour,priceFive)
print("The largest number is:",largest_number)

lowest_number=min(priceOne,priceTwo,priceThree,priceFour,priceFive)
print("The lowest number is:",lowest_number)
