import asyncio
from tabulate import tabulate
import time
from poke_env.player import RandomPlayer, cross_evaluate

async def main():
    # We create three random players
    players = [RandomPlayer(max_concurrent_battles=2, battle_format='gen1randombattle') for _ in range(3)]

    # Now, we can cross evaluate them: every player will play 20 games against every
    # other player.
    cross_evaluation = await cross_evaluate(players, n_challenges=10)

    # Defines a header for displaying results
    table = [["-"] + [p.username for p in players]]

    # Adds one line per player with corresponding results
    for p_1, results in cross_evaluation.items():
        table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in results])

    # Displays results in a nicely formatted table.
    print(tabulate(table))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())