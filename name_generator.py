from numpy.random import randint
from names import *

d_name = ['Aasimer', 'Drow', 'Duergar', 'Dwarf', 'Elf', 'Goblin', 'Human', 'Half-Orc', 'Half-Elf', 'Orc', 'Svirfneblin', 'Tian', 'Tengu', 'Tiefling',]
d_single = ['Catfolk', 'Fetchling', 'Gnome', 'Halfling', 'Hobgoblin', 'Ifrit', 'Kitsune', 'Lizardfolk', 'Nagaji', 'Oread', 'Ratfolk', 'Samsarans', 'Sylph', 'Undine', 'Kobold']
d_premade = ['Dhampir', 'Gillman', 'Grippli', 'Merfolk', 'Strix', 'Vishkanya', 'Wayangs',]

def default_name(race, gender='Male', doubled=True):
	''' Races under this category
	Aasimer, Drow, Duergar, Dwarf, Elf, Goblin, Human, Half-Orc, Half-Elf, Orc, Svirfneblin, Tian, Tengu, Tiefling
	'''
	# First name
	name = ''
	if gender == 'Male':
		name += race.m1[randint(len(race.m1))] + race.m2[randint(len(race.m2))] + race.m3[randint(len(race.m3))] 
		if randint(2) == 1 and doubled:
			name += race.m2[randint(len(race.m2))] + race.m3[randint(len(race.m3))] 
		name += race.m4[randint(len(race.m4))]

	else:  # Female
		name += race.f1[randint(len(race.f1))] + race.f2[randint(len(race.f2))] + race.f3[randint(len(race.f3))] 
		if randint(2) == 1 and doubled:
			name += race.f2[randint(len(race.f2))] + race.f3[randint(len(race.f3))] 
		name += race.f4[randint(len(race.f4))]
		
	# Last name
	name += ' ' + race.s1[randint(len(race.s1))] + race.s2[randint(len(race.s2))] + race.s3[randint(len(race.s3))] 
	if randint(2) == 1 and doubled:
		name += race.s2[randint(len(race.s2))] + race.s3[randint(len(race.s3))] 
	name += race.s4[randint(len(race.s4))]
	
	return name.title()

def default_single(race, gender='Male', doubled=True):
	''' Races under this category
	Catfolk, Fetchling, Gnome, Halfling, Hobgoblin, Ifrit, Kobold, Kitsune, Lizardfold, Nagaji, Oread, Ratfolk, Samsarans, Sylph, Undine, Vishkanya
	'''
	name = ''
	if gender == 'Male':
		name += race.m1[randint(len(race.m1))] + race.m2[randint(len(race.m2))] + race.m3[randint(len(race.m3))] 
		name += race.m2[randint(len(race.m2))] + race.m4[randint(len(race.m4))]
		if randint(2) == 1 and doubled:
			name += race.m3[randint(len(race.m3))] + race.m2[randint(len(race.m2))] + race.m4[randint(len(race.m4))] 

	else:  # Female
		name += race.f1[randint(len(race.f1))] + race.f2[randint(len(race.f2))] + race.f3[randint(len(race.f3))] 
		name += race.f2[randint(len(race.f2))] + race.f4[randint(len(race.f4))]
		if randint(2) == 1and doubled:
			name += race.f2[randint(len(race.f2))] + race.f3[randint(len(race.f3))]  + race.f4[randint(len(race.f4))]

	return name.title()
	
def default_premade(race, gender='Male', single=False):
	''' Races under this category
	Dhampir, Gillman, Grippli, Merfolk, Strix, Wayangs
	'''
	name = ''
	if gender == 'Male':
		name += race.m1[randint(len(race.m1))]
	else:
		name += race.f1[randint(len(race.f1))]
	if not single:
		name += ' ' + race.s1[randint(len(race.s1))]
	return name.title()

def changeling():
	name = ''
	name += Changeling.n1[randint(len(Changeling.n1))] + Changeling.n2[randint(len(Changeling.n2))] + Changeling.n3[randint(len(Changeling.n3))]
	name += Changeling.n2[randint(len(Changeling.n2))] + Changeling.n3[randint(len(Changeling.n3))]
	return name.title()

def suli(gender='Male'):
	s = default_name(Suli, gender) + ' the ' + Suli.t1[randint(len(Suli.t1))]
	return s.title()

def vanara(gender='Male'):
	s = Vanara.n1[randint(len(Vanara.n1))]
	if gender == 'Male':
		s += Vanara.n2[randint(len(Vanara.n2))]
	else:
		s += Vanara.n3[randint(len(Vanara.n3))]
	return s.title()

