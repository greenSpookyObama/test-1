#Ian Lawson and Reman Shretha
#Block 5
#Project 1

#Project

#Glossary:
#Functions Line 11 - 201
#Game Start Line 207
#Code Ending Tester Line 214
#Endings Line 123 - 164
#Tutorial Line 17 - 122

import random

def PlayTutorial():
  #Explanation of the code
  print ("You will start with 100 settlers, 5 defense, 10 food and 3 resources. Resources will be consumed when building things. Defense will determine the outcome of Conflict Events. Food will be major as it will affect the amount of settler, the amount of resource, and the defense output. There are two ways to win the game. Have more than 135 settlers or collect 12 reources for the mainland. There are three main ways to lose the game, either lose all of your settlers, having your food go 0 or below, or you did not meet the demand of 20 resources for the mainland. In special events, if you have enough oppurntunity points stored then you can skip these events. If you receive 11 oppurntunity points or more you automatically win the game.")
  print ("Every event the season will change. You will start in spring in the main gameplay and in tutorial. Spring is a season for oppruntunities so you could increase your chances for recieving settlers, gaining resources, gaining food, or increase defense. In summer, it is the time for Conflicts and gaining food and possible recruiting more settlers. In Fall, it is time to prepare for the winter, so building up resources, as well as food. But other settlements and Native Villages will also be challgening you at the same time. In Winter, you will gain only settlers and increase your defense. Your food and resources may go down. Conflicts are low but if you do encounter one you will achieve or lose a lot depending on your choiuce.  ")
  print ("There are 4 different kinds of events, Conflict Event, Town Event, Disaster Event, and Civil Event. Conflicts are Man VS Man or Man VS Environment type of situation. Town Events are construction projects or new setting up trade with other villages or other settlement. Disaster Events are famine or flood related. And Civil Event is settler related issues.  ")
  print ("Major Events are events that you will have to play through. All Events will give you at least 4 choices. Each choices will increase one area of points or decrease another area.")
  print (" Side Events are events that you do not have to play. But if you do play them then they can provide many new resources, fix the issues you currently have, or destroy your settlement. They also unlock hidden options as well. Now lets do some gameplay")
  print ("*Input every answer with their according letter and in Cap Locks*")
  
  print ("The First event for you in this tutorial will be a Conflict Event.")
  
  #Example Events
  print ("Each event will be different season and all types of event. ")
  tutorialEvent1= input("--|CONFLICT EVENT|-- /\ --|SUMMER SEASON|-- A group of Natives has been spotted near our settlement. It is unknown if they are friendly or hostile. What shall we do?\nA. Approach them in friendly manner.\nB. Ambush them\nC. Ignore them\nD. Scare them off\n")
  if (tutorialEvent1 == "A"):
    print ("They are hostile and fire upon us! We lose 10 settlers")
    print ("You would lose 10 settlers from, your settlement. ")
    print (" If you choose A you would have lost 10 settlers .If you choose B, you would have gain a resource. If you choose C, you would have lost 5 settlers and 1 resource. If you choose D, you would have recieved 1 settler. ")
  elif (tutorialEvent1 == "B"):
    print ("We successfully ambushed them and captured 1 resource!")
    print ("You would have gain 1 resource")
    print (" If you choose A you would have lost 10 settlers .If you choose B, you would have gain a resource. If you choose C, you would have lost 5 settlers and 1 resource. If you choose D, you would have recieved 1 settler. ")
  elif (tutorialEvent1 == "C"):
    print ("Your choice to ignore them had them attack our settlement! We lose 5 settlers and 1 resource!")
    print ("You would have lost 5 settlers and 1 resource")
    print (" If you choose A you would have lost 10 settlers .If you choose B, you would have gain a resource. If you choose C, you would have lost 5 settlers and 1 resource. If you choose D, you would have recieved 1 settler. ")
  elif (tutorialEvent1 == "D"):
    print ("We scared them off! One of your team has rescued an unknown settler, we gain 1 settler!")
    print ("You would have gain another settler. ")
    print (" If you choose A you would have lost 10 settlers .If you choose B, you would have gain a resource. If you choose C, you would have lost 5 settlers and 1 resource. If you choose D, you would have recieved 1 settler. ")



  print ("This event is a Town Event")
  tutorialEvent2= input("--|TOWN EVENT!|-- /\ --|SPRING SEASON!|-- Many settlers are hoping to build three buildings but we only have limited amount of resources. What shall we do?\nA. Build a church to attract more settlers.\nB. Make a fort to increase our defenses\nC. Make a farm to produce food\nD. Build all three ideas\nE. Deny the authorization to build anything in the settlement.")
  if (tutorialEvent2 == "A"):
    print ("We build a church and gain 10 settlers from a nearby settlement!")
    print ("You would gain 10 settlers but loose 1 resource. ")
    print (" If you choose A you would have gain 10 settlers .If you choose B, you would have gain 2 defenders. If you choose C, you would have more food at the next season. If you choose D, you would have gain all of above. If you choose E you would gain nothing but also loose nothing. D and above are consuming resources. If you choose E nothing would have happened.")
  elif (tutorialEvent2 == "B"):
    print ("We made a Fort and we have increased our Defense by 2 points!")
    print ("You would increased your defense by 2 points but loose 1 resource.")
    print (" If you choose A you would have gain 10 settlers .If you choose B, you would have gain 2 defenders. If you choose C, you would have more food at the next season. If you choose D, you would have gain all of above. If you choose E you would gain nothing but also loose nothing. D and above are consuming resources. If you choose E nothing would have happened.")
  elif (tutorialEvent2 == "C"):
    print ("We made a farm! Now we should gain harvest in the next season! Our farmers have also scrapped wild berries, we gain 1 food!")
    print ("You would gain 1 food but loose 1 resource. ")
    print (" If you choose A you would have gain 10 settlers .If you choose B, you would have gain 2 defenders. If you choose C, you would have more food at the next season. If you choose D, you would have gain all of above. If you choose E you would gain nothing but also loose nothing. D and above are consuming resources. If you choose E nothing would have happened.")
  elif (tutorialEvent2 == "D"):
    print ("You have decided to build all of the plans. We gain 10 settlers, increased our defense by 2, and a farm that will produce food at the next season.")
    print ("You would have gain 10 settlers, and 2 defences. We will gain food in the next season but we cannot build anything else since we have exhausted our resources. ")
    print (" If you choose A you would have gain 10 settlers .If you choose B, you would have gain 2 defenders. If you choose C, you would have more food at the next season. If you choose D, you would have gain all of above. If you choose E you would gain nothing but also loose nothing. D and above are consuming resources. If you choose E nothing would have happened. ")
  elif (tutorialEvent2 == "E"):
    print ("You denied the request of the plans to make new buildings. Nothing good or bad happens.")
    print ("You lose nothing and gained nothing. ")
    print (" If you choose A you would have gain 10 settlers .If you choose B, you would have gain 2 defenders. If you choose C, you would have more food at the next season. If you choose D, you would have gain all of above. If you choose E you would gain nothing but also loose nothing. D and above are consuming resources. If you choose E nothing would have happened. ")
  tutorialEvent3= input("—-|DISASTER EVENT!|—- /\ —-|FALL SEASON!|—- Our crops have failed to grow! We all have different ideas of what we can do to prevent a crisis! What shall we do?\nA. Gather wild berries, look for alternate sources of food, and hunt animals before winter.\nB. Do a raid on a Native Village nearby.\nC. Do a raid on a nearby settlement.\nD. Try to regrow the crop quickly.\nE. Limit the amount of food people will eat.\nF. Try to trade with another Village or Settlement.")
  if (tutorialEvent3 == "A"):
    print ("We have gathered some food from the resources outside of our settlement.")
    print ("Gain 1 food.")
    print ("If you choose option A, you would have gain 1 food. If you choose option B, you would have gain 6 food but loose 10 settlers. If you choose option C, you would have gain 3 food, 3 resources, and 1 oppurntunity but loose 20 settlers. If you choose option D, you would have lost 1 food. If you choose option E, you would have lost 25 settlers. If you choose option F, you would have gain 8 food but loose 2 resources. ")
  elif (tutorialEvent3 == "B"):
    print ("We have raided a nearby Native Village but we lost some brave souls.")
    print ("Gain 6 food but loose 10 settlers.")
    print ("If you choose option A, you would have gain 1 food. If you choose option B, you would have gain 6 food but loose 10 settlers. If you choose option C, you would have gain 3 food, 3 resources, and 1 oppurntunity but loose 20 settlers. If you choose option D, you would have lost 1 food. If you choose option E, you would have lost 25 settlers. If you choose option F, you would have gain 8 food but loose 2 resources. ")
  elif (tutorialEvent3 == "C"):
    print ("We did a raid on a rival settlement. We lost many brave souls today.")
    print ("You lost 20 settlers but gain 3 food and 3 resources. As well as 1 Oppurtunity.")
    print ("If you choose option A, you would have gain 1 food. If you choose option B, you would have gain 6 food but loose 10 settlers. If you choose option C, you would have gain 3 food, 3 resources, and 1 oppurntunity but loose 20 settlers. If you choose option D, you would have lost 1 food. If you choose option E, you would have lost 25 settlers. If you choose option F, you would have gain 8 food but loose 2 resources. ")
  elif (tutorialEvent3 == "D"):
    print ("We tried to regrow our crops but we have failed and wasted some food supply on this project!")
    print ("You would loose 2 food from this.")
    print ("If you choose option A, you would have gain 1 food. If you choose option B, you would have gain 6 food but loose 10 settlers. If you choose option C, you would have gain 3 food, 3 resources, and 1 oppurntunity but loose 20 settlers. If you choose option D, you would have lost 1 food. If you choose option E, you would have lost 25 settlers. If you choose option F, you would have gain 8 food but loose 2 resources. ")
  elif (tutorialEvent3 == "E"):
    print ("We have limited the amount of food settlers will receive but we have lost many settlers.")
    print ("You would have lost 25 settlers.")
    print ("If you choose option A, you would have gain 1 food. If you choose option B, you would have gain 6 food but loose 10 settlers. If you choose option C, you would have gain 3 food, 3 resources, and 1 oppurntunity but loose 20 settlers. If you choose option D, you would have lost 1 food. If you choose option E, you would have lost 25 settlers. If you choose option F, you would have gain 8 food but loose 2 resources. ")
  elif (tutorialEvent3 == "F"):
    print ("We have traded our resources for some food!")
    print ("You would gain 8 food but loose 2 resources.")
    print ("If you choose option A, you would have gain 1 food. If you choose option B, you would have gain 6 food but loose 10 settlers. If you choose option C, you would have gain 3 food, 3 resources, and 1 oppurntunity but loose 20 settlers. If you choose option D, you would have lost 1 food. If you choose option E, you would have lost 25 settlers. If you choose option F, you would have gain 8 food but loose 2 resources. ")
  tutorialEvent4= input("—-|CIVIL EVENT!|—- /\ —-|WINTER SEASON!|—- One of our settlers has a property dispute with another neighbor. What shall we do?\nA. The Settler who claims to have the property disputed on his because the flag he placed on the land marking it was his few months ago. He wants to use the land as a new workshop.\nB. The Settler who lives on the land promises to build a farm.\nC. One of your advisors proposes to use the land as a way to build a new building for the militia.\nD. Another settler proposes to build new houseses on the property.\nE. An old man walks by saying that you should keep the land empty until a oppurntunity will rise.")
  if (tutorialEvent4 == "A"):
    print ("THe workshop he made has generated 3 resources for us.")
    print ("Gain 3 resources.")
    print ("If you choose option A, you would have gain 3 resources. If you choose option B, you would have gain 5 food. If you choose option C, you would have gain 4 defense points. If you choose option D, you would have gained 20 settlers but loose 1 food. If you choose option E, you would have gained 1 food and 1 oppurntunity point.")
  elif (tutorialEvent4 == "B"):
    print ("The settler on the land has made a farm generating a lot of food for us.")
    print ("Gain 5 food.")
    print ("If you choose option A, you would have gain 3 resources. If you choose option B, you would have gain 5 food. If you choose option C, you would have gain 4 defense points. If you choose option D, you would have gained 20 settlers but loose 1 food. If you choose option E, you would have gained 1 food and 1 oppurntunity point.")
  elif (tutorialEvent4 == "C"):
    print ("An barracks were built on the land porducing muskets.")
    print ("Gain 4 defense points.")
    print ("If you choose option A, you would have gain 3 resources. If you choose option B, you would have gain 5 food. If you choose option C, you would have gain 4 defense points. If you choose option D, you would have gained 20 settlers but loose 1 food. If you choose option E, you would have gained 1 food and 1 oppurntunity point.")
  elif (tutorialEvent4 == "D"):
    print ("Many new houses were built on the land causing more settlers to move in but we lost some food.")
    print ("Gain 20 settlers but loose 1 food.")
    print ("If you choose option A, you would have gain 3 resources. If you choose option B, you would have gain 5 food. If you choose option C, you would have gain 4 defense points. If you choose option D, you would have gained 20 settlers but loose 1 food. If you choose option E, you would have gained 1 food and 1 oppurntunity point.")
  elif (tutorialEvent4 == "E"):
    print ("The land was kept empty but some gathers has salvaged the land bringing some berries in.")
    print ("You would have gain 1 food and 1 oppurntunity point.")
    print ("If you choose option A, you would have gain 3 resources. If you choose option B, you would have gain 5 food. If you choose option C, you would have gain 4 defense points. If you choose option D, you would have gained 20 settlers but loose 1 food. If you choose option E, you would have gained 1 food and 1 oppurntunity point.")
  print ("Many Civil Events has options to give boost for what you need in your settlement.")
  print ("The next type of event is called a Side Event. These are usually events you can either skip or play to obtain rewards. Becareful though, if you choose the wrong options in Side Events it will lead to your doom. ")
  tutorialSideEventPartA = input("--|SIDE EVENT|-- /\ --|WINTER SEASON|-- A group of Natives wants to meet with you privatly without any guards. Do you agree with this?\nA. Yes, lets meet with them privatly.\nB. I will meet with them but I want my guards with me.\nC. I don't want to meet these Natives. \nSkip. Skip it.")
  if (tutorialEventPartA == "A"):
    print ("As the native enter your office, few of them soon start to surrond you. From your cornor of vision, you can see your Raipers and Flintlock Pistol. More and more Native surrond you showing their weapons. What will you do?")
    tutorialSideEventPartAPathA = input("--|SIDE EVENT|-- \nA. Ignore what the Natives are doing.\nB. Grab your weapons and be ready to attack them.\nC. Run out of the door to get help since you are outnumbered heavily.\nD. Jump out of the window to escape them.")
  elif (tutorialSideEventPartA == "skip"):
    print ("You skipped it.")
