import json 

season_data = []

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

def sumTeamPoints(starting):
	pts = 0
	pts += starting['keeper']['points']
	pts += starting['defenders']['points']
	pts += starting['midfielders']['points']
	pts += starting['strikers']['points']
	return pts
	

def graphOne():

	print('Generating graph one...')

	gameweekPointsMatrix = [];

	# Init points matrix 
	for i in range(0,len(teams)):
		gameweekPointsMatrix.append([])


	for gameweek in season_data:

		for match in gameweek['matches']:

			team_one_pts = sumTeamPoints(match['team1']['starting'])
			team_two_pts = sumTeamPoints(match['team2']['starting'])
			print(team_one_pts)




with open('final.json') as match_json_file:

	season_data = json.load(match_json_file)

	graphOne()

	match_json_file.close()
