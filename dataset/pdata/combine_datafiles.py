import pandas as pd
import os

# Directory containing the Excel files
dirs = ['advanced_data', 'defense_data', 'per_game_data', 'usage_data']
file_prefixes = ['advanced', 'defense', 'per_game_regular', 'usage']
kept_col_headers = ["PLAYER", "TEAM", "AGE", "GP", "W", "L", "MIN"]

def create_combined_file(dir: str, file_prefix: str):
    dataframes = []
    # For each file in directory
    for filename in sorted(os.listdir(dir)):
        if filename.startswith(file_prefix) and filename.endswith('.xlsx'):
            # get full file path
            file_path = os.path.join(dir, filename)
            # Read excel file in 
            df = pd.read_excel(file_path)
            # Ensure column headers are uppercase
            df.columns = df.columns.str.upper()
            # Delete first column (index col)
            df = df.iloc[:, 1:]  # select all data except for first column
            # append dataframe to list
            dataframes.append(df)

    # Concatenate all dataframes
    combined_df = pd.concat(dataframes, ignore_index=True)
    # Rename headers
    if file_prefix == "per_game_regular":
        combined_df.columns = [f"{file_prefix}_{col}" if col not in kept_col_headers[:-1] else col for col in combined_df.columns]
    else:
        combined_df.columns = [f"{file_prefix}_{col}" if col not in kept_col_headers else col for col in combined_df.columns]

    # Write dataframe to excel
    output_fn = f"{file_prefix}_all.xlsx"
    combined_df.to_excel(output_fn, index=False)
    print(f"Created {output_fn} from data in directory {dir}")

for i, directory in enumerate(dirs):
    create_combined_file(directory, file_prefixes[i])

