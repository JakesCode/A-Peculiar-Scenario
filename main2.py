name="blank"
import os

#Set up all the processes and functions etc.
#----------------------------------------------------------------
def initLocations():
	locName = ["The Town","The Blacksmith Hut","The Pub","The Street","The Library"]
	locDesc = ["A Small Town","A Small Hut","A nice pub","An ancient paved street","Filled with brilliant books"]
	locLongDesc = ["This town is filled with beautiful shops, all built by hand by the local residents. It is a place of tranquility and friendliness.","The Blacksmith Hut is an old, hand-built establishment which has housed many blacksmiths over the years.","The Pub has always been here. Inside is a beautiful carpet with burgandy squares, and the bar is decorated with carved wood pillars and surfaces.","Neatly aligned cobble lines the street, with squares of stones filling in the road.","Old books line dusty shelves, but the strange mysterious nature of discovering something new within the leather-bound pages is too much to resist."]
	playerInv = ["A Leather Map","A Tattered Note"]
	inventoryData = ["map","note"]
	locItems = ["","A Steel Wrench","Shattered Glass","Top Hat","'The Human Brain' by Dr E. Jameson"]
	itemData = ["","wrench","glass","hat","book"]
	return locName, locDesc, locLongDesc, playerInv, inventoryData, locItems, itemData

def mainProcess(command):
	if command=="help":
		displayMessage("help")
		pass
	if command=="move":
		displayMessage("move")
		pass
	if command=="location":
		displayMessage("location")
		pass
	if command=="inventory":
		displayMessage("inventory")
		pass
	if command=="inspect":
		displayMessage("inspect")
		pass
	if command=="scan":
		displayMessage("scan")
		pass
	if command=="take":
		displayMessage("take")
		pass


def inspectItem(item):
	os.system("cls")
	if item=="map":
		print("A crumpled and worn map. You have circled many locations, but your current one seems to have lots of small scribblings around the circle.")
		pass

	if item=="note":
		print("The note reads:")
		print("")
		print("Hello there! I hear you're about to take the Memory Loss Potion. So, I welcome you to your new life. Enjoy the sights you see! This should be the only thing you'll have on you, if you have anything else - I highly recommend you drop it now. You might even remember who you are!")
		print("Lots of luck from,")
		print("Dr. Brandshire")
		print("CEO of NewLife Corp")
		pass

	if item=="wrench":
		print("It's a Steel Wrench. There are small marks along the base of this tool, showing years of usage.")

	print("")
	input("Press any key....")
	os.system("cls")

def takeItem(item):
	playerInv.append(locItems[currentLoc])
	inventoryData.append(itemData[currentLoc])
	del locItems[currentLoc]
	del itemData[currentLoc]

def displayMessage(call):
	global currentLoc
	global invPosition
	global storyProgression
	os.system("cls")
	if call=="help":
		print("**HELP**")
		print("")
		print("The Adventure Game uses a system of commands")
		print("Here is a list of currently known commands:")
		print("")
		print("- MOVE - Allows the player to move left or right.")
		print("- LOCATION - Look at the location in greater detail.")
		print("- INVENTORY - View the items you are currently holding.")
		print("- INSPECT - Look at, or read, an item in your inventory.")
		print("- SCAN - View the items in the current location.")
		print("- TAKE - Allows the player to obtain an item in a certain location.")
		print("")
		print("Believe it or not, there's a story in this game.")
		print("Your current position in the story is indicated by a percentage")
		print("located underneath the location information on the main screen.")
		print("")
		pass

	if call=="move":
		print("Move where?")
		print("")
		if currentLoc==0:
			print("Left: You cannot move left.")
			print("Right: " + locName[currentLoc+1])
		elif currentLoc>1:
			print("Left: " + locName[currentLoc-1])
			print("Right: " + locName[currentLoc+1])
		elif currentLoc==19:
			print("Left: " + locName[currentLoc-1])
			print("Right: You cannot move right.")
		print("")
		print("Move left or right? Enter your choice.")
		direction = input("?: ")
		if direction=="left":
			if currentLoc>1:
				print("Moved left.")
				currentLoc = currentLoc-1
				pass
		elif direction=="right":
			currentLoc = currentLoc+1
			pass
	pass

	if call=="location":
		os.system("cls")
		print(locLongDesc[currentLoc])
		pass

	if call=="inventory":
		os.system("cls")
		print(playerInv)
		print(inventoryData)
		pass

	if call=="inspect":
		os.system("cls")
		print("Inspect which item?")
		print("")
		print("Your current inventory:")
		print("")
		print(playerInv)
		print("")
		print("Use these keywords to inspect the item:")
		print("")
		print(inventoryData)
		print("")
		print("Please enter the keyword you want:")
		invSelection = input("?: ")
		inspectItem(invSelection)
		pass

	if call=="scan":
		os.system("cls")
		print("Current items in the location....")
		print(locItems[currentLoc])
		if (locItems[currentLoc])=="":
			print("There are no items here.")
			pass
		pass

	if call=="take":
		os.system("cls")
		print("Which item should be removed?")
		print("")
		print(locItems[currentLoc])
		print("(Their keywords:)")
		print(itemData[currentLoc])
		print("")
		print("Please enter the keyword you want:")
		itemSelection = input("?: ")
		takeItem(itemSelection)
		pass

	print("")
	input("Press any key to return....")
	os.system("cls")
#----------------------------------------------------------------

#Main Game

#print("Adventure Game")
#print("")
#print("Please enter your name: ")
#name = input("?: ")
#
#while name=="":
#	os.system("cls")
#	print("* - Make sure you enter a name.")
#	print("")
#	print("Please enter your name: ")
#	name = input("?: ")
#	pass
#
#print("Hello, " + name + "!")
#print("")

locName, locDesc, locLongDesc, playerInv, inventoryData, locItems, itemData = initLocations()
global health
health = 10
global currentLoc
currentLoc = 0
global invPosition
invPosition = 0
global storyProgression
storyProgression = 0

#Let's say the final location is 20.

while currentLoc < 20:
	print("----" + locName[currentLoc] + "----")
	print("--" + locDesc[currentLoc] + "--")
	print("")
	print("Story Progress - " + str(storyProgression) + "%")
	print("")
	print("Type 'Help' for advice on what to do next.")
	passedCommand = input("?: ")
	mainProcess(passedCommand)
	os.system("cls")