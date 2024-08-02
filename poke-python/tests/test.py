import pandas as pd

moveset_df = pd.read_csv(r'C:\projects\personal projects\pokemon-ai-battler\poke-python\data\gen1Moveset.csv', usecols=['lowerCaseName', 'id'])
moveset_df.set_index('lowerCaseName', inplace=True)

pokemon_df = pd.read_csv(r'C:\projects\personal projects\pokemon-ai-battler\poke-python\data\gen1Pokemon.csv', usecols=['lowerCaseName', 'id'])
pokemon_df.set_index('lowerCaseName', inplace=True)

status_df = pd.read_csv(r'C:\projects\personal projects\pokemon-ai-battler\poke-python\data\status.csv')
status_df.set_index('status', inplace=True)

type_df = pd.read_csv(r'C:\projects\personal projects\pokemon-ai-battler\poke-python\data\type.csv')
type_df.set_index('type', inplace=True)

matching_row_pokemon = pokemon_df.loc['Ivysaur'.lower()]['id']
matching_row_move = moveset_df.loc['body slam'.lower().replace(" ", "")]['id']
matching_row_status = status_df.loc['none'.split(" ")[0]]['id']
matching_row_type = type_df.loc['rock'.lower()]['id']

print(matching_row_status)