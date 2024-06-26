line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# Comments to the right, are improvements made after watching the solution.
letter = str(position[0]).lower() # Added .lower()
#abc = ["a", "b", "c"] # List created
#letter_index = abc.index(letter) # Compare the 'abc' list to check if input exists
#number_index = int(position[1]) - 1 # Converting the number into the relevant index. (Code starts at 0, not 1)
#map[number_index][letter_index] = "X" # How much cleaner is this, compared to the below IF/ELIF statement.
number = str(position[1])
if letter == "A" and number == "1":
  line1[0] = "X"
elif letter == "A" and number == "2":
  line2[0] = "X"
elif letter == "A" and number == "3":
  line3[0] = "X"
elif letter == "B" and number == "1":
  line1[1] = "X"
elif letter == "B" and number == "2":
  line2[1] = "X"
elif letter == "B" and number == "3":
  line3[1] = "X"
elif letter == "C" and number == "1":
  line1[2] = "X"
elif letter == "C" and number == "2":
  line2[2] = "X"
elif letter == "C" and number == "3":
  line3[2] = "X"
else:
  print("That input is not valid!")

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
