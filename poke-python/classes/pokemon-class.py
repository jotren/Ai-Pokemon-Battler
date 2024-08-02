from poke_env.environment.pokemon import Pokemon

pikachu = Pokemon(species="pikachu")

attack = pikachu.base_stats['atk']
defense = pikachu.base_stats['def']
current_hp_fraction = pikachu.current_hp_fraction
spa = pikachu.base_stats['spa']
spd = pikachu.base_stats['spd']
spe = pikachu.base_stats['spe']

pokemon_type1 = pikachu.type_1
pokemon_type2 = pikachu.type_2