def QuitGame():
  quit()
#Game Lost Functions


def PlayGameLostNoFood():
  sernarioPicker = random.randint(0,5)
  if (sernarioPicker == 1):
    print ("Your settlement has exhausted it's food supply. With no food your settlers begin to starve to death. You were soon dragged out of your court room and was beaten to death by starving settlers.")
    print ("GAME OVER")
  elif (sernarioPicker == 2):
    print ("Your settlement has exhausted it's food supply. With no food your settlers begin to starve to death. Evantually most of the settlers has starved to death and with the remaining settlers. You begin to live a nomad life outside of your settlement. In one of your hunting trips, you were eaten by a bear and your body was never found.")
    print ("GAME OVER")
  elif (sernarioPicker == 3):
    print ("Your settlement has exhausted it's food supply. With no food your settlers begin to starve to death. Evantually most of the settlers has starved to death and with the remaining settlers you soon lead a raiding life against rivals settlements and native villages. In one raiding trip you were killed in a skirmish.")
    print ("GAME OVER")
  elif (sernarioPicker == 4):
    print ("Your settlement has exhausted it's food supply. With no food your settlers begin to starve to death. You were the last remaining settler alive on your settlement. Due to your failures your colonial power has banished you away. Your reputation was soon forgotten.")
    print ("GAME OVER")
  elif (sernarioPicker == 5):
    print ("Your settlement has exhausted it's food supply. With no food your settlers begin to starve to death. You soon starved to death due to having no food and not knowing what to eat in the wilderness due to hostile Natives scavenging your village.")
    print ("GAME OVER")

