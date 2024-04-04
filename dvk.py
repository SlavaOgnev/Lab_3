with open ("dvk.txt", "w") as file:
  numbers = [4,5,3,5,5]
  znach = []
  k = 2
  amount = 0
  mesto = 0
  w = 0
  for i in range(max(numbers) + 1):
      znach.append(0)
  
  for i in range(len(numbers)):
      znach[numbers[i]] += 1
      if znach[numbers[i]] == 1:
          k -= 1
          if k < 0:
              znach[numbers[mesto]] = 0
              mesto += 1
              w = mesto
      if k <= 0:
          while (znach[numbers[mesto]] > 1):
              znach[numbers[mesto]] -= 1
              mesto += 1
          amount += mesto - w + 1
  file.write(amount)
