#Import a GUI
from tkinter import *
from tkinter.ttk import *

#initialize gui
master = Tk()



#Get from user the times, courts, and grades.

l1 = Label(master, text = "How many Courts do you have?")
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2 = Label(master, text = "How many Timeslots do you have?")
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
l3 = Label(master, text = "How many grades do you have?")
l3.grid(row = 2, column = 0, sticky = W, pady = 2)

 
courtCount = StringVar()
courtBox = Entry(master, textvariable = courtCount)
courtBox.grid(row = 0, column = 1, pady = 2)
courtBoxLabel = Label(master, text = '0')
courtBoxLabel.grid(row = 0, column = 2, sticky = W, pady = 2)


timeslots = StringVar()
timeBox = Entry(master, textvariable = timeslots)
timeBox.grid(row = 1, column = 1, pady = 2)
timeBoxLabel = Label(master, text = '0')
timeBoxLabel.grid(row = 1, column =2, sticky = W, pady = 2)

grades = StringVar()
gradesBox = Entry(master, textvariable = grades)
gradesBox.grid(row = 2, column = 1, pady = 2)
gradesBoxLabel = Label(master, text = '0')
gradesBoxLabel.grid(row = 2, column = 2, sticky = W, pady = 2)


#Pre-filled for testing
teamsList = ["A","B","C","D","E"]

#Pre-filled for testing, just delete these two



listVar = StringVar()

teamBox = Entry(master, textvariable = teamsList)
teamBox.grid(row = 3, column = 1, pady = 2)

#Adds teams entered by the user to the list. 
def addTeam():
	if teamBox.get() != '':
		teamsList.append(teamBox.get())
	listVar.set(teamsList)

#Creates the draw
#Does too much atm, currently working on adding the number of courts and the number of timeslots into the logic. 
#Thinking of creating a 2D array with courts and times here, and adding the games randomly into each space.
def generateDraw():

	#First, update the labels on the widget to display the current values the program will work with.
	if courtBox.get() != '':
		courtBoxLabel.config(text = str(courtBox.get()))
	if timeBox.get() != '':
		timeBoxLabel.config(text = str(timeBox.get()))
	if gradesBox.get() != '':
		gradesBoxLabel.config(text = str(gradesBox.get()))

	teamsTotal = len(teamsList)

	#initialize the use of the functions
	match = matches()
	#print (match)
	court = courts(match, courtBoxLabel.cget ("text"))
	print (court)
	time = times(court, timeBoxLabel.cget("text"))
	#print (time)
	games = grades(time)
	#print (games)

#Takes each team named in the list, and pits them against each other.
#Not quite working on bigger sample sets.
def matches():
	matchups = []
	#copies the origional teams list so it remains intact
	tL = teamsList
	for i in tL:
		for j in tL:
			#prevents a team from playing itself
			if i != j:
				matchups.append(i+" Vs. "+j)
		#removes doulbleups of games already in system
		tL.remove(i)
	return matchups

def courts(c, k):
	#print (c)
	#print (k)

	courtArr = []
	cA = c
	#If statements to make court assignment easy.. ish.
	if k == str(0):
		return ("Nowhere to play?")
	if k == str(1):
		for i in cA:
			courtArr.append(i+" on Court 1")

	#Could now be any number of courts. Needs to deal with odds and evens. 
	if int(k) >= 2:
		for i in range(int(k)):
			for f in cA:
				courtArr.append([f+" on Court "+str(i+1)])
				cA.remove(f)
	return courtArr

def times(t, l):
	return t

def grades(g):
	return g

#Get from user the teams

b1 = Button(master, text = "Add team and update list:", command = addTeam)
b1.grid(row = 3, column = 0, pady = 2)

l4 = Label(master, text = "Teams Entered-->")
l4.grid(row = 4, column = 0, sticky = W, pady = 2)

l5 = Label(master, textvariable = listVar)
l5.grid(row = 4, column = 1, sticky = W, pady = 2)

b2 = Button(master, text = "I confirm the teams list is complete.\n 	Lock in times, grades, and courts, and Generate Draw!", command  = generateDraw)
b2.grid(row = 6, column = 1, sticky = W, pady = 2)

l6 = Label(master, text = "If if comes to it, which would you prefer?").grid(row = 5, column = 0)

choice = {"Byes" : "1", "Doulble Headers" : "2"}
for (text, value) in choice.items():
	Radiobutton(master, text = text, value = value).grid(row = 5, column = int(value))

mainloop()