def PlayGameLostNoDefense():
    print ("With your settlement being vurnable to all attacks. The Militia of your settlement soon arrested you and excuted you.")
    print ("Game over.")



def PlayGameLostNoSettlers():
  sernarioPicker = random.randint(0,6)
  if (sernarioPicker == 1):
    print ("You have lost all of your settlers in a event. Being the last person alive in your settlement you soon wandered off into the forest of the New World. You were never seen again.")
    print ("GAME OVER")
  elif (sernarioPicker == 2):
    print ("You have lost all of your settlers in a event. Being the last person alive in your settlement you soon committed sucide due to your failures.")
    print ("GAME OVER")
  elif (sernarioPicker == 3):
    print ("You have lost all of your settlers in a event. Being the last person alive in your settlement you were soon captured by a search party from the Natives. You were never seen again.")
    print ("GAME OVER")
  elif (sernarioPicker == 4):
    print ("You have lost all of your settlers in a event. Being the last person alive in your settlement you were soon captured by a search party from the Rival Settlement. You were never seen again.")
    print ("GAME OVER")
  elif (sernarioPicker == 5):
    print ("You have lost all of your settlers in a event. Being the last person alive in your settlement you were soon excuted by your colonial power due to your failure.")
    print ("GAME OVER")
  elif (sernarioPicker == 6):
    print ("You have lost all of your settlers in a event. Being the last person alive in your settlement, you were soon found by a Pirate Gang and you join them. Few weeks later your pirate ship was attacked by the Colonial Power you once worked for. You soon died along with your ship and pirate crew.")
    print ("GAME OVER")





