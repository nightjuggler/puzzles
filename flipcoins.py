#!/usr/bin/python
import random

def flip():
	return 'H' if random.random() < 0.5 else 'T'

def flip_until(target_sequence):
	current_sequence = ''
	num_flips = 0

	for i in xrange(len(target_sequence)):
		current_sequence += flip()
		num_flips += 1

	while current_sequence != target_sequence:
		current_sequence = current_sequence[1:] + flip()
		num_flips += 1

	return num_flips

def average_flips(target_sequence, num_tries=10000):
	sum_flips = 0

	for i in xrange(num_tries):
		sum_flips += flip_until(target_sequence)

	print "Average number of flips to get '{}' = {}".format(target_sequence, float(sum_flips) / num_tries)

def print_equation(E, sequence):
	coefficient, num_flips, prefix_list = E[sequence]
	print "{}E[{}] = {}".format(coefficient if coefficient != 1 else '', sequence, num_flips),
	for coefficient, prefix in prefix_list:
		print "+ {}E[{}]".format(coefficient if coefficient != 1 else '', prefix),
	print

def expected_flips(target_sequence, verbose=True):
	sequence = target_sequence
	E = {}
	E[sequence] = [1, 0, []]

	while sequence != '':
		if verbose:
			print_equation(E, sequence)

		left_coefficient = 2
		left_prefix = sequence[:-1]
		num_flips = 2
		prefix_list = []

		if sequence[-1] == 'H':
			prefix1 = left_prefix + 'T'
			prefix2 = left_prefix + 'H'
		else:
			prefix1 = left_prefix + 'H'
			prefix2 = left_prefix + 'T'

		if verbose:
			print "2E[{}] = 2 + E[{}] + E[{}]".format(left_prefix, prefix1, prefix2)
			print "E[{}] =".format(prefix1),

		prefix1 = prefix1[1:]
		prefix1_len = len(prefix1)

		while prefix1 != sequence[:prefix1_len]:
			prefix1 = prefix1[1:]
			prefix1_len -= 1

		if verbose:
			print "E[{}]".format(prefix1)

		if prefix1 == left_prefix:
			left_coefficient -= 1
			if verbose:
				print "{}E[{}] = 2 + E[{}]".format(
					left_coefficient if left_coefficient != 1 else '', left_prefix, prefix2)
		else:
			prefix_list.append([1, prefix1])
			if verbose:
				print "2E[{}] = 2 + E[{}] + E[{}]".format(left_prefix, prefix1, prefix2)

		p2_coefficient, p2_num_flips, p2_list = E[prefix2]
		if p2_coefficient > 1:
			left_coefficient *= p2_coefficient
			num_flips *= p2_coefficient
			if verbose:
				print "{}E[{}] = {}".format(left_coefficient, left_prefix, num_flips),
			for p in prefix_list:
				p[0] *= p2_coefficient
				if verbose:
					print "+ {}E[{}]".format(p[0], p[1]),
			if verbose:
				print "+ {}E[{}]".format(p2_coefficient, prefix2)

		num_flips += p2_num_flips
		for p in p2_list:
			if p[1] == left_prefix:
				left_coefficient -= p[0]
			else:
				prefix_list.append(p)

		E[left_prefix] = [left_coefficient, num_flips, prefix_list]
		sequence = left_prefix

	if verbose:
		print_equation(E, '')

	left_coefficient, num_flips, prefix_list = E['']
	assert left_coefficient == 1
	assert len(prefix_list) == 0
	print "Expected number of flips to get '{}' = {}".format(target_sequence, num_flips)

if __name__ == '__main__':
	import argparse
	import sys

	parser = argparse.ArgumentParser()
	parser.add_argument('sequence', nargs='?', default='HH')
	parser.add_argument('-a', '--average', nargs='?', const=10000, default=0, type=int)
	parser.add_argument('-e', '--expected', action='store_true')
	parser.add_argument('-v', '--verbose', action='store_true')
	args = parser.parse_args()

	for letter in args.sequence:
		if letter not in ('H', 'T', 'h', 't'):
			sys.exit("The sequence argument must be a string containing only the letters H and T.")

	sequence = args.sequence.upper()

	if args.average < 0:
		sys.exit("The number of tries for calculating the average must be a positive integer.")

	if args.expected or args.average == 0:
		expected_flips(sequence, args.verbose)

	if args.average > 0:
		average_flips(sequence, args.average)
