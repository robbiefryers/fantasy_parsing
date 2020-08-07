import json 

with open('trades_raw.json') as trades_file:

	full_trade_json = json.load(trades_file)

	trades_file.close()

	minified_trade_json = []


	for trade_page in full_trade_json:

		for indiv_trade in trade_page['data']['tradesWithCount']['trades']:

			trade_obj = {}

			trade_obj['respondedAt'] = indiv_trade['respondedAt']
			trade_obj['status'] = indiv_trade['status']
			trade_obj['type'] = indiv_trade['type']
			trade_obj['outTeam'] = indiv_trade['outTeam']['user']['name']

			
			if indiv_trade['inTeam'] is not None:
				trade_obj['inTeam'] = indiv_trade['inTeam']['user']['name']

			else:
				trade_obj['inTeam'] = None

			trade_obj['playersIn'] = []

			for playerIn in indiv_trade['playersIn']:
				player = {}
				player['id'] = playerIn['_id']
				player['name'] = playerIn['web_name']

				trade_obj['playersIn'].append(player)


			trade_obj['playersOut'] = []

			for playerOut in indiv_trade['playersOut']:
				player = {}
				player['id'] = playerOut['_id']
				player['name'] = playerOut['web_name']

				trade_obj['playersOut'].append(player)
		
			minified_trade_json.append(trade_obj)


	trades_file = open("trades.json","w+")
		
	trades_file.write(json.dumps(minified_trade_json, indent=2, sort_keys=True))

	trades_file.close()