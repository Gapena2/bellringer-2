def check_3Digits(list1):
  # return number in range(100,1000)
  three_digit_list = []
  for n in list1:
    if n in range(100, 1000):
      three_digit_list.append(n)
      # return True
    else:
       pass

  return three_digit_list
  
  # pass
  
########################################################################################################################
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
def all_positives(list2):
  for n in list2:
    if n < 0:
      return False
    else:
      pass
  return True
########################################################################################################################
# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list (stored in the variable numbers) as long as they are greater than 0 and less than 1000, and returns the result of said sum.
def sum_less(list3):
  sum = 0
  for n in list3:
    if n > 0 and n < 1000:
      sum += n
    else:
      pass
  return sum


########################################################################################################################
# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def count_even(list4):
  counter = 0
  for n in list4:
    if n % 2 == 0:
      counter += 1
    else:
      pass
  return counter
    