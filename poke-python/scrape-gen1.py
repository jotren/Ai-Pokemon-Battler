import requests
import re
import pandas as pd
import copy
from status import status_to_id
import json

with open('pokemon_data.json', 'r') as file:
    pokemon_data = json.load(file)

def get_pokemon_id(pokemon_name):
    return pokemon_data.get(pokemon_name.lower(), {}).get('id', None)

url = 'https://replay.pokemonshowdown.com/gen1randombattle-1812374240.log'

response = requests.get(url)

if response.status_code != 200:
    print(f"Failed to fetch content from URL. Status code: {response.status_code}")
    exit()

turn_blocks = response.text.strip().split('|turn')

# Initialize a dictionary to store pokemon objects with their names as keys
p1a_pokemon_dict = {}
p2a_pokemon_dict = {}

# Define regex patterns for p1a
pattern_p1a = r"p1a:\s*([^|]+)"
pattern_p1a_status = r"\|-status\|p1a: [^\|]+\|(\w+)"
pattern_p1a_faint = r"\|faint\|p1a:"
pattern_damage_p1a = r'\|-damage\|p1a:[^|]+\|(\d+/\d+)'
pattern_p1a_switch = r'|switch|p1a: [^|]+\|'

# Define regex patterns
pattern_p2a = r"p2a:\s*([^|]+)"
pattern_p2a_status = r"\|-status\|p2a: [^\|]+\|(\w+)"
pattern_p2a_faint = r"\|faint\|p2a:"
pattern_damage_p2a = r'\|-damage\|p2a:[^|]+\|(\d+/\d+)'
pattern_p2a_switch = r'|switch|p2a: [^|]+\|'

p1a_previous_pokemon = {}
p2a_previous_pokemon = {}

p1a_dict_list_to_append = []
p2a_dict_list_to_append = []

# Parsing each turn
for turn_block in turn_blocks[1:]:  # Skipping the first block since it doesn't represent a turn

    # Searching for matches in the block
    pokemon_matches_p1a = re.search(pattern_p1a, turn_block)
    status_matches_p1a = re.search(pattern_p1a_status, turn_block)
    faint_matches_p1a = re.search(pattern_p1a_faint, turn_block)
    damage_matches_p1a = re.search(pattern_damage_p1a, turn_block)
    
    if pokemon_matches_p1a:
        pokemon_name = pokemon_matches_p1a.group(1).lower().split('\n')[0]
        pokemon_id = get_pokemon_id(pokemon_name)
        
        # If pokemon_id not in dictionary, create a new entry
        if pokemon_id and pokemon_id not in p1a_pokemon_dict:
            p1a_pokemon_dict[pokemon_id] = {
                "id": pokemon_id,
                "hp": 1,
                "status": 0,
                "fnt": 0,
                "active": 1
            }

        # Reference to the current pokemon object
        p1a_current_pokemon = p1a_pokemon_dict[pokemon_id]

        if p1a_previous_pokemon != p1a_current_pokemon:
            p1a_previous_pokemon['active'] = 0
            p1a_current_pokemon['active'] = 1

        # Update pokemon details
        if status_matches_p1a:
            status_str = status_matches_p1a.group(1)
            p1a_current_pokemon['status'] = status_to_id.get(status_str, 0)  # Default to 0 (none) if not found

        
        if damage_matches_p1a:
            p1a_current_pokemon['hp'] = round(eval(damage_matches_p1a.group(1)),2)

        if faint_matches_p1a:
            p1a_current_pokemon['fnt'] = 1
            p1a_current_pokemon['hp'] = 0
        
        p1a_previous_pokemon = p1a_pokemon_dict[pokemon_id]

    # Searching for matches in the block
    pokemon_matches_p2a = re.search(pattern_p2a, turn_block)
    status_matches_p2a = re.search(pattern_p2a_status, turn_block)
    faint_matches_p2a = re.search(pattern_p2a_faint, turn_block)
    damage_matches_p2a = re.search(pattern_damage_p2a, turn_block)
    
    if pokemon_matches_p2a:
        pokemon_name = pokemon_matches_p2a.group(1).lower().split('\n')[0]
        pokemon_id = get_pokemon_id(pokemon_name)
        
        # If pokemon_id not in dictionary, create a new entry
        if pokemon_id and pokemon_id not in p2a_pokemon_dict:
            p2a_pokemon_dict[pokemon_id] = {
                "id": pokemon_id,
                "hp": 1,
                "status": 0,
                "fnt": 0,
                "active": 1
            }

        # Reference to the current pokemon object
        p2a_current_pokemon = p2a_pokemon_dict[pokemon_id]

        if p2a_previous_pokemon != p2a_current_pokemon:
            p2a_previous_pokemon['active'] = 0
            p2a_current_pokemon['active'] = 1

        # Update pokemon details
        if status_matches_p2a:
            status_str = status_matches_p2a.group(1)
            p2a_current_pokemon['status'] = status_to_id.get(status_str, 0)  # Default to 0 (none) if not found
        
        if damage_matches_p2a:
            p2a_current_pokemon['hp'] = round(eval(damage_matches_p2a.group(1)))

        if faint_matches_p2a:
            p2a_current_pokemon['fnt'] = 1
            p2a_current_pokemon['hp'] = 0
        
        p2a_current_pokemon = p2a_pokemon_dict[pokemon_id]

    
    blank_dict = {
                "id": 0,
                "hp": 1,
                "status": 0,
                "fnt": 0,
                "active": 0
            }


    # The hp is correct at this point
    p1a_list_for_turn = list(p1a_pokemon_dict.values())
    p2a_list_for_turn = list(p2a_pokemon_dict.values())

    # The hp is working here
    for _ in range(6 - len(p1a_list_for_turn)):
        p1a_list_for_turn.append(copy.deepcopy(blank_dict))

    # The hp is working here
    for _ in range(6 - len(p2a_list_for_turn)):
        p2a_list_for_turn.append(copy.deepcopy(blank_dict))

    # THe code doesn't work here
    p1a_dict_list_to_append.append(copy.deepcopy(p1a_list_for_turn))
    p2a_dict_list_to_append.append(copy.deepcopy(p2a_list_for_turn))

df_p1a = pd.DataFrame()
df_p2a = pd.DataFrame()

# Flattening p1a_dict_list_to_append
for idx, nested_list in enumerate(p1a_dict_list_to_append):
    flattened = {}
    for j, d in enumerate(nested_list):
        for key, value in d.items():
            flattened[f'p1a_poke{j+1}_{key}'] = value
    df_p1a = pd.concat([df_p1a, pd.DataFrame([flattened])], ignore_index=True)

# Flattening p2a_dict_list_to_append
for idx, nested_list in enumerate(p2a_dict_list_to_append):
    flattened = {}
    for j, d in enumerate(nested_list):
        for key, value in d.items():
            flattened[f'p2a_poke{j+1}_{key}'] = value
    df_p2a = pd.concat([df_p2a, pd.DataFrame([flattened])], ignore_index=True)

# Joining the dataframes side by side
result_df = pd.concat([df_p1a, df_p2a], axis=1)

print(result_df)


# result_df.to_csv(r"C:\projects\personal projects\pokemon-ai-battler\poke-python\data\log_scrape_test.csv", index=False)