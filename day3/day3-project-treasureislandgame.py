#Treasure Island Game
print('''
___  __   ___       __        __   ___       __                  __  
 |  |__) |__   /\  /__` |  | |__) |__     | /__` |     /\  |\ | |  \ 
 |  |  \ |___ /~~\ .__/ \__/ |  \ |___    | .__/ |___ /~~\ | \| |__/ 
                                                                     
'''
)
input("Press Enter to Begin the Game!")
print("Welcome to Treasure Island.\nYour goal is to find the location where Pegleg Pete buried his treasure!\nGood luck!")
choice = input("You are standing on a beach.\nTo your right is a pier surrounded by deep waters.\nTo your left is a dark forest.\nWhich direction will you go? Left or Right?\n").lower()
if choice == "left":
  print("You step through the thick woods, and find a small river.\nIn order to cross the river you must swim.\nAlternatively you hear some people in the distance.\nYou think you could wait for help.")
  choice = input("Do you swim across the river, or will you wait for those who approach? Input Swim or Wait\n").lower()
  if choice == "swim":
    print("Swimming across the river felt like the correct choice.\nSomething about those voices seemed eerie.")
    print("When you emerge from the water, you see a marking on the nearby rock.\nIt says ""This way to Pete's Treasure""")
    choice = input("This could be a trap. Should you risk it? Yes or No.\n").lower()
    if choice == "yes":
      print("You choose to follow the path in the direction of the marking.\nA few minutes on the road and you spot a church.")
      choice = input("Should you stop and pray? Yes or No.\n").lower()
      if choice == "yes":
        print("You enter the church.\nThere is a priest sitting on the first pew.\nHe looks like he hasn't eaten in days.")
        choice = input("Will you offer him some food? Yes or No.\n").lower()
        if choice == "yes":
          print("The priest thanks you, and motions towards a large cross on the altar.")
          print("You ask the priest what is the meaning of his actions.")
          print("The priest tells you that Pegleg Pete was only a myth, but the real treasure lies within the cross.\nThe priest says that in order to gain the treasure you must make a donation to the church of $500. The end.")
        else:
          print("The priest attacks you like a ravenous vampire. You die. Game Over.")
      else:
        print("You continue on the beaten path for days, but on the third day you run out of water and food.\nIronically you now pray for the sweet release of death.\nGame over.")
    else:
      print("An adventurer who doesn't take risks, is no adventurer at all.\nI am not mad, just disappointed.\nGame over.")
  else:
    print("You chose the cowards way and waited for the voices to approach.\nThese were a party of cannibals and they ate you for dinner.\nGame over.")
else:
  print("You have fallen into the abyss. Your journey is over.")