def PlayGameLostNegativeOppurntunity():
  sernarioPicker = random.randint(0,2)
  if (sernarioPicker == 1):
    print ("You went into negative oppurntunity, which showed your weakness in your settlement government. You were soon assassinated by other settlers which they elected someone else to be the Governor.")
    print ("GAME OVER")
  elif (sernarioPicker == 2):
    print ("You went into negative oppurntunity, whiched showed your weakness in your settlement government. The Natives use your flaws to their advantage and soon attack your settlement. The settlers along with you were all killed during the raid.")
    print ("GAME OVER")



settlers = 100
defense = 10
food = 20
resource = 3
oppurntunity = 1
# EXTRA FUNCTIONS
def PlayTester():
  choice1 = input("Would you like to try to do somthing?")
  if (choice1 == "yes"):
    print("Now choose what to do!")
    PlayGameLostNoResource()
    PlayGameLostNegativeOppurntunity()
    PlayGameLostNoSettlers()
    PlayGameLostNoDefense()
  elif (choice1 == "no"):
    print ("Everyone in your town has died! Game over")
    quit()

def PlayGameLostNoResource():
  sernarioPicker = random.randint(0,6)
  if (sernarioPicker == 1):
    print ("Your settlement did not meet the demand of your colonial power. The higher power has decided it is best to replace with someone else.")
    print ("GAME OVER")
  elif (sernarioPicker == 2):
    print ("Your settlement did not meet the demand of your colonial power. The higher power has decided to banish you due to your failure.")
    print ("GAME OVER")
  elif (sernarioPicker == 3):
    print ("Your settlement did not meet the demand of your colonial power. The higher power has decided to excute you due to your failures.")
    print ("GAME OVER")
  elif (sernarioPicker == 4):
    print ("Your settlement did not meet the demand of your colonial power. Your colonial power did not have enough resources to support them in a war. Soon your colonial power loses the war losing all of it's colonies. You were soon removed from your power and excuted by a rival power.")
    print ("GAME OVER")
  elif (sernarioPicker == 5):
    print ("Your settlement did not meet the demand of your colonial power. Your reputation was soon destroyed with your failures making you an outcast. ")
    print ("GAME OVER")
  elif (sernarioPicker == 6):
    print ("Your settlement did not meet the demand of our colonial power. Your higher ups have decided you were corrupt and you were giving or selling the resources to other powers. You were soon imprisoned in a lonely island with other highly wanted crimnals.")
    print ("GAME OVER")
    


  settler = 100
  resources = 3
  defense = 5
  food = 10
  oppurntinities = 0
  #Actual Game now starts over here on line 207
