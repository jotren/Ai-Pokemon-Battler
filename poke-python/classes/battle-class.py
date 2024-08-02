from poke_env.environment.battle import Battle

battle_object = Battle(gen=1, logger=1, username=1, battle_tag=1)

active_pokemon = battle_object.active_pokemon
available_moves = battle_object.available_moves
available_switches = battle_object.available_switches
lost = battle_object.lost
won = battle_object.won

#Need to figure out how to loop through own team. Returns Pokemon Object
team = battle_object.team
turn = battle_object.turn

opponent_active_pokemon = battle_object.opponent_active_pokemon

# Need to figure out how to loop through this team. Returns Pokemon Object
opponent_team = battle_object.opponent_team