i=1

for value in {1..17}
do
	

	url="'https://draftfantasyfootball.co.uk/graphql' -H 'Host: draftfantasyfootball.co.uk' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:58.0) Gecko/20100101 Firefox/58.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://draftfantasyfootball.co.uk/league/started/k3viHLvuNpaYG6QFJ/team/RiriSDasHQJSKCJii/gameweek/"
	url+=$value
	url+="' -H 'content-type: application/json' -H 'meteor-login-token: gWSTITVwsA3FcO5IlV7It3L3X6T66udMOW_blZGvQHR' -H 'origin: https://draftfantasyfootball.co.uk' -H 'Connection: keep-alive' --data '{\"operationName\":\"getHeadToHeadMatches\",\"variables\":{\"leagueId\":\"k3viHLvuNpaYG6QFJ\",\"gameweek\":"$value"},\"query\":\"query getHeadToHeadMatches(\$leagueId: String!, \$gameweek: Int!) {\n  headToHeadMatches(leagueId: \$leagueId, gameweek: \$gameweek) {\n    _id\n    gameweek\n    leagueId\n    team1 {\n      _id\n      name\n      liveGameweekPoints(gameweek: \$gameweek)\n      user {\n        profile {\n          firstName\n          lastName\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    team2 {\n      _id\n      name\n      liveGameweekPoints(gameweek: \$gameweek)\n      user {\n        profile {\n          firstName\n          lastName\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\"}'"


	echo 'curl' $url '>> allResults.json' >> fetchData.sh
	echo 'echo "---" >> allResults.json' >> fetchData.sh
	echo 'sleep 1s' >> fetchData.sh

	echo $'\n' >> fetchData.sh

done