print ("Welcome to Settlement simulator, where a colonial power has sent you to the New World to collect resources for the main land back in the Age of Disvovery (1600s)! There are 35 events that you will have to play through, and a additional 15 minor events if you choose to do them. If your settlement's population reaches zero or you do not meet the demand of your mainland, you lose. ")
#Code  Tester
choice = input("Do you want to try tutorial first? Yes or No question.")
if (choice == "yes" or choice == "Yes"):
  PlayTutorial()
elif (choice == "Tester" or choice == "tester"):
  PlayTester()
elif (choice == "quit" or choice == "Quit" or choice == "QUIT"):
  QuitGame()
else: 
  print ("Let the game begin!")




print ("Settler Point =",settlers)
print ("Food Point =",food)
print ("Defence Point =",defense)
print ("Resource Point =",resource)
print ("Oppurntunity Point =",oppurntunity)
print ("*Input every answer with their according letter and in Cap Locks*")
epicEvent1= input("--|CONFLICT EVENT!|-- /\ --|SPRING SEASON!|-- A large Bandit Horde, probably pirates that landed nearby, has been spotted near our settlement. They have sent out demands and will attack if we do not meet them. What shall we do?\nA. Call the local militia in your settlement.\nB. Build a Fort.\nC. Build a Cannon.\nD. Give in to their demand.")
if (epicEvent1 == "A"):
  print ("You called the militia in your settlement to fight the Bandit Horde. We lost many brave souls.")
  print ("You would lose 20 settlers but gain 3 resource")
  settlers -= 20
  resource += 3
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)
elif (epicEvent1 == "B"):
  print ("We made a Fort and we have increased our Defense by 6 points! We have stopped their attack!")
  print ("You would increased your defense by 6 points but loose 2 resource and 2 settlers.")
  settlers -= 2
  resource -= 2
  defense += 6
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)
elif (epicEvent1 == "C"):
  print ("We made a cannon! Now we can shoot bandits away and we gain 1 defence but we lost a man!")
  print ("You would gain 1 defence but loose 1 resource and 1 settler. ")
  settlers -= 1
  resource -= 1
  defense += 1
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)
elif (epicEvent1 == "D"):
  print ("We have given the bandits what supplies they want. In return they give us litte resources for our coperation. ")
  print ("Loose 5 food, 2 Defense, 5 settlers, gain 1 resource.")
  settlers -= 5
  food -= 5
  defense -= 2
  resource += 1
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)

