coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]

# retrieve the coffee names and and price from the above tuple
# hint you can use a for loop
from dynamic_functions import *

result = check_3Digits([55, 99, 600, 555, 769])
print(result)
result2 = all_positives([55,77,88,99])
print(result2)
result3 = sum_less([33,98,989])
print(result3)
result4 = count_even([55, 64, 26, 23])
print(f'there are {result4} even numbers')

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