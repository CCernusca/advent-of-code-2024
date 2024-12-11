
full_stones = "4610211 4 0 59 3907 201586 929 33750"

test_stones = "125 17"

def parse_stones(raw_stones):
	return raw_stones.split()

def blink(stones):
	new_stones = []
	for i, stone in enumerate(stones):
		if stone == '0':
			new_stones.append('1')
		elif len(stone) % 2 == 0:
			new_stones.append(str(int(stone[:len(stone) // 2])))
			new_stones.append(str(int(stone[len(stone) // 2:])))
		else:
			new_stones.append(str(int(stone) * 2024))
	return new_stones

stones = parse_stones(full_stones)

for _ in range(25):
	stones = blink(stones)

print(len(stones))
