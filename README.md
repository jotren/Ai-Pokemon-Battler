# Pokemon Showdown Battler #

## Introduction

In order to run this batter, you need to download the pokemon-showdown repository from github:

https://github.com/smogon/pokemon-showdown

Need to find a way to scrape battles and essentialyl collected training data for my algorithmn.

This website looks like it could help:

https://github.com/smogon/pokemon-showdown-client/blob/master/WEB-API.md

https://replay.pokemonshowdown.com/?0.7615615604358281

Here are the steps to generating battles

1. First we scrape this replay website, searching the format for gen1randombattle. 

```
https://replay.pokemonshowdown.com/ 
```

2. We then save these user names and use this URL to search all the games that user has done:

```
https://replay.pokemonshowdown.com/search.json?user=BrockThruWalls&page=1
```
3. We note down the "id" value and then use this to get a json replay of the battle:
``` 
https://replay.pokemonshowdown.com/gen1randombattle-1954508473.json
```
_note_: Could also use this to scrape more users

4. Save the log values of these battles but first need to create a script to pull all the relevant data:


5. This is where we can get the probability of moves:

```
https://play.pkmn.cc/data/random/gen1randombattle.json
```