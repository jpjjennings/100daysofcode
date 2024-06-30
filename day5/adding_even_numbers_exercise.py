target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
#if target <= 1000:
  #if (target % 2) < 1:
  #  for number in range(0, (target + 1), 2):
   #   target += number
  #  print(target)
  #else:
 #   print("An error occurred")
#else:
 #   print("You entered a number greater than 1000")

#--------------------
even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)
    
