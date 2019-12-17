import town_generator
import os
import simplejson as json
from stores import Store, Inn
from quests import QuestBoard
import sys
from PC import PC
from character import Character


if __name__ == '__main__':
	if len(sys.argv) > 1:
		info = sys.argv[1]
	else:
		info = input("Enter the Town name you'd like to regenerate: ")
	if not info.endswith(".town.json"):
		info += ".town.json"

	# Try and find if the file exists
	if not os.path.exists(info):
		print("______________ File Doesn't Exist ______________")
	else:
		town_dict = json.load(open(info, 'r'))
		# Build Town
		town_generator.townHTML += "<h1>" + info.split('.')[0] + "</h1><p>Description</p>"
		town_generator.townHTML += """<h2 class="text-lg bold center">Shops</h2>"""

		Q = []
		for key, value in town_dict.items():
			if not key.isdigit():
				Q.append({key: value})
				continue
			if 'TownName' in value:
				board = QuestBoard(value['Low'], value['High'], value['Quantity'], value['TownName'])
				town_generator.townHTML += str(board)
				continue
			if "Stock" not in value.keys():
				new_store = Store(None, None, 0.0, None)
				new_store.from_dict(value)
			else:
				new_store = Inn(None, None, 0.0, 0, 0)
				new_store.from_dict(value)

			# Setup Shop keeper
			new_store.Shopkeeper = Character(None, None, None, None, None, None, None)
			new_store.Shopkeeper.from_dict(value["Shopkeeper"])
			
			if "(Library)" in new_store.Store_name or "(Inn)" in new_store.Store_name:
				town_generator.write_store(new_store, False)
			else:
				town_generator.write_store(new_store)

		print("Finished parsing shops")
		# Questboard
		for pair in Q:
			# print(pair.keys(), pair.values())
			key, value = list(pair.keys())[0], list(pair.values())[0]
			if 'Class' in value:
				# Add NPC here.
				npc = PC()
				npc.from_dict(value)
				town_generator.write_people(npc, key)
			else:
				# Add people here
				person = Character(None, None, None, None, None, None, None)
				person.from_dict(value)
				town_generator.write_people(person, key)
		town_generator.write_html(info.split('.')[0])

