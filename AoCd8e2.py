
full_map = """
....................8.D.........Y...........c.....
....f.............D......O...........Y............
.......z..........7.N..........g..................
..........h...........9g.7....................Y...
.............8...............................c....
...9..8...............L........D....O.....l.......
..........f.9.......h.........................l...
...z...B..........................................
.................M.....C.....OR7.Y..g..........l..
........................M.......N.................
...............h..................TD....H.........
......z......M........C8.......N.......m.T........
......O.......................................A...
...........a...........h..........................
................B..................j..............
..............v..f..........g.....................
.......N..........s.M.........n..............Q....
...............s.........j.......................A
......................a......................T...b
........s....v......H..c..............j..i....m...
.......................a........2H.......m..V.....
................n.B..........o.....H......2.......
.....3.......s.B..............x......S..K.........
.3.G..................J................V...l.x..T.
....3.......................E..................V..
3..........................E..........V...i.......
...............v.......n.E...................2.i..
..F.........r.e......n....E...........A..Q.....K..
..z................................A....Q.........
.................................b..Q...d.Sw......
..G...0..e............v.......Z...j.....m...b.....
..y.............0.a.............................K.
.............Gp....Z.................4......S.....
....oJ....G........e.........Z............b.X.....
C........o.r........WL..1.......X........K.....d..
..................Z1.....r...............F........
............L.4................1.6..............tF
...y...............L......1............26.t.......
......e.k......y........I......x......d........t.R
.......0.........k...............d.........tWR..x.
..........q.....r......J..................F..P..w.
..........................5..........XwW..........
...........0....y.............J.............6p....
..q...k.......................I.....4........SR...
.........q..o.......P................W............
.............q.IP..............................p..
.....k...................w.............X.......f..
.............P...............4..................p.
.................I..........5.....................
.C.................................5...6..........
"""

test_map = """
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
"""

def parse_map(map: str):
    bounds = len(map.strip().splitlines()[0]), len(map.strip().splitlines())
    map_ = map.replace('#', '.')
    antennas = {}
    for y, line in enumerate(map_.strip().splitlines()):
        for x, char in enumerate(line):
            if char != '.':
                if char in antennas:
                    antennas[char].append((x, y))
                else:
                    antennas[char] = [(x, y)]
    return antennas, bounds

def get_antinodes_two_antennas(ant1: tuple, ant2: tuple, bounds: tuple):
    antinodes = []
    x1, y1 = ant1
    x2, y2 = ant2
    dx = x2 - x1
    dy = y2 - y1

    i = 0
    anode1 = (x1 - dx * i, y1 - dy * i)
    while 0 <= anode1[0] < bounds[0] and 0 <= anode1[1] < bounds[1]:
        antinodes.append(anode1)
        i += 1
        anode1 = (x1 - dx * i, y1 - dy * i)
    
    i = 0
    anode2 = (x2 + dx * i, y2 + dy * i)
    while 0 <= anode2[0] < bounds[0] and 0 <= anode2[1] < bounds[1]:
        antinodes.append(anode2)
        i += 1
        anode2 = (x2 + dx * i, y2 + dy * i)
    
    return antinodes

def get_antinodes(antennas: list, bounds: tuple):
    antinodes = []
    for i, ant1 in enumerate(antennas):
        for ant2 in antennas[i + 1:]:
            antinodes.extend(get_antinodes_two_antennas(ant1, ant2, bounds))
    return antinodes

def get_all_antinodes(antennas: dict, bounds: tuple):
    antinodes = {}
    for ant in antennas:
        antinodes[ant] = get_antinodes(antennas[ant], bounds)
    return antinodes

def get_unique_antinodes(antinodes: dict):
    unique_antinodes = set()
    for ant in antinodes:
        unique_antinodes.update(antinodes[ant])
    return unique_antinodes

antennas_dict, bounds = parse_map(full_map)
antinodes = get_all_antinodes(antennas_dict, bounds)
unique_antinodes = get_unique_antinodes(antinodes)

for y in range(bounds[1]):
    row = ""
    for x in range(bounds[0]):
        if (x, y) in unique_antinodes:
            row += "#"
        else:
            row += "."
    print(row)
print(unique_antinodes)
print(len(unique_antinodes))