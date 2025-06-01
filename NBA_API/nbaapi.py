import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import requests

# function to convert list of dicts to dict of lists
def one_dict(list_dict):
    if not list_dict:
        print("Input list is empty!")
        return {}
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        # Ensure all dicts have the same keys
        if dict_.keys() != keys:
            print("Warning: Mismatched keys found:", dict_.keys())
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# get all NBA teams
nba_teams = teams.get_teams()
if not nba_teams:
    raise ValueError("Could not retrieve NBA teams. Check your internet connection and nba_api installation.")

dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)

# find Warriors team
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
if df_warriors.empty:
    raise ValueError("Could not find Warriors in NBA teams.")

id_warriors = df_warriors['id'].values[0]

# get the Warriors games
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
games = gamefinder.get_data_frames()[0]

# down and load pre saved Warriors data
filename_url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
local_filename = "Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download file from {url}")

download(filename_url, local_filename)

# load the pickled DataFrame
games = pd.read_pickle(local_filename)

# filter games vs. Toronto
games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']

# calculate means
home_mean = games_home['PLUS_MINUS'].mean()
away_mean = games_away['PLUS_MINUS'].mean()

# printing results
print(games.head())
print("Home PLUS_MINUS mean:", home_mean)
print("Away PLUS_MINUS mean:", away_mean)

# plot results
fig, ax = plt.subplots()
games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()