def name_parser(race, gender):
	name = ''
	if race in d_name:
		if race == 'Aasimer':
			name = default_name(Aasimer, gender)
		elif race == 'Drow':
			name = default_name(Drow, gender)
		elif race == 'Duergar':
			name = default_name(Duergar, gender, False)
		elif race == 'Dwarf':
			name = default_name(Dwarf, gender)
		elif race == 'Elf':
			name = default_name(Elf, gender)
		elif race == 'Goblin':
			name = default_name(Goblin, gender, False)
		elif race == 'Human':
			name = default_name(Human, gender, False)
		elif race == 'Half-Elf':
			name = default_name(HalfElf, gender)
		elif race == 'Half-Orc':
			name = default_name(HalfOrc, gender)
		elif race == 'Orc':
			name = default_name(Orc, gender)
		elif race == 'Svirfneblin':
			name = default_name(Svirfneblin, gender)
		elif race == 'Tian':
			name = default_name(Tian, gender)
		elif race == 'Tengu':
			name = default_name(Tengu, gender)
		elif race == 'Tiefling':
			name = default_name(Tiefling, gender)
			
	elif race in d_single:
		if race == 'Catfolk':
			name = default_single(Catfolk, gender)
		if race == 'Fetchling':
			name = default_single(Fetchling, gender)
		if race == 'Gnome':
			name = default_single(Gnome, gender)
		if race == 'Halfling':
			name = default_single(Halfling, gender)
		if race == 'Hobgoblin':
			name = default_single(Hobgoblin, gender)
		if race == 'Ifrit':
			name = default_single(Ifrit, gender)
		if race == 'Kitsune':
			name = default_single(Kitsune, gender)
		if race == 'Kobold':
			name = default_single(Kobold, gender)
		if race == 'Lizardfolk':
			name = default_single(Lizardfolk, gender)
		if race == 'Nagaji':
			name = default_single(Nagaji, gender)
		if race == 'Oread':
			name = default_single(Oread, gender)
		if race == 'Ratfolk':
			name = default_single(Ratfolk, gender)
		if race == 'Samsarans':
			name = default_single(Samsarans)
		if race == 'Sylph':
			name = default_single(Sylph, gender)
		if race == 'Undine':
			name = default_single(Undine, gender)

	elif race in d_premade:
		if race == 'Dhampir':
			name = default_premade(Dhampir, gender)
		if race == 'Gillman':
			name = default_premade(Gillman, gender, True)
		if race == 'Grippli':
			name = default_premade(Grippli, gender, True)
		if race == 'Merfolk':
			name = default_premade(Merfolk, gender, True)
		if race == 'Strix':
			name = default_premade(Strix, gender)
		if race == 'Vishkanya':
			name = default_premade(Vishkanya, gender)
		if race == 'Wayangs':
			name = default_premade(Wayangs, gender, True)
			
	elif race == 'Changeling':
		name = changeling()
	elif race == 'Suli':
		suli(gender)
	elif race == 'Vanara':
		vanara(gender)
	else:
		name = None
	return name

