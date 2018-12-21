#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import json




for j in range (1, 86):

	file = open("rawHTML/" + str(j) + ".html", "r")

	lines = file.readlines()

	teamIndex = 0

	team1Points = []
	team1SubPoints = 0
	team2SubPoints = 0
	team2Points = []
	gameweek = 0
	teamNames = []


	positionIndex = 0


	for i in range(0, len(lines)):

		#Grab gameweek number
		if re.search('\W<small>Gameweek', lines[i]):
			gameweek = re.search('[0-9]+', lines[i]).group()
			print 'This is gameweek ' + str(gameweek)

		#Grab teamNames
		if re.search('\W<h2>[0-9 A-Z a-z á é \& ; , \W]+/h2>', lines[i]):
			teamNames.append(re.findall('[A-Za-z\sáé\&;\']+', lines[i])[2] + ', ' + re.findall('[A-Za-z\sáé\&;\']+', lines[i])[5])

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

					playerPoints = re.search('[\w-]+', lines[i+2]).group()

					if teamIndex == 0:

						team1Points[positionsProcessed-1].append(playerPoints)

					else:
						team2Points[positionsProcessed-1].append(playerPoints)

				i=i+1

			positionsProcessed = 0
			teamIndex += 1

		subsDiv = re.search('\s<div class="bench"', lines[i])
		
		if subsDiv is not None:
			
			subsProcessed = 0
			subPts = 0
			
			while subsProcessed < 4:
				if re.search('\s[-0-9]+', lines[i+1]):
					subPts += int(re.search('\s[-0-9]+', lines[i+1]).group())
					subsProcessed += 1
				i=i+1

			if teamIndex-1 == 0:
				team1SubPoints = subPts


			else:
				team2SubPoints = subPts

			subsProcessed = 0


	
	#Serialize to master JSON
	with open('final.json') as file:
		data = json.load(file)

		thisMatch = {}

		#head to head match
		if teamNames[0][0:3] != 'Ave' and teamNames[1][0:3] != 'Ave':

			thisMatch['team1'] = {}
			thisMatch['team1']['name'] = teamNames[0]
			thisMatch['team1']['starting'] = {}
			thisMatch['team1']['starting']['keeper'] = {}
			thisMatch['team1']['starting']['defenders'] = {}
			thisMatch['team1']['starting']['midfielders'] = {}
			thisMatch['team1']['starting']['strikers'] = {}

			thisMatch['team1']['starting']['keeper']['points'] = team1Points[0][0]
			thisMatch['team1']['starting']['keeper']['count'] = 1

			defenderPts = 0
			for i in range(0, len(team1Points[1])):
				defenderPts += int(team1Points[1][i])
			
			thisMatch['team1']['starting']['defenders']['points'] = defenderPts 
			thisMatch['team1']['starting']['defenders']['count'] = len(team1Points[1])
			

			midfielderPts = 0
			for i in range(0, len(team1Points[2])):
				midfielderPts += int(team1Points[2][i])
			
			thisMatch['team1']['starting']['midfielders']['points'] = midfielderPts 
			thisMatch['team1']['starting']['midfielders']['count'] = len(team1Points[2])	


			strikerPts = 0
			for i in range(0, len(team1Points[3])):
				strikerPts += int(team1Points[3][i])
			
			thisMatch['team1']['starting']['strikers']['points'] = strikerPts 
			thisMatch['team1']['starting']['strikers']['count'] = len(team1Points[3])

			thisMatch['team1']['subs'] = {}
			thisMatch['team1']['subs']['points'] = team1SubPoints


			thisMatch['team2'] = {}
			thisMatch['team2']['name'] = teamNames[1]
			thisMatch['team2']['starting'] = {}
			thisMatch['team2']['starting']['keeper'] = {}
			thisMatch['team2']['starting']['defenders'] = {}
			thisMatch['team2']['starting']['midfielders'] = {}
			thisMatch['team2']['starting']['strikers'] = {}
			
			print team2Points
			print teamNames[1][0:3]

			thisMatch['team2']['starting']['keeper']['points'] = team2Points[0][0]
			thisMatch['team2']['starting']['keeper']['count'] = 1

			defenderPts = 0
			for i in range(0, len(team2Points[1])):
				defenderPts += int(team2Points[1][i])
			
			thisMatch['team2']['starting']['defenders']['points'] = defenderPts 
			thisMatch['team2']['starting']['defenders']['count'] = len(team2Points[1])
			

			midfielderPts = 0
			for i in range(0, len(team2Points[2])):
				midfielderPts += int(team2Points[2][i])
			
			thisMatch['team2']['starting']['midfielders']['points'] = midfielderPts 
			thisMatch['team2']['starting']['midfielders']['count'] = len(team2Points[2])	


			strikerPts = 0
			for i in range(0, len(team2Points[3])):
				strikerPts += int(team2Points[3][i])
			
			thisMatch['team2']['starting']['strikers']['points'] = strikerPts 
			thisMatch['team2']['starting']['strikers']['count'] = len(team2Points[3])

			thisMatch['team2']['subs'] = {}
			thisMatch['team2']['subs']['points'] = team2SubPoints

		#Avg team contest

		else:

			thisMatch['team1'] = {}
			if teamNames[0][0:3] == 'Ave':
				thisMatch['team1']['name'] = teamNames[1]
			else :
				thisMatch['team1']['name'] = teamNames[0]

			thisMatch['team1']['starting'] = {}
			thisMatch['team1']['starting']['keeper'] = {}
			thisMatch['team1']['starting']['defenders'] = {}
			thisMatch['team1']['starting']['midfielders'] = {}
			thisMatch['team1']['starting']['strikers'] = {}

			thisMatch['team1']['starting']['keeper']['points'] = team1Points[0][0]
			thisMatch['team1']['starting']['keeper']['count'] = 1

			defenderPts = 0
			for i in range(0, len(team1Points[1])):
				defenderPts += int(team1Points[1][i])
			
			thisMatch['team1']['starting']['defenders']['points'] = defenderPts 
			thisMatch['team1']['starting']['defenders']['count'] = len(team1Points[1])
			

			midfielderPts = 0
			for i in range(0, len(team1Points[2])):
				midfielderPts += int(team1Points[2][i])
			
			thisMatch['team1']['starting']['midfielders']['points'] = midfielderPts 
			thisMatch['team1']['starting']['midfielders']['count'] = len(team1Points[2])	


			strikerPts = 0
			for i in range(0, len(team1Points[3])):
				strikerPts += int(team1Points[3][i])
			
			thisMatch['team1']['starting']['strikers']['points'] = strikerPts 
			thisMatch['team1']['starting']['strikers']['count'] = len(team1Points[3])

			thisMatch['team1']['subs'] = {}
			thisMatch['team1']['subs']['points'] = team1SubPoints


	
		data[int(gameweek)-1]['matches'].append(thisMatch)

		f= open("final.JSON","w+")
		
		f.write(json.dumps(data, indent=2, sort_keys=True))

		f.close()

