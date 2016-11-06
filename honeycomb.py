#!/usr/bin/python
#
# This is a constant time solution to the honeycomb cell distance puzzle at https://affirm.com/jobs
# by Pius Fischer -- March 1, 2013
#
import math
import sys

def get_xy_for_cell(cell):
	assert isinstance(cell, int) and cell > 0

	# Determine which ring the cell is located in.
	# Ring 0 consists only of cell 1.
	# Ring 1 consists of the 6 cells 2 through 7.
	# Each subsequent ring contains 6 more cells than the previous ring.
	# So the n'th ring (for n > 0) has 6*n cells and the first n rings have a total
	# of 1 + 6 + 12 + ... + 6 * n cells.
	# This is equivalent to 1 + 6 * (1 + 2 + ... + n) = 1 + 6 * n * (n + 1) / 2
	# which is 1 + 3 * n * (n + 1).
	# So to find the ring a given cell is located in, we want to solve the following:
	# cell = 3 * ring * (ring + 1) + 1
	# Let's say c = (cell - 1) / 3
	# Then we have c = ring^2 + ring
	# Using the quadratic formula, we get ring = (-1 + sqrt(1 + 4 * c)) / 2

	ring = int(math.ceil((math.sqrt(4 * (cell - 1.0) / 3 + 1) - 1) / 2))

	# Determine the position (counterclockwise from 0 to 6*ring-1) within the ring.

	position = 3 * ring * (ring + 1) + 1 - cell

	# Now determine x and y.
	#                            x
	#       -5  -4  -3  -2  -1   0   1   2   3   4
	#   -3                  48  28  29  30  31  54
	#   -2              47  27  13  14  15  32  55
	#   -1          46  26  12   4   5  16  33  56
	# y  0      45  25  11   3   1   6  17  34  57
	#    1  70  44  24  10   2   7  18  35  58
	#    2  69  43  23   9   8  19  36  59
	#    3  68  42  22  21  20  37  60
	#    4  67  41  40  39  38  61

	# Start with position 0: x = 0, y = ring
	# For each position between 1 and ring: x += 1, y -= 1
	# For each position between ring+1 and 2*ring: y -= 1
	# For each position between 2*ring+1 and 3*ring: x -= 1
	# For each position between 3*ring+1 and 4*ring: x -= 1, y += 1
	# For each position between 4*ring+1 and 5*ring: y += 1
	# For each position between 5*ring+1 and 6*ring-1: x += 1

	x_mult = (1, 0, -1, -1, 0, 1)
	y_mult = (-1, -1, 0, 1, 1, 0)
	i = 0
	x = 0
	y = ring

	while i < 6:
		delta = position - i * ring
		if delta <= ring:
			x += delta * x_mult[i]
			y += delta * y_mult[i]
			break

		x += ring * x_mult[i]
		y += ring * y_mult[i]
		i += 1
	assert i < 6

	return x, y

def get_distance(x1, y1, x2, y2):
	assert isinstance(x1, int)
	assert isinstance(y1, int)
	assert isinstance(x2, int)
	assert isinstance(y2, int)

	delta_x = x1 - x2
	delta_y = y1 - y2

	abs_delta_x = delta_x if delta_x >= 0 else -delta_x
	abs_delta_y = delta_y if delta_y >= 0 else -delta_y

	if (delta_x < 0 and delta_y > 0) or (delta_x > 0 and delta_y < 0):
		return abs_delta_y if abs_delta_x < abs_delta_y else abs_delta_x

	return abs_delta_x + abs_delta_y

if __name__ == '__main__':
	cell1 = int(sys.argv[1])
	cell2 = int(sys.argv[2])

	x1, y1 = get_xy_for_cell(cell1)
	x2, y2 = get_xy_for_cell(cell2)

	distance = get_distance(x1, y1, x2, y2)

	print "The distance between cells %u (%d, %d) and %u (%d, %d) is %u." % (
		cell1, x1, y1, cell2, x2, y2, distance)
