name = "blank"
global microscopeState
microscopeState = 0
import os

#Set up all the dictionaries.
#----------------------------------------------------------------
microscopeFindings = {"map": "There is nothing special about this.", "note": "There is nothing special about this.", "wrench": "A metal wrench that has a few scratches and marks on it. Apart from that, there's nothing very interesting or new about it.", "glass": "The glass semes to be fully jagged around the edges, showing somebody threw it to the floor.", "hat": "Wait a minute.... The marks really are burns. It looks like the hat fell onto a flame, before it was taken away again."}

itemDict = {"blank": "There is nothing here!", "map": "A crumpled and worn map. You have circled many locations, but your current one seems to have lots of small scribblings around the circle.", "note": "Hello there! I hear you're about to take the Memory Loss Potion. So, I welcome you to your new life. Enjoy the sights you will see! This should be the only thing you'll have on you, if you have anything else - I highly recommend you drop it now. You might even remember who you are! Lots of luck - Dr. Brandshire (CEO of NewLife Corp)", "wrench": "It's a Steel Wrench. There are small marks along the base of this tool, showing years of usage.", "glass": "Hmm.... why would nobody notice this piece of glass? It was on the bar, near to the right.", "hat": "The hat seems to have a few marks on it, but there are many black marks on it; they look like burns....","book": "The book goes into great detail about the Human Brain. However, someone looks like they skimmed through these pages in a hurry....", "microscope": "A small and handy piece of technology that can look at evidence in greater detail."}

journalDict = {"letter": "Hello there! I hear you're about to take the Memory Loss Potion. So, I welcome you to your new life. Enjoy the sights you see! This should be the only thing you'll have on you, if you have anything else - I highly recommend you drop it now. You might even remember who you are! Lots of luck - Dr. Brandshire (CEO of NewLife Corp)"}

fullJournalDict = {"letter": "Hello there! I hear you're about to take the Memory Loss Potion. So, I welcome you to your new life. Enjoy the sights you see! This should be the only thing you'll have on you, if you have anything else - I highly recommend you drop it now. You might even remember who you are! Lots of luck - Dr. Brandshire (CEO of NewLife Corp)", "wrench": "The wrench I found seems to have a few red marks on it. I can't say it's blood, but it looks too dark to be paint. I'll have to remember this for future reference.", "glass": "This piece of glass was with many other pieces of glass. This is the largest piece, it seems.", "bolts": "There are bolts around the door, near where I found the broken glass. Perhaps a certain tool will help me open the door.", "poison": "The storage locker in the Pub seemed to have a little too much Rat Poison to match the cleanliness of the Pub. Something is going on here....","microscope": "The microscope is a small but handy piece of equipment. I can now use the microscope from the command MICROSCOPE."}

#Set up all the processes and functions etc.
#----------------------------------------------------------------
def initLocations():
	locName = ["The Town","The Blacksmith Hut","The Pub","The Street","The Library","The Laboratory","You cannot move right."]
	locDesc = ["A Small Town","A Small Hut","A nice pub","An ancient paved street","Filled with brilliant books","A modern and advanced building"]
	locLongDesc = ["This town is filled with beautiful shops, all built by hand by the local residents. It is a place of tranquility and friendliness.","The Blacksmith Hut is an old, hand-built establishment which has housed many blacksmiths over the years.","The Pub has always been here. Inside is a beautiful carpet with burgandy squares, and the bar is decorated with carved wood pillars and surfaces.","Neatly aligned cobble lines the street, with squares of stones filling in the road.","Old books line dusty shelves, but the strange mysterious nature of discovering something new within the leather-bound pages is too much to resist.","The lab is decorated with gleaming white paint, symbolizing the graceful advance of modern science in the world today."]
	playerInv = ["A Leather Map","A Tattered Note"]
	inventoryData = ["map","note"]
	locItems = ["","A Steel Wrench","Shattered Glass","Top Hat","'The Human Brain' by Dr E. Jameson","Microscope"]
	itemData = ["","wrench","glass","hat","book","microscope"]

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
	if command=="use":
		displayMessage("use")
		pass
	if command=="kill":
		# Will's idea I swear
		print("")
		print("That's just sad.")
		input("")
		os.system("cls")
		pass
	if command=="microscope":
		if microscopeState==1:
			displayMessage("microscope")
			pass
		elif microscopeState==0:
			pass
		pass


def inspectItem(item):
	global itemDict
	os.system("cls")

	print(itemDict[item])

	print("")
	input("Press any key....")
	os.system("cls")

def journalRead(entry):
	print(journalDict[entry])

def microscope(item):
	print(microscopeFindings[item])
	pass

