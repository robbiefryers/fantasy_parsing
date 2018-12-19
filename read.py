#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


file = open("rawHTML/88.html", "r")
lines = file.readlines()

teamIndex = 0

team1Points = []
team2Points = []
gameweek = 0
teamNames = []


positionIndex = 0


for i in range(0, len(lines)):
	if re.search('\W<small>Gameweek', lines[i]):
		gameweek = re.search('[0-9]+', lines[i]).group()
		print 'This is gameweek ' + str(gameweek)

	if re.search('\W<h2>[A-Z a-z á]+,\W<s', lines[i]):
		print re.findall('[a-zA-Z\sá]+', lines[i])[2] +  ', ' + re.findall('[a-zA-Z\sá]+', lines[i])[5]

	
	startingDiv = re.search('\s<div class="starting', lines[i])

	if startingDiv is not None:

		positionsProcessed = 0
		
		while positionsProcessed < 5:
			
			if re.search('\s<div class="historyPitchRow', lines[i+1]):
				
				if teamIndex == 0:
					team1Points.append([])

				else:
					team2Points.append([])

				positionsProcessed+=1

			if re.search('\s<span class="pick-text', lines[i+1]):

				playerPoints = re.search('\w', lines[i+2]).group()

				if teamIndex == 0:

					team1Points[positionsProcessed-1].append(playerPoints)

				else:
					team2Points[positionsProcessed-1].append(playerPoints)

			i=i+1

		positionsProcessed = 0
		teamIndex += 1


print team1Points
print team2Points
		



