import pandas as pd
from nba_api.stats.static import players

# Prereq: 'players_to_be_rated.xlsx' in working directory; contains full names of all POIs

# Read list of POIs
df = pd.read_excel('players_to_be_rated.xlsx')
print(f"{df.shape[0]} players to be rated")
# Retrieve all player info
all_players = players.get_players()
print(f"{len(all_players)} players in total")
# print("player Column Names:")
# for column in all_players[0].keys():
#     print(f"- {column}")
# # Dict with id, full_name, first_name, last_name, is_active
# Convert list of dicts to DataFrame
all_players_df = pd.DataFrame(all_players)

# Note: assuming exact matches to name data
# Match spreadsheet POI names to IDs from the API call
matched_players = df.merge(all_players_df, left_on='player', right_on='full_name')

# Create new dataframe with ids and names
output_df = matched_players[['player', 'id']]

# Step 5: Write the output DataFrame to a new Excel file
output_df.to_excel('players_to_be_rated_w_ids.xlsx', index=False)

