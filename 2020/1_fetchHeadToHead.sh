for i in {1..38}
do

	#1 Generate the CURL command by concatenating the gameweek number $i into the command
	url="curl 'https://draftfantasyfootball.co.uk/graphql' -H 'Accept: */*' -H 'content-type: application/json' -H 'meteor-login-token: NT9GwfxJGWlo-rfq2oUGRIyZFUZFTrOP1YWezLNzSuu' --data-raw '{\"operationName\":\"getHeadToHeadMatches\",\"variables\":{\"leagueId\":\"HsDdm8wkGv72n8sAC\",\"gameweek\":$i},\"query\":\"fragment MatchTeam on Team {  _id  name  livePoints: liveGameweekPoints(gameweek: \$gameweek)  user {    _id    profile {      firstName      lastName      __typename    }    __typename  }  __typename}query getHeadToHeadMatches(\$leagueId: String!, \$gameweek: Int!) {  headToHeadMatches(leagueId: \$leagueId, gameweek: \$gameweek) {    _id    gameweek    leagueId    team1 {      ...MatchTeam      __typename    }    team2 {      ...MatchTeam      __typename    }    __typename  }  league(_id: \$leagueId) {    _id    gameweekAverage(gameweek: \$gameweek)    __typename  }}\"}'"

	#2 Evavulate the Curl command from the String $url and store the JSON result in the variable $response
	response=$(eval $url)

	#3 Clean the ' from the Taigy names so it can be used with the jq utility
	cleanResponse=${response//\'/}

	#4 Create a string that contains the full jq command, which incorporates the cleaned JSON
	jqCommand="jq '. += ["$cleanResponse"]' headToHead.json"

	#5 Evaluate the jq command and store the result (this will not be pretty print JSON)
	latestJSON=$(eval $jqCommand)

	#6 Get a pretty print of the latest JSON and overwrite the head to head file with the latest
	echo $latestJSON | jq '.' > headToHead.json

	#7 Sleep so the draftfantasy server doesnt gurn
	sleep 1s

done