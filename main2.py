name="blank"
import os

itemDict = {"blank": "There is nothing here!", "map": "A crumpled and worn map. You have circled many locations, but your current one seems to have lots of small scribblings around the circle.", "note": "Hello there! I hear you're about to take the Memory Loss Potion. So, I welcome you to your new life. Enjoy the sights you see! This should be the only thing you'll have on you, if you have anything else - I highly recommend you drop it now. You might even remember who you are! Lots of luck - Dr. Brandshire (CEO of NewLife Corp)", "wrench": "It's a Steel Wrench. There are small marks along the base of this tool, showing years of usage.", "glass": "Hmm.... why would nobody notice this piece of glass? It was on the bar, near to the right."}

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

	journalEntries = ["null"]
	journalData = ["letter"]
	return locName, locDesc, locLongDesc, playerInv, inventoryData, locItems, itemData, journalEntries, journalData

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
	if command=="journal":
		displayMessage("journal")
		pass


def inspectItem(item):
	global itemDict
	os.system("cls")

	print(itemDict[item])

	print("")
	input("Press any key....")
	os.system("cls")

def journalRead(entry):
	if entry==1:
		print("")
		pass


def callEvent(eventName):
	global storyProgression
	if eventName=="wrench" and storyProgression==0:
		os.system("cls")
		print("The wrench has a lot of marks on it.")
		print("")
		print("Wait a minute.... there's a red mark on it!")
		storyProgression += 10

def takeItem(passedItem):
	playerInv.append(locItems[currentLoc])
	inventoryData.append(itemData[currentLoc])

	# Is it an event item?
	if itemData[currentLoc]=="wrench":
		callEvent("wrench")
		pass

	locItems[currentLoc]=""
	itemData[currentLoc]=""

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
		print("- JOURNAL - Read thoughts of the player and re-read certain events.")
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
		elif currentLoc>=1:
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

	if call=="journal":
		os.system("cls")
		print("Which item would you like to read again?")
		print("")
		print(journalData)
		print("Please enter the keyword you want:")
		print("")
		entrySelection = input("?: ")
		journalRead(int(entrySelection))
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

locName, locDesc, locLongDesc, playerInv, inventoryData, locItems, itemData, journalEntries, journalData = initLocations()
global health
health = 10
global currentLoc
currentLoc = 0
global invPosition
invPosition = 0
global storyProgression
storyProgression = 0

#Let's say the final location is 20.

while currentLoc < 20: #Change to max location if ever changed (if max location is ever changed)
	print(" _____                _ _               _____                           _       ")
	print("|  __ \              | (_)             / ____|                         (_)      ")
	print("| |__) |__  ___ _   _| |_  __ _ _ __  | (___   ___ ___ _ __   __ _ _ __ _  ___  ")
	print("|  ___/ _ \/ __| | | | | |/ _` | '__|  \___ \ / __/ _ \ '_ \ / _` | '__| |/ _ \ ")
	print("| |  |  __/ (__| |_| | | | (_| | |     ____) | (_|  __/ | | | (_| | |  | | (_) |")
	print("|_|   \___|\___|\__,_|_|_|\__,_|_|    |_____/ \___\___|_| |_|\__,_|_|  |_|\___/ ")
	print("")	
	print("----" + locName[currentLoc] + "----")
	print("--" + locDesc[currentLoc] + "--")
	print("")
	print("Story Progress - " + str(storyProgression) + "%")
	print("")
	print("Type 'Help' for advice on what to do next.")
	passedCommand = input("?: ")
	mainProcess(passedCommand)
	os.system("cls")
