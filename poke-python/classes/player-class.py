from poke_env.player.player import Player

# Get the attributes of the Player class
player_attributes = dir(Player)

# Filter and select relevant attributes
relevant_attributes = [attr for attr in player_attributes if not callable(getattr(Player, attr))]

# Print the relevant attributes
for attr in relevant_attributes:
    print(attr)

print('----------------')