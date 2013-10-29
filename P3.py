field = ('Field', 'You are in a field that seems to go on for miles, a capsule of sorts is behind you')
village = ('Deserted village', 'You are in a village that seams to be abandoned.')
city = ('City', 'A lively city with a bunch of people wandering')

transitions = {
	field: (village, city),
	village: (field,),
	city: (field,),
}

location = field

while True:
	print location[1]
	print 'You can go to these places:'

	for (i, t) in enumerate(transitions[location]):
		print i + 1, t[0]

	choice = int(raw_input('Choose one'))
	location = transitions[location][choice - 1]