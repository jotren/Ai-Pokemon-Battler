from poke_env.environment.battle import Battle

# Dummy values for battle_tag, username, and logger (you can replace them with actual values)
dummy_battle_tag = "dummy_battle_tag"
dummy_username = "dummy_username"
dummy_logger = None  # You can provide a logger if needed

# Initialize a Battle object with the specified format
dummy_battle = Battle(
    battle_format="gen1randombattle",
    battle_tag=dummy_battle_tag,
    username=dummy_username,
    logger=dummy_logger,
)

# Get the attributes of the Battle object
battle_attributes = dir(dummy_battle)

# Filter and select relevant attributes
relevant_attributes = [attr for attr in battle_attributes if not callable(getattr(dummy_battle, attr))]

# Print the relevant attributes
for attr in relevant_attributes:
    print(attr)
