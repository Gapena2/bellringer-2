coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]

# retrieve the coffee names and and price from the above tuple
# hint you can use a for loop

#create a function for retrieving the highest priced coffee and name
def expensive_coffee(coffee_prices):
  highest_price = 0
  my_most_expensive_coffee =''
  for coffee, price in coffee_prices:
    if price > highest_price:
      highest_price = price
      my_most_expensive_coffee = coffee
    else:
      pass
  return(my_most_expensive_coffee,highest_price) 
print(expensive_coffee(coffee_prices))