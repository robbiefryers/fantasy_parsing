#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import json


teams = [
	['ArsenalFamTV', 'Sean Phelan'],
	['FC Breezy', 'Fearghal Breslin'],
	['Chocolate Busquets Cake', 'Eoghan O\'Sullivan'],
	['Making Up the Numbers XI', 'Conall Ennis'],
	['James McCarthyism', 'Ruairi Langhammer'],
	['Arouna Koné 2012', 'Robbie Fryers'],
	['Willian Dollar Baby', 'Peter O\'Boyle'],
	['John Carver of Mars', 'Gavin Cooney'],
	['The Raging Varmints', 'Conor Kenny'],
	['Core Kylian', 'Cillian Dickson']
]

matches_processed_this_week = 0
gameweek = 0

for j in range (1, 191):

	raw_file = open("raw/" + str(j) + ".html", "r")

	lines = raw_file.readlines()

	team1Name = ''
	team2Name = ''

	team1Points = [
		[],	#keeper
		[],	#defenders
		[],	#midfields
		[],	#forwards
		[]	#subs
	]

	team2Points = [
		[],	#keeper
		[],	#defenders
		[],	#midfields
		[],	#forwards
		[]	#subs
	]	
	

	for i in range(0, len(lines)):


		#Grab important line which has the minified HTML with the game 
		if re.search('\W<h2>[0-9 A-Z a-z á é \& ; , \W]+/h2>', lines[i]):

			#gamweek cant be grabbed from 2 lines above the main minfified line
			gameweek = int(re.findall('>Gameweek ([0-9]+)<', lines[i-2])[0])

			print('Processing match ' + str(matches_processed_this_week+1) + ' from gameweek ' + str(gameweek))
			
		
			#Split this minified line into the elements which contain data for team 1 and 2
			team1Raw = lines[i].split('col-md-6')[1]
			team2Raw = lines[i].split('col-md-6')[2]
			
			for k in range(0, len(teams)):
				if (re.search(teams[k][0], team1Raw)):
					team1Name = teams[k][0]
				if (re.search(teams[k][0], team2Raw)):
					team2Name = teams[k][0]
			
			team1StartingRaw = team1Raw.split('bench')[0]
			team1BenchRaw = team1Raw.split('bench')[1]

			team2StartingRaw = team2Raw.split('bench')[0]
			team2BenchRaw = team2Raw.split('bench')[1]

			team1RowsRaw = team1StartingRaw.split('historyPitchRow')
			team2RowsRaw = team2StartingRaw.split('historyPitchRow')

			for k in range(1,5):
				team1Points[k-1] = re.findall('>([-0-9]+)<', team1RowsRaw[k])
				team2Points[k-1] = re.findall('>([-0-9]+)<', team2RowsRaw[k])

			team1Points[4] = re.findall('>([-0-9]+)<', team1BenchRaw)
			team2Points[4] = re.findall('>([-0-9]+)<', team2BenchRaw)

			break

	raw_file.close()


	#Serialize to master JSON
	with open('final.json') as latest_json_file:
		
		latest_json_data = json.load(latest_json_file)

		latest_json_file.close()

		thisMatch = {}

	
		thisMatch['team1'] = {}
		thisMatch['team1']['name'] = team1Name
		thisMatch['team1']['starting'] = {}
		thisMatch['team1']['starting']['keeper'] = {}
		thisMatch['team1']['starting']['defenders'] = {}
		thisMatch['team1']['starting']['midfielders'] = {}
		thisMatch['team1']['starting']['strikers'] = {}

		thisMatch['team1']['starting']['keeper']['points'] = int(team1Points[0][0])
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


		subPts = 0
		for i in range(0, len(team1Points[4])):
			subPts += int(team1Points[4][i])

		thisMatch['team1']['subs'] = {}
		thisMatch['team1']['subs']['points'] = subPts


		thisMatch['team2'] = {}
		thisMatch['team2']['name'] = team2Name
		thisMatch['team2']['starting'] = {}
		thisMatch['team2']['starting']['keeper'] = {}
		thisMatch['team2']['starting']['defenders'] = {}
		thisMatch['team2']['starting']['midfielders'] = {}
		thisMatch['team2']['starting']['strikers'] = {}

		thisMatch['team2']['starting']['keeper']['points'] = int(team2Points[0][0])
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


		subPts = 0
		for i in range(0, len(team2Points[4])):
			subPts += int(team2Points[4][i])

		thisMatch['team2']['subs'] = {}
		thisMatch['team2']['subs']['points'] = subPts

		if matches_processed_this_week == 0:

			latest_json_data.append({})
			latest_json_data[gameweek-1]['gameweek'] = gameweek
			latest_json_data[gameweek-1]['matches'] = []

		latest_json_data[gameweek-1]['matches'].append(thisMatch)

		f = open("final.JSON","w+")
		
		f.write(json.dumps(latest_json_data, indent=2, sort_keys=True))

		f.close()

	matches_processed_this_week += 1

	if(matches_processed_this_week == 5):
		matches_processed_this_week = 0

