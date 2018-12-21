#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import json

with open('final.json') as file:
	data = json.load(file)

	for j in range(0, len(data)):

		totalWeeksKeeperPts = 0 
		totalWeeksDefencePts = 0 
		totalWeeksMidfieldPts = 0 
		totalWeeksStrikerPts = 0 


		for i in range(0, len(data[j]['matches'])):
			
			if len(data[j]['matches'][i]) == 1:
				totalWeeksKeeperPts += int(data[j]['matches'][i]['team1']['starting']['keeper']['points'])
				totalWeeksDefencePts += int(data[j]['matches'][i]['team1']['starting']['defenders']['points'])
				totalWeeksMidfieldPts += int(data[j]['matches'][i]['team1']['starting']['midfielders']['points'])
				totalWeeksStrikerPts += int(data[j]['matches'][i]['team1']['starting']['strikers']['points'])
			
			else:
				totalWeeksKeeperPts += int(data[j]['matches'][i]['team1']['starting']['keeper']['points'])
				totalWeeksDefencePts += int(data[j]['matches'][i]['team1']['starting']['defenders']['points'])
				totalWeeksMidfieldPts += int(data[j]['matches'][i]['team1']['starting']['midfielders']['points'])
				totalWeeksStrikerPts += int(data[j]['matches'][i]['team1']['starting']['strikers']['points'])
				totalWeeksKeeperPts += int(data[j]['matches'][i]['team2']['starting']['keeper']['points'])
				totalWeeksDefencePts += int(data[j]['matches'][i]['team2']['starting']['defenders']['points'])
				totalWeeksMidfieldPts += int(data[j]['matches'][i]['team2']['starting']['midfielders']['points'])
				totalWeeksStrikerPts += int(data[j]['matches'][i]['team2']['starting']['strikers']['points'])

		totalWeek = totalWeeksKeeperPts + totalWeeksDefencePts + totalWeeksMidfieldPts + totalWeeksStrikerPts

		print round(totalWeek/9.0)
		data[j]['averagePts'] = round(totalWeek/9.0)


f= open("finalAv.json","w+")

f.write(json.dumps(data, indent=2, sort_keys=True))

f.close()