import csv
import re
import sys

import random

def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i
def get_tags(match):

	tags_list = []	
	with open(match + ".csv", 'rb') as csvfile:	
		reader = csv.reader(csvfile, delimiter ='\t')
		header_row = next(reader)
		matches = len(header_row[0].split(',')) - 1

		for i in range(matches):
			tags_list.append({})

		for row in reader:
			for i in range(matches):
				tag = row[0].split(',')[i+1]
				if tag not in tags_list[i]:
					tags_list[i][tag] = 1
				else:
					tags_list[i][tag] += 1
	return tags_list

def get_weight(tags_list):
	weights = []
	for tags in tags_list:
		weights.append([tags[i] for i in tags])
	return weights

def get_games(weights):
	games = []
	for i in range(len(weights)):
		games.append([])
		for n in range(3):
			if n==2 and games[i][0] == games[i][1]:
				continue
			games[i].append(weighted_choice([weights[i][0], weights[i][1]]) + 1)
	return games

def print_results(tags_list, games, match):
	f = open(match + '.txt', 'w')
	for i in range(len(games)):
		for j in tags_list[i]:
			print str(j) + '(' + str(tags_list[i][j]) + ')'
		f.write(str(tags_list[i]) + '\n')
		f.write(str(games[i]) + '\n')
	f.close()

def main():
	if len(sys.argv) != 2:
		print "Requires Name of CSV file"
		exit()
	tags = get_tags(sys.argv[1])
	weights = get_weight(tags)
	games = get_games(weights)
	print_results(tags, games, sys.argv[1])

if __name__ == "__main__":
    main()

