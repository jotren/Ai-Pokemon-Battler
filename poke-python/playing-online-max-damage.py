import asyncio
import pandas as pd
from poke_env.player import RandomPlayer, Player
from poke_env import PlayerConfiguration, ShowdownServerConfiguration

# Import the gen1 pokemon data

moveset_df = pd.read_csv(r'C:\projects\personal projects\pokemon-ai-battler\poke-python\data\gen1Moveset.csv', usecols=['lowerCaseName', 'id'])
moveset_df.set_index('lowerCaseName', inplace=True)

pokemon_df = pd.read_csv(r'C:\projects\personal projects\pokemon-ai-battler\poke-python\data\gen1Pokemon.csv', usecols=['lowerCaseName', 'id'])
pokemon_df.set_index('lowerCaseName', inplace=True)

status_df = pd.read_csv(r'C:\projects\personal projects\pokemon-ai-battler\poke-python\data\status.csv')
status_df.set_index('status', inplace=True)

type_df = pd.read_csv(r'C:\projects\personal projects\pokemon-ai-battler\poke-python\data\type.csv')
type_df.set_index('type', inplace=True)

class MaxDamagePlayer(Player):
    def choose_move(self, battle):
        
        #First I want to simple print out all the classes I am interested in.       

        current_turn = battle.turn

        active_pokemon = pokemon_df.loc[str(battle.active_pokemon.species).lower()]['id']
        active = int(battle.active_pokemon.active)
        active_status = status_df.loc[str(battle.active_pokemon.status).lower().split(" ")[0]]['id']
        
        opponent_species = pokemon_df.loc[str(battle.opponent_active_pokemon.species).lower()]['id']
        opponent_active = int(battle.opponent_active_pokemon.active)     
        opponent_status = status_df.loc[str(battle.opponent_active_pokemon.status).lower().split(" ")[0]]['id']   

        #Then we will do the move class
        
        #Then the pokemon class

        attack = battle.active_pokemon.base_stats['atk']
        defense = battle.active_pokemon.base_stats['def']
        current_hp = battle.active_pokemon.current_hp_fraction
        spd = battle.active_pokemon.base_stats['spd']
        special = battle.active_pokemon.base_stats['spe']

        type_1 = type_df.loc[str(battle.active_pokemon.type_1).lower().split(" ")[0]]['id']        
        type_2 = type_df.loc[str(battle.active_pokemon.type_2).lower().split(" ")[0]]['id']

        opponent_type_1 = type_df.loc[str(battle.opponent_active_pokemon.type_1).lower().split(" ")[0]]['id']        
        opponent_type_2 = type_df.loc[str(battle.opponent_active_pokemon.type_2).lower().split(" ")[0]]['id']

        opponent_attack = battle.opponent_active_pokemon.base_stats['atk']
        opponent_defense = battle.opponent_active_pokemon.base_stats['def']
        opponent_current_hp = battle.opponent_active_pokemon.current_hp_fraction
        opponent_spd = battle.opponent_active_pokemon.base_stats['spd']
        opponent_special = battle.opponent_active_pokemon.base_stats['spe']


        print(f"Battle Turn: {current_turn}")   

        print(f"Active Pokemon: {active_pokemon}, Active: {active}, Status: {active_status} ")
        print(f"Active Pokemon -> Attack: {attack}, Defense: {defense}, Current HP: {current_hp}, Speed: {spd}, Special: {special}")
        print(f"Types -> Type 1: {type_1}, Type 2: {type_2}")

        if current_hp == 0:

            print("Pokemon Fainted, Penalise") 

        for x in battle.available_moves:
            move_id = moveset_df.loc[str(x).lower().split(" ")[0]]['id']
            accuracy = x.accuracy
            base_power = x.base_power
            heal = x.heal
            move_status = status_df.loc[str(x.status).lower().split(" ")[0]]['id']
            self_boost = x.self_boost

            print(f"Move ID: {move_id} -> Accuracy: {accuracy}, Base Power: {base_power}, Heal: {heal}, Status: {move_status}, Self Boost: {self_boost}")
        
        print("   ")
        for x in battle.available_switches:
            available_pokemon = pokemon_df.loc[str(x.species).lower()]['id']
            pokemon_active = int(x.active)
            pokemon_status = status_df.loc[str(x.status).lower().split(" ")[0]]['id']

            print(f"Available Pokemon: {available_pokemon}, Active: {pokemon_active}, Status: {pokemon_status}")

        print("   ")

        print("--------------------------------")

        print(f"Opponent Pokemon: {opponent_species}, Active: {opponent_active}, Status: {opponent_status}" )
        print(f"Opponent Pokemon -> Attack: {opponent_attack}, Defense: {opponent_defense}, Current HP: {opponent_current_hp}, Speed: {opponent_spd}, Special: {opponent_special}")
        print(f"Types -> Type 1: {opponent_type_1}, Type 2: {opponent_type_2}")

        if opponent_current_hp == 0:
            print("Opponent Pokemon Fainted, Reward!")

        for x in battle.opponent_team:
            opponent_pokemon = pokemon_df.loc[str(x).split(" ")[1].lower()]['id']
            print(f"Opponent Pokemon: {opponent_pokemon}, Active: 0")

        # lost = int(battle.lost)
        # won = int(battle.won) 
        
        # print(f"Battle won: {won}")
        
        print(" ")
        print("____________________________________")
        print(" ")
    
        # If the player can attack, it will
        if battle.available_moves:
            # Finds the best move among available ones
            best_move = max(battle.available_moves, key=lambda move: move.base_power)
            return self.create_order(best_move)

        # If no attack is available, a random switch will be made
        else:
            return self.choose_random_move(battle)

async def main():
    # We create a random player
    player = MaxDamagePlayer(
        player_configuration=PlayerConfiguration("HAL-pokemon", "pokemon-AI"),
        server_configuration=ShowdownServerConfiguration,
        battle_format="gen1randombattle"  # Set the desired Gen 1 format here
    )

    # Playing 5 games on the ladder
    await player.ladder(1)

    # Print the rating of the player and its opponent after each battle
    for battle in player.battles.values():
        print(battle.rating, battle.opponent_rating)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