if __name__ == '__main__':
	print("\t Aasimer Male")
	for _ in range(10):
		print(default_name(Aasimer))
	print("\t Aasimer Female")
	for _ in range(10):
		print(default_name(Aasimer, 'Female'))

	print("\t Catfolk Male")
	for _ in range(10):
		print(default_single(Catfolk))
	print("\t Catfolk Female")
	for _ in range(10):
		print(default_single(Catfolk, 'Female'))

	print('\t Changeling')
	for _ in range(10):
		print(changeling())
	
	print("\t Dhampir Male")
	for _ in range(10):
		print(default_premade(Dhampir))
	print("\t Dhampir Female")
	for _ in range(10):
		print(default_premade(Dhampir, 'Female'))
	
	print("\t Drow Male")
	for _ in range(10):
		print(default_name(Drow))
	print("\t Drow Female")
	for _ in range(10):
		print(default_name(Drow, 'Female'))
		
	print("\t Duergar Male")
	for _ in range(10):
		print(default_name(Duergar, 'Male', False))
	print("\t Duergar Female")
	for _ in range(10):
		print(default_name(Duergar, 'Female', False))
	
	print("\t Dwarf Male")
	for _ in range(10):
		print(default_name(Dwarf))
	print("\t Dwarf Female")
	for _ in range(10):
		print(default_name(Dwarf, 'Female'))
		
	print("\t Elf Male")
	for _ in range(10):
		print(default_name(Elf))
	print("\t Elf Female")
	for _ in range(10):
		print(default_name(Elf, 'Female'))

	print("\t Fetchling Male")
	for _ in range(10):
		print(default_single(Fetchling))
	print("\t Fetchling Female")
	for _ in range(10):
		print(default_single(Fetchling, 'Female'))
		
	print("\t Gillman Male")
	for _ in range(10):
		print(default_premade(Gillman, 'Male', True))
	print("\t Gillman Female")
	for _ in range(10):
		print(default_premade(Gillman, 'Female', True))
		
	print("\t Gnome Male")
	for _ in range(10):
		print(default_single(Gnome))
	print("\t Gnome Female")
	for _ in range(10):
		print(default_single(Gnome, 'Female'))
		
	print("\t Goblin Male")
	for _ in range(10):
		print(default_name(Goblin, 'Male', False))
	print("\t Goblin Female")
	for _ in range(10):
		print(default_name(Goblin, 'Female', False))
		
	print("\t Grippli Male")
	for _ in range(10):
		print(default_premade(Grippli, 'Male', True))
	print("\t Grippli Female")
	for _ in range(10):
		print(default_premade(Grippli, 'Female', True))
		
	print("\t Halfling Male")
	for _ in range(10):
		print(default_single(Halfling, 'Male', False))
	print("\t Halfling Female")
	for _ in range(10):
		print(default_single(Halfling, 'Female', False))
		
	print("\t Hobgoblin Male")
	for _ in range(10):
		print(default_single(Hobgoblin))
	print("\t Hobgoblin Female")
	for _ in range(10):
		print(default_single(Hobgoblin, 'Female'))

	print("\t Human Male")
	for _ in range(10):
		print(default_name(Human))
	print("\t Human Female")
	for _ in range(10):
		print(default_name(Human, 'Female'))

	print("\t Half-Elf Male")
	for _ in range(10):
		print(default_name(HalfElf))
	print("\t Half-Elf Female")
	for _ in range(10):
		print(default_name(HalfElf, 'Female'))
		
	print("\t Half-Orc Male")
	for _ in range(10):
		print(default_name(HalfOrc))
	print("\t Half-Orc Female")
	for _ in range(10):
		print(default_name(HalfOrc, 'Female'))

	print("\t Ifrit Male")
	for _ in range(10):
		print(default_single(Ifrit))
	print("\t Ifrit Female")
	for _ in range(10):
		print(default_single(Ifrit, 'Female'))

	print("\t Kitsune Male")
	for _ in range(10):
		print(default_single(Kitsune))
	print("\t Kitsune Female")
	for _ in range(10):
		print(default_single(Kitsune, 'Female'))

	print("\t Lizardfolk Male")
	for _ in range(10):
		print(default_single(Lizardfolk))
	print("\t Lizardfolk Female")
	for _ in range(10):
		print(default_single(Lizardfolk, 'Female'))
	
	print("\t Merfolk Male")
	for _ in range(10):
		print(default_name(Merfolk, 'Male', True))
	print("\t Merfolk Female")
	for _ in range(10):
		print(default_name(Merfolk, 'Female', True))

	print("\t Nagaji Male")
	for _ in range(10):
		print(default_single(Nagaji))
	print("\t Nagaji Female")
	for _ in range(10):
		print(default_single(Nagaji, 'Female'))
		
	print("\t Orc Male")
	for _ in range(10):
		print(default_name(Orc))
	print("\t Orc Female")
	for _ in range(10):
		print(default_name(Orc, 'Female'))

	print("\t Oread Male")
	for _ in range(10):
		print(default_single(Oread))
	print("\t Oread Female")
	for _ in range(10):
		print(default_single(Oread, 'Female'))
	
	print("\t Ratfolk Male")
	for _ in range(10):
		print(default_single(Ratfolk))
	print("\t Ratfolk Female")
	for _ in range(10):
		print(default_single(Ratfolk, 'Female'))
	
	print("\t Samsarans")
	for _ in range(10):
		print(default_single(Samsarans))
		
	print("\t Strix Male")
	for _ in range(10):
		print(default_premade(Strix))
	print("\t Strix Female")
	for _ in range(10):
		print(default_premade(Strix, 'Female'))
	
	print('\t Suli Male')
	for _ in range(10):
		print(suli())
	
	print('\t Suli Female')
	for _ in range(10):
		print(suli('Female'))
		
	print("\t Svirfneblin Male")
	for _ in range(10):
		print(default_name(Svirfneblin))
	print("\t Svirfneblin Female")
	for _ in range(10):
		print(default_name(Svirfneblin, 'Female'))
		
	print("\t Sylph Male")
	for _ in range(10):
		print(default_single(Sylph))
	print("\t Sylph Female")
	for _ in range(10):
		print(default_single(Sylph, 'Female'))
	
	print("\t Tian Male")
	for _ in range(10):
		print(default_name(Tian))
	print("\t Tian Female")
	for _ in range(10):
		print(default_name(Tian, 'Female'))
	
	print("\t Tengu Male")
	for _ in range(10):
		print(default_name(Tengu))
	print("\t Tengu Female")
	for _ in range(10):
		print(default_name(Tengu, 'Female'))
	
	print("\t Tiefling Male")
	for _ in range(10):
		print(default_name(Tiefling))
	print("\t Tiefling Female")
	for _ in range(10):
		print(default_name(Tiefling, 'Female'))
	
	print("\t Undine Male")
	for _ in range(10):
		print(default_single(Undine))
	print("\t Undine Female")
	for _ in range(10):
		print(default_single(Undine, 'Female'))
	
	print("\t Vanara")
	for _ in range(10):
			print(vanara())
	print("\t Vanara")
	for _ in range(10):
			print(vanara('Female'))
	
	print("\t Vishkanya Male")
	for _ in range(10):
		print(default_premade(Vishkanya))
	print("\t Vishkanya Female")
	for _ in range(10):
		print(default_premade(Vishkanya, 'Female'))
		
	print("\t Wayangs Male")
	for _ in range(10):
		print(default_premade(Wayangs, 'Male', True))
	print("\t Wayangs Female")
	for _ in range(10):
		print(default_premade(Wayangs, 'Female', True))

	