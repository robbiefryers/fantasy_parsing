#There are 25 pages of trades for the 2020 season

for i in {1..25}

do
	url="curl 'https://draftfantasyfootball.co.uk/graphql' -H 'Accept: */*'  -H 'content-type: application/json' -H 'meteor-login-token: NT9GwfxJGWlo-rfq2oUGRIyZFUZFTrOP1YWezLNzSuu'  --data-raw '{\"operationName\":\"TradesForLeague\",\"variables\":{\"leagueId\":\"HsDdm8wkGv72n8sAC\",\"page\":$i},\"query\":\"query TradesForLeague(\$leagueId: String!, \$count: Int, \$page: Int, \$tradeType: TradeType) {  tradesWithCount(leagueId: \$leagueId, count: \$count, page: \$page, tradeType: \$tradeType) {    hasMore    trades {      _id      type      createdAt      respondedAt      status      outTeam {        ...TeamDetails        __typename      }      inTeam {        ...TeamDetails        __typename      }      playersOut {        ...PlayerDetails        __typename      }      playersIn {        ...PlayerDetails        __typename      }      __typename    }    __typename  }}fragment TeamDetails on Team {  _id  name  user {    _id    name    __typename  }  __typename}fragment PlayerDetails on Player {  _id  web_name  __typename}\"}'"
	
	response=$(eval $url)

	cleanResponse=${response//\'/}

	jqCommand="jq '. += ["$cleanResponse"]' trades_raw.json"

	latestJSON=$(eval $jqCommand)

	echo $latestJSON | jq '.' > trades_raw.json

	sleep 1s

done