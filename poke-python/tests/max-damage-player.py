import asyncio
import time

from poke_env.player import Player, RandomPlayer


class MaxDamagePlayer(Player):

    def choose_move(self, battle):

        active_pokemon = battle.active_pokemon

        print("-------------------------------")

        print("Active Pokémon:", active_pokemon.species)

        for x in battle.available_moves:
            print(x)
            print(x.accuracy)
            print(x.base_power)
            print(x.status)
            print(x.type)

        print("Type1: ", active_pokemon.type_1)
        print("Type2: ", active_pokemon.type_2)

        print("Base Stats: ", active_pokemon.base_stats )
        print("STAB Multi: ", active_pokemon.stab_multiplier)

        print("-------------------------------")

        # If statement taking STAB & Accuracy
        type_1 = active_pokemon.type_1
        type_2 = active_pokemon.type_2

        for x in battle.available_moves:
            if x.type == type_1 or x.type == type_2:
                best_move = x
            else:
                pass

        if battle.available_moves:
            # Finds the best move among available ones
            best_move = max(battle.available_moves, key=lambda move: move.base_power)
        
        return self.create_order(best_move)

async def main():
    start = time.time()

    # We create two players.
    random_player = RandomPlayer(
        battle_format="gen1randombattle",
    )
    max_damage_player = MaxDamagePlayer(
        battle_format="gen1randombattle",
    )

    # Now, let's evaluate our player
    await max_damage_player.battle_against(random_player, n_battles=100)

    print(
        "Max damage player won %d / 100 battles [this took %f seconds]"
        % (
            max_damage_player.n_won_battles, time.time() - start
        )
    )


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())