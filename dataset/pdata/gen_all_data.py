import pandas as pd

# Load data from each excel file
advanced = pd.read_excel('advanced_all.xlsx')
defense = pd.read_excel('defense_all.xlsx')
per_game = pd.read_excel('per_game_regular_all.xlsx')
usage = pd.read_excel('usage_all.xlsx')

# Remove unwanted columns 
cols_to_ignore = ["TEAM", "AGE", "GP", "W", "L", "MIN"]
advanced = advanced.drop(columns=[col for col in cols_to_ignore if col in advanced.columns])
defense = defense.drop(columns=[col for col in cols_to_ignore if col in defense.columns])
per_game = per_game.drop(columns=[col for col in cols_to_ignore if col in per_game.columns])
usage = usage.drop(columns=[col for col in cols_to_ignore if col in usage.columns])

# merge dataframes on player column
data_frames = [advanced, defense, per_game, usage]
combined_df = data_frames[0]
for df in data_frames[1:]:
    # Inner join to remove players which lack sections of data
    combined_df = combined_df.merge(df, on='PLAYER', how='inner')

# Extract year from the player column and create year column
combined_df['YEAR'] = combined_df['PLAYER'].str.extract('(\d{4})')
# Insert year after player column
player_index = combined_df.columns.get_loc('PLAYER')
combined_df = combined_df.reindex(columns=combined_df.columns.tolist()[:player_index + 1] + ['YEAR'] + combined_df.columns.tolist()[player_index + 1:-1])

# Save the combined data to a new excel file
combined_df.to_excel('all_data.xlsx', index=False)

print("Saved data to all_data.xlsx")
