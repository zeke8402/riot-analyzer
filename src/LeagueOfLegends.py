import os
import glob
import json
from pathlib import Path

class LeagueOfLegends():
    def total_spent_on_league(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = Path(dir_path)
        path = path.parent
        path = str(path) + '/data/leagueoflegends/rp_purchase_history.json'
        with open(path, encoding='utf-8', mode='r') as f:
            json_data = json.load(f)

        amount = 0

        for i in json_data:
            amount = amount + i['amount']

        print('You spent ' + str(round(amount, 2)))



