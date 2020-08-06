import json

matchIDs = []

with open('headToHead.json') as json_file:

	data = json.load(json_file)

	for week in data:
		for match in week['data']['headToHeadMatches']:
			matchIDs.append(match['_id'])
			print('"' + match['_id'] + '", ', end = '')
		
print(len(matchIDs))

