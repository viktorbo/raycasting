from settings import *

map_width = 14
map_text = [
    'WWWWWWWWWWWWWWWW',
    'W..............W',
    'W...WW.........W',
    'W..............W',
    'W..............W',
    'W.........WWW..W',
    'W...........W..W',
    'W.....W.....W..W',
    'W..............W',
    'W..............W',
    'W..............W',
    'WWWWWWWWWWWWWWWW'
]

world_map = set()
for j, row in enumerate(map_text):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE_SIZE, j * TILE_SIZE))
