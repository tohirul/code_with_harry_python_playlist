apple_price = int(input("How much does an apple cost per kilo? "))

customer_budget = int(input("Well I have: ? "))

if customer_budget > apple_price:
    if customer_budget >= apple_price * 10:
        print("You can buy as much apple as you want.")
    else:
        print("You can buy some.")
elif customer_budget == apple_price:
    print("You can buy only 1 kilo apple.")
else:
    print("You don't have enough money.")