def useMicroscope():
	os.system("cls")
	print("You hold the microscope close to your eye....")
	print("")
	print("Your current inventory:")
	print("")
	print(playerInv)
	print("")
	print("Use these keywords to use the microscope on the item:")
	print("")
	print(inventoryData)
	print("")
	print("Please enter the keyword you want:")
	microscopeSelection = input("?: ")
	if microscopeSelection!="":
		microscope(microscopeSelection)
		pass

def callEvent(eventName):
	global storyProgression
	global microscopeState
	if eventName=="wrench":
		os.system("cls")
		print("The wrench has a lot of marks on it.")
		print("")
		print("Wait a minute.... there's a red mark on it!")
		print("")
		input("Please press a key....")
		print("")
		print("! - Journal Entry Added.")
		journalData.append("wrench")
		journalDict["wrench"] = fullJournalDict["wrench"]
		storyProgression += 10
		pass

	if eventName=="glass":
		os.system("cls")
		print("Wait.... this isn't the only piece. There's loads of glass here....")
		print("Could this possibly be a murder case?")
		print("")
		print("There seems to be a door near the glass, but it's bolted shut.")
		print("")
		print("! - Journal Entry Added")
		journalData.append("glass")
		journalDict["glass"] = fullJournalDict["glass"]
		storyProgression += 10
		journalData.append("bolts")
		journalDict["bolts"] = fullJournalDict["bolts"]
		pass

	if eventName=="microscope":
		os.system("cls")
		print("The lab is filled with these amazing inventions.")
		print("Perhaps it would come in handy?")
		print("")
		print("! - Journal Entry Added")
		journalData.append("microscope")
		journalDict["microscope"] = fullJournalDict["microscope"]
		storyProgression += 10
		microscopeState = 1
		pass

def useItem(item):
	global storyProgression
	global currentLoc

	if item=="wrench" and currentLoc==2 and storyProgression==20:
		os.system("cls")
		print("The door is unbolted.")
		print("")
		print("It's just a storage locker. There's a few screws and around four bottles.")
		print("The bottles seem to all be rat poison. I don't see why somebody would need")
		print("such an exessive amount; the pub seems clean enough....")
		print("")
		print("! - Journal Entry Added")
		print("")
		input("Please press a key....")
		os.system("cls")
		print("! - Mystery Completed! - 'The Bolted Door'")
		input("Press any key to return....")
		journalData.append("poison")
		journalDict["poison"] = fullJournalDict["poison"]
		storyProgression += 10
		journalData.remove("bolts")
		pass

def takeItem(passedItem):
	global itemSelection
	global storyProgression

	# Is it an event item?
	if itemData[currentLoc]=="wrench" and storyProgression==0 and itemSelection=="wrench":
		callEvent("wrench")
		playerInv.append(locItems[currentLoc])
		inventoryData.append(itemData[currentLoc])
		locItems[currentLoc]=""
		itemData[currentLoc]=""
		pass

	if itemData[currentLoc]=="glass" and storyProgression==10 and itemSelection=="glass":
		callEvent("glass")
		playerInv.append(locItems[currentLoc])
		inventoryData.append(itemData[currentLoc])
		locItems[currentLoc]=""
		itemData[currentLoc]=""
		pass
	elif itemData[currentLoc]=="glass" and storyProgression!=10 and itemSelection=="glass":
		print("I don't need that yet.")
		pass

	if itemData[currentLoc]=="microscope" and storyProgression==30 and itemSelection=="microscope":
		callEvent("microscope")
		playerInv.append(locItems[currentLoc])
		inventoryData.append(itemData[currentLoc])
		locItems[currentLoc]=""
		itemData[currentLoc]=""
		pass
	elif itemData[currentLoc]=="microscope" and storyProgression!=30 and itemSelection=="microscope":
		print("I don't need that yet.")
		pass

def displayMessage(call):
	global currentLoc
	global invPosition
	global storyProgression
	global itemSelection

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
		print("- USE - Apply an item to an area. This will lead to the completion of mysteries.")
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
		elif currentLoc>=1 and currentLoc<=5:
			print("Left: " + locName[currentLoc-1])
			print("Right: " + locName[currentLoc+1])
		elif currentLoc==6:
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
		if itemSelection=="":
			print("Please enter a selection.")
			pass
		elif itemSelection!="":
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
		journalRead(entrySelection)
		pass

	if call=="use":
		os.system("cls")
		print("Use which item?")
		print("")
		print(playerInv)
		print("")
		print("Their keywords are as follows:")
		print("")
		print(inventoryData)
		print("")
		print("Please enter the keyword you want:")
		print("")
		useSelection = input("?: ")
		useItem(useSelection)
		pass

	if call=="microscope":
		os.system("cls")
		useMicroscope()
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

while currentLoc < 7:
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
	print("Type 'help' for advice on what to do next.")
	passedCommand = input("?: ")
	mainProcess(passedCommand)
	os.system("cls")
