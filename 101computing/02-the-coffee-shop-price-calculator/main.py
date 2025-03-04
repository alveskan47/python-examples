#The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

price = 0
valid_input = True

coffee = input("What type of coffee would you like? > ").title()
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3
elif coffee=="Latte":
   price = price + 2.50
elif coffee=="Cappuccino":
   price = price + 3
elif coffee=="Macchiato":
   price = price + 2.50
elif coffee=="Mocha":
   price = price + 3.50
elif coffee=="Flat White":
   price = price + 2.50
else:
   print("Incorrect input")
   valid_input = False
print("----------------------------")

if valid_input:
    size = input("Pick a size: > ").title()
    if size == "Medium":
        pass
    elif size == "Large":
        price = price + 1
    elif size == "Xl":
        price = price + 1.50
    else:
        print("Incorrect input")
        valid_input = False

if valid_input:
    location = input("Eat in or take away: > ").title()
    if location == "Eat In":
        pass
    elif location == "Take Away":
        price = price + 1
    else:
        print("Incorrect input")
        valid_input = False

#Complete the code here...
print("----------------------------")
if valid_input:
    print("Total Cost: £" + str(price))
else:
    print("Incorrect input for calculating coffee price")