import asyncio
from poke_env.player import RandomPlayer, Player
from poke_env import PlayerConfiguration, ShowdownServerConfiguration   

# Define a RandomPlayer subclass
class MyRandomPlayer(RandomPlayer):
    pass

async def main():
    # We create a random player
    player = MyRandomPlayer(
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
