from espn_api.basketball import league
import pandas as pd
# pd.set_option('display.max_colwidth', -1)
import pickle

p = open('league.pkl', 'rb')
league = pickle.load(p)

myTeam = league.teams[2]

# print(myTeam.roster)

roster = pd.DataFrame()

for player in myTeam.roster:
    roster = roster.append([[player.name, player.proTeam, player.position, player.stats]])
    # print(player.name, player.proTeam, player.position)

roster.columns = ['Player', 'Team', 'Position', 'Stats']

print(roster)

# print(roster.groupby('Team')['Player'].count().sort_values(ascending=False))
