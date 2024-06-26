#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n£"))
tip = int(input("How much of a tip would you like to give? 10%, 12%, or 15%? \n"))
num_of_people = int(input("How many people are splitting the bill? \n"))
bill_with_tip = bill + (bill / 100 * (tip))
split_bill = round((bill_with_tip / num_of_people) , 2)
split_bill = "{:.2f}".format(split_bill)
print(f"Each person should pay: £{split_bill}")
