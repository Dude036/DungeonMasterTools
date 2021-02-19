import simplejson as json
'''
    'Sample' : { 'Weight': 10, 'Cost' : 1, 'Type' : ['B','S','P','LA','MA','HA','2','1','Si','Ma','Ex','Ra','Ar',], },
B, S, P          - Blunt, Slash, Pierce
LA, MA, HA        - Light Armor, Medium Armor, Heavy Armor
2, 1                - 2 Handed, 1 Handed
Si, Ma, Ex, Ra, Ar  - Simple, Martial, Exotic, Ranged (bows), Ranged (arrows)s
    If you want to make your life hell:
https://the-eye.eu/public/Books/rpg.rem.uz/Pathfinder/3rd%20Party/Rite%20Publishing/101%20Series/101%20Special%20Materials%20%26%20Power%20Components.pdf
'''
common_material = {
    'Bronze': {
        'Weight': 1,
        'AC': 8,
        'Cost': .8,
        'Type': ['B', 'S', 'P', 'MA', 'HA', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Copper': {
        'Weight': 1,
        'AC': 6,
        'Cost': .8,
        'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Iron': {
        'Weight': 1,
        'AC': 10,
        'Cost': 1,
        'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Lead': {
        'Weight': 1.5,
        'AC': 8,
        'Cost': 1.1,
        'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Steel': {
        'Weight': 1,
        'AC': 10,
        'Cost': 1,
        'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Oak': {
        'Weight': .5,
        'AC': 2,
        'Cost': .25,
        'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra'],
    },
    'Yew': {
        'Weight': .5,
        'AC': 2,
        'Cost': .25,
        'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra'],
    },
    'Hide': {
        'Weight': .5,
        'AC': 8,
        'Cost': .8,
        'Type': ['LA', 'MA'],
    },
    'Leather': {
        'Weight': .5,
        'AC': 8,
        'Cost': .8,
        'Type': ['LA', 'MA'],
    },
}
uncommon_material = {
    'Adamantine': {
        'Weight': 1,
        'AC': 20,
        'Cost': 1.8,
        'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Bone': {
        'Weight': 1,
        'AC': 6,
        'Cost': .8,
        'Type': ['B', 'S', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Darkwood': {
        'Weight': .2,
        'AC': 5,
        'Cost': 1.05,
        'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra'],
    },
    'Dragonskin': {
        'Weight': 1,
        'AC': 12,
        'Cost': 2.25,
        'Type': ['LA', 'MA', 'HA'],
    },
    'Dragonhide': {
        'Weight': 1,
        'AC': 10,
        'Cost': 2.5,
        'Type': ['LA', 'MA', 'HA'],
    },
    'Gold': {
        'Weight': 1,
        'AC': 5,
        'Cost': 10,
        'Type': ['S', 'P', 'MA', '1', 'Si', 'Ex', 'Ra', 'Ar'],
    },
    'Greenwood': {
        'Weight': .5,
        'AC': 2,
        'Cost': 1.15,
        'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra'],
    },
    'Platinum': {
        'Weight': .7,
        'AC': 15,
        'Cost': 5,
        'Type': ['S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar']
    },
    'Silkweave': {
        'Weight': .15,
        'AC': 10,
        'Cost': 2,
        'Type': ['LA']
    },
    'Silver': {
        'Weight': 1,
        'AC': 8,
        'Cost': 1.15,
        'Type': ['S', 'P', 'MA', '1', 'Si', 'Ex', 'Ra', 'Ar'],
    },
    'Stone': {
        'Weight': .75,
        'AC': 2,
        'Cost': .25,
        'Type': ['B', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
}
rare_material = {
    'Angelskin': {
        'Weight': .2,
        'AC': 5,
        'Cost': 2.75,
        'Type': ['LA', 'MA'],
    },
    'Cold Iron': {
        'Weight': 1,
        'AC': 10,
        'Cost': 2,
        'Type': ['S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Dreamstone': {
        'Weight': .5,
        'AC': 10,
        'Cost': 2.25,
        'Type': ['B', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Elysian Bronze': {
        'Weight': 1,
        'AC': 10,
        'Cost': 2,
        'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Griffon Mane': {
        'Weight': .2,
        'AC': 1,
        'Cost': 2,
        'Type': ['LA', 'MA'],
    },
    'Ironwood': {
        'Weight': .7,
        'AC': 10,
        'Cost': 1.8,
        'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra'],
    },
    'Obsidian': {
        'Weight': .75,
        'AC': 5,
        'Cost': 1.5,
        'Type': ['S', 'P', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Viridium': {
        'Weight': 1,
        'AC': 10,
        'Cost': 1.5,
        'Type': ['S', 'P', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
}
very_rare_material = {
    'Blood Crystal': {
        'Weight': 1,
        'AC': 10,
        'Cost': 2.75,
        'Type': ['S', 'P', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Darkleaf Cloth': {
        'Weight': .2,
        'AC': 10,
        'Cost': 2.75,
        'Type': ['LA',],
    },
    'Mithral': {
        'Weight':
            .5,
        'AC':
            15,
        'Cost':
            3,
        'Type': [
            'B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'
        ],
    },
    'Hot Siccatite': {
        'Weight':
            .8,
        'AC':
            10,
        'Cost':
            3,
        'Type': [
            'B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'
        ],
    },
    'Cold Siccatite': {
        'Weight':
            .8,
        'AC':
            10,
        'Cost':
            3,
        'Type': [
            'B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'
        ],
    },
    'Wyroot': {
        'Weight': 1.5,
        'AC': 5,
        'Cost': 2.5,
        'Type': ['B', 'P', '2', '1', 'Si', 'Ma', 'Ex', 'Ra'],
    },
}
legendary_material = {
    'Horacalcum': {
        'Weight': 1,
        'AC': 15,
        'Cost': 5,
        'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Mindglass': {
        'Weight': 1,
        'AC': 10,
        'Cost': 4,
        'Type': ['B', 'S', 'P', 'LA', 'MA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Noqual': {
        'Weight':
            .5,
        'AC':
            10,
        'Cost':
            3,
        'Type': [
            'B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'
        ],
    },
    'Umbrite': {
        'Weight':
            1,
        'AC':
            18,
        'Cost':
            3,
        'Type': [
            'B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'
        ],
    },
    'Voidglass': {
        'Weight': .5,
        'AC': 10,
        'Cost': 3.25,
        'Type': ['S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar'],
    },
    'Whipwood': {
        'Weight': .2,
        'AC': 9,
        'Cost': 3,
        'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra'],
    },
}

masterwork_traits_weapon = [
    'Adaptive', 'Advancing', 'Agile', 'Allying', 'Ambushing', 'Anarchic',
    'Anchoring', 'Answering', 'Axiomatic', 'Bane', 'Beaming', 'Benevolent',
    'Bewildering', 'Blood-Hunting', 'Bloodsong', 'Brawling', 'Breaking',
    'Brilliant Energy', 'Called', 'Compassionate', 'Concealed',
    'Lesser Concealed', 'Conductive', 'Conserving', 'Corrosive',
    'Corrosive Burst', 'Countering', 'Courageous', 'Cruel', 'Culling',
    'Cyclonic', 'Dazzling', 'Dazzling Radiance', 'Deadly', 'Debilitating',
    'Defending', 'Defiant', 'Greater Designating', 'Lesser Designating',
    'Dispelling', 'Dispelling Burst', 'Disruption', 'Distance', 'Distracting',
    'Driving', 'Dry Load', 'Dueling', 'Endless Ammunition', 'Exhausting',
    'Fervent', 'Flaming', 'Flaming Burst', 'Flying', 'Fortuitous', 'Frost',
    'Furious', 'Furyborn', 'Ghost Touch', 'Glitterwake', 'Glorious', 'Gory',
    'Grayflame', 'Grounding', 'Growing', 'Guardian', 'Heart-Piercing',
    'Heartseeker', 'Heretical', 'Holy', 'Huntsman', 'Icy Burst', 'Igniting',
    'Impact', 'Impervious', 'Injecting', 'Interfering', 'Invigorating', 'Keen',
    'Ki Focus', 'Ki Intensifying', 'Kinslayer', 'Legbreaker', 'Liberating',
    'Lifesurge', 'Limning', 'Lucky', 'Greater Lucky', 'Menacing', 'Merciful',
    'Mighty Cleaving', 'Mimetic', 'Miserable', 'Negating', 'Neutralizing',
    'Nimble Shot', 'Ominous', 'Patriotic', 'Peaceful', 'Penetrating',
    'Phantom Ammunition', 'Phase Locking', 'Planestriking', 'Plummeting',
    'Quaking', 'Quenching', 'Redeemed', 'Reliable', 'Greater Reliable',
    'Repositioning', 'Returning', 'Rusting', 'Sacred', 'Sapping', 'Seaborne',
    'Second Chance', 'Seeking', 'Shadowshooting', 'Sharding', 'Shattering',
    'Shock', 'Shocking Burst', 'Shrinking', 'Silencing', 'Smashing', 'Sneaky',
    'Sonic Boom', 'Speed', 'Spell Siphon', 'Spell Stealing', 'Spell Storing',
    'Stalking', 'Summon Bane', 'Tailwind', 'Thawing', 'Throwing', 'Thundering',
    'Toxic', 'Training', 'Treasonous', 'Truthful', 'Umbral', 'Underwater',
    'Unholy', 'Unseen', 'Valiant', 'Vampiric', 'Greater Vampiric', 'Vicious',
    'Vorpal', 'Wounding'
]

masterwork_trait_cost_weapon = {
    1: [
        'Adaptive', 'Agile', 'Allying', 'Ambushing', 'Answering', 'Bane', 
        'Beaming', 'Benevolent',  'Bewildering', 'Blood-Hunting', 'Bloodsong',
        'Brawling', 'Breaking', 'Brilliant Energy', 'Called', 'Compassionate',
        'Lesser Concealed', 'Conductive', 'Conserving', 'Corrosive', 
        'Countering', 'Courageous', 'Cruel', 'Dazzling Radiance', 'Deadly', 
        'Debilitating', 'Defending', 'Dispelling', 'Distance', 'Distracting',
        'Driving', 'Dry Load', 'Fervent', 'Flaming', 'Fortuitous', 'Frost', 
        'Furious', 'Ghost Touch', 'Grayflame', 'Grounding', 'Growing', 
        'Guardian', 'Heartseeker', 'Huntsman', 'Impervious', 'Injecting',
        'Keen', 'Ki Focus', 'Kinslayer', 'Limning', 'Lucky', 'Menacing',
        'Merciful', 'Mighty Cleaving', 'Mimetic', 'Miserable', 'Neutralizing',
        'Ominous', 'Patriotic', 'Phantom Ammunition', 'Plummeting', 'Quaking',
        'Quenching', 'Reliable', 'Returning', 'Rusting', 'Sacred', 'Sapping', 
        'Seaborne', 'Seeking', 'Shadowshooting','Shock', 'Shrinking', 'Smashing',
        'Spell Storing', 'Stalking', 'Summon Bane', 'Thawing', 'Throwing',
        'Thundering', 'Training', 'Underwater', 'Valiant', 'Vampiric', 'Vicious',
    ],
    2: [
        'Advancing', 'Anarchic', 'Anchoring', 'Axiomatic', 'Concealed', 
        'Corrosive Burst', 'Culling', 'Cyclonic', 'Dazzling', 'Defiant', 
        'Lesser Designating', 'Dispelling Burst', 'Disruption', 
        'Greater Distracting', 'Endless Ammunition', 'Flaming Burst', 'Furyborn',
        'Glitterwake', 'Glorious', 'Heretical', 'Holy', 'Icy Burst', 'Igniting',
        'Impact', 'Invigorating', 'Ki Intensifying', 'Legbreaker', 'Liberating', 
        'Lifesurge', 'Negating', 'Peaceful', 'Penetrating', 'Phase Locking', 
        'Planestriking', 'Sharding', 'Shattering', 'Shocking Burst', 'Silencing',
        'Sneaky', 'Toxic', 'Treasonous', 'Truthful', 'Unseen', 
        'Greater Vampiric', 'Wounding',
    ],
    3: [
        'Dueling', 'Exhausting', 'Gory', 'Greater Lucky', 'Redeemed',
        'Sonic Boom', 'Speed', 'Spell Stealing', 'Tailwind', 'Umbral',
        'Unholy', 
    ],
    4: [
        'Greater Designating', 'Nimble Shot', 'Greater Reliable',
        'Repositioning', 'Second Chance'
    ],
    5: ['Flying', 'Heart-Piercing', 'Interfering', 'Spell Siphon', 'Vorpal'],
}

masterwork_traits_armor = [
    'Adamant', 'Adhesive', 'Advancing', 'Amorphous', 'Animated',
    'Arrow Catching', 'Arrow Deflection', 'Arrow-Collecting', 'Assiduous',
    'Balanced', 'Balanced', 'Bashing', 'Bastion', 'Benevolent', 'Billowing',
    'Bitter', 'Blinding', 'Bloodthirsty', 'Bolstering', 'Brawling', 'Buoyant',
    'Burdenless', 'Calming', 'Champion', 'Channeling', 'Clangorous',
    'Cocooning', 'Comfort', 'Creeping', 'Crusading',
    'Cushioned', 'Deathless', 'Deceiving', 'Defiant', 'Delving',
    'Determination', 'Dread Wing', 'Energy Resistance',
    'Greater Energy Resistance', 'Improved Energy Resistance', 'Etherealness',
    'Evolving', 'Expeditious', 'Light Fortification', 'Medium Fortification',
    'Heavy Fortification', 'Frosted', 'Glamered', 'Grinding', 'Harmonizing',
    'Hosteling', 'Invulnerability', 'Jawbreaker', 'Locksmith', 'Malevolent',
    'Martyring', 'Mastering', 'Mental Focus', 'Merging', 'Mind Buttressing',
    'Mirrored','Phantasmal', 'Phase Lurching', 'Poison-Resistant', 'Poisoning',
    'Putrid', 'Radiant', 'Radiant Flight', 'Rallying', 'Rebounding',
    'Reflecting', 'Restful', 'Righteous', 'Sensing', 'Shadow',
    'Shadow Blending', 'Greater Shadow', 'Improved Shadow', 'Singing',
    'Spell Dodging', 'Spell Resistance', 'Spell Storing', 'Spellrending',
    'Spellsink', 'Spirit-Bonded', 'Terrain-Striding', 'Titanic', 'Trackless',
    'Unbowed', 'Unrighteous', 'Volcanic', 'Warding', 'Weeping', 'Wild',
    'Withstanding', 'Wyrmsbreath'
]

masterwork_trait_cost_armor = {
    1: [
        'Advancing', 'Amorphous', 'Arrow Catching', 'Assiduous', 'Balanced', 
        'Balanced', 'Bashing', 'Benevolent', 'Billowing', 'Bitter', 'Blinding',
        'Bolstering', 'Buoyant', 'Calming', 'Champion', 'Channeling',
        'Clangorous', 'Cocooning', 'Comfort', 'Creeping', 'Crusading',
        'Cushioned', 'Deceiving', 'Defiant', 'Expeditious',
        'Light Fortification', 'Frosted', 'Glamered', 'Grinding',
        'Harmonizing', 'Jawbreaker', 'Locksmith', 'Mind Buttressing',
        'Mirrored', 'Poison-Resistant', 'Poisoning', 'Putrid', 'Rebounding',
        'Restful', 'Sensing', 'Shadow', 'Singing', 'Spell Storing',
        'Spellrending', 'Spirit-Bonded', 'Terrain-Striding', 'Trackless',
        'Warding', 'Withstanding'
    ],
    2: [
        'Adamant', 'Adhesive', 'Animated', 'Arrow Deflection', 'Bloodthirsty',
        'Burdenless', 'Corsair', 'Delving', 'Evolving', 'Hosteling',
        'Malevolent', 'Mastering', 'Mental Focus', 'Phantasmal',
        'Phase Lurching', 'Radiant', 'Rallying', 'Shadow Blending', 
        'Spell Dodging', 'Lesser Spell Resistance', 'Volcanic', 'Weeping', 
        'Wyrmsbreath'
    ],
    3: [
        'Arrow-Collecting', 'Brawling', 'Determination', 'Energy Resistance',
        'Etherealness', 'Medium Fortification', 'Invulnerability', 'Merging',
        'Radiant Flight', 'Reflecting', 'Righteous', 'Sensing',
        'Improved Shadow', 'Spell Resistance', 'Titanic', 'Unrighteous', 'Wild'
    ],
    4: [
        'Bastion', 'Deathless', 'Improved Energy Resistance', 'Martyring',
        'Greater Shadow', 'Improved Spell Resistance' 
    ],
    5: [
        'Dread Wing', 'Greater Energy Resistance', 'Heavy Fortification',
        'Greater Spell Resistance', 'Spellsink', 'Unbowed'
    ],
}
"""
https://the-eye.eu/public/Books/rpg.rem.uz/Pathfinder/Roleplaying%20Game/PZO1114%20GameMastery%20Guide%20%283rd%20printing%29.pdf
Level 0 : 12.5 GP
Level 1 : 25 GP
Level 2 : 150 GP
Level 3 : 375 GP
Level 4 : 700 GP
Level 5 : 1125 GP
Level 6 : 1650 GP
Level 7 : 2275 GP
Level 8 : 3000 GP
Level 9 : 4825 GP
"""
MasterSpellBlacklist = ["https://homebrewery.naturalcrit.com/share/r1TpuSfiz"]
SpellSource = json.load(open('settings.json', 'r'))['System']
if SpellSource == 'D&D 5':
    level_0 = [
        'Acid Splash', 'Blade Ward', 'Booming Blade', 'Chill Touch', 'Control Flames', 'Create Bonfire', 'Dancing Lights', 'Druidcraft', 'Eldritch Blast', 'Encode Thoughts', 'Enter Mindscape', 'Fire Bolt', 'Friends', 'Frostbite', 'Green-Flame Blade', 'Guidance', 'Gust', 'Hand of Radiance (UA)', 'Infestation', 'Infestation (UA)', 'Light', 'Lightning Lure', 'Mage Hand', 'Magic Stone', 'Mending', 'Message', 'Mind Fist', 'Mind Sliver', 'Mind Strike', 'Minor Illusion', 'Mold Earth', 'On/Off (UA)', 'Poison Spray', 'Prestidigitation', 'Primal Savagery', 'Primal Savagery (UA)', 'Produce Flame', 'Psychic Step', 'Ray of Frost', 'Resistance', 'Sacred Flame', 'Sapping Sting', 'Shape Water', 'Shillelagh', 'Shocking Grasp', 'Spare the Dying', 'Sword Burst', 'Thaumaturgy', 'Thorn Whip', 'Thunderclap', 'Toll the Dead', 'Toll the Dead (UA)', 'True Strike', 'Vicious Mockery', 'Virtue (UA)', 'Word of Radiance'
    ]
    level_1 = [
        'Absorb Elements', 'Acid Stream', 'Alarm', 'Animal Friendship', 'Arcane Weapon', 'Armor of Agathys', 'Arms of Hadar', 'Bane', 'Beast Bond', 'Bless', 'Burning Hands', 'Catapult', 'Cause Fear', 'Cause Fear (UA)', 'Ceremony', 'Ceremony (UA)', 'Chaos Bolt', 'Chaos Bolt (UA)', 'Charm Person', 'Chromatic Orb', 'Color Spray', 'Command', 'Compelled Duel', 'Comprehend Languages', 'Create or Destroy Water', 'Cure Wounds', 'Detect Evil and Good', 'Detect Magic', 'Detect Poison and Disease', 'Disguise Self', 'Dissonant Whispers', 'Distort Value', 'Divine Favor', 'Earth Tremor', 'Ensnaring Strike', 'Entangle', 'Expeditious Retreat', 'Faerie Fire', 'False Life', 'Feather Fall', 'Find Familiar', 'Fog Cloud', 'Frost Fingers', 'Gift of Alacrity', 'Goodberry', 'Grease', 'Guiding Bolt', 'Guiding Hand (UA)', 'Hail of Thorns', 'Healing Elixir (UA)', 'Healing Word', 'Hellish Rebuke', 'Heroism', 'Hex', "Hunter's Mark", 'Ice Knife', 'Id Insinuation', 'Identify', 'Illusory Script', 'Infallible Relay (UA)', 'Inflict Wounds', "Jim's Magic Missile", 'Jump', 'Longstrider', 'Mage Armor', 'Magic Missile', 'Magnify Gravity', 'Protection from Evil and Good', 'Puppet (UA)', 'Purify Food and Drink', 'Ray of Sickness', 'Remote Access (UA)', 'Sanctuary', 'Searing Smite', 'Sense Emotion (UA)', 'Shield', 'Shield of Faith', 'Silent Image', 'Sleep', 'Snare', 'Snare (UA)', 'Speak with Animals', 'Sudden Awakening (UA)', "Tasha's Hideous Laughter", "Tenser's Floating Disk", 'Thunderous Smite', 'Thunderwave', 'Unearthly Chorus (UA)', 'Unseen Servant', 'Wild Cunning (UA)', 'Witch Bolt', 'Wrathful Smite', 'Zephyr Strike', 'Zephyr Strike (UA)'
    ]
    level_2 = [
        "Aganazzar's Scorcher", 'Aid', 'Alter Self', 'Animal Messenger', 'Arcane Hacking (UA)', 'Arcane Lock', 'Augury', 'Barkskin', 'Beast Sense', 'Blindness/Deafness', 'Blur', 'Branding Smite', 'Calm Emotions', 'Cloud of Daggers', 'Continual Flame', 'Cordon of Arrows', 'Crown of Madness', 'Darkness', 'Darkvision', 'Detect Thoughts', 'Digital Phantom (UA)', "Dragon's Breath", 'Dust Devil', 'Earthbind', 'Enhance Ability', 'Enlarge/Reduce', 'Enthrall', 'Find Steed', 'Find Traps', 'Find Vehicle (UA)', 'Flame Blade', 'Flaming Sphere', 'Flock of Familiars', "Fortune's Favor", 'Gentle Repose', 'Gift of Gab', 'Gust of Wind', 'Healing Spirit', 'Heat Metal', 'Hold Person', 'Immovable Object', 'Invisibility', "Jim's Glowing Coin", 'Knock', 'Lesser Restoration', 'Levitate', 'Locate Animals or Plants', 'Locate Object', 'Magic Mouth', 'Magic Weapon', "Maximilian's Earthen Grasp", "Melf's Acid Arrow", 'Mental Barrier', 'Mind Spike', 'Mind Thrust', 'Mirror Image', 'Misty Step', 'Moonbeam', "Nystul's Magic Aura", 'Pass without Trace', 'Phantasmal Force', 'Prayer of Healing', 'Protection from Poison', 'Pyrotechnics', 'Ray of Enfeeblement', 'Rope Trick', 'Scorching Ray', 'See Invisibility', 'Shadow Blade', 'Shatter', 'Silence', 'Skywrite', "Snilloc's Snowball Swarm", 'Spider Climb', 'Spike Growth', 'Spiritual Weapon', 'Suggestion', 'Summon Bestial Spirit', 'Thought Shield', 'Warding Bond', 'Warding Wind', 'Web', 'Wristpocket', 'Zone of Truth'
    ]
    level_3 = [
        'Animate Dead', 'Aura of Vitality', 'Beacon of Hope', 'Bestow Curse', 'Blinding Smite', 'Blink', 'Call Lightning', 'Catnap', 'Clairvoyance', 'Conjure Animals', 'Conjure Barrage', 'Conjure Lesser Demon (UA)', 'Counterspell', 'Create Food and Water', "Crusader's Mantle", 'Daylight', 'Dispel Magic', 'Elemental Weapon', 'Enemies Abound', 'Erupting Earth', 'Fast Friends', 'Fear', 'Feign Death', 'Fireball', 'Flame Arrows', 'Fly', "Galder's Tower", 'Gaseous Form', 'Glyph of Warding', 'Haste', 'Haywire (UA)', 'Hunger of Hadar', 'Hypnotic Pattern', 'Incite Greed', 'Invisibility to Cameras (UA)', "Leomund's Tiny Hut", 'Life Transference', 'Lightning Arrow', 'Lightning Bolt', 'Magic Circle', 'Major Image', 'Mass Healing Word', 'Meld into Stone', "Melf's Minute Meteors", 'Motivational Speech', 'Nondetection', 'Phantom Steed', 'Plant Growth', 'Protection from Ballistics (UA)', 'Protection from Energy', 'Psionic Blast', 'Pulse Wave', 'Remove Curse', 'Revivify', 'Sending', 'Sleet Storm', 'Slow', 'Speak with Dead', 'Speak with Plants', 'Spirit Guardians', 'Spirit Shroud', 'Stinking Cloud', 'Summon Fey Spirit', 'Summon Lesser Demons', 'Summon Shadow Spirit', 'Summon Undead Spirit', 'Thunder Step', 'Tidal Wave', 'Tiny Servant', 'Tongues', 'Vampiric Touch', 'Wall of Sand', 'Wall of Water', 'Water Breathing', 'Water Walk', 'Wind Wall'
    ]
    level_4 = [
        'Arcane Eye', 'Aura of Life', 'Aura of Purity', 'Banishment', 'Blight', 'Charm Monster', 'Compulsion', 'Confusion', 'Conjure Barlgura (UA)', 'Conjure Knowbot (UA)', 'Conjure Minor Elementals', 'Conjure Shadow Demon (UA)', 'Conjure Woodland Beings', 'Control Water', 'Death Ward', 'Dimension Door', 'Divination', 'Dominate Beast', 'Ego Whip', 'Elemental Bane', "Evard's Black Tentacles", 'Fabricate', 'Find Greater Steed', 'Fire Shield', 'Freedom of Movement', "Galder's Speedy Courier", 'Giant Insect', 'Grasping Vine', 'Gravity Sinkhole', 'Greater Invisibility', 'Guardian of Faith', 'Guardian of Nature', 'Hallucinatory Terrain', 'Ice Storm', "Leomund's Secret Chest", 'Locate Creature', "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", 'Phantasmal Killer', 'Polymorph', 'Shadow of Moil', 'Sickening Radiance', 'Staggering Smite', 'Stone Shape', 'Stoneskin', 'Storm Sphere', 'Summon Aberrant Spirit', 'Summon Elemental Spirit', 'Summon Greater Demon', 'Synchronicity (UA)', 'System Backdoor (UA)', 'Vitriolic Sphere', 'Wall of Fire', 'Watery Sphere'
    ]
    level_5 = [
        'Animate Objects', 'Antilife Shell', 'Awaken', 'Banishing Smite', "Bigby's Hand", 'Circle of Power', 'Cloudkill', 'Commune', 'Commune with City (UA)', 'Commune with Nature', 'Cone of Cold', 'Conjure Elemental', 'Conjure Volley', 'Conjure Vrock (UA)', 'Contact Other Plane', 'Contagion', 'Control Winds', 'Creation', 'Danse Macabre', 'Dawn', 'Destructive Wave', 'Dispel Evil and Good', 'Dominate Person', 'Dream', 'Enervation', 'Far Step', 'Flame Strike', 'Geas', 'Greater Restoration', 'Hallow', 'Hold Monster', 'Holy Weapon', 'Immolation', 'Infernal Calling', 'Insect Plague', 'Intellect Fortress', 'Legend Lore', 'Maelstrom', 'Mass Cure Wounds', 'Mislead', 'Modify Memory', 'Negative Energy Flood', 'Passwall', 'Planar Binding', 'Raise Dead', "Rary's Telepathic Bond", 'Reincarnate', 'Scrying', 'Seeming', 'Shutdown (UA)', 'Skill Empowerment', 'Steel Wind Strike', 'Summon Celestial Spirit', 'Swift Quiver', 'Synaptic Static', 'Telekinesis', 'Teleportation Circle', 'Temporal Shunt', 'Transmute Rock', 'Tree Stride', 'Wall of Force', 'Wall of Light', 'Wall of Stone', 'Wrath of Nature'
    ]
    level_6 = [
        'Arcane Gate', 'Blade Barrier', 'Bones of the Earth', 'Chain Lightning', 'Circle of Death', 'Conjure Fey', 'Contingency', 'Create Homunculus', 'Create Undead', 'Disintegrate', "Drawmij's Instant Summons", 'Druid Grove', 'Eyebite', 'Find the Path', 'Flesh to Stone', 'Forbiddance', 'Globe of Invulnerability', 'Gravity Fissure', 'Guards and Wards', 'Harm', 'Heal', "Heroes' Feast", 'Investiture of Flame', 'Investiture of Ice', 'Investiture of Stone', 'Investiture of Wind', 'Magic Jar', 'Mass Suggestion', 'Mental Prison', 'Move Earth', 'Otherworldly Form', "Otiluke's Freezing Sphere", "Otto's Irresistible Dance", 'Planar Ally', 'Primordial Ward', 'Programmed Illusion', 'Psychic Crush', 'Scatter', 'Soul Cage', 'Summon Fiendish Spirit', 'Sunbeam', "Tenser's Transformation", 'Transport via Plants', 'True Seeing', 'Wall of Ice', 'Wall of Thorns', 'Wind Walk', 'Word of Recall'
    ]
    level_7 = [
        'Conjure Celestial', 'Conjure Hezrou (UA)', 'Create Magen', 'Crown of Stars', 'Delayed Blast Fireball', 'Divine Word', 'Etherealness', 'Finger of Death', 'Fire Storm', 'Forcecage', 'Mirage Arcane', "Mordenkainen's Magnificent Mansion", "Mordenkainen's Sword", 'Plane Shift', 'Power Word Pain', 'Prismatic Spray', 'Project Image', 'Regenerate', 'Resurrection', 'Reverse Gravity', 'Sequester', 'Simulacrum', 'Symbol', 'Teleport', 'Temple of the Gods', 'Tether Essence', 'Whirlwind'
    ]
    level_8 = [
        "Abi-Dalzim's Horrid Wilting", 'Animal Shapes', 'Antimagic Field', 'Antipathy/Sympathy', 'Clone', 'Control Weather', 'Dark Star', 'Demiplane', 'Dominate Monster', 'Earthquake', 'Feeblemind', 'Glibness', 'Holy Aura', 'Illusory Dragon', 'Incendiary Cloud', 'Maddening Darkness', 'Maze', 'Mighty Fortress', 'Mind Blank', 'Power Word Stun', 'Reality Break', 'Sunburst', 'Telepathy', 'Tsunami'
    ]
    level_9  = [
        'Astral Projection', 'Blade of Disaster', 'Foresight', 'Gate', 'Imprisonment', 'Invulnerability', 'Mass Heal', 'Mass Polymorph', 'Meteor Swarm', 'Power Word Heal', 'Power Word Kill', 'Prismatic Wall', 'Psychic Scream', 'Ravenous Void', 'Shapechange', 'Storm of Vengeance', 'Time Ravage', 'Time Stop', 'True Polymorph', 'True Resurrection', 'Weird', 'Wish'
    ]

elif SpellSource == 'Pathfinder 1':
    level_0 = [
        'Acid Splash', 'Arcane Mark', 'Bleed', 'Create Water', 'Dancing Lights', 'Daze', 'Detect Magic', 'Detect Poison', 'Disrupt Undead', 'Flare', 'Ghost Sound', 'Guidance', 'Haunted Fey Aspect', 'Know Direction', 'Light', 'Lullaby', 'Mage Hand', 'Mending', 'Message', 'Open/Close', 'Prestidigitation', 'Purify Food and Drink', 'Ray of Frost', 'Read Magic', 'Resistance', 'Stabilize', 'Summon Instrument', 'Touch of Fatigue', 'Virtue', 'Brand', 'Putrefy Food and Drink', 'Sift', 'Spark', 'Unwitting Ally'
    ]
    level_1 = [
        'Alarm', 'Animal Messenger', 'Animate Dead, Lesser', 'Animate Rope', 'Anticipate Peril', 'Bane', 'Bless', 'Bless Water', 'Bless Weapon', 'Burning Hands', 'Calm Animals', 'Cause Fear', 'Charm Animal', 'Charm Person', 'Chill Touch', 'Color Spray', 'Command', 'Comprehend Languages', 'Confusion, Lesser', 'Corrosive Touch', 'Cure Light Wounds', 'Curse Water', 'Deathwatch', 'Delay Poison', 'Detect Animals or Plants', 'Detect Chaos', 'Detect Evil', 'Detect Good', 'Detect Law', 'Detect Secret Doors', 'Detect Snares and Pits', 'Detect Undead', 'Diagnose Disease', 'Disguise Self', 'Divine Favor', 'Doom', 'Ear-Piercing Scream', 'Endure Elements', 'Enlarge Person', 'Entangle', 'Entropic Shield', 'Erase', 'Expeditious Retreat', 'Faerie Fire', 'Feather Fall', 'Floating Disk', 'Goodberry', 'Grease', 'Hide from Animals', 'Hide from Undead', 'Hideous Laughter', 'Hold Portal', 'Hypnotism', 'Identify', 'Inflict Light Wounds', 'Jump', 'Longstrider', 'Mage Armor', 'Magic Aura', 'Magic Fang', 'Magic Missile', 'Magic Mouth', 'Magic Stone', 'Magic Weapon', 'Mount', 'Obscure Object', 'Obscuring Mist', 'Pass without Trace', 'Produce Flame', 'Protection from Chaos', 'Protection from Evil', 'Protection from Good', 'Protection from Law', 'Ray of Enfeeblement', 'Reduce Person', 'Remove Fear', 'Resist Energy', 'Restoration, Lesser', 'Sanctuary', 'Shield', 'Shield of Faith', 'Shillelagh', 'Shocking Grasp', 'Silent Image', 'Sleep', 'Speak with Animals', 'Summon Monster I', "Summon Nature's Ally I", 'True Strike', 'Undetectable Alignment', 'Unseen Servant', 'Ventriloquism', 'Alter Winds', 'Ant Haul', 'Aspect of the Falcon', 'Beguiling Gift', "Bomber's Eye", 'Borrow Skill', 'Break', 'Bristle', 'Burst Bonds', 'Call Animal', 'Challenge Evil', 'Cloak of Shade', "Crafter's Curse", "Crafter's Fortune", 'Dancing Lantern', 'Detect Aberration', 'Expeditious Excavation', 'Feather Step', 'Flare Burst', 'Ghostbane Dirge', 'Glide', 'Grace', 'Gravity Bow', "Hero's Defiance", 'Honeyed Tongue', "Hunter's Howl", 'Hydraulic Push', 'Ill Omen', 'Innocence', 'Invigorate', 'Keen Senses', "Knight's Calling", 'Lead Blades', 'Mask Dweomer', 'Memory Lapse', 'Negate Aroma', 'Rally Point', 'Rejuvenate Eidolon, Lesser', 'Residual Tracking', 'Restful Sleep', 'Saving Finale', 'Sculpt Corpse', 'Share Language', 'Solid Note', 'Stone Fist', 'Stumble Gap', 'Timely Inspiration', 'Tireless Pursuit', 'Touch of Gracelessness', 'Touch of the Sea', 'Unfetter', 'Vanish', 'Veil of Positive Energy', 'Wrath', 'Abundant Ammunition', 'Adjuring Step', 'Adoration', 'Air Bubble', 'Bowstaff', 'Compel Hostility', 'Damp Powder', "Deadeye's Lore", 'Fabricate Bullets', 'Illusion of Calm', 'Jury-Rig', 'Liberating Command', 'Life Conduit', 'Litany of Sloth', 'Litany of Weakness', 'Lock Gaze', 'Longshot', 'Mirror Strike', 'Moment of Greatness', 'Negative Reaction', 'Peacebond', 'Reinforce Armaments', 'Returning Weapon', 'See Alignment', 'Shock Shield', 'Sun Metal', 'Tactical Acumen', 'Targeted Bomb Admixture', 'Unerring Weapon', 'Warding Weapon', 'Weaken Powder'
    ]
    level_2 = [
        'Acid Arrow', 'Aid', 'Align Weapon', 'Alter Self', 'Animal Trance', 'Arcane Lock', 'Augury', 'Barkskin', "Bear's Endurance", 'Blinding Ray', 'Blindness/Deafness', 'Blur', "Bull's Strength", 'Calm Emotions', "Cat's Grace", 'Chill Metal', 'Command Undead', 'Consecrate', 'Continual Flame', 'Cure Moderate Wounds', 'Darkness', 'Darkvision', 'Daze Monster', 'Death Knell', 'Desecrate', 'Detect Thoughts', 'Disfiguring Touch', "Eagle's Splendor", 'Enthrall', 'Excruciating Deformation', 'False Life', 'Find Traps', 'Fire Trap', 'Flame Blade', 'Flaming Sphere', 'Fog Cloud', "Fox's Cunning", 'Gentle Repose', 'Ghoul Touch', 'Glitterdust', 'Gust of Wind', 'Heat Metal', 'Heroism', 'Hold Animal', 'Hold Person', 'Hypnotic Pattern', 'Inflict Moderate Wounds', 'Invisibility', 'Knock', 'Levitate', 'Locate Object', 'Make Whole', 'Minor Image', 'Mirror Image', 'Misdirection', "Owl's Wisdom", 'Phantom Trap', 'Protection from Arrows', 'Protection from Energy', 'Pyrotechnics', 'Rage', 'Reduce Animal', 'Remove Paralysis', 'Rope Trick', 'Scare', 'Scorching Ray', 'See Invisibility', 'Shatter', 'Shield Other', 'Silence', 'Snare', 'Soften Earth and Stone', 'Sound Burst', 'Speak with Plants', 'Spectral Hand', 'Spider Climb', 'Spike Growth', 'Spiritual Weapon', 'Status', 'Suggestion', 'Summon Monster II', "Summon Nature's Ally II", 'Summon Swarm', 'Tongues', 'Touch of Idiocy', 'Tree Shape', 'Warp Wood', 'Web', 'Whispering Wind', 'Wind Wall', 'Wood Shape', 'Zone of Truth', 'Accelerate Poison', 'Alchemical Allocation', 'Allfood', 'Arrow Eruption', 'Aspect of the Bear', 'Aura of Greater Courage', 'Bestow Grace', 'Blessing of Courage and Life', 'Blood Biography', 'Bloodhound', 'Burning Gaze', 'Cacophonous Call', 'Campfire Wall', 'Castigate', 'Chameleon Stride', 'Confess', 'Corruption Resistance', 'Create Pit', 'Create Treasure Map', 'Dust of Twilight', 'Eagle Eye', 'Elemental Speech', 'Elemental Touch', 'Enter Image', 'Evolution Surge, Lesser', 'Feast of Ashes', 'Fester', 'Fire Breath', 'Fire of Entanglement', 'Flames of the Faithful', 'Follow Aura', 'Gallant Inspiration', 'Guiding Star', 'Hidden Speech', 'Hide Campsite', "Hunter's Eye", 'Instant Armor', 'Light Lance', 'Lockjaw', 'Natural Rhythm', "Oracle's Burden", "Paladin's Sacrifice", 'Perceive Cues', 'Pox Pustules', 'Protective Spirit', 'Righteous Vigor', 'Sacred Bond', 'Saddle Surge', 'Scent Trail', 'Slipstream', 'Stone Call', 'Summon Eidolon', 'Transmute Potion to Poison', 'Versatile Weapon', 'Vomit Swarm', 'Wake of Light', 'Weapon of Awe', 'Ablative Barrier', 'Animal Aspect', 'Ant Haul, Communal', 'Bestow Weapon Proficiency', 'Blistering Invective', 'Brow Gasher', 'Bullet Shield', 'Certain Grip', 'Destabilize Powder', 'Discovery Torch', 'Divine Arrow', 'Effortless Armor', 'Endure Elements, Communal', 'Fiery Shuriken', 'Forest Friend', 'Frost Fall', 'Instrument of Agony', 'Kinetic Reverberation', 'Litany of Defense', 'Litany of Eloquence', 'Litany of Entanglement', 'Litany of Righteousness', 'Litany of Warding', 'Locate Weakness', 'Magic Siege Engine', 'Mask Dweomer, Communal', 'Mount, Communal', 'Pilfering Hand', 'Protection from Chaos, Communal', 'Protection from Evil, Communal', 'Protection from Good, Communal', 'Protection from Law, Communal', 'Qualm', 'Recoil Fire', 'Reinforce Armaments, Communal', 'Reloading Hands', 'Returning Weapon, Communal', 'Ricochet Shot', 'Shadow Bomb Admixture', 'Share Language, Communal', 'Spontaneous Immolation', 'Stabilize Powder', 'Telekinetic Assembly', 'Thunder Fire', 'Touch Injection', 'Twisted Space', 'Wilderness Soldiers', 'Frostbite', 'Murderous Command', 'Persuasive Goad', 'Pick Your Poison', 'Polypurpose Panacea', 'Ray of Sickening', 'Remove Sickness'
    ]
    level_3 = [
        'Animate Dead', 'Arcane Sight', 'Beast Shape I', 'Bestow Curse', 'Blink', 'Burst of Nettles', 'Call Lightning', 'Channel Vigor', 'Charm Monster', 'Clairaudience/Clairvoyance', 'Command Plants', 'Confusion', 'Contagion', 'Create Food and Water', 'Crushing Despair', 'Cure Serious Wounds', 'Daylight', 'Deeper Darkness', 'Deep Slumber', 'Diminish Plants', 'Discern Lies', 'Dispel Magic', 'Displacement', 'Dominate Animal', 'Explosive Runes', 'Fear', 'Fireball', 'Flame Arrow', 'Fly', 'Gaseous Form', 'Geas, Lesser', 'Glibness', 'Glyph of Warding', 'Good Hope', 'Halt Undead', 'Haste', 'Heal Mount', 'Helping Hand', 'Illusory Script', 'Inflict Serious Wounds', 'Invisibility Purge', 'Invisibility Sphere', 'Keen Edge', 'Lightning Bolt', 'Magic Circle against Chaos', 'Magic Circle against Evil', 'Magic Circle against Good', 'Magic Circle against Law', 'Magic Fang, Greater', 'Magic Vestment', 'Magic Weapon, Greater', 'Major Image', 'Meld into Stone', 'Neutralize Poison', 'Nondetection', 'Phantom Steed', 'Plant Growth', 'Poison', 'Prayer', 'Quench', 'Ray of Exhaustion', 'Remove Blindness/Deafness', 'Remove Curse', 'Remove Disease', 'Repel Vermin', 'Scrying', 'Sculpt Sound', 'Searing Light', 'Secret Page', 'Sepia Snake Sigil', 'Shrink Item', 'Sleet Storm', 'Slow', 'Speak with Dead', 'Stinking Cloud', 'Stone Shape', 'Summon Monster III', "Summon Nature's Ally III", 'Tiny Hut', 'Vampiric touch', 'Water Breathing', 'Water Walk', 'Absorbing Touch', 'Amplify Elixir', 'Aqueous Orb', 'Arcane Concordance', 'Aspect of the Stag', 'Banish Seeming', 'Bloody Claws', 'Borrow Fortune', 'Cast Out', 'Cloak of Winds', 'Coordinated Effort', 'Cup of Dust', 'Defile Armor', 'Devolution', 'Divine Transfer', 'Draconic Reservoir', 'Elemental Aura', 'Evolution Surge', 'Feather Step, Mass', 'Fire of Judgment', 'Ghostbane Dirge, Mass', 'Holy Whisper', 'Hydraulic Torrent', 'Instant Enemy', 'Invigorate, Mass', "Jester's Jaunt", 'Life Bubble', 'Lily Pad Stride', 'Marks Of Forbiddance', 'Nap Stack', "Nature's Exile", 'Pain Strike', 'Purging Finale', 'Rejuvenate Eidolon', 'Retribution', 'Reviving Finale', 'Sanctify Armor', 'Screech', 'Seek Thoughts', 'Share Senses', 'Shifting Sand', 'Spiked Pit', 'Strong Jaw', 'Thorn Body', 'Thundering Drums', 'Tireless Pursuers', 'Twilight Knife', 'Venomous Bolt', 'Ward the Faithful', 'Wrathful Mantle', 'Absorb Toxicity', 'Animal Aspect, Greater', 'Burst of Speed', 'Chain of Perdition', 'Companion Mind Link', 'Darkvision, Communal', 'Daybreak Arrow', 'Deadly Juggernaut', 'Delay Poison, Communal', 'Flash Fire', 'Healing Thief', 'Hostile Levitation', 'Life Conduit, Improved', 'Lightning Lash Bomb Admixture', 'Litany of Escape', 'Litany of Sight', 'Named Bullet', 'Obsidian Flow', 'Pellet Blast', 'Phantom Chariot', 'Phantom Driver', 'Phantom Steed, Communal', 'Protection from Arrows, Communal', 'Protection from Energy, Communal', 'Pup Shape', 'Resinous Skin', 'Resist Energy, Communal', 'Spider Climb, Communal', 'Tongues, Communal', 'Frigid Touch', 'Ghostly Disguise', 'Ghoul Hunger', 'Id Insinuation I', 'Mad Hallucination', 'Piercing Shriek', 'Secret Speech', 'Share Memory', 'Symbol of Mirroring', 'Touch of Chaos', 'Touch of Evil', 'Touch of Good', 'Touch of Law', 'Touch of Madness', 'Unnatural Lust', 'Unshakable Chill', 'Water of Maddening'
    ]
    level_4 = [
        'Air Walk', 'Animal Growth', 'Antiplant Shell', 'Arcane Eye', 'Beast Shape II', 'Black Tentacles', 'Blight', 'Break Enchantment', 'Chaos Hammer', 'Commune with Nature', 'Control Summoned Creature', 'Control Water', 'Cure Critical Wounds', 'Death Ward', 'Detect Scrying', 'Dimensional Anchor', 'Dimension Door', 'Dismissal', 'Dispel Chaos', 'Dispel Evil', 'Divination', 'Divine Power', 'Dominate Person', 'Elemental Body I', 'Enervation', 'Enlarge Person, Mass', 'Fire Shield', 'Flame Strike', 'Freedom of Movement', 'Giant Vermin', 'Globe of Invulnerability, Lesser', 'Hallucinatory Terrain', 'Hold Monster', 'Holy Smite', 'Holy Sword', 'Ice Storm', 'Illusory Wall', 'Imbue with Spell Ability', 'Inflict Critical Wounds', 'Invisibility, Greater', 'Legend Lore', 'Locate Creature', 'Mark of Justice', 'Minor Creation', 'Mnemonic Enhancer', 'Modify Memory', "Order's Wrath", 'Phantasmal Killer', 'Planar Ally, Lesser', 'Rainbow Pattern', 'Reduce Person, Mass', 'Reincarnate', 'Resilient Sphere', 'Restoration', 'Rusting Grasp', 'Secure Shelter', 'Sending', 'Shadow Conjuration', 'Shout', 'Solid Fog', 'Spell Immunity', 'Spike Stones', 'Stoneskin', 'Summon Monster IV', "Summon Nature's Ally IV", 'Tree Stride', 'Unholy Blight', 'Wall of Fire', 'Wall of Ice', 'Zone of Silence', 'Acid Pit', 'Aspect of the Wolf', 'Ball Lightning', 'Blaze of Glory', 'Blessing of Fervor', 'Blessing of the Salamander', 'Bow Spirit', 'Brand, Greater', 'Calcific Touch', "Coward's Lament", 'Denounce', 'Detonate', 'Discordant Blast', "Dragon's Breath", 'Evolution Surge, Greater', 'Firefall', 'Fire of Vengeance', 'Fluid Form', 'Forced Repentance', 'Geyser', 'Grove of Respite', 'Heroic Finale', "King's Castle", 'Moonstruck', 'Oath of Peace', 'Planar Adaptation', 'Purified Calling', 'Rebuke', 'Resounding Blow', 'Rest Eternal', 'River of Wind', 'Sacrificial Oath', 'Shadow Projection', 'Shared Wrath', 'Sleepwalk', 'Spiritual Ally', 'Spite', 'Stay the Hand', 'Threefold Aspect', 'Transmogrify', 'Treasure Stitching', 'True Form', 'Universal Formula', 'Wandering Star Motes', 'Air Walk, Communal', 'Debilitating Portent', 'Find Quarry', 'Hostile Juxtaposition', 'Judgment Light', 'Litany of Madness', 'Litany of Thunder', 'Litany of Vengeance', 'Magic Siege Engine, Greater', 'Mutagenic Touch', 'Named Bullet, Greater', 'Nondetection, Communal', 'Shocking Image', 'Stoneskin, Communal', 'Summoner Conduit', 'Telekinetic Charge', 'Terrain Bond', 'Viper Bomb Admixture', 'Water Walk, Communal', 'Wreath of Blades', 'Leashed Shackles', 'Fire Trail', 'Force Punch', 'Geas', 'Id Insinuation II', "Lover's Vengeance", 'Overwhelming Grief', 'Reckless Infatuation', 'Shadow Evocation, Lesser', 'Terrible Remorse', 'Thorny Entanglement', 'Witness'
    ]
    level_5 = [
        'Atonement', 'Awaken', 'Baleful Polymorph', 'Beast Shape III', 'Breath of Life', 'Call Lightning Storm', 'Charm Animal, Mass', 'Cloudkill', 'Command, Greater', 'Commune', 'Cone of Cold', 'Contact Other Plane', 'Control Winds', 'Cure Light Wounds, Mass', 'Dispel Good', 'Dispel Law', 'Dispel Magic, Greater', 'Disrupting Weapon', 'Dream', 'Elemental Body II', 'Fabricate', 'False Vision', 'Feeblemind', 'Hallow', 'Heroism, Greater', 'Inflict Light Wounds, Mass', 'Insect Plague', 'Interposing Hand', "Mage's Faithful Hound", "Mage's Private Sanctum", 'Magic Jar', 'Major Creation', 'Mind Fog', 'Mirage Arcana', 'Mislead', 'Nightmare', 'Overland Flight', 'Passwall', 'Permanency', 'Persistent Image', 'Planar Binding, Lesser', 'Plane Shift', 'Plant Shape I', 'Polymorph', 'Prying Eyes', 'Raise Dead', 'Righteous Might', 'Secret Chest', 'Seeming', 'Shadow Evocation', 'Shadow Walk', 'Slay Living', 'Song of Discord', 'Spell Resistance', 'Suggestion, Mass', 'Summon Monster V', "Summon Nature's Ally V", 'Symbol of Pain', 'Symbol of Sleep', 'Telekinesis', 'Telepathic Bond', 'Teleport', 'Transmute Mud to Rock', 'Transmute Rock to Mud', 'True Seeing', 'Unhallow', 'Wall of Force', 'Wall of Stone', 'Wall of Thorns', 'Waves of Fatigue', "Bard's Escape", 'Cacophonous Call, Mass', 'Castigate, Mass', 'Cleanse', 'Cloak of Dreams', 'Deafening Song Bolt', 'Delayed Consumption', 'Elude Time', 'Fire Snake', 'Foe to Friend', 'Frozen Note', 'Hungry Pit', 'Pain Strike, Mass', 'Phantasmal Web', 'Pillar of Life', 'Rejuvenate Eidolon, Greater', 'Resurgent Transformation', 'Snake Staff', 'Stunning Finale', 'Suffocation', 'Unwilling Shield', 'Dust Form', 'Energy Siege Shot', 'Languid Bomb Admixture', 'Life Conduit, Greater', 'Spell Immunity, Communal', 'Symbol of Striking', 'Tar Pool', 'Id Insinuation III', 'Sands of Time', 'Shadow Step', 'Sonic Thrust', 'Symbol of Slowing'
    ]
    level_6 = [
        'Acid Fog', 'Analyze Dweomer', 'Animate Objects', 'Antilife Shell', 'Antimagic Field', 'Banishment', "Bear's Endurance, Mass", 'Beast Shape IV', 'Blade Barrier', "Bull's Strength, Mass", "Cat's Grace, Mass", 'Chain Lightning', 'Charm Monster, Mass', 'Circle of Death', 'Cold Ice Strike', 'Contingency', 'Create Undead', 'Cure Moderate Wounds, Mass', 'Disintegrate', "Eagle's Splendor, Mass", 'Elemental Body III', 'Eyebite', 'Find the Path', 'Fire Seeds', 'Flesh to Stone', 'Forbiddance', 'Forceful Hand', 'Form of the Dragon I', "Fox's Cunning, Mass", 'Freezing Sphere', 'Geas/Quest', 'Globe of Invulnerability', 'Glyph of Warding, Greater', 'Guards and Wards', 'Harm', 'Heal', "Heroes' Feast", 'Inflict Moderate Wounds, Mass', 'Ironwood', 'Irresistible Dance', 'Liveoak', "Mage's Lucubration", 'Move Earth', "Owl's Wisdom, Mass", 'Permanent Image', 'Planar Ally', 'Planar Binding', 'Plant Shape II', 'Programmed Image', 'Project Image', 'Repel Wood', 'Repulsion', 'Scrying, Greater', 'Shout, Greater', 'Spellstaff', 'Stone Tell', 'Stone to Flesh', 'Summon Monster VI', "Summon Nature's Ally VI", 'Symbol of Fear', 'Symbol of Persuasion', 'Sympathetic Vibration', 'Transformation', 'Transport via Plants', 'Undeath to Death', 'Veil', 'Wall of Iron', 'Wind Walk', 'Word of Recall', 'Brilliant Inspiration', 'Contagious Flame', 'Deadly Finale', 'Enemy Hammer', 'Euphoric Tranquility', 'Fester, Mass', "Fool's Forbiddance", 'Getaway', 'Pied Piping', 'Planar Adaptation, Mass', 'Sirocco', 'Swarm Skin', 'Twin Form', 'Caging Bomb Admixture', 'Energy Siege Shot, Greater', 'Hostile Juxtaposition, Greater', 'Walk through Space', 'Plague Storm', 'Vengeful Outrage', 'Icy Prison', 'Id Insinuation IV', 'Lightning Arc', 'Possess Object', 'Rapid Repair', 'Soothe Construct', 'Unbreakable Construct'
    ]
    level_7 = [
        'Animate Plants', 'Arcane Sight, Greater', 'Blasphemy', 'Changestaff', 'Control Construct', 'Control Undead', 'Control Weather', 'Creeping Doom', 'Cure Serious Wounds, Mass', 'Delayed Blast Fireball', 'Destruction', 'Dictum', 'Elemental Body IV', 'Ethereal Jaunt', 'Finger of Death', 'Fire Storm', 'Forcecage', 'Form of the Dragon II', 'Giant Form I', 'Grasping Hand', 'Hold Person, Mass', 'Holy Word', 'Inflict Serious Wounds, Mass', 'Insanity', 'Instant Summons', 'Invisibility, Mass', 'Limited Wish', "Mage's Magnificent Mansion", "Mage's Sword", 'Phase Door', 'Plant Shape III', 'Polymorph, Greater', 'Power Word Blind', 'Prismatic Spray', 'Refuge', 'Regenerate', 'Restoration, Greater', 'Resurrection', 'Reverse Gravity', 'Sequester', 'Shadow Conjuration, Greater', 'Simulacrum', 'Spell Turning', 'Statue', 'Summon Monster VII', "Summon Nature's Ally VII", 'Sunbeam', 'Symbol of Stunning', 'Symbol of Weakness', 'Teleport, Greater', 'Teleport Object', 'Transmute Metal to Wood', 'Vision', 'Waves of Exhaustion', 'Word of Chaos', 'Deflection', 'Expend', 'Firebrand', 'Fly, Mass', 'Phantasmal Revenge', 'Rampart', 'Vortex', 'Arcane Cannon', 'Jolting Portent', 'Siege of Trees', 'Terraform'
    ]
    level_8 = [
        'Animal Shapes', 'Antipathy', 'Bestow Curse, Greater', 'Binding', 'Clenched Fist', 'Cloak of Chaos', 'Clone', 'Control Plants', 'Create Greater Undead', 'Cure Critical Wounds, Mass', 'Demand', 'Dimensional Lock', 'Discern Location', 'Earthquake', 'Form of the Dragon III', 'Giant Form II', 'Holy Aura', 'Horrid Wilting', 'Incendiary Cloud', 'Inflict Critical Wounds, Mass', 'Iron Body', 'Maze', 'Mind Blank', 'Moment of Prescience', 'Planar Ally, Greater', 'Planar Binding, Greater', 'Polar Ray', 'Polymorph Any Object', 'Power Word Stun', 'Prismatic Wall', 'Protection from Spells', 'Prying Eyes, Greater', 'Repel Metal or Stone', 'Scintillating Pattern', 'Screen', 'Shadow Evocation, Greater', 'Shield of Law', 'Spell Immunity, Greater', 'Summon Monster VIII', "Summon Nature's Ally VIII", 'Sunburst', 'Symbol of Death', 'Symbol of Insanity', 'Sympathy', 'Telekinetic Sphere', 'Temporal Stasis', 'Trap the Soul', 'Unholy Aura', 'Whirlwind', 'Divine Vessel', 'Seamantle', 'Stormbolts', 'Wall of Lava', 'Frightful Aspect'
    ]
    level_9 = [
        'Astral Projection', 'Crushing Hand', 'Cursed Earth', 'Dominate Monster', 'Elemental Swarm', 'Energy Drain', 'Etherealness', 'Foresight', 'Freedom', 'Gate', 'Heal, Mass', 'Hold Monster, Mass', 'Implosion', 'Imprisonment', "Mage's Disjunction", 'Meteor Swarm', 'Miracle', 'Power Word Kill', 'Prismatic Sphere', 'Shades', 'Shambler', 'Shapechange', 'Soul Bind', 'Storm of Vengeance', 'Summon Monster IX', "Summon Nature's Ally IX", 'Teleportation Circle', 'Time Stop', 'True Resurrection', 'Wail of the Banshee', 'Weird', 'Wish', 'Clashing Rocks', 'Fiery Body', 'Suffocation, Mass', 'Tsunami', 'Wall of Suppression', 'Winds of Vengeance', 'World Wave', 'Heroic Invocation', 'Mind Blank, Communal', 'Siege of Trees, Greater', 'Spell Immunity, Greater Communal', 'Icy Prison, Mass', 'Overwhelming Presence', 'Polar Midnight', 'Symbol of Scrying', 'Symbol of Strife', 'Symbol of Vulnerability'
    ]
level_likelihood = {
    0: 0.2597402597402597,
    1: 0.21038961038961038,
    2: 0.16623376623376623,
    3: 0.12727272727272726,
    4: 0.09350649350649351,
    5: 0.06493506493506493,
    6: 0.04155844155844156,
    7: 0.023376623376623377,
    8: 0.01038961038961039,
    9: 0.0025974025974025974,
}
odd_price = {
    'Magic Mouth': 1.0666666666666667,
    'Arcane Lock': 1.1666666666666667,
    'Continual Flame': 1.3333333333333333,
    'Phantom Trap': 1.3333333333333333,
    'Illusory Script': 1.1333333333333333,
    'Nondetection': 1.1333333333333333,
    'Sepia Snake Sigil': 2.3333333333333335,
    'Fire Trap': 1.0357142857142858,
    'Mnemonic Enhancer': 1.0714285714285714,
    'Stoneskin': 1.3571428571428572,
    'Animate Dead': 1.5,
    'False Vision': 1.2222222222222223,
    'Symbol of Pain': 1.8888888888888888,
    'Symbol of Sleep': 1.8888888888888888,
    'Create Undead': 1.0294117647058822,
    'Legend Lore': 1.1176470588235294,
    'True Seeing': 1.1176470588235294,
    'Circle of Death': 1.2647058823529411,
    'Undeath to Death': 1.2647058823529411,
    'Symbol of Fear': 1.5588235294117647,
    'Symbol of Persuasion': 3.911764705882353,
    'Project Image': 1.0021978021978022,
    'Vision': 1.10989010989011,
    'Forcecage': 1.2197802197802199,
    'Instant Summons': 1.4395604395604396,
    'Limited Wish': 1.6593406593406594,
    'Symbol of Stunning': 3.4175824175824174,
    'Symbol of Weakness': 3.4175824175824174,
    'Simulacrum': 3.857142857142857,
    'Create Greater Undead': 1.05,
    'Protection from Spells': 1.1666666666666667,
    'Sympathy': 1.5,
    'Symbol of Death': 2.6666666666666665,
    'Symbol of Insanity': 2.6666666666666665,
    'Temporal Stasis': 2.6666666666666665,
    'Trap the Soul': 7.666666666666667,
    'Refuge': 1.130718954248366,
    'Astral Projection': 1.261437908496732,
    'Teleportation Circle': 1.261437908496732,
    'Wish': 7.5359477124183005
}
die_values = {
    'Heavy Axe': [10, 12],
    'Light Axe': [8, 10],
    'Heavy Blade': [8, 10, 12],
    'Light Blade': [6, 8],
    'Close': [4, 6, 8],
    'Double': [4, 6, 8, 10],
    'Flail': [4, 6, 8],
    'Hammer': [4, 6, 8],
    'Monk': [4, 6, 8, 10, 12],
    'Polearm': [6, 8, 10],
    'Spear': [6, 8],
    'Bows': [8, 10],
    'Crossbow': [6, 8],
    'Thrown': [4, 6],
}
possible_melee = {
    'Heavy Axe': [
        'bardiche', 'bardiche', 'battleaxe', 'battleaxe', 'boarding axe',
        'boarding axe', 'dwarven waraxe', 'greataxe', 'greataxe', 'heavy pick',
        'orc double axe', 'tongi'
    ],
    'Light Axe': [
        'boarding axe', 'boarding axe', 'butchering cleaver', 'gandasa',
        'handaxe', 'handaxe', 'hooked axe', 'hooked axe', 'knuckle axe',
        'knuckle axe', 'kumade', 'light pick', 'mattock', 'throwing axe',
        'throwing axe', 'kaiser blade', 'ankus'
    ],
    'Heavy Blade': [
        'dueling sword', 'dueling sword', 'bastard sword', 'bastard sword',
        'broadsword', 'broadsword', 'elven curved blade', 'elven curved blade',
        'estoc', 'estoc', 'falcata', 'falchion', 'falchion', 'flambard',
        'greatsword', 'greatsword', 'great macuahuitl', 'katana', 'katana',
        'khopesh', 'longsword', 'longsword', 'macuahuitl',
        'nine-ring broadsword', 'nodachi', 'nodachi', 'scimitar',
        'scimitar', 'scythe', 'scythe', 'seven-branched sword', 'shotel',
        'temple sword', 'terbutje', 'two-bladed sword', 'two-bladed sword'
    ],
    'Light Blade': [
        'bayonet', 'butterfly knife', 'butterfly knife', 'chakram', 'dagger',
        'chicken saber', 'dagger', 'deer horn knife', 'drow razor',
        'dueling dagger', 'dueling dagger', 'gladius', 'gladius',
        'hunga munga', 'kama', 'kama', 'katar', 'kerambit', 'kerambit', 'kukri',
        'kukri', 'machete', 'machete', 'manople', 'pata', 'quadrens', 'rapier',
        'rapier', 'sawtooth sabre', 'scizore', 'shortsword', 'shortsword',
        'sica', 'sickle', 'sickle', 'spiral rapier', 'starknife',
        'swordbreaker dagger', 'swordbreaker dagger', 'sword cane',
        'sword cane', 'tanto', 'tanto', 'wakizashi', 'war razor', 'waveblade'
    ],
    'Close': [
        'bayonet', 'brass knuckles', 'brass knuckles', 'cestus', 'cestus',
        'emei piercer', 'fighting fan', 'gauntlet', 'gauntlet', 'katar',
        'klar', 'punching dagger', 'punching dagger', 'rope gauntlet', 'sap',
        'scizore', 'spiked gauntlet', 'tekko-kagi', 'tonfa',  'tonfa',
        'tri-bladed katar', 'stake', 'wushu dart'
    ],
    'Double': [
        'bo staff', 'bo staff', 'Woarding gaff', 'chain-hammer', 'chain spear',
        'dire flail', 'double walking stick katana', 'double-chained kama',
        'dwarven urgrosh', 'gnome battle ladder', 'gnome hooked hammer',
        'kusarigama', 'monk\'s spade', 'monk\'s spade', 'orc double axe',
        'orc double axe', 'quarterstaff', 'quarterstaff', 'taiaha',
        'two-bladed sword', 'weighted spear', 'weighted spear'
    ],
    'Flail': [
        'battle poi', 'bladed scarf', 'Cat-o\'-nine-tails', 'chain spear',
        'dire flail', 'double chained kama', 'dwarven dorn-dergar', 'flail',
        'flying talon', 'gnome pincher', 'halfling rope-shot', 'heavy flail',
        'kusarigama', 'kyoketsu shoge', 'meteor hammer', 'morningstar',
        'nine-section whip', 'nunchaku', 'sansetsukon', 'scorpion whip',
        'spiked chain', 'urumi', 'whip'
    ],
    'Hammer': [
        'aklys', 'battle aspergillum', 'Chain-hammer', 'club', 'club',
        'gnome piston maul', 'greatclub', 'greatclub', 'heavy mace',
        'heavy mace', 'kanabo', 'kanabo', 'lantern staff',
        'light hammer', 'light hammer', 'light mace', 'light mace',
        'mere club', 'planson', 'taiaha', 'tetsubo', 'tetsubo', 'wahaika',
        'warhammer', 'warhammer'
    ],
    'Monk': [
        'bo staff', 'bo staff', 'brass knuckles', 'butterfly sword', 'cestus',
        'dan bong', 'deer horn knife', 'double chained kama',
        'double chicken saber', 'emei piercer', 'fighting fan', 'hanbo',
        'jutte', 'kama', 'kusarigama', 'kyoketsu shoge', 'lungshuan tamo',
        'monk\'s spade', 'monk\'s spade', 'nine-ring broadsword',
        'nine-section whip', 'nunchaku', 'quarterstaff', 'quarterstaff',
        'rope dart', 'sai', 'sanpkhang', 'sansetsukon', 'seven-branched sword',
        'shang gou', 'shuriken', 'siangham', 'temple sword', 'tiger fork',
        'tonfa', 'tri-point double-edged sword', 'urumi', 'wushu dart'
    ],
    'Polearm': [
        'bardiche', 'bardiche', 'bec de corbin', 'bill', 'Boarding gaff',
        'crook', 'crook', 'fauchard', 'glaive', 'glaive', 'glaive-guisarme',
        'glaive-guisarme', 'gnome ripsaw glaive', 'guisarme', 'guisarme',
        'halberd', 'halberd', 'hooked lance', 'lucerne hammer', 'mancatcher',
        'monk\'s spade', 'naginata', 'naginata', 'nodachi', 'ranseur',
        'rhomphaia', 'tepoztopilli', 'tiger fork'
    ],
    'Spear': [
        'amentum', 'boar spear', 'chain spear', 'elven branched spear',
        'javelin', 'javelin', 'harpoon', 'lance', 'lance', 'longspear',
        'longspear', 'orc skull ram', 'pilum', 'planson', 'shortspear',
        'shortspear', 'sibat', 'spear', 'spear', 'stormshaft javelin',
        'tiger fork', 'trident', 'trident', 'weighted spear', 'weighted spear'
    ],
}
possible_ranged = {
    'Bows': [
        'composite longbow', 'composite shortbow', 'composite hornbow',
        'longbow', 'shortbow', 'hornbow'
    ],
    'Crossbow': [
        'double crossbow', 'hand crossbow', 'hand crossbow', 'heavy crossbow',
        'heavy crossbow', 'launching crossbow', 'light crossbow',
        'light crossbow', 'heavy repeating crossbow',
        'light repeating crossbow'
    ],
    'Thrown': [
        'aklys', 'amentum', 'atlatl', 'blowgun', 'bolas', 'bolas', 'boomerang',
        'boomerang', 'brutal bolas', 'chain-hammer', 'chakram', 'chakram',
        'club', 'dagger', 'dagger', 'dart', 'dart', 'deer horn knife',
        'dueling dagger', 'flask thrower', 'halfling sling staff', 'harpoon',
        'javelin', 'javelin', 'kestros', 'light hammer', 'pilum',
        'poisoned sand tube', 'rope dart', 'shortspear', 'shortspear',
        'shuriken', 'shuriken', 'sibat', 'sling', 'sling', 'sling glove',
        'sling glove', 'spear', 'spear', 'starknife', 'stormshaft javelin',
        'throwing axe', 'throwing axe', 'trident', 'trident',
        'tube arrow shooter', 'wushu dart'
    ],
}
possible_guns = {
    'Pistol': [
        'derringer', 'flintlock', 'revolver', 'hand cannon', 'handgun',
        'handgun', 'machine pistol', 'machine pistol', 'matchlock', 'pistol',
        'pistol', 'pistol', 'revolver', 'wheellock'
    ],
    'Rifle': [
        'assault rifle', 'carbine', 'carbine', 'rifle', 'rifle', 'rifle',
        'scoped rifle', 'submachine gun'
    ],
    'Sniper': [
        'long gun', 'scoped sniper', 'scoped sniper', 'sniper', 'sniper',
        'sniper'
    ],
    'Shotgun': [
        'blunderbuss', 'blunderbuss', 'pump shotgun', 'shotgun', 'shotgun',
        'shotgun'
    ],
}
weapon_cost_and_weight = {
    'Heavy Axe': [19, 1.6],
    'Light Axe': [11, .9],
    'Heavy Blade': [12, 1.3],
    'Light Blade': [10, 1],
    'Close': [5, .5],
    'Double': [20, 1.1],
    'Flail': [14, 1.2],
    'Hammer': [22, 1.7],
    'Monk': [10, 1],
    'Polearm': [9, .8],
    'Spear': [13, 1.2],
    'Bows': [17, .4],
    'Crossbow': [29, 1.1],
    'Thrown': [7, .7],
}
Potion_Name_Potential = [
    'Potion of ', 'Potion of ', 'Potion of ', 'Potion of ', 'Potion of ',
    'Potion of ', 'Potion of ', 'Potion of ', 'Oil of ', 'Tincture of ',
    'Solution of ', 'Philter of ', 'Draught of ', 'Elixir of ', 'Draft of ',
    'Brew of '
]
Scroll_Name_Potential = [
    'Scroll of ', 'Scroll of ', 'Scroll of ', 'Tome of ', 'Spellbook of ',
    'Book of '
]
Wand_Name_Potential = [
    'Rod of ', 'Rod of ', 'Stave of ', 'Scepter of ', 'Staff of ', 'Staff of ',
    'Wand of ', 'Wand of '
]

Food_f1 = [
    'Acai Berry', 'Apple', 'Apricot', 'Banana', 'Blackberry', 'Blueberry',
    'Boysenberry', 'Crab Apple', 'Cherry', 'Cloudberry', 'Coconut', 'Cranberry',
    'Elderberry', 'Grape', 'Grapefruit', 'Guava', 'Huckleberry',
    'Juniper berry', 'Kiwi', 'Lemon', 'Lime', 'Mango', 'Melon', 'Cantaloupe',
    'Honeydew', 'Watermelon', 'Nectarine', 'Orange', 'Blood Orange',
    'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Plum',
    'Pineapple', 'Pineberry', 'Pomegranate', 'Raspberry', 'Star Apple',
    'Strawberry'
]
Food_f2 = ['Jam', 'Current', 'Spread', 'Puree', 'Sauce', 'Slices']
Food_v1 = [
    '', '', '', '', 'Steamed ', 'Cooked ', 'Baked ', 'Mashed ', 'Pickled ',
    'Chopped ', 'Roasted ', 'Toasted ', 'Sliced ', 'Fried ', 'Boiled ',
    'Uncooked '
]
Food_v2 = [
    'Artichoke', 'Eggplant', 'Avocado', 'Asparagus', 'Legumes',
    'Alfalfa Sprouts', 'Beans', 'Peas', 'Broccoli', 'Brussels Sprouts',
    'Cabbage', 'Cauliflower', 'Celery', 'Spinach', 'Lettuce', 'Arugula',
    'Chives', 'Leek', 'Onion', 'Scallion', 'Rhubarb', 'Beet', 'Carrot',
    'Parsnip', 'Turnip', 'Radish', 'Horseradish', 'Sweetcorn', 'Zucchini',
    'Cucumber', 'Squash', 'Pumpkin', 'Potato', 'Sweet Potato', 'Yam',
    'Water Chestnut', 'Watercress'
]
Food_m1 = [
    'Aged ', 'Baked ', 'Barbecued ', 'Braised ', 'Dried ', 'Fried ', 'Ground ',
    'Marinated ', 'Pickled ', 'Poached ', 'Roasted ', 'Salt-cured ', 'Smoked ',
    'Stewed ', 'Corned ', 'Sliced '
]
Food_m2 = [
    'Bear', 'Beef', 'Buffalo', 'Bison', 'Caribou', 'Goat', 'Ham', 'Horse',
    'Kangaroo', 'Lamb', 'Moose', 'Mutton', 'Pork', 'Bacon', 'Rabbit', 'Tripe',
    'Veal', 'Venison', 'Chicken', 'Duck', 'Emu', 'Goose', 'Grouse', 'Liver',
    'Ostrich', 'Pheasant', 'Quail', 'Squab', 'Turkey', 'Abalone', 'Anchovy',
    'Bass', 'Calamari', 'Carp', 'Catfish', 'Cod', 'Crab', 'Crayfish', 'Dolphin',
    'Eel', 'Flounder', 'Grouper', 'Haddock', 'Halibut', 'Herring', 'Kingfish',
    'Lobster', 'Mackerel', 'Mahi', 'Marlin', 'Milkfish', 'Mussel', 'Octopus',
    'Oyster', 'Perch', 'Pike', 'Pollock', 'Salmon', 'Sardine', 'Scallop',
    'Shark', 'Shrimp', 'Swai', 'Swordfish', 'Tilapia', 'Trout', 'Tuna',
    'Walleye', 'Whale'
]
Food_m3 = [
    '', '', '', '', 'Burger', 'Charcuterie', 'Chop', 'Cured', 'Cutlet', 'Dum',
    'Fillet', 'Kebab', 'Meatball', 'Meatloaf', 'Offal', 'Sausage', 'Steak',
    'Tandoor', 'Tartare'
]
Food_g1 = ['', '', '', '', 'Buttered ', 'Spiced ', 'Cheesy ']
Food_g2 = ['Barley', 'Corn', 'Oat', 'Rice', 'Wheat', 'Rye', 'Maize']
Food_g3 = [
    'Bun', 'Roll', 'Bread', 'Cake', 'Patty', 'Muffin', 'Toast', 'Biscuit',
    'Loaf'
]
Food_spice = [
    'Basil', 'Ginger', 'Caraway', 'Cilantro', 'Chamomile', 'Dill', 'Fennel',
    'Lavender', 'Lemon Grass', 'Marjoram', 'Oregano', 'Parsley', 'Rosemary',
    'Sage', 'Thyme', 'Garlic', 'Chili Pepper', 'Jalapeno', 'Habanero',
    'Paprika', 'Cayenne Pepper'
]
Drink_d1 = [
    'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water',
    'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Acai Juice',
    'Apple Juice', 'Apricot Juice', 'Banana Juice', 'Blackberry Juice',
    'Blueberry Juice', 'Boysenberry Juice', 'Crab Apples Juice', 'Cherry Juice',
    'Cloudberry Juice', 'Coconut Juice', 'Cranberry Juice', 'Grape Juice',
    'Grapefruit Juice', 'Guava Juice', 'Honeyberry Juice', 'Huckleberry Juice',
    'Kiwi Juice', 'Lemon Juice', 'Lime Juice', 'Mango Juice', 'Melon Juice',
    'Cantaloupe Juice', 'Honeydew Juice', 'Watermelon Juice', 'Nectarine Juice',
    'Orange Juice', 'Papaya Juice', 'Peach Juice', 'Pear Juice',
    'Pineapple Juice', 'Pomegranate Juice', 'Raspberry Juice',
    'Strawberry Juice', 'Acai Contentrate', 'Apple Contentrate',
    'Apricot Contentrate', 'Banana Contentrate', 'Blackberry Contentrate',
    'Blueberry Contentrate', 'Boysenberry Contentrate',
    'Crab Apples Contentrate', 'Cherry Contentrate', 'Cloudberry Contentrate',
    'Coconut Contentrate', 'Cranberry Contentrate', 'Grape Contentrate',
    'Grapefruit Contentrate', 'Guava Contentrate', 'Honeyberry Contentrate',
    'Huckleberry Contentrate', 'Kiwi Contentrate', 'Lemon Contentrate',
    'Lime Contentrate', 'Mango Contentrate', 'Melon Contentrate',
    'Cantaloupe Contentrate', 'Honeydew Contentrate', 'Watermelon Contentrate',
    'Nectarine Contentrate', 'Orange Contentrate', 'Papaya Contentrate',
    'Peach Contentrate', 'Pear Contentrate', 'Pineapple Contentrate',
    'Pomegranate Contentrate', 'Raspberry Contentrate',
    'Strawberry Contentrate', 'Acai Cider', 'Apple Cider', 'Apricot Cider',
    'Banana Cider', 'Blackberry Cider', 'Blueberry Cider', 'Boysenberry Cider',
    'Crab Apples Cider', 'Cherry Cider', 'Cloudberry Cider', 'Coconut Cider',
    'Cranberry Cider', 'Grape Cider', 'Grapefruit Cider', 'Guava Cider',
    'Honeyberry Cider', 'Huckleberry Cider', 'Kiwi Cider', 'Lemon Cider',
    'Lime Cider', 'Mango Cider', 'Melon Cider', 'Cantaloupe Cider',
    'Honeydew Cider', 'Watermelon Cider', 'Nectarine Cider', 'Orange Cider',
    'Papaya Cider', 'Peach Cider', 'Pear Cider', 'Pineapple Cider',
    'Pomegranate Cider', 'Raspberry Cider', 'Strawberry Cider', 'Acai Soda',
    'Apple Soda', 'Apricot Soda', 'Banana Soda', 'Blackberry Soda',
    'Blueberry Soda', 'Boysenberry Soda', 'Crab Apples Soda', 'Cherry Soda',
    'Cloudberry Soda', 'Coconut Soda', 'Cranberry Soda', 'Grape Soda',
    'Grapefruit Soda', 'Guava Soda', 'Honeyberry Soda', 'Huckleberry Soda',
    'Kiwi Soda', 'Lemon Soda', 'Lime Soda', 'Mango Soda', 'Melon Soda',
    'Cantaloupe Soda', 'Honeydew Soda', 'Watermelon Soda', 'Nectarine Soda',
    'Orange Soda', 'Papaya Soda', 'Peach Soda', 'Pear Soda', 'Pineapple Soda',
    'Pomegranate Soda', 'Raspberry Soda', 'Strawberry Soda', 'Acai Infusion',
    'Apple Infusion', 'Apricot Infusion', 'Banana Infusion',
    'Blackberry Infusion', 'Blueberry Infusion', 'Boysenberry Infusion',
    'Crab Apples Infusion', 'Cherry Infusion', 'Cloudberry Infusion',
    'Coconut Infusion', 'Cranberry Infusion', 'Grape Infusion',
    'Grapefruit Infusion', 'Guava Infusion', 'Honeyberry Infusion',
    'Huckleberry Infusion', 'Kiwi Infusion', 'Lemon Infusion', 'Lime Infusion',
    'Mango Infusion', 'Melon Infusion', 'Cantaloupe Infusion',
    'Honeydew Infusion', 'Watermelon Infusion', 'Nectarine Infusion',
    'Orange Infusion', 'Papaya Infusion', 'Peach Infusion', 'Pear Infusion',
    'Pineapple Infusion', 'Pomegranate Infusion', 'Raspberry Infusion',
    'Strawberry Infusion'
]
Drink_d2 = [
    'Absinthe', 'Cognac', 'Gin', 'Pale Ale', 'Pilsner', 'Amber Ale',
    'Wheat Beer', 'Ale', 'Porter', 'Marzen', 'Scotch', 'Stout', 'Pale Lager',
    'Rye Ale', 'Rum', 'Cocktail', 'Whiskey', 'Vodka', 'Moonshine', 'Bourban',
    'Brandy', 'Rum', 'Vermouth'
]
