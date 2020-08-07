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


with open('final.json') as match_json_file:

	match_json = json.load(match_json_file)

	match_json_file.close()


	totalPointsMatrix = []

	for i in range(0, len(teams)):
		totalPointsMatrix.append([])

	print(totalPointsMatrix)