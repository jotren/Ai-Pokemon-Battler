csv_data = """ id,Name,lowerCaseName,Types,Type1,Type2,atk,def,spe,spc
1,Bulbasaur,bulbasaur,2,grass,poison
2,Ivysaur,ivysaur,2,grass,poison
3,Venusaur,venusaur,2,grass,poison
4,Charmander,charmander,1,fire,None
5,Charmeleon,charmeleon,1,fire,None
6,Charizard,charizard,2,fire,flying
7,Squirtle,squirtle,1,water,None
8,Wartortle,wartortle,1,water,None
9,Blastoise,blastoise,1,water,None
10,Caterpie,caterpie,1,bug,None
11,Metapod,metapod,1,bug,None
12,Butterfree,butterfree,2,bug,flying
13,Weedle,weedle,2,bug,poison
14,Kakuna,kakuna,2,bug,poison
15,Beedrill,beedrill,2,bug,poison
16,Pidgey,pidgey,2,normal,flying
17,Pidgeotto,pidgeotto,2,normal,flying
18,Pidgeot,pidgeot,2,normal,flying
19,Rattata,rattata,1,normal,None
20,Raticate,raticate,1,normal,None
21,Spearow,spearow,2,normal,flying
22,Fearow,fearow,2,normal,flying
23,Ekans,ekans,1,poison,None
24,Arbok,arbok,1,poison,None
25,Pikachu,pikachu,1,electric,None
26,Raichu,raichu,1,electric,None
27,Sandshrew,sandshrew,1,ground,None
28,Sandslash,sandslash,1,ground,None
29,Nidoran,nidoran,1,poison,None
30,Nidorina,nidorina,1,poison,None
31,Nidoqueen,nidoqueen,2,poison,ground
32,Nidoran,nidoran,1,poison,None
33,Nidorino,nidorino,1,poison,None
34,Nidoking,nidoking,2,poison,ground
35,Clefairy,clefairy,1,normal,None
36,Clefable,clefable,1,normal,None
37,Vulpix,vulpix,1,fire,None
38,Ninetales,ninetales,1,fire,None
39,Jigglypuff,jigglypuff,1,normal,None
40,Wigglytuff,wigglytuff,1,normal,None
41,Zubat,zubat,2,poison,flying
42,Golbat,golbat,2,poison,flying
43,Oddish,oddish,2,grass,poison
44,Gloom,gloom,2,grass,poison
45,Vileplume,vileplume,2,grass,poison
46,Paras,paras,2,bug,grass
47,Parasect,parasect,2,bug,grass
48,Venonat,venonat,2,bug,poison
49,Venomoth,venomoth,2,bug,poison
50,Diglett,diglett,1,ground,None
51,Dugtrio,dugtrio,1,ground,None
52,Meowth,meowth,1,normal,None
53,Persian,persian,1,normal,None
54,Psyduck,psyduck,1,water,None
55,Golduck,golduck,1,water,None
56,Mankey,mankey,1,fighting,None
57,Primeape,primeape,1,fighting,None
58,Growlithe,growlithe,1,fire,None
59,Arcanine,arcanine,1,fire,None
60,Poliwag,poliwag,1,water,None
61,Poliwhirl,poliwhirl,1,water,None
62,Poliwrath,poliwrath,2,water,fighting
63,Abra,abra,1,psychic,None
64,Kadabra,kadabra,1,psychic,None
65,Alakazam,alakazam,1,psychic,None
66,Machop,machop,1,fighting,None
67,Machoke,machoke,1,fighting,None
68,Machamp,machamp,1,fighting,None
69,Bellsprout,bellsprout,2,grass,poison
70,Weepinbell,weepinbell,2,grass,poison
71,Victreebel,victreebel,2,grass,poison
72,Tentacool,tentacool,2,water,poison
73,Tentacruel,tentacruel,2,water,poison
74,Geodude,geodude,2,rock,ground
75,Graveler,graveler,2,rock,ground
76,Golem,golem,2,rock,ground
77,Ponyta,ponyta,1,fire,None
78,Rapidash,rapidash,1,fire,None
79,Slowpoke,slowpoke,2,water,psychic
80,Slowbro,slowbro,2,water,psychic
81,Magnemite,magnemite,1,electric,None
82,Magneton,magneton,1,electric,None
83,Farfetchd,farfetchd,2,normal,flying
84,Doduo,doduo,2,normal,flying
85,Dodrio,dodrio,2,normal,flying
86,Seel,seel,1,water,None
87,Dewgong,dewgong,2,water,ice
88,Grimer,grimer,1,poison,None
89,Muk,muk,1,poison,None
90,Shellder,shellder,1,water,None
91,Cloyster,cloyster,2,water,ice
92,Gastly,gastly,2,ghost,poison
93,Haunter,haunter,2,ghost,poison
94,Gengar,gengar,2,ghost,poison
95,Onix,onix,2,rock,ground
96,Drowzee,drowzee,1,psychic,None
97,Hypno,hypno,1,psychic,None
98,Krabby,krabby,1,water,None
99,Kingler,kingler,1,water,None
100,Voltorb,voltorb,1,electric,None
101,Electrode,electrode,1,electric,None
102,Exeggcute,exeggcute,2,grass,psychic
103,Exeggutor,exeggutor,2,grass,psychic
104,Cubone,cubone,1,ground,None
105,Marowak,marowak,1,ground,None
106,Hitmonlee,hitmonlee,1,fighting,None
107,Hitmonchan,hitmonchan,1,fighting,None
108,Lickitung,lickitung,1,normal,None
109,Koffing,koffing,1,poison,None
110,Weezing,weezing,1,poison,None
111,Rhyhorn,rhyhorn,2,ground,rock
112,Rhydon,rhydon,2,ground,rock
113,Chansey,chansey,1,normal,None
114,Tangela,tangela,1,grass,None
115,Kangaskhan,kangaskhan,1,normal,None
116,Horsea,horsea,1,water,None
117,Seadra,seadra,1,water,None
118,Goldeen,goldeen,1,water,None
119,Seaking,seaking,1,water,None
120,Staryu,staryu,1,water,None
121,Starmie,starmie,2,water,psychic
122,Mr.Mime,mr.mime,1,psychic,None
123,Scyther,scyther,2,bug,flying
124,Jynx,jynx,2,ice,psychic
125,Electabuzz,electabuzz,1,electric,None
126,Magmar,magmar,1,fire,None
127,Pinsir,pinsir,1,bug,None
128,Tauros,tauros,1,normal,None
129,Magikarp,magikarp,1,water,None
130,Gyarados,gyarados,2,water,flying
131,Lapras,lapras,2,water,ice
132,Ditto,ditto,1,normal,None
133,Eevee,eevee,1,normal,None
134,Vaporeon,vaporeon,1,water,None
135,Jolteon,jolteon,1,electric,None
136,Flareon,flareon,1,fire,None
137,Porygon,porygon,1,normal,None
138,Omanyte,omanyte,2,rock,water
139,Omastar,omastar,2,rock,water
140,Kabuto,kabuto,2,rock,water
141,Kabutops,kabutops,2,rock,water
142,Aerodactyl,aerodactyl,2,rock,flying
143,Snorlax,snorlax,1,normal,None
144,Articuno,articuno,2,ice,flying
145,Zapdos,zapdos,2,electric,flying
146,Moltres,moltres,2,fire,flying
147,Dratini,dratini,1,dragon,None
148,Dragonair,dragonair,1,dragon,None
149,Dragonite,dragonite,2,dragon,flying
150,Mewtwo,mewtwo,1,psychic,None
151,Mew,mew,1,psychic,None
"""

type_mapping = {
    'none': 0,
    'bug': 1,
    'dragon': 2,
    'electric': 3,
    'fighting': 4,
    'fire': 5,
    'flying': 6,
    'ghost': 7,
    'grass': 8,
    'ground': 9,
    'ice': 10,
    'normal': 11,
    'poison': 12,
    'psychic': 13,
    'rock': 14,
    'water': 15
}

import json

lines = csv_data.strip().split("\n")[1:]  # [1:] to skip the header
pokemon_data = {}

for line in lines:
    parts = line.split(",")
    data = {
        "id": int(parts[0]),
        "Name": parts[1],
        "Types": int(parts[3]),
        "Type1": type_mapping[parts[4].lower()],  # Correct the index to 4
        "Type2": type_mapping[parts[5].lower()] if parts[5].lower() != "none" else type_mapping['none'],
        # ... add other attributes here
    }
    pokemon_data[parts[2].lower()] = data


# Exporting the pokemon_data dictionary to a JSON file
with open('pokemon_data.json', 'w') as file:
    json.dump(pokemon_data, file, indent=4)