food -= 1         
epicEvent2= input("--|TOWN EVENT!|-- /\ --|SUMMER SEASON!|-- Many designers of your settlment have the idea of building new buildings. But are divided on what to build as one side wants a more militaristic buildings while the others want a more of population buildings. \nA. Go with the militaritic idea. More defenses means that no one will attack us right? \nB. Go with a settler idea. If the homefront is secured then the defense can be always upgraded later. If we don't get attacked. \nC. Some settlers have the idea to make the whole land into a food paradise! As long as we don't have a famine. \nD. Leave the land empty. Lets keep it that way and hope nothing happens.")
if (epicEvent2 == "A"):
  print ("Your settlement defense has rose incredibly high. This will make natives and rivals settlements think twice about raiding your settlement.")
  print ("You gain defense points and resources. But you loose some food.")
  resource += 2
  defense += 4
  food -= 2
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)
elif (epicEvent2 == "B"):
  print ("Your plan to make the settlement richer has worked! New buildings were made which saw the increase of population and resources!  ")
  print ("Gain some settlers and few resources but loose some food.")
  settlers += 20
  resource += 2
  food -= 3
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)
elif (epicEvent2 == "C"):
  print ("This project has attracted many new settlers but we lost some food and resources.")
  
sideEvent1= input
epicEvent3= input("--|DISASTER EVENT!|-- /\ --|FALL SEASON!|-- A river nearby our settlement has starting to overflow due to the rain season. The river will soon over flow it self and possibly flood our entire settlement! What shall we do?\nA. Evacuate the settlement towards higher ground.\nB. Build ditches around the settlement to guide the flood water away.\nC. Pray. \nD. Move all of the supplies up towards higher ground but leave settlers behind. \nE. Do nothing because the flood is not going to hit us. ")
if (epicEvent3 == "A"):
  print ("You were able to get most of the settlers towards high ground. But we lost many resources and food. ")
  print ("Gain few settlers but lose resources and food.")
  settlers += 5
  food -= 5
  resource -= 3
  defense -= 12
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)
elif (epicEvent3 == "B"):
  print (" Your settlement has built ditches around the whole settlement. Which was able to guide the flood water away from the settlement. Extra resources were found after the flood was over and the ditches proved to be a power defense line. ")
  print ("Gain resources and defense but lose some food.")
  resource += 3
  defense += 10
  food -= 2
  settlers += 1
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)
elif (epicEvent3 == "C"):
  print ("You prayed for god to help you but it did absolutly nothing at all.")
  while (epicEvent3 == "C"):
    resource -= 1
    defense -= 1
    food -= 1
    settlers -= 1
    oppurntunity -= 1
    print ("Settler Point =",settlers)
    print ("Food Point =",food)
    print ("Defence Point =",defense)
    print ("Resource Point =",resource)
    print ("Oppurntunity Point =",oppurntunity)
    if (resource == 0):
      break
      PlayGameLostNoResource()
      QuitGame()
    elif (oppurntunity == 0):
      break
      PlayGameLostNoOppurntunity()
      QuitGame()
    elif (settlers == 0):
      break
      PlayGameLostNoSettlers()
      QuitGame()
    elif (food == 0):
      break
      PlayGameLostNoFood()
      QuitGame()
    elif (defense == 0):
      break
      PlayGameLostNoDefense()
      QuitGame()


