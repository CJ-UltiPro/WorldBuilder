all_list = ['landscapes', 'seascapes', coastal]

landscapes = ['Island',
'Mountain',
'Plains',
'Unusual',
'Swamp',
'Forested',
'Arid',
'Arctic',
'Road',
'Hills',
'River']

seascapes = ['Oceanic',
'Landlike',
'Arid',
'Unusual']

coastal = ['Muddy',
'Beach',
'Cliffs',
'Flora',
'Artificial']

coastal_muddy = ['Swamp',
'Estuary',
'Saltflats',
'Mudflats',
'Quicksand']

coastal_beach = ['Pebble Beach',
'Pure White Sand',
'Volcanic Black Sand',
'Gravel',
'Sheltered Coves']

coastal_cliff = ['Boulderfield',
'Clifftops',
'Screed Slopes',
'Headlands']

coastal_flora = ['Mangrove',
'Grassy Dunes',
'Verdant',
'Broads/Bush']

coastal_artificial = ['Protective Wall',
'Hydroelectic',
'Harbours',
'Settlement']

seascapes_oceanic = ['Deep Dark',
'Stormy',
'Acidic',
'Doldrums']

seascapes_unusual = ['Lava',
'Magic',
'Sporesea',
'Sludge',
'Acid']

seascapes_arid = ['Dunesea',
'Wasteland']

seascapes_landlike = ['Archipelago',
'Barrier Reef',
'Islets',
'Major Isle',
'Atoll',
'River Network',
'Delta',
'Icefloes']

landscapes_island = ['Archipeligo',
'Islets',
'Major Isle',
'Atoll',
'Barrier Reef',
'Floating island']

landscapes_mountain = ['Moraine',
'Cliffs',
'Crags',
'Caves',
'Highlands']

landscapes_plain = ['Barren',
'Meadow',
'Wildflower',
'Tallgrass Prairie']

landscapes_unusual = ['Spacestation',
'Voidspace',
'Astral Plane',
'Afterlife',
'Simulation',
'Underworld',
'Skylands',
'Underwater']

landscapes_swamp = ['Fen',
'Moorland',
'Bog',
'Mangrove',
'Wetlands']

landscapes_forested = ['Jungle',
'Woodland',
'Copse',
'Mangrove']

landscapes_arid = ['Desert',
'Dustbowl',
'Scrubland',
'Outback',
'Tundra']

landscapes_arctic = ['Tundra',
'Taiga',
'Iceshelf',
'Permafrost',
'Glacier',
'Snowfield',
'Frozen Lake']

landscapes_hill = ['Hillfort',
'Henge',
'Copse',
'Tor']

landscapes_road = ['Crossroads',
'Bridge',
'Waystone',
'Traderoute',
'Ruin',
'Border Crossing']

landscapes_river = ['Forked River',
'Canal Port',
'Bay',
'Waterfall',
'Floodplain',
'Major Crossing',
'Riverhead']

features = ['Monument',
'Temple',
'Portal',
'Spacetime Anomaly',
'Spire',
'Runic Stones',
'Ancient Square',
'Hidden cave',
'Caverns',
'Spacejunk',
'Monsoon',
'Flashfloods',
'Tropical Climate',
'Temperate Climate',
'Continental Climate',
'Predators',
'Poisonous Plants',
'Flotsam and Jetsam',
'Dragons',
'Caldera']

settlements = ['City',
'Village',
'Market Town',
'Coastal Fort',
'Castle',
'Dungeon',
'Ruin']

settlements_city = ['Huge Metropolis',
'Seat of Power',
'Military Citystate',
'Post Apocalyptic',
'Undercity Crime',
'Blessed Whitestone',
'Fortified Control',
'Merged Towns']

settlements_village = ['Tribal Huts',
'Ancient Stone',
'Tourist Spot',
'Hidden',
'Sleepy Hamlet',
'Up and Coming',
'Abandoned']

settlements_markettown = ['Bustling Community',
'River/Road Meeting',
'Carnival or Circus',
'First/Last Stop',
'Trade Specialist',
'Guild Focus',
'Docklands',
'Farming Community']

settlements_coastal_fort = ['Disused',
'Active',
'Magical',
'Kingdoms Retreat',
'Ruins',
'Dark Presence']

settlements_castle = ['Sprawling Dependants',
'Private Owner',
"King's Throne",
'Last Bastion',
'Haunted',
'Steampunk Lord',
'Apoc Decay Facility']

settlements_dungeon = ['Sprawling Chaotic',
'Active Jail',
'Dank Caves',
'Hell Dimension',
'Sunken City',
'Proving Grounds',
'Fallen Robot Titan',
'Shipcrash']

settlements_ruins = ['Castle',
'Portal',
'Temple',
'Shipcrash',
'Burnt Remains',
'Organic Husk',
'Shattered Rock',
'Volcanic Floe']

traits = {'hot':['Caldera', 'Volcanic Black Sand','Lava', 'Dunesea', 'Volcanic Floe', 'Burnt Remains'],
          'cold':['Icefloes'],
          'wet':['Flotsam and Jetsam', 'Flashfloods', 'Monsoon', 'Docklands', 'Swamp', 'Mudflats', 'Quicksand', 'Stormy', 'Sludge', 'River Network', 'Delta', 'Underwater', 'Fen', 'Moorland', 'Bog', 'Mangrove', 'Wetlands'],
          'dry':['Saltflats', 'Dunesea', 'Wasteland', 'Arid', 'Barren']
          }

rules = {'conflict':[('hot', 'cold'),('wet', 'dry')]}