epicEvent4= input("—-|CIVIL EVENT!|—- /\ —-|WINTER SEASON!|—- One of our settlers has a property dispute with another neighbor. What shall we do?\nA. The Settler who claims to have the property disputed on his because the flag he placed on the land marking it was his few months ago. He wants to use the land as a new workshop.\nB. The Settler who lives on the land promises to build a farm.\nC. One of your advisors proposes to use the land as a way to build a new building for the militia.\nD. Another settler proposes to build new houseses on the property.\nE. An old man walks by saying that you should keep the land empty until a oppurntunity will rise.")
if (epicEvent4 == "A"):
  print ("The workshop was soon set up on the land generating resources for us.")
  print ("Gain some resources but lose some food.")
  food -= 1
  resource += 3
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)

elif (epicEvent4 == "B"):
  print ("The settler on the land has constructed a farm for us and it is generating food for us.")
  print ("Gain some food but lose some resources.")
  food += 5
  resource -= 1
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)
    
elif (epicEvent4 == "C"):
  print ("An barracks were built on the land porducing muskets.")
  print ("Gain some defense points")
  defense += 5
  resource -= 2
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)

elif (epicEvent4 == "D"):
  print ("Many new houses were built on the land causing more settlers to move in but we lost some food.")
  print ("Gain lots of settlers but lose some food.")
  settlers += 20
  food -= 5
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)

elif (epicEvent4 == "E"):
  print ("The land was kept empty but some gathers has salvaged the land bringing some berries in.")
  print ("The empty land gave you few found and few oppurntunities.")
  food += 1
  oppurntunity += 2
  print ("Settler Point =",settlers)
  print ("Food Point =",food)
  print ("Defence Point =",defense)
  print ("Resource Point =",resource)
  print ("Oppurntunity Point =",oppurntunity)

choice1= input("Would you like to play side event? Yes or No?")
if (choice1 == "Yes" or choice1 == "yes" or choice1 == "YES"):
  sideEvent2= input("In you office you receive word that a trading company wants to meet you in your settlement outside of your courthouse. \nA. Meet him outside. \nB. Ignore him.")
  if (sideEvent2 == "A"):
    print ("You met with him outside which he has brought a extremely good deal you agreed to.")
    print ("You gain lots of resources but loose few food.")
    resource += 3
    oppurntunity += 1
    food -= 4
    print ("Settler Point =",settlers)
    print ("Food Point =",food)
    print ("Defence Point =",defense)
    print ("Resource Point =",resource)
    print ("Oppurntunity Point =",oppurntunity)
  else:
    print ("The trader hated your choice and stole many of your supplies.")
    print ("You lose lots of food and resources as well as oppurntunities.")
    resource -= 2
    food -= 25
    oppurntnity -= 2
    print ("Settler Point =",settlers)
    print ("Food Point =",food)
    print ("Defence Point =",defense)
    print ("Resource Point =",resource)
    print ("Oppurntunity Point =",oppurntunity)
            
else:
  print ("You skipped the side event.")

print ("Settler Point =",settlers)
print ("Food Point =",food)
print ("Defence Point =",defense)
print ("Resource Point =",resource)
print ("Oppurntunity Point =",oppurntunity)
if (settlers == 135 or settlers >= 135):
  print ("You have made a successful colony filled with settlers. Although your main objective was to gather resources. the higher up has approved of your work. ")
  print ("You beat the game!")
  QuitGame()
elif (resource == 12 or resource >= 12):
  print ("Your settlement has brought back resources for your colonial empire. The higher ups are very proud of your work and made you governor of their clonies. ")
  print ("You beat the game!")
  QuitGame()
elif (oppurntunity == 10 or oppurntunity >= 10):
  print ("You present many oppurntunities to your colonial power. They take your word and soon build a powerful empire. They reward you greatly.")
  print ("You beat the game!")
  QuitGame()
else:
  print ("You have failed your colonial power and you are soon excuted.")
  print ("GAME OVER")
  QuitGame()














