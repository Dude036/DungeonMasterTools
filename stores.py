from numpy.random import randint, choice, random_sample
import json
from names import Antiques, Books, Enchanter, Potions, Tavern, Restaurant, Jeweller, Blacksmith, GeneralStore, Weapons,\
    Jewelling, Brothel, Gunsmithing
from variance import normalize_dict
from character import create_person
from spell_list import MasterSpells
from wondrous_list import MasterWondrous

MasterID = 1

'''
    'Sample' : { 'Weight': 10, 'Cost' : 1, 'Type' : ['B','S','P','LA','MA','HA','2','1','Si','Ma','Ex','Ra','Ar',], },
B, S, P          - Blunt, Slash, Pierce
LA, MA, HA        - Light Armor, Medium Armor, Heavy Armor
2, 1                - 2 Handed, 1 Handed   
Si, Ma, Ex, Ra, Ar  - Simple, Martial, Exotic, Ranged (bows), Ranged (arrows)
    If you want to make your life hell:
https://the-eye.eu/public/Books/rpg.rem.uz/Pathfinder/3rd%20Party/Rite%20Publishing/101%20Series/101%20Special%20Materials%20%26%20Power%20Components.pdf
'''
common_material = {
    'Bronze': {'Weight': 1, 'AC': 8, 'Cost': .8,
               'Type': ['B', 'S', 'P', 'MA', 'HA', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Copper': {'Weight': 1, 'AC': 6, 'Cost': .8,
               'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Iron': {'Weight': 1, 'AC': 10, 'Cost': 1,
             'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Lead': {'Weight': 1.5, 'AC': 8, 'Cost': 1.1,
             'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Steel': {'Weight': 1, 'AC': 10, 'Cost': 1,
              'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Oak': {'Weight': .5, 'AC': 2, 'Cost': .25,
            'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Yew': {'Weight': .5, 'AC': 2, 'Cost': .25,
            'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Hide': {'Weight': .5, 'AC': 8, 'Cost': .8,
             'Type': ['LA', 'MA', ], },
    'Leather': {'Weight': .5, 'AC': 8, 'Cost': .8,
                'Type': ['LA', 'MA', ], },
}
uncommon_material = {
    'Adamantine': {'Weight': 1, 'AC': 20, 'Cost': 1.8,
                   'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Bone': {'Weight': 1, 'AC': 6, 'Cost': .8,
             'Type': ['B', 'S', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Darkwood': {'Weight': .2, 'AC': 5, 'Cost': 1.05,
                 'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Dragonskin': {'Weight': 1, 'AC': 12, 'Cost': 2.25,
                   'Type': ['LA', 'MA', 'HA'], },
    'Dragonhide': {'Weight': 1, 'AC': 10, 'Cost': 2.5,
                   'Type': ['LA', 'MA', 'HA', ], },
    'Gold': {'Weight': 1, 'AC': 5, 'Cost': 10,
             'Type': ['S', 'P', 'MA', '1', 'Si', 'Ex', 'Ra', 'Ar', ], },
    'Greenwood': {'Weight': .5, 'AC': 2, 'Cost': 1.15,
                  'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Platinum': {'Weight': .7, 'AC': 15, 'Cost': 5,
                 'Type': ['S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Silkweave': {'Weight': .15, 'AC': 10, 'Cost': 2,
                  'Type': ['LA', ], },
    'Silver': {'Weight': 1, 'AC': 8, 'Cost': 1.15,
               'Type': ['S', 'P', 'MA', '1', 'Si', 'Ex', 'Ra', 'Ar', ], },
    'Stone': {'Weight': .75, 'AC': 2, 'Cost': .25,
              'Type': ['B', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
}
rare_material = {
    'Angelskin': {'Weight': .2, 'AC': 5, 'Cost': 2.75,
                  'Type': ['LA', 'MA', ], },
    'Cold Iron': {'Weight': 1, 'AC': 10, 'Cost': 2,
                  'Type': ['S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Dreamstone': {'Weight': .5, 'AC': 10, 'Cost': 2.25,
                   'Type': ['B', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Elysian Bronze': {'Weight': 1, 'AC': 10, 'Cost': 2,
                       'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Griffon Mane': {'Weight': .2, 'AC': 1, 'Cost': 2,
                     'Type': ['LA',  'MA',  'HA', ], },
    'Ironwood': {'Weight': .7, 'AC': 10, 'Cost': 1.8,
                 'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Obsidian': {'Weight': .75, 'AC': 5, 'Cost': 1.5,
                 'Type': ['S', 'P', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Viridium': {'Weight': 1, 'AC': 10, 'Cost': 1.5,
                 'Type': ['S', 'P', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
}
very_rare_material = {
    'Blood Crystal': {'Weight': 1, 'AC': 10, 'Cost': 2.75,
                      'Type': ['S', 'P', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Darkleaf Cloth': {'Weight': .2, 'AC': 10, 'Cost': 2.75,
                       'Type': ['LA', ], },
    'Mithral': {'Weight': .5, 'AC': 15, 'Cost': 3,
                'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Hot Siccatite': {'Weight': .8, 'AC': 10, 'Cost': 3,
                      'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Cold Siccatite': {'Weight': .8, 'AC': 10, 'Cost': 3,
                       'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Wyroot': {'Weight': 1.5, 'AC': 5, 'Cost': 2.5,
               'Type': ['B', 'P', '2', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
}
legendary_material = {
    'Horacalcum': {'Weight': 1, 'AC': 15, 'Cost': 5,
                   'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Mindglass': {'Weight': 1, 'AC': 10, 'Cost': 4,
                  'Type': ['B', 'S', 'P', 'LA', 'MA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Noqual': {'Weight': .5, 'AC': 10, 'Cost': 3,
               'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Umbrite': {'Weight': 1, 'AC': 18, 'Cost': 3,
                'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Voidglass': {'Weight': .5, 'AC': 10, 'Cost': 3.25,
                  'Type': ['S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Whipwood': {'Weight': .2, 'AC': 9, 'Cost': 3,
                 'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
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
level_0 = [
    'Acid Splash',
    'Arcane Mark',
    'Bleed',
    'Create Water',
    'Dancing Lights',
    'Daze',
    'Detect Magic',
    'Detect Poison',
    'Disrupt Undead',
    'Flare',
    'Ghost Sound',
    'Guidance',
    'Know Direction',
    'Light',
    'Lullaby',
    'Mage Hand',
    'Mending',
    'Message',
    'Open/Close',
    'Prestidigitation',
    'Purify Food and Drink',
    'Ray of Frost',
    'Read Magic',
    'Resistance',
    'Stabilize',
    'Summon Instrument',
    'Touch of Fatigue',
    'Virtue',
    'Brand',
    'Putrefy Food and Drink',
    'Sift',
    'Spark',
    'Unwitting Ally',
    'Haunted Fey Aspect',
]
level_1 = [
    'Alarm',
    'Animal Messenger',
    'Animate Rope',
    'Bane',
    'Bless',
    'Bless Water',
    'Bless Weapon',
    'Burning Hands',
    'Calm Animals',
    'Cause Fear',
    'Charm Animal',
    'Charm Person',
    'Chill Touch',
    'Color Spray',
    'Command',
    'Comprehend Languages',
    'Confusion, Lesser',
    'Cure Light Wounds',
    'Curse Water',
    'Deathwatch',
    'Delay Poison',
    'Detect Animals or Plants',
    'Detect Chaos',
    'Detect Evil',
    'Detect Good',
    'Detect Law',
    'Detect Secret Doors',
    'Detect Snares and Pits',
    'Detect Undead',
    'Disguise Self',
    'Divine Favor',
    'Doom',
    'Endure Elements',
    'Enlarge Person',
    'Entangle',
    'Entropic Shield',
    'Erase',
    'Expeditious Retreat',
    'Faerie Fire',
    'Feather Fall',
    'Floating Disk',
    'Goodberry',
    'Grease',
    'Hide from Animals',
    'Hide from Undead',
    'Hideous Laughter',
    'Hold Portal',
    'Hypnotism',
    'Identify',
    'Inflict Light Wounds',
    'Jump',
    'Longstrider',
    'Mage Armor',
    'Magic Aura',
    'Magic Fang',
    'Magic Missile',
    'Magic Mouth',
    'Magic Stone',
    'Magic Weapon',
    'Mount',
    'Obscure Object',
    'Obscuring Mist',
    'Pass without Trace',
    'Produce Flame',
    'Protection from Chaos',
    'Protection from Evil',
    'Protection from Good',
    'Protection from Law',
    'Ray of Enfeeblement',
    'Reduce Person',
    'Remove Fear',
    'Resist Energy',
    'Restoration, Lesser',
    'Sanctuary',
    'Shield',
    'Shield of Faith',
    'Shillelagh',
    'Shocking Grasp',
    'Silent Image',
    'Sleep',
    'Speak with Animals',
    'Summon Monster I',
    "Summon Nature's Ally I",
    'True Strike',
    'Undetectable Alignment',
    'Unseen Servant',
    'Ventriloquism',
    'Alter Winds',
    'Ant Haul',
    'Aspect of the Falcon',
    'Beguiling Gift',
    "Bomber's Eye",
    'Borrow Skill',
    'Break',
    'Bristle',
    'Burst Bonds',
    'Call Animal',
    'Challenge Evil',
    'Cloak of Shade',
    "Crafter's Curse",
    "Crafter's Fortune",
    'Dancing Lantern',
    'Detect Aberration',
    'Expeditious Excavation',
    'Feather Step',
    'Flare Burst',
    'Ghostbane Dirge',
    'Glide',
    'Grace',
    'Gravity Bow',
    "Hero's Defiance",
    'Honeyed Tongue',
    "Hunter's Howl",
    'Hydraulic Push',
    'Ill Omen',
    'Innocence',
    'Invigorate',
    'Keen Senses',
    "Knight's Calling",
    'Lead Blades',
    'Mask Dweomer',
    'Memory Lapse',
    'Negate Aroma',
    'Rally Point',
    'Rejuvenate Eidolon, Lesser',
    'Residual Tracking',
    'Restful Sleep',
    'Saving Finale',
    'Sculpt Corpse',
    'Share Language',
    'Solid Note',
    'Stone Fist',
    'Stumble Gap',
    'Timely Inspiration',
    'Tireless Pursuit',
    'Touch of Gracelessness',
    'Touch of the Sea',
    'Unfetter',
    'Vanish',
    'Veil of Positive Energy',
    'Wrath',
    'Abundant Ammunition',
    'Adjuring Step',
    'Adoration',
    'Air Bubble',
    'Bowstaff',
    'Compel Hostility',
    'Damp Powder',
    "Deadeye's Lore",
    'Fabricate Bullets',
    'Illusion of Calm',
    'Jury-Rig',
    'Liberating Command',
    'Life Conduit',
    'Litany of Sloth',
    'Litany of Weakness',
    'Lock Gaze',
    'Longshot',
    'Mirror Strike',
    'Moment of Greatness',
    'Negative Reaction',
    'Peacebond',
    'Reinforce Armaments',
    'Returning Weapon',
    'See Alignment',
    'Shock Shield',
    'Sun Metal',
    'Tactical Acumen',
    'Targeted Bomb Admixture',
    'Unerring Weapon',
    'Warding Weapon',
    'Weaken Powder'
]
level_2 = [
    'Acid Arrow',
    'Aid',
    'Align Weapon',
    'Alter Self',
    'Animal Trance',
    'Arcane Lock',
    'Augury',
    'Barkskin',
    "Bear's Endurance",
    'Blindness/Deafness',
    'Blur',
    "Bull's Strength",
    'Calm Emotions',
    "Cat's Grace",
    'Chill Metal',
    'Command Undead',
    'Consecrate',
    'Continual Flame',
    'Cure Moderate Wounds',
    'Darkness',
    'Darkvision',
    'Daze Monster',
    'Death Knell',
    'Desecrate',
    'Detect Thoughts',
    "Eagle's Splendor",
    'Enthrall',
    'False Life',
    'Find Traps',
    'Fire Trap',
    'Flame Blade',
    'Flaming Sphere',
    'Fog Cloud',
    "Fox's Cunning",
    'Gentle Repose',
    'Ghoul Touch',
    'Glitterdust',
    'Gust of Wind',
    'Heat Metal',
    'Heroism',
    'Hold Animal',
    'Hold Person',
    'Hypnotic Pattern',
    'Inflict Moderate Wounds',
    'Invisibility',
    'Knock',
    'Levitate',
    'Locate Object',
    'Make Whole',
    'Minor Image',
    'Mirror Image',
    'Misdirection',
    "Owl's Wisdom",
    'Phantom Trap',
    'Protection from Arrows',
    'Protection from Energy',
    'Pyrotechnics',
    'Rage',
    'Reduce Animal',
    'Remove Paralysis',
    'Rope Trick',
    'Scare',
    'Scorching Ray',
    'See Invisibility',
    'Shatter',
    'Shield Other',
    'Silence',
    'Snare',
    'Soften Earth and Stone',
    'Sound Burst',
    'Speak with Plants',
    'Spectral Hand',
    'Spider Climb',
    'Spike Growth',
    'Spiritual Weapon',
    'Status',
    'Suggestion',
    'Summon Monster II',
    "Summon Nature's Ally II",
    'Summon Swarm',
    'Tongues',
    'Touch of Idiocy',
    'Tree Shape',
    'Warp Wood',
    'Web',
    'Whispering Wind',
    'Wind Wall',
    'Wood Shape',
    'Zone of Truth',
    'Accelerate Poison',
    'Alchemical Allocation',
    'Allfood',
    'Arrow Eruption',
    'Aspect of the Bear',
    'Aura of Greater Courage',
    'Bestow Grace',
    'Blessing of Courage and Life',
    'Blood Biography',
    'Bloodhound',
    'Burning Gaze',
    'Cacophonous Call',
    'Campfire Wall',
    'Castigate',
    'Chameleon Stride',
    'Confess',
    'Corruption Resistance',
    'Create Pit',
    'Create Treasure Map',
    'Dust of Twilight',
    'Eagle Eye',
    'Elemental Speech',
    'Elemental Touch',
    'Enter Image',
    'Evolution Surge, Lesser',
    'Feast of Ashes',
    'Fester',
    'Fire Breath',
    'Fire of Entanglement',
    'Flames of the Faithful',
    'Follow Aura',
    'Gallant Inspiration',
    'Guiding Star',
    'Hidden Speech',
    'Hide Campsite',
    "Hunter's Eye",
    'Instant Armor',
    'Light Lance',
    'Lockjaw',
    'Natural Rhythm',
    "Oracle's Burden",
    "Paladin's Sacrifice",
    'Perceive Cues',
    'Pox Pustules',
    'Protective Spirit',
    'Righteous Vigor',
    'Sacred Bond',
    'Saddle Surge',
    'Scent Trail',
    'Slipstream',
    'Stone Call',
    'Summon Eidolon',
    'Transmute Potion to Poison',
    'Versatile Weapon',
    'Vomit Swarm',
    'Wake of Light',
    'Weapon of Awe',
    'Ablative Barrier',
    'Animal Aspect',
    'Ant Haul, Communal',
    'Bestow Weapon Proficiency',
    'Blistering Invective',
    'Brow Gasher',
    'Bullet Shield',
    'Certain Grip',
    'Destabilize Powder',
    'Discovery Torch',
    'Divine Arrow',
    'Effortless Armor',
    'Endure Elements, Communal',
    'Fiery Shuriken',
    'Forest Friend',
    'Frost Fall',
    'Instrument of Agony',
    'Kinetic Reverberation',
    'Litany of Defense',
    'Litany of Eloquence',
    'Litany of Entanglement',
    'Litany of Righteousness',
    'Litany of Warding',
    'Locate Weakness',
    'Magic Siege Engine',
    'Mask Dweomer, Communal',
    'Mount, Communal',
    'Pilfering Hand',
    'Protection from Chaos, Communal',
    'Protection from Evil, Communal',
    'Protection from Good, Communal',
    'Protection from Law, Communal',
    'Qualm',
    'Recoil Fire',
    'Reinforce Armaments, Communal',
    'Reloading Hands',
    'Returning Weapon, Communal',
    'Ricochet Shot',
    'Shadow Bomb Admixture',
    'Share Language, Communal',
    'Spontaneous Immolation',
    'Stabilize Powder',
    'Telekinetic Assembly',
    'Thunder Fire',
    'Touch Injection',
    'Twisted Space',
    'Wilderness Soldiers'
]
level_3 = [
    'Animate Dead',
    'Arcane Sight',
    'Beast Shape I',
    'Bestow Curse',
    'Blink',
    'Call Lightning',
    'Charm Monster',
    'Clairaudience/Clairvoyance',
    'Command Plants',
    'Confusion',
    'Contagion',
    'Create Food and Water',
    'Crushing Despair',
    'Cure Serious Wounds',
    'Daylight',
    'Deeper Darkness',
    'Deep Slumber',
    'Diminish Plants',
    'Discern Lies',
    'Dispel Magic',
    'Displacement',
    'Dominate Animal',
    'Explosive Runes',
    'Fear',
    'Fireball',
    'Flame Arrow',
    'Fly',
    'Gaseous Form',
    'Geas, Lesser',
    'Glibness',
    'Glyph of Warding',
    'Good Hope',
    'Halt Undead',
    'Haste',
    'Heal Mount',
    'Helping Hand',
    'Illusory Script',
    'Inflict Serious Wounds',
    'Invisibility Purge',
    'Invisibility Sphere',
    'Keen Edge',
    'Lightning Bolt',
    'Magic Circle against Chaos',
    'Magic Circle against Evil',
    'Magic Circle against Good',
    'Magic Circle against Law',
    'Magic Fang, Greater',
    'Magic Vestment',
    'Magic Weapon, Greater',
    'Major Image',
    'Meld into Stone',
    'Neutralize Poison',
    'Nondetection',
    'Phantom Steed',
    'Plant Growth',
    'Poison',
    'Prayer',
    'Quench',
    'Ray of Exhaustion',
    'Remove Blindness/Deafness',
    'Remove Curse',
    'Remove Disease',
    'Repel Vermin',
    'Scrying',
    'Sculpt Sound',
    'Searing Light',
    'Secret Page',
    'Sepia Snake Sigil',
    'Shrink Item',
    'Sleet Storm',
    'Slow',
    'Speak with Dead',
    'Stinking Cloud',
    'Stone Shape',
    'Summon Monster III',
    "Summon Nature's Ally III",
    'Tiny Hut',
    'Vampiric touch',
    'Water Breathing',
    'Water Walk',
    'Absorbing Touch',
    'Amplify Elixir',
    'Aqueous Orb',
    'Arcane Concordance',
    'Aspect of the Stag',
    'Banish Seeming',
    'Bloody Claws',
    'Borrow Fortune',
    'Cast Out',
    'Cloak of Winds',
    'Coordinated Effort',
    'Cup of Dust',
    'Defile Armor',
    'Devolution',
    'Divine Transfer',
    'Draconic Reservoir',
    'Elemental Aura',
    'Evolution Surge',
    'Feather Step, Mass',
    'Fire of Judgment',
    'Ghostbane Dirge, Mass',
    'Holy Whisper',
    'Hydraulic Torrent',
    'Instant Enemy',
    'Invigorate, Mass',
    "Jester's Jaunt",
    'Life Bubble',
    'Lily Pad Stride',
    'Marks Of Forbiddance',
    'Nap Stack',
    "Nature's Exile",
    'Pain Strike',
    'Purging Finale',
    'Rejuvenate Eidolon',
    'Retribution',
    'Reviving Finale',
    'Sanctify Armor',
    'Screech',
    'Seek Thoughts',
    'Share Senses',
    'Shifting Sand',
    'Spiked Pit',
    'Strong Jaw',
    'Thorn Body',
    'Thundering Drums',
    'Tireless Pursuers',
    'Twilight Knife',
    'Venomous Bolt',
    'Ward the Faithful',
    'Wrathful Mantle',
    'Absorb Toxicity',
    'Animal Aspect, Greater',
    'Burst of Speed',
    'Chain of Perdition',
    'Companion Mind Link',
    'Darkvision, Communal',
    'Daybreak Arrow',
    'Deadly Juggernaut',
    'Delay Poison, Communal',
    'Flash Fire',
    'Healing Thief',
    'Hostile Levitation',
    'Life Conduit, Improved',
    'Lightning Lash Bomb Admixture',
    'Litany of Escape',
    'Litany of Sight',
    'Named Bullet',
    'Obsidian Flow',
    'Pellet Blast',
    'Phantom Chariot',
    'Phantom Driver',
    'Phantom Steed, Communal',
    'Protection from Arrows, Communal',
    'Protection from Energy, Communal',
    'Pup Shape',
    'Resinous Skin',
    'Resist Energy, Communal',
    'Spider Climb, Communal',
    'Tongues, Communal'
]
level_4 = [
    'Air Walk',
    'Animal Growth',
    'Antiplant Shell',
    'Arcane Eye',
    'Beast Shape II',
    'Black Tentacles',
    'Blight',
    'Break Enchantment',
    'Chaos Hammer',
    'Commune with Nature',
    'Control Water',
    'Cure Critical Wounds',
    'Death Ward',
    'Detect Scrying',
    'Dimensional Anchor',
    'Dimension Door',
    'Dismissal',
    'Dispel Chaos',
    'Dispel Evil',
    'Divination',
    'Divine Power',
    'Dominate Person',
    'Elemental Body I',
    'Enervation',
    'Enlarge Person, Mass',
    'Fire Shield',
    'Flame Strike',
    'Freedom of Movement',
    'Giant Vermin',
    'Globe of Invulnerability, Lesser',
    'Hallucinatory Terrain',
    'Hold Monster',
    'Holy Smite',
    'Holy Sword',
    'Ice Storm',
    'Illusory Wall',
    'Imbue with Spell Ability',
    'Inflict Critical Wounds',
    'Invisibility, Greater',
    'Legend Lore',
    'Locate Creature',
    'Mark of Justice',
    'Minor Creation',
    'Mnemonic Enhancer',
    'Modify Memory',
    "Order's Wrath",
    'Phantasmal Killer',
    'Planar Ally, Lesser',
    'Rainbow Pattern',
    'Reduce Person, Mass',
    'Reincarnate',
    'Resilient Sphere',
    'Restoration',
    'Rusting Grasp',
    'Secure Shelter',
    'Sending',
    'Shadow Conjuration',
    'Shout',
    'Solid Fog',
    'Spell Immunity',
    'Spike Stones',
    'Stoneskin',
    'Summon Monster IV',
    "Summon Nature's Ally IV",
    'Tree Stride',
    'Unholy Blight',
    'Wall of Fire',
    'Wall of Ice',
    'Zone of Silence',
    'Acid Pit',
    'Aspect of the Wolf',
    'Ball Lightning',
    'Blaze of Glory',
    'Blessing of Fervor',
    'Blessing of the Salamander',
    'Bow Spirit',
    'Brand, Greater',
    'Calcific Touch',
    "Coward's Lament",
    'Denounce',
    'Detonate',
    'Discordant Blast',
    "Dragon's Breath",
    'Evolution Surge, Greater',
    'Firefall',
    'Fire of Vengeance',
    'Fluid Form',
    'Forced Repentance',
    'Geyser',
    'Grove of Respite',
    'Heroic Finale',
    "King's Castle",
    'Moonstruck',
    'Oath of Peace',
    'Planar Adaptation',
    'Purified Calling',
    'Rebuke',
    'Resounding Blow',
    'Rest Eternal',
    'River of Wind',
    'Sacrificial Oath',
    'Shadow Projection',
    'Shared Wrath',
    'Sleepwalk',
    'Spiritual Ally',
    'Spite',
    'Stay the Hand',
    'Threefold Aspect',
    'Transmogrify',
    'Treasure Stitching',
    'True Form',
    'Universal Formula',
    'Wandering Star Motes',
    'Air Walk, Communal',
    'Debilitating Portent',
    'Find Quarry',
    'Hostile Juxtaposition',
    'Judgment Light',
    'Litany of Madness',
    'Litany of Thunder',
    'Litany of Vengeance',
    'Magic Siege Engine, Greater',
    'Mutagenic Touch',
    'Named Bullet, Greater',
    'Nondetection, Communal',
    'Shocking Image',
    'Stoneskin, Communal',
    'Summoner Conduit',
    'Telekinetic Charge',
    'Terrain Bond',
    'Viper Bomb Admixture',
    'Water Walk, Communal',
    'Wreath of Blades'
]
level_5 = [
    'Atonement',
    'Awaken',
    'Baleful Polymorph',
    'Beast Shape III',
    'Breath of Life',
    'Call Lightning Storm',
    'Cloudkill',
    'Command, Greater',
    'Commune',
    'Cone of Cold',
    'Contact Other Plane',
    'Control Winds',
    'Cure Light Wounds, Mass',
    'Dispel Good',
    'Dispel Law',
    'Dispel Magic, Greater',
    'Disrupting Weapon',
    'Dream',
    'Elemental Body II',
    'Fabricate',
    'False Vision',
    'Feeblemind',
    'Hallow',
    'Heroism, Greater',
    'Inflict Light Wounds, Mass',
    'Insect Plague',
    'Interposing Hand',
    "Mage's Faithful Hound",
    "Mage's Private Sanctum",
    'Magic Jar',
    'Major Creation',
    'Mind Fog',
    'Mirage Arcana',
    'Mislead',
    'Nightmare',
    'Overland Flight',
    'Passwall',
    'Permanency',
    'Persistent Image',
    'Planar Binding, Lesser',
    'Plane Shift',
    'Plant Shape I',
    'Polymorph',
    'Prying Eyes',
    'Raise Dead',
    'Righteous Might',
    'Secret Chest',
    'Seeming',
    'Shadow Evocation',
    'Shadow Walk',
    'Slay Living',
    'Song of Discord',
    'Spell Resistance',
    'Suggestion, Mass',
    'Summon Monster V',
    "Summon Nature's Ally V",
    'Symbol of Pain',
    'Symbol of Sleep',
    'Telekinesis',
    'Telepathic Bond',
    'Teleport',
    'Transmute Mud to Rock',
    'Transmute Rock to Mud',
    'True Seeing',
    'Unhallow',
    'Wall of Force',
    'Wall of Stone',
    'Wall of Thorns',
    'Waves of Fatigue',
    "Bard's Escape",
    'Cacophonous Call, Mass',
    'Castigate, Mass',
    'Cleanse',
    'Cloak of Dreams',
    'Deafening Song Bolt',
    'Delayed Consumption',
    'Elude Time',
    'Fire Snake',
    'Foe to Friend',
    'Frozen Note',
    'Hungry Pit',
    'Pain Strike, Mass',
    'Phantasmal Web',
    'Pillar of Life',
    'Rejuvenate Eidolon, Greater',
    'Resurgent Transformation',
    'Snake Staff',
    'Stunning Finale',
    'Suffocation',
    'Unwilling Shield',
    'Dust Form',
    'Energy Siege Shot',
    'Languid Bomb Admixture',
    'Life Conduit, Greater',
    'Spell Immunity, Communal',
    'Symbol of Striking',
    'Tar Pool'
]
level_6 = [
    'Acid Fog',
    'Analyze Dweomer',
    'Animate Objects',
    'Antilife Shell',
    'Antimagic Field',
    'Banishment',
    "Bear's Endurance, Mass",
    'Beast Shape IV',
    'Blade Barrier',
    "Bull's Strength, Mass",
    "Cat's Grace, Mass",
    'Chain Lightning',
    'Charm Monster, Mass',
    'Circle of Death',
    'Contingency',
    'Create Undead',
    'Cure Moderate Wounds, Mass',
    'Disintegrate',
    "Eagle's Splendor, Mass",
    'Elemental Body III',
    'Eyebite',
    'Find the Path',
    'Fire Seeds',
    'Flesh to Stone',
    'Forbiddance',
    'Forceful Hand',
    'Form of the Dragon I',
    "Fox's Cunning, Mass",
    'Freezing Sphere',
    'Geas/Quest',
    'Globe of Invulnerability',
    'Glyph of Warding, Greater',
    'Guards and Wards',
    'Harm',
    'Heal',
    "Heroes' Feast",
    'Inflict Moderate Wounds, Mass',
    'Ironwood',
    'Irresistible Dance',
    'Liveoak',
    "Mage's Lucubration",
    'Move Earth',
    "Owl's Wisdom, Mass",
    'Permanent Image',
    'Planar Ally',
    'Planar Binding',
    'Plant Shape II',
    'Programmed Image',
    'Project Image',
    'Repel Wood',
    'Repulsion',
    'Scrying, Greater',
    'Shout, Greater',
    'Spellstaff',
    'Stone Tell',
    'Stone to Flesh',
    'Summon Monster VI',
    "Summon Nature's Ally VI",
    'Symbol of Fear',
    'Symbol of Persuasion',
    'Sympathetic Vibration',
    'Transformation',
    'Transport via Plants',
    'Undeath to Death',
    'Veil',
    'Wall of Iron',
    'Wind Walk',
    'Word of Recall',
    'Brilliant Inspiration',
    'Contagious Flame',
    'Deadly Finale',
    'Enemy Hammer',
    'Euphoric Tranquility',
    'Fester, Mass',
    "Fool's Forbiddance",
    'Getaway',
    'Pied Piping',
    'Planar Adaptation, Mass',
    'Sirocco',
    'Swarm Skin',
    'Twin Form',
    'Caging Bomb Admixture',
    'Energy Siege Shot, Greater',
    'Hostile Juxtaposition, Greater',
    'Walk through Space'
]
level_7 = [
    'Animate Plants',
    'Arcane Sight, Greater',
    'Blasphemy',
    'Changestaff',
    'Control Undead',
    'Control Weather',
    'Creeping Doom',
    'Cure Serious Wounds, Mass',
    'Delayed Blast Fireball',
    'Destruction',
    'Dictum',
    'Elemental Body IV',
    'Ethereal Jaunt',
    'Finger of Death',
    'Fire Storm',
    'Forcecage',
    'Form of the Dragon II',
    'Giant Form I',
    'Grasping Hand',
    'Hold Person, Mass',
    'Holy Word',
    'Inflict Serious Wounds, Mass',
    'Insanity',
    'Instant Summons',
    'Invisibility, Mass',
    'Limited Wish',
    "Mage's Magnificent Mansion",
    "Mage's Sword",
    'Phase Door',
    'Plant Shape III',
    'Polymorph, Greater',
    'Power Word Blind',
    'Prismatic Spray',
    'Refuge',
    'Regenerate',
    'Restoration, Greater',
    'Resurrection',
    'Reverse Gravity',
    'Sequester',
    'Shadow Conjuration, Greater',
    'Simulacrum',
    'Spell Turning',
    'Statue',
    'Summon Monster VII',
    "Summon Nature's Ally VII",
    'Sunbeam',
    'Symbol of Stunning',
    'Symbol of Weakness',
    'Teleport, Greater',
    'Teleport Object',
    'Transmute Metal to Wood',
    'Vision',
    'Waves of Exhaustion',
    'Word of Chaos',
    'Deflection',
    'Expend',
    'Firebrand',
    'Fly, Mass',
    'Phantasmal Revenge',
    'Rampart',
    'Vortex',
    'Arcane Cannon',
    'Jolting Portent',
    'Siege of Trees'
]
level_8 = [
    'Animal Shapes',
    'Antipathy',
    'Binding',
    'Clenched Fist',
    'Cloak of Chaos',
    'Clone',
    'Control Plants',
    'Create Greater Undead',
    'Cure Critical Wounds, Mass',
    'Demand',
    'Dimensional Lock',
    'Discern Location',
    'Earthquake',
    'Form of the Dragon III',
    'Giant Form II',
    'Holy Aura',
    'Horrid Wilting',
    'Incendiary Cloud',
    'Inflict Critical Wounds, Mass',
    'Iron Body',
    'Maze',
    'Mind Blank',
    'Moment of Prescience',
    'Planar Ally, Greater',
    'Planar Binding, Greater',
    'Polar Ray',
    'Polymorph Any Object',
    'Power Word Stun',
    'Prismatic Wall',
    'Protection from Spells',
    'Prying Eyes, Greater',
    'Repel Metal or Stone',
    'Scintillating Pattern',
    'Screen',
    'Shadow Evocation, Greater',
    'Shield of Law',
    'Spell Immunity, Greater',
    'Summon Monster VIII',
    "Summon Nature's Ally VIII",
    'Sunburst',
    'Symbol of Death',
    'Symbol of Insanity',
    'Sympathy',
    'Telekinetic Sphere',
    'Temporal Stasis',
    'Trap the Soul',
    'Unholy Aura',
    'Whirlwind',
    'Divine Vessel',
    'Seamantle',
    'Stormbolts',
    'Wall of Lava',
    'Frightful Aspect'
]
level_9 = [
    'Astral Projection',
    'Crushing Hand',
    'Dominate Monster',
    'Elemental Swarm',
    'Energy Drain',
    'Etherealness',
    'Foresight',
    'Freedom',
    'Gate',
    'Heal, Mass',
    'Hold Monster, Mass',
    'Implosion',
    'Imprisonment',
    "Mage's Disjunction",
    'Meteor Swarm',
    'Miracle',
    'Power Word Kill',
    'Prismatic Sphere',
    'Shades',
    'Shambler',
    'Shapechange',
    'Soul Bind',
    'Storm of Vengeance',
    'Summon Monster IX',
    "Summon Nature's Ally IX",
    'Teleportation Circle',
    'Time Stop',
    'True Resurrection',
    'Wail of the Banshee',
    'Weird',
    'Wish',
    'Clashing Rocks',
    'Fiery Body',
    'Suffocation, Mass',
    'Tsunami',
    'Wall of Suppression',
    'Winds of Vengeance',
    'World Wave',
    'Heroic Invocation',
    'Mind Blank, Communal',
    'Siege of Trees, Greater',
    'Spell Immunity, Greater Communal'
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

def find_spell_level(spell):
    l = None
    a = [level_0, level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9]
    for level in range(len(a)):
        if spell in a[level]:
            l = level
    return l

def find_spell_details(spell):
    if spell in list(MasterSpells.keys()):
        return MasterSpells[spell]['link'], MasterSpells[spell]['school'], MasterSpells[spell]['casting_time'], MasterSpells[spell]['components'], MasterSpells[spell]['range'], MasterSpells[spell]['description'],
    else:
        return None

def find_spell_description(spell):
    if spell in list(MasterSpells.keys()):
        return MasterSpells[spell]['description']
    else:
        return None

def find_spell_link(spell):
    if spell in list(MasterSpells.keys()):
        return MasterSpells[spell]['link']
    else:
        return None

def find_spell_range(spell):
    if spell in list(MasterSpells.keys()):
        return MasterSpells[spell]['range']
    else:
        return None

def find_spell_components(spell):
    if spell in list(MasterSpells.keys()):
        return MasterSpells[spell]['components']
    else:
        return None

def determine_cost(c):
    s = ""
    if isinstance(type(c), int):
        s = format(c, ',d') + " gp"
    else:
        if int(c) > 0:
            s += format(int(c), ',d') + " gp "
            c %= int(c)
        if int(c * 10) > 0:
            s += str(int(c*10)) + " sp "
        if int((c * 100) % 10) > 0:
            s += str(int((c*100) % 10)) + " cp"
    if len(s) == 0:
        s = "1 cp"
    return s

def determine_rarity(q):
    if q[0] == q[1]:
        return q[0]
    l = []
    for x in range(q[0], q[1] + 1):
        l.append((x+1) * x * x)
    l[0] += 1
    l = l[::-1]
    d = {}
    pos = 0
    for x in range(q[0], q[1]+1):
        d[x] = l[pos]
        pos += 1
    return choice(list(d.keys()), p=list(normalize_dict(d).values()))


class Store(object):
    """Everyone needs things!
    Inflation is the upsell rate at which things are sold for. this could be due
        to the amount of market dominance, rarity of items, or accessibility
    Quality is the spectrum of item rarity and quantity. There will be 3 digits
        First and Second: Low and High End of the Item spawn rate
        Third: Quantity of item generation
    """
    Shopkeeper = None
    Store_name = ''
    Quality = Stock = []
    Inflation = 0.0

    def __init__(self, keeper, name, service, qual):
        self.Shopkeeper = keeper
        self.Store_name = name
        self.Inflation = service
        self.Quality = qual
        self.Stock = []

    def fill_store(self, Item, quantity):
        for _ in range(quantity):
            same = True
            while same:
                # qual = randint(self.Quality[0], self.Quality[1] + 1)
                qual = determine_rarity(self.Quality)
                i = Item(qual)
                i.Cost = i.Cost * self.Inflation
                if i not in self.Stock:
                    self.Stock.append(i)
                    same = False

    def add_relic(self, Item):
        qual = randint(self.Quality[0], self.Quality[1] + 1)
        if isinstance(Item, Weapon):
            typ = choice(["Axe", "Bow", "Dagger", "Hammer", "Mace", "Spear", "Sword", ])
            name = str(Weapons(typ))
            if typ == "Sword":
                typ = choice(['Light', 'Heavy']) + " Sword"
            elif typ == "Axe":
                typ = choice(['Light', 'Heavy']) + " Axe"
            elif typ == "Dagger":
                typ = "Close"
            elif typ == "Bow":
                typ = str(choice(["", "Cross"]) + "bow").title()

            self.Stock.append(Item(4, iName=name, iClass=typ))

    def add_enchanted(self, Item, Enchantment=None):
        qual = randint(self.Quality[0], self.Quality[1] + 1)
        i = Item(qual)
        if Enchantment is None:
            ench = Enchant()
            i.add_enchantment(ench)
        else:
            i.add_enchantment(Enchantment)
        self.Stock.append(i)


class Weapon(object):
    """
    Cost shoudl be in GP
    Rarity [0, 4] - Common, Uncommon, Rare, Very Rare, Legendary
        Rarity will also determine what types of material to use as well as the
            price for an item. Also note, that the prices are how much they cost
            to make, not the cost they'll be sold for.
    """
    Weight = Cost = Rarity = Masterwork = 0
    Name = Dice = Crit = Class = ''
    Damage = []
    Enchantment = None

    die_values = {
        'Heavy Axe': [10, 12],
        'Light Axe': [8, 10],
        'Heavy Blade': [6, 8, 10],
        'Light Blade': [6, 8],
        'Close': [4, 6, 8],
        'Double': [4, 6, 8, 10],
        'Flail': [4, 6, 8],
        'Hammer': [4, 6, 8],
        'Monk': [4, 6, 8, 10],
        'Polearm': [6, 8, 10],
        'Spear': [6, 8],
        'Bows': [8, 10],
        'Crossbow': [6, 8],
        'Thrown': [4, 6],
    }
    cost_and_weight = {
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

    possible_melee = {
        'Heavy Axe': ['bardiche', 'battleaxe', 'boarding axe','dwarven waraxe', 'greataxe', 'heavy pick', 'orc double axe', 'tongi',],
        'Light Axe': ['boarding axe', 'butchering axe', 'collapsible kumade', 'gandasa', 'handaxe', 'hooked axe', 'knuckle axe', 'kumade', 'light pick', 'mattock', 'throwing axe',],
        'Heavy Blade': ['Ankus', 'dueling sword', 'bastard sword', 'chakram', 'double chicken saber', 'double walking stick katana', 'elven curve blade', 'estoc', 'falcata', 'falchion', 'flambard', 'greatsword', 'great terbutje', 'katana', 'khopesh', 'klar', 'longsword', 'nine-ring broadsword', 'nodachi', 'scimitar', 'scythe', 'seven-branched sword', 'shotel', 'temple sword', 'terbutje', 'two-bladed sword',],
        'Light Blade': ['bayonet', 'butterfly knife', 'butterfly sword', 'chakram', 'dagger', 'deer horn knife', 'Drow razor', 'dueling dagger', 'gladius', 'hunga munga', 'kama', 'katar', 'kerambit', 'kukri', 'machete', 'madu', 'manople', 'pata', 'quadrens', 'rapier', 'sanpkhang', 'sawtooth sabre', 'scizore', 'shortsword', 'sica', 'sickle', 'spiral rapier', 'starknife', 'swordbreaker dagger', 'sword cane', 'wakizashi', 'war razor',],
        'Close': ['bayonet', 'brass knuckles', 'cestus', 'dan bong', 'emei piercer', 'fighting fan', 'gauntlet', 'iron brush', 'katar', 'klar', 'madu', 'mere club', 'punching dagger', 'rope gauntlet', 'sap', 'scizore', 'spiked gauntlet', 'tekko-kagi', 'tonfa', 'tri-bladed katar', 'stake', 'waveblade', 'wushu dart',],
        'Double': ['bo staff', 'Boarding gaff', 'chain-hammer', 'chain spear', 'dire flail', 'double walking stick katana', 'double-chained kama', 'dwarven urgrosh', 'gnome battle ladder', 'gnome hooked hammer', 'kusarigama', 'monk\'s spade', 'orc double axe', 'quarterstaff', 'taiaha', 'two-bladed sword', 'weighted spear',],
        'Flail': ['battle poi', 'bladed scarf', 'Cat-o\'-nine-tails', 'chain spear', 'dire flail', 'double chained kama', 'dwarven dorn-dergar', 'flail', 'flying talon', 'gnome pincher', 'halfling rope-shot', 'heavy flail', 'kusarigama', 'kyoketsu shoge', 'meteor hammer', 'morningstar', 'nine-section whip', 'nunchaku', 'sansetsukon', 'scorpion whip', 'spiked chain', 'urumi', 'whip',],
        'Hammer': ['aklys', 'battle aspergillum', 'Chain-hammer', 'club', 'gnome piston maul', 'greatclub', 'heavy mace', 'lantern staff', 'light hammer', 'light mace', 'mere club', 'planson', 'taiaha', 'tetsubo', 'wahaika', 'warhammer',],
        'Monk': ['bo staff', 'brass knuckles', 'butterfly sword', 'cestus', 'dan bong', 'deer horn knife', 'double chained kama', 'double chicken saber', 'emei piercer', 'fighting fan', 'hanbo', 'jutte', 'kama', 'kusarigama', 'kyoketsu shoge', 'lungshuan tamo', 'monk\'s spade', 'nine-ring broadsword', 'nine-section whip', 'nunchaku', 'quarterstaff', 'rope dart', 'sai', 'sanpkhang', 'sansetsukon', 'seven-branched sword', 'shang gou', 'shuriken', 'siangham', 'temple sword', 'tiger fork', 'tonfa', 'tri-point double-edged sword', 'urumi', 'wushu dart',],
        'Polearm': ['bardiche', 'bec de corbin', 'bill', 'Boarding gaff', 'crook', 'fauchard', 'glaive', 'glaive-guisarme', 'gnome ripsaw glaive', 'guisarme', 'halberd', 'hooked lance', 'lucerne hammer', 'mancatcher', 'monk\'s spade', 'naginata', 'nodachi', 'ranseur', 'rhomphaia', 'tepoztopilli', 'tiger fork',],
        'Spear': ['amentum', 'boar spear', 'chain spear', 'elven branched spear', 'javelin', 'harpoon', 'lance', 'longspear', 'orc skull ram', 'pilum', 'planson', 'shortspear', 'sibat', 'spear', 'stormshaft javelin', 'tiger fork', 'trident', 'weighted spear',],
    }
    possible_ranged = {
        'Bows': ['Composite longbow', 'composite shortbow', 'longbow', 'hornbow', 'composite hornbow', 'shortbow',],
        'Crossbow': ['double crossbow', 'hand crossbow', 'heavy crossbow', 'launching crossbow', 'light crossbow', 'heavy repeating crossbow', 'light repeating crossbow', 'tube arrow shooter',],
        'Thrown': ['aklys', 'amentum', 'atlatl', 'blowgun', 'bolas', 'boomerang', 'brutal bolas', 'Chain-hammer', 'chakram', 'club', 'dagger', 'dart', 'deer horn knife', 'dueling dagger', 'flask thrower', 'halfling sling staff', 'harpoon', 'hunga munga', 'javelin', 'kestros', 'light hammer', 'pilum', 'poisoned sand tube', 'rope dart', 'shortspear', 'shuriken', 'sibat', 'sling', 'sling glove', 'spear', 'starknife', 'stormshaft javelin', 'throwing axe', 'trident', 'wushu dart',],
    }

    def __init__(self, rare, iClass=None, iName=None):
        self.Rarity = rare
        self.Name = iName
        self.__choose_type(iClass)
        self.__choose_metal()

        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_enchantment(Enchant())
        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_masterwork(determine_rarity([1, 9]))

    def __choose_type(self, requirement=None):
        if requirement == None:
            # Make a pick with each weapon type
            if randint(2):
                self.Class = choice(list(self.possible_melee.keys()))
                self.Name = choice(list(self.possible_melee[self.Class])).title()
            else:
                self.Class = choice(list(self.possible_ranged.keys()))
                self.Name = choice(list(self.possible_ranged[self.Class])).title()
        # Existing requirement
        elif requirement in list(self.possible_melee.keys()):
            self.Class = requirement
            self.Name = choice(list(self.possible_melee[self.Class])).title()

        elif requirement in list(self.possible_ranged.keys()):
            self.Class = requirement
            self.Name = choice(list(self.possible_ranged[self.Class])).title()

        else:
            print("The requirement is not in the list of possible weapons.")
            return None

        # We have a class of weapon. Get weapon Damage
        self.Dice = str(int(self.Rarity / 2) + 1) + 'd' + str(choice(self.die_values[self.Class]))

        # print(self.Name + '\t' + self.Dice)
        # print(self.Class)

        # Give Damage Types
        if self.Class == 'Heavy Axe' or self.Class == 'Light Axe':
            self.Damage = ['S']
        elif self.Class == 'Heavy Blade' or self.Class == 'Light Blade':
            self.Damage = ['S', 'P']
        elif self.Class == 'Close':
            self.Damage = ['B', 'P']
        elif self.Class == 'Double':
            self.Damage = ['S', 'B', 'P']
        elif self.Class == 'Flail':
            self.Damage = ['B', 'S']
        elif self.Class == 'Hammer':
            self.Damage = ['B']
        elif self.Class == 'Monk':
            self.Damage = ['B', 'S', 'P']
        elif self.Class == 'Polearm':
            self.Damage = ['P', 'S']
        elif self.Class == 'Spear':
            self.Damage = ['P']
        elif self.Class == 'Bows':
            self.Damage = ['Ra', 'P', choice(['30', '40', '50', '60', '70', '80', '90', '100']) + ' ft.']
        elif self.Class == 'Crossbow':
            self.Damage = ['Ra', 'P', choice(['60', '70', '80', '90', '100', '110', '120']) + ' ft.']
        elif self.Class == 'Thrown':
            self.Damage = ['Ar', 'P', 'S', choice(['5', '10', '15', '20', '25', '30', '35', '40']) + ' ft.']
        return

    def __choose_metal(self):
        if self.Rarity > 4:
            self.Rarity %= 4

        if self.Rarity == 0:  # Common Materials
            m = self.__verify_metal(common_material)

        elif self.Rarity == 1:  # Uncommon Materials
            m = self.__verify_metal(uncommon_material)

        elif self.Rarity == 2:  # Rare Materials
            m = self.__verify_metal(rare_material)

        elif self.Rarity == 3:  # Very Rare Materials
            m = self.__verify_metal(very_rare_material)

        elif self.Rarity == 4:  # Legendary Materials
            m = self.__verify_metal(legendary_material)

        self.Name = m[0] + ' ' + self.Name
        self.__crit()
        self.__weigh(m[0], m[1])

    def __verify_metal(self, cl):
        metal = None
        while metal == None:
            metal = choice(list(cl.keys()))
            # print(metal, '=', cl[metal])
            t = 0
            while t < len(self.Damage):
                if self.Damage[t] not in cl[metal]['Type']:
                    if 'ft.' not in self.Damage[t]:
                        # print(metal, 'Not compatible with a', self.Name, '(\''+self.Damage[t]+'\')')
                        metal = None
                        t = len(self.Damage)
                t += 1
        return metal, cl

    def __crit(self):
        chance = randint(100) + self.Rarity * 10
        if chance < 75:
            self.Crit = 'x2'
        elif chance < 80:
            self.Crit = '19-20 x2'
        elif chance < 92:
            self.Crit = '18-20 x2'
        elif chance < 97:
            self.Crit = 'x3'
        elif chance < 99:
            self.Crit = '19-20 x3'
        else:
            self.Crit = '18-20 x3'

    def __weigh(self, metal, cl):
        self.Cost = self.cost_and_weight[self.Class][0] * cl[metal]['Cost'] * (self.Rarity+1) ** (self.Rarity)
        self.Weight = round(self.cost_and_weight[self.Class][1] * cl[metal]['Weight'] * 14, 1)

    def add_enchantment(self, ench):
        if self.Enchantment is None:
            self.Enchantment = ench
            self.Cost = self.Cost + self.Enchantment.Cost
        else:
            print("This Item is already enchanted.")

    def add_masterwork(self, mlevel):
        if mlevel > 10:
            mlevel %= 9
        if self.Masterwork == 0:
            self.Masterwork = mlevel
            self.Cost += (1 + mlevel) * (1 + mlevel) * 1000
            self.Name = "+" + str(mlevel) + ' ' + self.Name
            self.Dice += "+" + str(mlevel)
        # else:
        #     print("This Item is already Masterwork")

    def __str__(self):
        global MasterID
        r = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary']
        l = ["Level 0", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", ]
        dam = ''
        master = "Masterwork " if self.Masterwork > 0 else ""
        for c in self.Damage:
            dam += '\'' + c + '\','
        if self.Enchantment is None:
            s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Name + \
            ' (' + self.Class + """) </span><br /><span class="text-sm emp">""" + \
            'Damage: ' + self.Dice + ' (' + self.Crit + ') [' + dam + '] Weight: ' + \
            str(self.Weight) + """ lbs</span></td><td>""" + determine_cost(self.Cost) + \
            """</td><td>""" + master + r[self.Rarity] + """</td></tr>"""
        else:
            s = """<tr><td style="width:50%;"><span class="text-md" onclick="show_hide('""" + str(MasterID) + \
                """')" style="color:blue;">""" + self.Name + ' (' + self.Class + \
                """) </span><br /><span class="text-sm emp" id=\"""" + str(MasterID) + \
                """\" style="display: none;">""" + 'Damage: ' + self.Dice + ' (' + self.Crit + ') [' + dam + \
                '] Weight: ' + str(self.Weight) + """ lbs""" + str(self.Enchantment) + """"</span></td><td>""" + \
                determine_cost(self.Cost) + """</td><td>""" + master +  r[self.Rarity] + ', ' + \
                l[self.Enchantment.Level] + """</td></tr>"""
            MasterID += 1
        return s

    def to_string(self):
        ench = ''
        if self.Enchantment is not None:
            ench = ' ' + self.Enchantment.to_string()
        return self.Name + ench + ' (' + determine_cost(self.Cost) + ')'


class Firearm(object):
    possible = {
        'Pistol': ['Akdal Ghost TR01', 'ALFA Combat', 'ALFA Defender', 'AMT AutoMag II', 'AMT AutoMag III',
                   'AMT AutoMag IV', 'AMT Backup', 'AMT Hardballer', 'AMT Lightning pistol', 'AMT Skipper',
                   'Armatix iP1', 'Arsenal P-M02', 'Ashani', 'ASP pistol', 'Paris Theodore', 'Astra 400', 'Astra 600',
                   'Astra Model 900', 'Astra Model 903', 'Astra A-60', 'Astra A-80', 'Astra A-100', 'Ballester-Molina',
                   'Bauer Automatic', 'Bayard 1908', 'Anciens Etablissements Pieper', 'Bechowiec-1',
                   'Bataliony Chiopskie', 'Beholla pistol', 'Benelli B76', 'Benelli MP 90S', 'Benelli MP 95E',
                   'Beretta M9', 'Beretta 21A Bobcat', 'Beretta 70', 'Beretta 90two', 'Beretta 92',
                   'Beretta 92G-SD/96G-SD', 'Beretta 93R', 'Beretta 418', 'Beretta 950', 'Beretta 3032 Tomcat',
                   'Beretta 8000', 'Beretta 9000', 'Beretta Cheetah', 'Beretta M1923', 'Beretta M1934',
                   'Beretta M1935', 'Beretta M1951', 'Beretta Nano', 'Beretta Pico', 'Beretta Px4 Storm',
                   'Beretta U22 Neos', 'Bersa 83', 'Bersa Thunder 9', 'Bersa Thunder 380', 'Bergmann-Bayard',
                   'Theodor Bergmann', 'Bren Ten', 'FN Herstal', 'Browning BDM', 'Browning Buck Mark',
                   'Browning Hi-Power', 'FN Herstal', 'Brugger & Thomet MP9', 'BUL Cherokee', 'BUL Transmark',
                   'BUL M-5', 'BUL Transmark', 'BUL Storm', 'BUL Transmark', 'Calico M950', 'Campo Giro',
                   'Caracal pistol', 'Claridge Hi-Tec/Goncz Pistol', 'Colt Delta Elite', 'Colt Mustang',
                   'Colt OHWS', 'Colt SCAMP', 'CZ vz. 27', 'CZ vz. 38', 'CZ vz. 50 / CZ vz. 70', 'CZ 52', 'CZ 85',
                   'CZ 97B', 'Daewoo Precision Industries K5', 'Danuvia VD-01', 'Davis Warner Infallible', 'Deer gun',
                   'Dreyse M1907', 'Rheinische Metallwaaren- und Maschinenfabrik AG', 'FB P-64', 'FeG 37M Pistol',
                   'Fegyver- es Gepgyar', 'FEG PA-63', 'Fegyver- es Gepgyar', 'RPC Fort', 'Fort-17', 'RPC Fort',
                   'FN Baby Browning', 'FN M1900', 'FN Model 1903', 'FN M1905', 'FN Model 1910', 'FN Forty-Nine',
                   'FN Five-seven', 'FN FNP', 'FN FNS', 'FN FNX', 'FP-45 Liberator', 'Fegyver- es Gepgyar',
                   'Gaztanaga Destroyer', 'Gaztanaga', 'Glisenti Model 1910', 'Glock Ges.m.b.H.', 'Grand Power K100',
                   'GSh-18', 'Guncrafter Industries Model No. 1', 'Gyrojet',
                   'Hamada Type pistol', 'Harper\'s Ferry Model 1805', 'Harpers Ferry Armory', 'Hi-Point C-9',
                   'Hi-Point CF-380', 'Hi-Point Model JCP', 'Hi-Point Model JHP', 'High Standard HDM', 'Howdah pistol',
                   'HS2000', 'HS Produkt', 'Intratec TEC-22', 'Intratec', 'JO.LO.AR.', 'Kahr K series',
                   'Kahr MK series', 'Kahr P series', 'Kahr PM series', 'Kel-Tec P-3AT', 'Kel-Tec P-11', 'Kel-Tec P-32',
                   'Kel-Tec PF-9', 'Kel-Tec PLR-16', 'Kel-Tec PMR-30', 'Kimber Aegis',
                   'Kimber Custom', 'Kimber Eclipse', 'Kimel AP-9', 'Kongsberg Colt', 'Korovin', 'Krag-Jorgensen',
                   'KRISS KARD', 'Lahti L-35', 'Valtion Kivaaritehdas', 'Lancaster pistol', 'Lercker pistol', 'Italy',
                   'Liliput pistol', 'Llama M82', 'Luger pistol', 'Deutsche Waffen und Munitionsfabriken', 'M15 pistol',
                   'Rock Island Arsenal', 'MAB Model A', 'MAB PA-15 pistol', 'MAC Mle 1950', 'MAC-10', 'MAC-11',
                   'Makarov pistol', 'Makarych', 'Mamba Pistol', 'Mars Automatic Pistol', 'Mauser C96', 'Mauser',
                   'Mauser HSc', 'Mauser', 'MGP-15 submachine gun', 'Minebea PM-9', 'Minebea',
                   'Modele 1935 pistol', 'MP-443 Grach', 'Musgrave Pistol', 'NAACO Brigadier', 'Obregon pistol',
                   'Ortgies Semi-Automatic Pistol', 'OTs-02 Kiparis', 'OTs-23 Drotik', 'OTs-33 Pernach', 'P9RC',
                   'Fegyver- es Gepgyar', 'PAMAS modele G1', 'Para-Ordnance P14-45', 'Para USA', 'Pardini GT9',
                   'Pindad G2', 'Pindad P3', 'Pindad', 'Pindad PS-01', 'Pindad', 'Pistol model 2000', 'Pistole vz. 22',
                   'PP-2000', 'Prilutsky M1914', 'PSM pistol', 'QSW-06', 'QSZ-92', 'Remington 1911 R1',
                   'Remington Model 51', 'Remington R51', 'Remington Rider Single Shot Pistol', 'Remington XP-100',
                   'Remington Zig-Zag Derringer', 'Rock Island Armory 1911 series', 'Rohrbaugh R9', 'Ruby pistol',
                   'Ruger Hawkeye', 'Ruger LCP', 'Ruger LC9', 'Ruger MP9', 'Ruger SR1911', 'Sauer 38H',
                   'Savage Model 1907', 'Schwarzlose Model 1898', 'Schonberger-Laumann 1892', 'SP-21 Barak',
                   'SPP-1 underwater pistol', 'Star Firestar M43', 'Star Model 14', 'Star Model S', 'Star Ultrastar',
                   'Steyr GB', 'Steyr M', 'Steyr TMP', 'Steyr M1912', 'Sugiura pistol', 'Tanfoglio Force', 'Tanfoglio',
                   'Tanfoglio GT27', 'Tanfoglio', 'Tanfoglio T95', 'Tanfoglio', 'Taurus PT92',
                   'Taurus Millennium series', 'Taurus PT1911', 'TEC-9', 'Intratec', 'TP-82', 'TT pistol',
                   'Tokarev TT-33', 'Fedor Tokarev', 'Trejo pistol', 'Type 14 Nambu', 'Type 64 pistol',
                   'Type 77 pistol', 'Israel Military Industries', 'Vektor CP1', 'Vektor SP1', 'Viper Jaws pistol',
                   'Volkspistole', 'Mauser', 'Walther CCP', 'Walther HP', 'Walther Model 9', 'Walther P5',
                   'Walther P22', 'Walther P38', 'Walther P88', 'Walther P99', 'Walther PP', 'Walther PK380',
                   'Walther PPQ', 'Walther PPS', 'Walther TPH', 'Webley Self-Loading Pistol', 'Welrod',
                   'Werder pistol model 1869', 'Johann Ludwig Werder', 'Whitney Wolverine', 'Wildey', 'WIST-94',
                   'Zaragoza Corla', 'Zastava P25', 'Zastava M57', 'Zastava M70', 'Zastava M88', 'Zastava PPZ', ],
        'Rifle': ['1792 contract rifle', 'Advanced Combat Rifle', 'ArmaLite AR-5', 'ArmaLite AR-7', 'ArmaLite AR-10',
                  'ArmaLite AR-30', 'Barrett REC7', 'Barrett XM109', 'Barrett XM500', 'Bendix Hyde carbine',
                  'Berdan rifle', 'Browning BLR', 'Burnside carbine', 'Bushmaster Arm Pistol',
                  'Bushmaster M4-type Carbine', 'Bushmaster M17S', 'CAR-15', 'Close Quarters Battle Receiver',
                  'CMMG Mk47 Mutant', 'Advanced Colt Carbine-Monolithic', 'Colt Advanced Piston Carbine',
                  'Colt Lightning Carbine', 'Colt Model 1839 Carbine', 'Colt Ring Lever rifles', 'Colt-Burgess rifle',
                  'Crazy Horse rifle', 'Demro TAC-1', 'Frank Wesson Rifles', 'Grendel R31', 'Harpers Ferry Model 1803',
                  'Hawken rifle', 'Henry rifle', 'Hi-Point Carbine', 'Hillberg carbine', 'Individual Carbine',
                  'Iver Johnson AMAC-1500', 'Krag-Jorgensen', 'M1 Garand', 'M4 carbine', 'M14 rifle', 'M16 rifle',
                  'M21 Sniper Weapon System', 'M27 Infantry Automatic Rifle', 'M86 Rifle',
                  'M231 Firing Port Weapon', 'M1819 Hall rifle', 'M1885 Remington-Lee', 'M1895 Lee Navy',
                  'M1903 Springfield', 'M1917 Enfield', 'M1918 Browning Automatic Rifle', 'M1922 Bang rifle',
                  'M1941 Johnson rifle', 'M1944 Hyde Carbine', 'M1947 Johnson auto carbine', 'Marlin Levermatic',
                  'Marlin Model 20', 'Marlin Model 60', 'Marlin Model 70P', 'Marlin Model 336', 'Marlin Model 780',
                  'Marlin Model 795', 'Marlin Model 1894', 'Marlin Model Golden 39A', 'Marlin Model XT-22',
                  'Maynard carbine', 'Mk 14 Enhanced Battle Rifle', 'Model 1814 common rifle',
                  'Model 1817 common rifle', 'Mosin-Nagant', 'Mossberg 464', 'Mossberg Plinkster', 'Palmer carbine',
                  'Pedersen rifle', 'Precision Sniper Rifle', 'PTR rifle', 'Remington ACR', 'Remington Model 5',
                  'Remington Model 241', 'Remington Model 572', 'Remington Model 600', 'Remington Model 660',
                  'Remington Model 673', 'Remington Model 700', 'Remington Model 721', 'Remington Model 750',
                  'Remington Model 760', 'Remington Model 770', 'Remington Model 7400', 'Remington Model 7600',
                  'Remington Rolling Block rifle', 'Ruger American Rifle', 'Ruger M77', 'Ruger SR-556',
                  'Savage Model 99', 'Savage Model 110', 'SEAL Recon Rifle', 'Sharps & Hankins Model 1862 Carbine',
                  'Sharps rifle', 'Smith & Wesson M&P10', 'Smith & Wesson M&P15', 'Smith & Wesson M&P15-22',
                  'Smith & Wesson Model 1940 Light Rifle', 'Spencer repeating rifle', 'Springfield Model 1865',
                  'Springfield Model 1866', 'Springfield Model 1868', 'Springfield Model 1869',
                  'Springfield model 1870', 'Springfield model 1870 Remington-Navy', 'Springfield model 1871',
                  'Springfield model 1873', 'Springfield Model 1875', 'Springfield Model 1877',
                  'Springfield model 1880', 'Springfield Model 1882', 'Springfield model 1884',
                  'Springfield Model 1886', 'Springfield Model 1888', 'Springfield Model 1892-99',
                  'Springfield Model 1922', 'Springfield rifle', 'Starr carbine', 'Stoner 63', 'T48 rifle',
                  'Thompson Autorifle', 'Thompson Light Rifle', 'Tubb 2000',
                  'United States Army Squad Designated Marksman Rifle',
                  'United States Marine Corps Designated Marksman Rifle', 'Volcanic Repeating Arms',
                  'Winchester Hotchkiss', 'Winchester Model 67', 'Winchester Model 68', 'Winchester Model 69',
                  'Winchester Model 1886', 'Winchester Model 1890', 'Winchester Model 1892', 'Winchester Model 1894',
                  'Winchester Model 1895', 'Winchester Model 1906', 'Winchester Model 1907', 'Winchester rifle',
                  'Winder musket', 'AAC Honey Badger', 'AAI ACR', 'Adcor A-556', 'ADS amphibious rifle',
                  'Advanced Combat Rifle', 'Advanced Individual Combat Weapon', 'AG-043', 'AK-9', 'AK-12', 'AK-47',
                  'AK-63', 'AK-74', 'AK-100 (rifle family)', 'AK-103', 'AK-104', 'AK-105', 'AKM', 'AKMSU', 'AL-7',
                  'AMD-65', 'AMP-69', 'AMR-69', 'AO-27 rifle', 'AO-35 assault rifle', 'AO-38 assault rifle',
                  'AO-46 (firearm)', 'AO-63 assault rifle', 'APS underwater rifle', 'AR-M1', 'Ares Shrike 5.56',
                  'ArmaLite AR-15', 'Armtech C30R', 'AS Val', 'AS-44', 'ASh-12.7', 'ASM-DT amphibious rifle',
                  'Barrett M468', 'Bendix Hyde carbine', 'Beretta AS70/90', 'BSA 28P', 'CAR 816', 'CEAM Modele 1950',
                  'CETME', 'CETME rifle', 'Close Quarters Battle Receiver', 'CMMG Mk47 Mutant', 'Colt ACR',
                  'Colt Advanced Piston Carbine', 'Comparison of the AK-47 and M16',
                  'Conventional Multirole Combat Rifle', 'CornerShot', 'Cristobal Carbine', 'CZ 807', 'CZ 2000',
                  'Dlugov assault rifle', 'EM-2 rifle', 'EM-4 rifle', 'EMERK', 'FA-MAS Type 62', 'FB Mini-Beryl',
                  'FB Onyks', 'FB Tantal', 'Featureless rifles', 'Floro PDW', 'Gahendra Rifle', 'Grad AR',
                  'GRAM 63 battle rifle', 'Grossfuss Sturmgewehr', 'Heckler & Koch G11', 'Heckler & Koch G36',
                  'Heckler & Koch HK36', 'Heckler & Koch HK416', 'Howa Type 64', 'Howa Type 89', 'IWI Tavor 7',
                  'Interdynamics MKR', 'Interdynamics MKS', 'IWI ACE', 'IWI Tavor X95', 'Kalashnikov rifle',
                  'Kbkg wz. 1960', 'L64/65', 'LAPA FA-03', 'Lightweight Small Arms Technologies', 'LR-300',
                  'LSAT rifle', 'LVOA-C', 'LWRC M6', 'M4 carbine', 'M4-WAC-47', 'M231 Firing Port Weapon',
                  'M1944 Hyde Carbine', 'Madsen LAR', 'MPT-76', 'MR-C', 'MSBS rifle',
                  'Multi Caliber Individual Weapon System', 'Nesterov assault rifle', 'Norinco Type 86S',
                  'Objective Individual Combat Weapon', 'OTs-12 Tiss', 'OTs-14 Groza', 'PAPOP', 'Pindad SS3',
                  'Pistol Mitraliera model 1963/1965', 'POF Eye', 'Project Abakan', 'Pusca Automata model 1986',
                  'QBZ-03', 'QTS-11', 'RK 62', 'RK 95 TP', 'SA M-7', 'SIG Sauer SIG516', 'SIG Sauer SIGM400', 'SLEM-1',
                  'SR-3 Vikhr', 'Steyr ACR', 'STG-556', 'Sturmgewehr 52', 'Sturmgewehr 58', 'Thompson Light Rifle',
                  'TKB-010', 'TKB-011', 'TKB-022PM', 'TKB-059', 'TKB-072', 'TKB-0146', 'TKB-408', 'TKB-517',
                  'Type 56 assault rifle', 'Type 58 assault rifle', 'Type 63 assault rifle', 'Type 81 assault rifle',
                  'United States Army Squad Designated Marksman Rifle', 'VAHAN (firearm)', 'VB Berapi LP06', 'Vepr',
                  'Vollmer M35', 'Vz. 58', 'Maschinenkarabiner 42(W)', 'WASR-series rifles', 'Wimmersperg Spz',
                  'Winchester LMR', 'Zastava M70', 'Zastava M77 B1', 'Zastava M90', ],
        'Sniper': ['Anzio 20mm rifle', 'Barrett M82', 'Barrett M90', 'Barrett M95', 'Barrett Model 98B', 'Barrett MRAD',
                   'CheyTac Intervention', 'Desert Tech HTI', 'Desert Tech SRS', 'EDM Arms Windrunner',
                   'Grizzly Big Boar', 'H-S Precision Pro Series 2000 HTR', 'Harris Gun Works M-96',
                   'Knight\'s Armament Company SR-25', 'Longbow T-76', 'M1 Garand', 'M24 Sniper Weapon System',
                   'M25 Sniper Weapon System', 'M39 Enhanced Marksman Rifle', 'M40 rifle',
                   'M110 Semi-Automatic Sniper System', 'M1903 Springfield', 'McMillan TAC-50', 'MICOR Leader 50',
                   'Mk 12 Special Purpose Rifle', 'Pauza P-50', 'Precision-guided firearm', 'Remington Model 700',
                   'Remington MSR', 'Remington Semi Automatic Sniper System', 'Robar RC-50', 'Savage 10FP',
                   'Savage 110 BA', 'United States Marine Corps Squad Advanced Marksman Rifle',
                   'M2010 Enhanced Sniper Rifle', ],
        'Shotgun': ['Blunderbuss', 'Cynergy Shotgun', 'TOZ-106', 'Ithaca Mag-10', 'Remington Model SP-10',
                    'Winchester Model 1200', 'Marlin Model 55', 'Akdal MKA', 'Armsel Striker',
                    'Atchisson Assault Shotgun', 'Baikal MP-153', 'Bandayevsky RB-12', 'Benelli M4',
                    'Benelli Raffaello', 'Benelli Supernova', 'Benelli Vinci', 'Beretta FP', 'Beretta A303',
                    'Beretta DT-10', 'Beretta Xtrema 2', 'Browning Double Automatic Shotgun', 'FN Herstal',
                    'Ciener Ultimate Over/Under', 'ENARM Pentagun', 'Fabarm SDASS Tactical', 'FN SLP', 'FN TPS',
                    'FN SC-1', 'Franchi SPAS-12', 'Franchi SPAS-15', 'Heckler & Koch FABARM FP6',
                    'Heckler & Koch HK CAWS', 'High Standard Model 10', 'KAC Masterkey', 'Kel-Tec KSG',
                    'M26 Modular Accessory Shotgun System', 'MAG-7', 'MAUL (shotgun)', 'Mossberg 930', 'NeoStead',
                    'Norinco HP9-1', 'Pancor Jackhammer', 'Remington Model 10', 'Remington Model 878',
                    'Remington Model 887', 'Remington Spartan 453', 'RMB-93', 'Ruger Gold Label', 'Sjogren shotgun',
                    'TOZ-194', 'USAS-12', 'Valtro PM-5/PM-5-350', 'Weatherby Orion', 'Winchester Model', 'Browning BSS',
                    'Molot Bekas-M', 'Browning Auto-5', 'Browning Superposed', 'Remington Model 11',
                    'Remington Model 31', 'Remington Model 58', 'Stevens Model 520/620', 'Winchester Model 1897',
                    'Stoeger Condor', 'Ithaca 37', 'Winchester Model 1897', 'Winchester Model 1887', 'Browning Citori',
                    'Cooey 84', 'Remington Model 11-48', 'Remington Model 870', 'Remington Model 1912',
                    'Winchester Model 21', 'Winchester Model 37', 'Benelli M1', 'Benelli M3', 'Benelli Nova',
                    'Beretta AL391', 'H&R Ultraslug Hunter', 'Remington Model 11-87', 'Weatherby SA-08', 'Mossberg 500',
                    'Mossberg 590', 'Remington Spartan 100', 'Saiga-12', 'Stoeger Coach Gun', 'Blaser F3',
                    'Beretta 682', 'Beretta Silver Pigeon', 'Remington Spartan 310', 'MTs-255', 'Remington Model 17',
                    'Franchi AL-48', 'KS-23', 'RGA-86', 'Winchester Model 20', 'Vepr-12', ],
    }
    cost_and_weight = {
        'Pistol': [1000, .8],
        'Rifle': [2500, 2],
        'Sniper': [10000, 5],
        'Shotgun': [5000, 3],
    }
    Weight = Cost = Rarity = Masterwork = Range = Capacity = 0
    Name = Dice = Crit = Class = ''
    Enchantment = None

    def __init__(self, rarity, iClass=None, iName=None):
        if iClass is None or iClass not in list(self.possible.keys()):
            self.Class = choice(list(self.possible.keys()))
        self.Rarity = rarity
        self.Crit = 'x' + str(randint(2, 5))
        self.__choose_metal()
        self.Name += choice(self.possible[self.Class])

        if self.Class == 'Pistol':
            self.Capacity = int(choice([1, 2, 4, 6, 8]))
            self.Range = 10 + randint(1, 4) * 5 * (self.Rarity + 1)
            self.Dice = str(int((self.Rarity + 2) / 2)) + 'd' + str(choice([4, 6, 8]))

        elif self.Class == 'Rifle':
            self.Capacity = int(10 + randint(1, 8) * 5)
            self.Range = 10 + randint(1, 6) * 5 * (self.Rarity + 1)
            self.Dice = str(int((self.Rarity + 2) / 2)) + 'd' + str(choice([4, 6, 8, 10]))

        elif self.Class == 'Shotgun':
            self.Capacity = int(choice([1, 2, 4, 6, 8, 10, 12]))
            self.Range = randint(3, 6) * 5 * (self.Rarity + 1)
            self.Dice = str(int((self.Rarity + 2) / 2)) + 'd' + str(choice([6, 8, 10, 12]))

        elif self.Class == 'Sniper':
            self.Capacity = int(choice([1, 2, 4]))
            self.Range = 30 + randint(3, 7) * 10 * (self.Rarity + 1)
            self.Dice = str(int((self.Rarity + 2) / 2)) + 'd' + str(choice([8, 10, 12]))

        if iName is not None:
            self.Name = iName

        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_enchantment(Enchant())
        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_masterwork(determine_rarity([1, 9]))

    def __choose_metal(self):
        if self.Rarity > 4:
            self.Rarity %= 4

        cl = [common_material, uncommon_material, rare_material, very_rare_material, legendary_material][self.Rarity]
        metal = None
        while metal is None:
            metal = choice(list(cl.keys()))
            if 'HA' in cl[metal]['Type'] and 'P' in cl[metal]['Type']:
                self.Name += metal + ' '
            else:
                metal = None
        self.Cost = self.cost_and_weight[self.Class][0] * cl[metal]['Cost'] * (self.Rarity + 1) ** self.Rarity
        self.Weight = round(self.cost_and_weight[self.Class][1] * cl[metal]['Weight'] * 4, 1)

    def add_enchantment(self, ench):
        if self.Enchantment is None:
            self.Enchantment = ench
            self.Cost = self.Cost + self.Enchantment.Cost
        else:
            print("This Item is already enchanted.")

    def add_masterwork(self, mlevel):
        if mlevel > 10:
            mlevel %= 9
        if self.Masterwork == 0:
            self.Masterwork = mlevel
            self.Cost += (1 + mlevel) * (1 + mlevel) * 1000
            self.Name = "+" + str(mlevel) + ' ' + self.Name
            self.Dice += "+" + str(mlevel)
        # else:
        #     print("This Item is already Masterwork")

    def __str__(self):
        global MasterID
        r = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary']
        l = ["Level 0", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", ]
        dam = ''
        master = "Masterwork " if self.Masterwork > 0 else ""
        if self.Enchantment is None:
            s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Name.title() + ' (' + self.Class + \
            ') </span><br /><span class="text-sm emp">' + 'Damage: ' + self.Dice + ' (' + self.Crit + ') Weight: ' + \
            str(self.Weight) + ' lbs. Range:' + str(self.Range) + "ft.</span></td><td>" + determine_cost(self.Cost) + \
            """</td><td>""" + master + r[self.Rarity] + """</td></tr>"""
        else:
            s = """<tr><td style="width:50%;"><span class="text-md" onclick="show_hide('""" + str(MasterID) + \
                """')" style="color:blue;">""" + self.Name.title() + ' (' + self.Class + \
                """) </span><br /><span class="text-sm emp" id=\"""" + str(MasterID) + \
                """\" style="display: none;">""" + 'Damage: ' + self.Dice + ' (' + self.Crit + ') Weight: ' + \
                str(self.Weight) + ' lbs. Range:' + str(self.Range) + ' ft.' + str(self.Enchantment) + "</span>" + \
                """</td><td>""" + determine_cost(self.Cost) + """</td><td>""" + master + r[self.Rarity] + ', ' + \
                l[self.Enchantment.Level] + """</td></tr>"""
            MasterID += 1
        return s


class Armor(object):
    light_armor = {
        # Name	: 			HP, AC, Cost, Weight
        'Padded':			[5, 1, 5, 10],
        'Leathered':		[10, 1, 10, 15],
        'Studded':	        [15, 2, 25, 20],
        'Chained':	        [20, 2, 100, 25],
    }
    medium_armor = {
        # Name	: 			HP, AC, Cost, Weight
        'Hide':	            [15, 2, 15, 25, ],
        'Scale mail':		[20, 2, 50, 30, ],
        'Chainmail':		[25, 3, 150, 40, ],
        'Breastplate':		[25, 3, 200, 30, ],
    }
    heavy_armor = {
        # Name	: 			HP, AC, Cost, Weight
        'Splint mail':		[30, 3, 200, 45, ],
        'Banded mail':		[30, 3, 250, 35, ],
        'Half-plate':		[35, 4, 600, 50, ],
        'Full plate':		[40, 4, 1500, 50, ],
    }
    shield = {
        # Name	: 			HP, AC, Cost, Weight
        'Buckler':			[5, 1, 5, 5, ],
        'Light Shield':	    [10, 1, 9, 6, ],
        'Heavy Shield':	    [20, 2, 20, 15, ],
        'Tower Shield':	    [20, 4, 30, 45, ],
        # Wooden cost's 2/3's less
    }

    Weight = Cost = Rarity = Masterwork = AC = 0
    Name = Class = ''
    Metal = Enchantment = None

    def __init__(self, rare, iClass=None, iName=None):
        self.Rarity = rare
        self.Name = iName
        self.Class = iClass
        self.__choose_metal()
        self.__choose_type()

        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_enchantment(Enchant())
        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_masterwork(determine_rarity([1, 9]))

    def __choose_metal(self):
        if self.Rarity > 4:
            self.Rarity %= 4

        if self.Rarity == 0:
            self.Metal = choice(list(common_material.keys()))
            self.AC = round(common_material[self.Metal]['AC'] / 10)
            self.Cost = common_material[self.Metal]['Cost']
            self.Weight = common_material[self.Metal]['Weight']
        elif self.Rarity == 1:
            self.Metal = choice(list(uncommon_material.keys()))
            self.AC = round(uncommon_material[self.Metal]['AC'] / 10)
            self.Cost = uncommon_material[self.Metal]['Cost']
            self.Weight = uncommon_material[self.Metal]['Weight']
        elif self.Rarity == 2:
            self.Metal = choice(list(rare_material.keys()))
            self.AC = round(rare_material[self.Metal]['AC'] / 10)
            self.Cost = rare_material[self.Metal]['Cost']
            self.Weight = rare_material[self.Metal]['Weight']
        elif self.Rarity == 3:
            self.Metal = choice(list(very_rare_material.keys()))
            self.AC = round(very_rare_material[self.Metal]['AC'] / 10)
            self.Cost = very_rare_material[self.Metal]['Cost']
            self.Weight = very_rare_material[self.Metal]['Weight']
        elif self.Rarity == 4:
            self.Metal = choice(list(legendary_material.keys()))
            self.AC = round(legendary_material[self.Metal]['AC'] / 10)
            self.Cost = legendary_material[self.Metal]['Cost']
            self.Weight = legendary_material[self.Metal]['Weight']

    def __choose_type(self):
        if self.Class not in ['Light', 'Medium', 'Heavy', 'Shield'] or self.Class is None:
            self.Class = choice(['Light', 'Medium', 'Heavy', 'Shield'])
        if self.Class == 'Light':
            c = choice(list(self.light_armor.keys()))
            self.AC += self.light_armor[c][1]
            self.Cost = round(self.Cost * self.light_armor[c][2] * (self.Rarity+1) ** self.Rarity)
            self.Weight *= round(self.light_armor[c][3], 1)
            self.Name = c + " " + self.Metal
            if c == 'Leathered' and self.Metal == "Leather":
                self.Name = "Leather"
        elif self.Class == 'Medium':
            c = choice(list(self.medium_armor.keys()))
            self.AC += self.medium_armor[c][1]
            self.Cost = round(self.Cost * self.medium_armor[c][2] * (self.Rarity+1) ** self.Rarity)
            self.Weight *= round(self.medium_armor[c][3], 1)
            self.Name = self.Metal + " " + c
        elif self.Class == 'Heavy':
            c = choice(list(self.heavy_armor.keys()))
            self.AC += self.heavy_armor[c][1]
            self.Cost = round(self.Cost * self.heavy_armor[c][2] * (self.Rarity+1) ** self.Rarity)
            self.Weight *= round(self.heavy_armor[c][3], 1)
            self.Name = self.Metal + " " + c
        else:
            c = choice(list(self.shield.keys()))
            self.AC += self.shield[c][1]
            self.Cost = round(self.Cost * self.shield[c][2] * (self.Rarity+1) ** self.Rarity)
            self.Weight *= round(self.shield[c][3], 1)
            self.Name = self.Metal + " " + c
        # print(c)

    def __str__(self):
        global MasterID
        r = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary']
        l = ["Level 0", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", ]
        master = "Masterwork " if self.Masterwork > 0 else ""
        if self.Enchantment is None:
            s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Name + ' (' + self.Class + \
                """) </span><br /><span class="text-sm emp">""" + 'AC: +' + str(self.AC) + ' Weight: ' + \
                str(self.Weight) + """ lbs</span></td><td>""" + determine_cost(self.Cost) + """</td><td>""" + \
                master + r[self.Rarity] + """</td></tr>"""
        else:
            s = """<tr><td style="width:50%;"><span class="text-md" onclick="show_hide('""" + str(MasterID) + \
                """')" style="color:blue;">""" + self.Name + ' (' + self.Class + \
                """) </span><br /><span class="text-sm emp" id=\"""" + str(MasterID) + \
                """\" style="display: none;">""" + 'AC: +' + str(self.AC) + ' Weight: ' + str(self.Weight) + " lbs " + \
                str(self.Enchantment) + """</span></td><td>""" + determine_cost(self.Cost) + """</td><td>""" + \
                master + r[self.Rarity] + ', ' + l[self.Enchantment.Level] + """</td></tr>"""
            MasterID += 1
        return s

    def add_enchantment(self, ench):
        if self.Enchantment is None:
            self.Enchantment = ench
            self.Cost = round(self.Cost + self.Enchantment.Cost)
        else:
            print("This Item is already enchanted.")

    def add_masterwork(self, mlevel):
        if mlevel > 10:
            mlevel %= 9
        if self.Masterwork == 0:
            self.Masterwork = mlevel
            self.Cost += 2 * mlevel * mlevel * 1000
            self.Name = "+" + str(mlevel) + ' ' + self.Name
            self.AC += mlevel
        # else:
        #     print("This Item is already Masterwork")

    def to_string(self):
        ench = ''
        if self.Enchantment is not None:
            ench = ' ' + self.Enchantment.to_string()
        return self.Name + ench + ' (' + determine_cost(self.Cost) + ')'


class Scroll(object):
    Name_Potential = ['Scroll of ', 'Scroll of ', 'Scroll of ', 'Tome of ', 'Spellbook of ', 'Book of ', ]
    Name = Spell = Add = ''
    Enchantment = None
    Cost = 0

    def __init__(self, level, spell=None, naming=True):
        if spell is None:
            if level == 0:
                self.Spell = choice(level_0)
                self.Cost = 12.5
            elif level == 1:
                self.Spell = choice(level_1)
                self.Cost = 25
            elif level == 2:
                self.Spell = choice(level_2)
                self.Cost = 150
            elif level == 3:
                self.Spell = choice(level_3)
                self.Cost = 375
            elif level == 4:
                self.Spell = choice(level_4)
                self.Cost = 700
            elif level == 5:
                self.Spell = choice(level_5)
                self.Cost = 1125
            elif level == 6:
                self.Spell = choice(level_6)
                self.Cost = 1650
            elif level == 7:
                self.Spell = choice(level_7)
                self.Cost = 2275
            elif level == 8:
                self.Spell = choice(level_8)
                self.Cost = 3000
            elif level == 9:
                self.Spell = choice(level_9)
                self.Cost = 4825

            if self.Spell in odd_price:
                self.Cost = round(self.Cost * odd_price[self.Spell])

            self.Enchantment = Enchant(iSpell=self.Spell, rechargable=False)
        else:
            if find_spell_level(spell) == level:
                self.Spell = spell
                self.Enchantment = Enchant(iSpell=self.Spell, rechargable=False)

        if naming:
            self.Name = self.Name_Potential[randint(len(self.Name_Potential))] + self.Spell
        else:
            self.Name = self.Spell
            self.Add = '+'

    def __str__(self):
        # print(self.Enchantment.Level)
        global MasterID
        l = ["Level 0", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", ]

        s = """<tr><td style="width:50%;"><span class="text-md" onclick="show_hide('""" + str(MasterID) + \
            """')" style="color:blue;">""" + self.Name + """</span><br /><span class="text-sm emp" id=\"""" + \
            str(MasterID) + """\" style="display: none;">""" + str(self.Enchantment) + """</span></td><td>""" + \
            self.Add + determine_cost(self.Cost) + """</td><td>""" + l[self.Enchantment.Level] + """</td></tr>"""
        MasterID += 1
        return s

    def to_string(self):
        return self.Name + ' (' + str(self.Cost) + ')'


class Enchant(object):
    Spell = Description = ""
    Level = Cost = Uses = 0

    def __init__(self, iSpell=None, rechargable=True):
        self.Spell = iSpell

        if self.Spell is not None:
            self.Level = find_spell_level(self.Spell)
        else:
            self.Level = choice(list(level_likelihood.keys()), p=list(level_likelihood.values()))
            if self.Level == 0:
                self.Spell = choice(level_0)
            elif self.Level == 1:
                self.Spell = choice(level_1)
            elif self.Level == 2:
                self.Spell = choice(level_2)
            elif self.Level == 3:
                self.Spell = choice(level_3)
            elif self.Level == 4:
                self.Spell = choice(level_4)
            elif self.Level == 5:
                self.Spell = choice(level_5)
            elif self.Level == 6:
                self.Spell = choice(level_6)
            elif self.Level == 7:
                self.Spell = choice(level_7)
            elif self.Level == 8:
                self.Spell = choice(level_8)
            elif self.Level == 9:
                self.Spell = choice(level_9)

        self.__lp()

        if rechargable:
            self.Uses = choice([2, 4, 6, 8, 10, 12], p=[.35, .3, .15, .1, .05, .05])
            self.Cost += self.Uses * (self.Level+1) ** self.Level
            self.__describe(rechargable)
        else:
            self.Uses = 1
            self.__describe(rechargable)

    def __lp(self):
            if self.Level == 0:
                self.Cost = 12.5
            elif self.Level == 1:
                self.Cost = 25
            elif self.Level == 2:
                self.Cost = 150
            elif self.Level == 3:
                self.Cost = 375
            elif self.Level == 4:
                self.Cost = 700
            elif self.Level == 5:
                self.Cost = 1125
            elif self.Level == 6:
                self.Cost = 1650
            elif self.Level == 7:
                self.Cost = 2275
            elif self.Level == 8:
                self.Cost = 3000
            elif self.Level == 9:
                self.Cost = 4825
            # Odd pricing for more complex spells
            if self.Spell in odd_price:
                self.Cost *= odd_price[self.Spell]

    def __describe(self, recharge):
        deets = find_spell_details(self.Spell)
        usable = ""
        if recharge:
            usable += "<p>This item has " + str(self.Uses) + " charges. You may cast the spell at a level above the " + \
                     "natural spell level, but for every spell level above, expend an additional charge until " + \
                     "depletion. Once depleted, roll 1d20. On a Natural 1, the item is destroyed. This item " + \
                     "regenerates 1d" + str(self.Uses) + " charges at Sunrise.</P>"
        self.Description = '<p>Name: <a href="' + deets[0] + '">' + self.Spell + '</a> (' + deets[1] + \
                           ')</p><p>Casting: ' + deets[2] + ' | ' + deets[3] + ' | ' + deets[4] + '</p>' + usable + \
                           deets[5]

    def __str__(self):
        return self.Description

    def to_string(self):
        return self.Spell + ' (' + determine_cost(self.Cost) + ')'


class Book(object):
    g = {
        0: 'Children',
        1: 'Drama',
        2: 'Fiction',
        3: 'Horror',
        4: 'Humor',
        5: 'Mystery',
        6: 'Nonfiction',
        7: 'Romance',
        8: 'SciFi',
        9: 'Tome',
    }

    Name = Genre = ''
    Cost = 0

    def __init__(self, rarity):
        self.Genre = self.g[rarity]
        self.Name = str(Books(genre=self.Genre))
        self.Cost = 0.5 + random_sample()

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Name + \
            """</span></td><td>""" + determine_cost(self.Cost) + """</td><td>""" + \
            self.Genre + """</td></tr>"""
        return s

    def to_string(self):
        return self.Name + ' (Book) (' + determine_cost(self.Cost) + ')'


class Potion(object):
    Name_Potential = ['Potion of ', 'Potion of ', 'Potion of ', 'Potion of ', 'Potion of ', 'Potion of ', 'Potion of ', 'Potion of ', 'Oil of ', 'Tincture of ', 'Solution of ', 'Philter of ', 'Draught of ', 'Elixir of ', 'Draft of ', 'Brew of ', ]
    Spell = Name = ""
    Cost = 0
    Enchantment = None

    def __init__(self, level, spell=None):
        if spell is None:
            if level == 0:
                self.Spell = choice(level_0)
                self.Cost = 13
            elif level == 1:
                self.Spell = choice(level_1)
                self.Cost = 25
            elif level == 2:
                self.Spell = choice(level_2)
                self.Cost = 150
            elif level == 3:
                self.Spell = choice(level_3)
                self.Cost = 375
            elif level == 4:
                self.Spell = choice(level_4)
                self.Cost = 700
            elif level == 5:
                self.Spell = choice(level_5)
                self.Cost = 1125
            elif level == 6:
                self.Spell = choice(level_6)
                self.Cost = 1650
            elif level == 7:
                self.Spell = choice(level_7)
                self.Cost = 2275
            elif level == 8:
                self.Spell = choice(level_8)
                self.Cost = 3000
            elif level == 9:
                self.Spell = choice(level_9)
                self.Cost = 4825

            if self.Spell in odd_price:
                self.Cost = round(self.Cost * odd_price[self.Spell])

            self.Enchantment = Enchant(iSpell=self.Spell, rechargable=False)
        else:
            if find_spell_level(spell) == level:
                self.Spell = spell
                self.Enchantment = Enchant(iSpell=self.Spell, rechargable=False)

        self.Name = self.Name_Potential[randint(len(self.Name_Potential))] + self.Spell

    def __str__(self):
        # print(self.Enchantment.Level)
        global MasterID
        l = ["Level 0", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", ]

        s = """<tr><td style="width:50%;"><span class="text-md" onclick="show_hide('""" + str(MasterID) + \
            """')" style="color:blue;">""" + self.Name + """</span><br /><span class="text-sm emp" id=\"""" + \
            str(MasterID) + """\" style="display: none;">""" + str(self.Enchantment) + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + l[self.Enchantment.Level] + """</td></tr>"""
        MasterID += 1
        return s

    def to_string(self):
        return self.Name + ' (' + determine_cost(self.Cost) + ')'


class Wand(object):
    Name_Potential = ['Rod of ', 'Rod of ', 'Stave of ', 'Scepter of ', 'Staff of ', 'Staff of ', 'Wand of ', 'Wand of ', ]
    Spell = Name = ""
    Level = Cost = 0
    Enchantment = None

    def __init__(self, level, spell=None):
        if spell is None:
            if level == 0:
                self.Spell = choice(level_0)
                self.Cost = 13
            elif level == 1:
                self.Spell = choice(level_1)
                self.Cost = 25
            elif level == 2:
                self.Spell = choice(level_2)
                self.Cost = 150
            elif level == 3:
                self.Spell = choice(level_3)
                self.Cost = 375
            elif level == 4:
                self.Spell = choice(level_4)
                self.Cost = 700
            elif level == 5:
                self.Spell = choice(level_5)
                self.Cost = 1125
            elif level == 6:
                self.Spell = choice(level_6)
                self.Cost = 1650
            elif level == 7:
                self.Spell = choice(level_7)
                self.Cost = 2275
            elif level == 8:
                self.Spell = choice(level_8)
                self.Cost = 3000
            elif level == 9:
                self.Spell = choice(level_9)
                self.Cost = 4825

            if self.Spell in odd_price:
                self.Cost = round(self.Cost * odd_price[self.Spell])

            self.Enchantment = Enchant(iSpell=self.Spell)
        else:
            if find_spell_level(spell) == level:
                self.Spell = spell
                self.Enchantment = Enchant(iSpell=self.Spell)
        self.Name = self.Name_Potential[randint(len(self.Name_Potential))] + self.Spell

    def __str__(self):
        # print(self.Enchantment.Level)
        global MasterID
        l = ["Level 0", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", ]

        s = """<tr><td style="width:50%;"><span class="text-md" onclick="show_hide('""" + str(MasterID) + \
            """')" style="color:blue;">""" + self.Name + """</span><br /><span class="text-sm emp" id=\"""" + \
            str(MasterID) + """\" style="display: none;">""" + str(self.Enchantment) + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + l[self.Enchantment.Level] + """</td></tr>"""
        MasterID += 1
        return s

    def to_string(self):
        return self.Name + ' (' + determine_cost(self.Cost) + ')'


class Inn(object):
    Store_name = ""
    Shopkeeper = Rooms = None
    Edibles = Stock = []
    Cost = Inflation = Quality = 0

    def __init__(self, keeper, name, service, qual, rooms, quan):
        self.Shopkeeper = keeper
        self.Store_name = name
        self.Inflation = service
        self.Stock = []
        self.Quality = qual

        self.__fill_rooms(rooms)
        self.__fill_stock(quan)

    def __fill_rooms(self, rooms):
        self.Rooms = []
        for n in range(1, rooms+1):
            r = Room(n, self.Quality)
            r.Cost *= self.Inflation
            self.Rooms.append(r)


    def __fill_stock(self, quan):
        # Add room Price
        for item in self.Rooms:
            self.Stock.append(item)
        for _ in range(quan):
            d = Drink(self.Quality)
            d.Cost *= self.Inflation
            self.Stock.append(d)
            f = Food(self.Quality)
            f.Cost *= self.Inflation
            self.Stock.append(f)


class Food(object):
    f1 = ['Acai Berry', 'Apple', 'Apricot', 'Banana', 'Blackberry', 'Blueberry', 'Boysenberry', 'Crab Apple', 'Cherry',
          'Cloudberry', 'Coconut', 'Cranberry', 'Elderberry', 'Grape', 'Grapefruit', 'Guava', 'Huckleberry',
          'Juniper berry', 'Kiwi', 'Lemon', 'Lime', 'Mango', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon',
          'Nectarine', 'Orange', 'Blood Orange', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear',
          'Plum', 'Pineapple', 'Pineberry', 'Pomegranate', 'Raspberry', 'Star Apple', 'Strawberry', ]
    f2 = ['Jam', 'Current', 'Spread', 'Puree', 'Sauce', 'Slices', ]
    v1 = ['', '', '', '', 'Steamed ', 'Cooked ', 'Baked ', 'Mashed ', 'Pickled ', 'Chopped ', 'Roasted ', 'Toasted ',
          'Sliced ', 'Fried ', 'Boiled ', 'Uncooked ', ]
    v2 = ['Artichoke', 'Eggplant', 'Avocado', 'Asparagus', 'Legumes', 'Alfalfa Sprouts', 'Beans' 'Peas', 'Broccoli',
          'Brussels Sprouts', 'Cabbage', 'Cauliflower', 'Celery', 'Spinach', 'Lettuce', 'Arugula', 'Chives', 'Leek',
          'Onion', 'Scallion', 'Rhubarb', 'Beet', 'Carrot', 'Parsnip', 'Turnip', 'Radish', 'Horseradish', 'Sweetcorn',
          'Zucchini', 'Cucumber', 'Squash', 'Pumpkin', 'Potato', 'Sweet Potato', 'Yam', 'Water Chestnut',
          'Watercress', ]
    m1 = ['Aged ', 'Baked ', 'Barbecued ', 'Braised ', 'Dried ', 'Fried ', 'Ground ', 'Marinated ', 'Pickled ',
          'Poached ', 'Roasted ', 'Salt-cured ', 'Smoked ', 'Stewed ', 'Corned ', 'Sliced ', ]
    m2 = ['Bear', 'Beef', 'Buffalo', 'Bison', 'Caribou', 'Goat', 'Ham', 'Horse', 'Kangaroo', 'Lamb', 'Moose', 'Mutton',
          'Pork', 'Bacon', 'Rabbit', 'Tripe', 'Veal', 'Venison', 'Chicken', 'Duck', 'Emu', 'Goose', 'Grouse', 'Liver',
          'Ostrich', 'Pheasant', 'Quail', 'Squab', 'Turkey', 'Abalone', 'Anchovy', 'Bass', 'Calamari', 'Carp',
          'Catfish', 'Cod', 'Crab', 'Crayfish', 'Dolphin', 'Eel', 'Flounder', 'Grouper', 'Haddock', 'Halibut',
          'Herring', 'Kingfish', 'Lobster', 'Mackerel', 'Mahi', 'Marlin', 'Milkfish', 'Mussel', 'Octopus', 'Oyster',
          'Perch', 'Pike', 'Pollock', 'Salmon', 'Sardine', 'Scallop', 'Shark', 'Shrimp', 'Swai', 'Swordfish', 'Tilapia',
          'Trout', 'Tuna', 'Walleye', 'Whale', ]
    m3 = ['', '', '', '', 'Burger', 'Charcuterie', 'Chop', 'Cured', 'Cutlet', 'Dum', 'Fillet', 'Kebab', 'Meatball',
          'Meatloaf', 'Offal', 'Sausage', 'Steak', 'Tandoor', 'Tartare', ]
    g1 = ['', '', '', '', 'Buttered ', 'Spiced ', 'Cheesy ']
    g2 = ['Barley', 'Corn', 'Oat', 'Rice', 'Wheat', 'Rye', 'Maize', ]
    g3 = ['Bun', 'Roll', 'Bread', 'Cake', 'Patty', 'Muffin', 'Toast', 'Biscuit', 'Loaf', ]
    spice = ['Basil', 'Ginger', 'Caraway', 'Cilantro', 'Chamomile', 'Dill', 'Fennel', 'Lavender', 'Lemon Grass',
             'Marjoram', 'Oregano', 'Parsley', 'Rosemary', 'Sage', 'Thyme', 'Garlic', 'Chili Pepper', 'Jalapeno',
             'Habanero', 'Paprika', 'Cayenne Pepper', ]
    String = Descriptor = ''
    Cost = 0

    def __init__(self, rarity):
        s = ""
        meal_option = randint(15) + rarity
        if meal_option <= 10:
            self.Descriptor = "Meat, Bread"
            s += self.m1[randint(len(self.m1))] + self.m2[randint(len(self.m2))] + " " + self.m3[
                randint(len(self.m3))] + " with a "
            s += self.g1[randint(len(self.g1))] + self.g2[randint(len(self.g2))] + " " + self.g3[randint(len(self.g3))]
        elif meal_option == 11:
            self.Descriptor = "Meat, Bread, Fruit"
            s += self.m1[randint(len(self.m1))] + self.m2[randint(len(self.m2))] + " " + self.m3[
                randint(len(self.m3))] + " with a "
            s += self.g1[randint(len(self.g1))] + self.g2[randint(len(self.g2))] + " " + self.g3[randint(len(self.g3))]
            s += " and a side of " + self.f1[randint(len(self.f1))] + ' ' + self.f2[randint(len(self.f2))]

        elif meal_option == 12:
            self.Descriptor = "Meat, Bread, Vegetable"
            s += self.m1[randint(len(self.m1))] + self.m2[randint(len(self.m2))] + " " + self.m3[
                randint(len(self.m3))] + " with a "
            s += self.g1[randint(len(self.g1))] + self.g2[randint(len(self.g2))] + " " + self.g3[randint(len(self.g3))]
            s += " and a side of " + self.v1[randint(len(self.v1))] + ' ' + self.v2[randint(len(self.v2))]
        elif meal_option == 13:
            self.Descriptor = "Vegetable, Bread, Fruit"
            s += self.v1[randint(len(self.v1))] + ' ' + self.v2[randint(len(self.v2))] + " with a "
            s += self.g1[randint(len(self.g1))] + self.g2[randint(len(self.g2))] + " " + self.g3[randint(len(self.g3))]
            s += " and a side of " + self.f1[randint(len(self.f1))] + ' ' + self.f2[randint(len(self.f2))]
        elif meal_option == 14:
            self.Descriptor = "Meat, Fruit, Vegetable"
            s += self.m1[randint(len(self.m1))] + self.m2[randint(len(self.m2))] + " " + self.m3[randint(len(self.m3))]
            s += " with " + self.f1[randint(len(self.f1))] + ' ' + self.f2[randint(len(self.f2))]
            s += " and " + self.v1[randint(len(self.v1))] + ' ' + self.v2[randint(len(self.v2))]
        else:
            self.Descriptor = "Meat, Fruit, Vegetable, Bread"
            s += self.m1[randint(len(self.m1))] + self.m2[randint(len(self.m2))] + " " + self.m3[
                randint(len(self.m3))] + " with a "
            s += self.g1[randint(len(self.g1))] + self.g2[randint(len(self.g2))] + " " + self.g3[randint(len(self.g3))]
            s += " with " + self.f1[randint(len(self.f1))] + ' ' + self.f2[randint(len(self.f2))]
            s += " and " + self.v1[randint(len(self.v1))] + ' ' + self.v2[randint(len(self.v2))]
        self.String = s
        if meal_option == 0:
            self.Cost = (len(s) * random_sample()+.5)/10
        else:
            self.Cost = (len(s) * (sum(random_sample(meal_option)) / meal_option))/10

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.String + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + self.Descriptor + """</td></tr>"""
        return s


class Drink(object):
    d1 = ['Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water',
          'Water', 'Water', 'Acai Juice', 'Apple Juice', 'Apricot Juice', 'Banana Juice', 'Blackberry Juice',
          'Blueberry Juice', 'Boysenberry Juice', 'Crab Apples Juice', 'Cherry Juice', 'Cloudberry Juice',
          'Coconut Juice', 'Cranberry Juice', 'Grape Juice', 'Grapefruit Juice', 'Guava Juice', 'Honeyberry Juice',
          'Huckleberry Juice', 'Kiwi Juice', 'Lemon Juice', 'Lime Juice', 'Mango Juice', 'Melon Juice',
          'Cantaloupe Juice', 'Honeydew Juice', 'Watermelon Juice', 'Nectarine Juice', 'Orange Juice', 'Papaya Juice',
          'Peach Juice', 'Pear Juice', 'Pineapple Juice', 'Pomegranate Juice', 'Raspberry Juice', 'Strawberry Juice',
          'Acai Contentrate', 'Apple Contentrate', 'Apricot Contentrate', 'Banana Contentrate',
          'Blackberry Contentrate', 'Blueberry Contentrate', 'Boysenberry Contentrate', 'Crab Apples Contentrate',
          'Cherry Contentrate', 'Cloudberry Contentrate', 'Coconut Contentrate', 'Cranberry Contentrate',
          'Grape Contentrate', 'Grapefruit Contentrate', 'Guava Contentrate', 'Honeyberry Contentrate',
          'Huckleberry Contentrate', 'Kiwi Contentrate', 'Lemon Contentrate', 'Lime Contentrate', 'Mango Contentrate',
          'Melon Contentrate', 'Cantaloupe Contentrate', 'Honeydew Contentrate', 'Watermelon Contentrate',
          'Nectarine Contentrate', 'Orange Contentrate', 'Papaya Contentrate', 'Peach Contentrate', 'Pear Contentrate',
          'Pineapple Contentrate', 'Pomegranate Contentrate', 'Raspberry Contentrate', 'Strawberry Contentrate',
          'Acai Cider', 'Apple Cider', 'Apricot Cider', 'Banana Cider', 'Blackberry Cider', 'Blueberry Cider',
          'Boysenberry Cider', 'Crab Apples Cider', 'Cherry Cider', 'Cloudberry Cider', 'Coconut Cider',
          'Cranberry Cider', 'Grape Cider', 'Grapefruit Cider', 'Guava Cider', 'Honeyberry Cider', 'Huckleberry Cider',
          'Kiwi Cider', 'Lemon Cider', 'Lime Cider', 'Mango Cider', 'Melon Cider', 'Cantaloupe Cider', 'Honeydew Cider',
          'Watermelon Cider', 'Nectarine Cider', 'Orange Cider', 'Papaya Cider', 'Peach Cider', 'Pear Cider',
          'Pineapple Cider', 'Pomegranate Cider', 'Raspberry Cider', 'Strawberry Cider', 'Acai Soda', 'Apple Soda',
          'Apricot Soda', 'Banana Soda', 'Blackberry Soda', 'Blueberry Soda', 'Boysenberry Soda', 'Crab Apples Soda',
          'Cherry Soda', 'Cloudberry Soda', 'Coconut Soda', 'Cranberry Soda', 'Grape Soda', 'Grapefruit Soda',
          'Guava Soda', 'Honeyberry Soda', 'Huckleberry Soda', 'Kiwi Soda', 'Lemon Soda', 'Lime Soda', 'Mango Soda',
          'Melon Soda', 'Cantaloupe Soda', 'Honeydew Soda', 'Watermelon Soda', 'Nectarine Soda', 'Orange Soda',
          'Papaya Soda', 'Peach Soda', 'Pear Soda', 'Pineapple Soda', 'Pomegranate Soda', 'Raspberry Soda',
          'Strawberry Soda', 'Acai Infusion', 'Apple Infusion', 'Apricot Infusion', 'Banana Infusion',
          'Blackberry Infusion', 'Blueberry Infusion', 'Boysenberry Infusion', 'Crab Apples Infusion',
          'Cherry Infusion', 'Cloudberry Infusion', 'Coconut Infusion', 'Cranberry Infusion', 'Grape Infusion',
          'Grapefruit Infusion', 'Guava Infusion', 'Honeyberry Infusion', 'Huckleberry Infusion', 'Kiwi Infusion',
          'Lemon Infusion', 'Lime Infusion', 'Mango Infusion', 'Melon Infusion', 'Cantaloupe Infusion',
          'Honeydew Infusion', 'Watermelon Infusion', 'Nectarine Infusion', 'Orange Infusion', 'Papaya Infusion',
          'Peach Infusion', 'Pear Infusion', 'Pineapple Infusion', 'Pomegranate Infusion', 'Raspberry Infusion',
          'Strawberry Infusion', ]
    d2 = ['Absinthe', 'Cognac', 'Gin', 'Pale Ale', 'Pilsner', 'Amber Ale', 'Wheat Beer', 'Ale', 'Porter', 'Marzen',
          'Scotch', 'Stout', 'Pale Lager', 'Rye Ale', 'Rum', 'Cocktail', 'Whiskey', 'Vodka', 'Moonshine', 'Bourban',
          'Brandy', 'Rum', 'Vermouth', ]
    String = Descriptor = ''
    Cost = 0

    def __init__(self, level):
        s = ''
        num = randint(4) + level
        if num < 2:
            self.Descriptor = "Non-Alcoholic"
            s += self.d1[randint(len(self.d1))]
        else:
            self.Descriptor = "Alcoholic"
            s += self.d2[randint(len(self.d2))]
        self.String = s
        if num == 0:
            self.Cost = (len(s) * random_sample()+.5)/10
        else:
            self.Cost = (len(s) * (sum(random_sample(num)) / num))/10

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.String + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + self.Descriptor + """</td></tr>"""
        return s


class Room(object):
    Name = ""
    Beds = Cost = 0

    def __init__(self, beds, qual, name=None):
        self.Beds = beds
        if name is not None:
            self.Name = name
        else:
            self.Name = str(self.Beds) + " Bed"
        self.Cost = 0.5 * (qual+1) * beds

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Name + ' (Room Rental)</span></td><td>' + \
            determine_cost(self.Cost) + """</td><td>Lodging</td></tr>"""
        return s


class Jewel(object):
    value = [10, 50, 100, 500, 1000, 5000, ]
    Name = ""
    Cost = Rarity = 0

    def __init__(self, rarity):
        self.Name = Jewelling.j1[randint(len(Jewelling.j1))] + Jewelling.j2[randint(len(Jewelling.j2))] + \
                    Jewelling.j3[randint(len(Jewelling.j3))]
        if rarity >= 5:
            rarity %= 5
        self.Rarity = rarity
        self.Cost = self.value[self.Rarity] * (random_sample() + 1)

    def __str__(self):
        l = ['Low Quality Gems', 'Semi Precious Gems', 'Medium Quality Gemstones', 'High Quality Gemstones', 'Jewels', 'Grand Jewels']
        s = '<tr><td style="width:50%;"><span class="text-md">' + self.Name + '</span></td><td>' + \
            determine_cost(self.Cost) + '</td><td>' + l[self.Rarity] + '</td></tr>'
        return s

    def to_string(self):
        return self.Name + ' (' + determine_cost(self.Cost) + ')'


class General(object):
    from trinkets import Trinkets, Gear
    Cost = 0
    Name = Type = Describe = ''

    def __init__(self, level, trinket=False):
        if not trinket:
            if level == 0:
                self.Name = self.__choose_type__('C')
                self.Cost = self.Gear['C'][self.Name]['Base Price']
                self.Type = self.Gear['C'][self.Name]['Class']
            elif level == 1:
                self.Name = self.__choose_type__('U')
                self.Cost = self.Gear['U'][self.Name]['Base Price']
                self.Type = self.Gear['U'][self.Name]['Class']
            elif level == 2:
                self.Name = self.__choose_type__('R')
                self.Cost = self.Gear['R'][self.Name]['Base Price']
                self.Type = self.Gear['R'][self.Name]['Class']
            elif level == 3:
                self.Name = self.__choose_type__('E')
                self.Cost = self.Gear['E'][self.Name]['Base Price']
                self.Type = self.Gear['E'][self.Name]['Class']
        else:
            self.Name = "Trinket"
            self.Cost = random_sample() * 10
            self.Describe = choice(self.Trinkets)
            self.Type = "Trinket"

    def __choose_type__(self, rarity):
        options = {
            'Adventuring Gear/Luxury Items': 250,
            'Tools & Skill Kits': 200,
            'Food & Drink & Lodging': 150,
            'Clothing': 150,
            'Services': 5,
            'Transport': 5,
        }
        c = choice(list(options.keys()), p=list(normalize_dict(options).values()))
        item = choice(list(self.Gear[rarity].keys()))
        while self.Gear[rarity][item]['Class'] != c:
            item = choice(list(self.Gear[rarity].keys()))
        return item

    def __str__(self):
        d = ""
        if self.Describe != "":
            d += '<br /><span class="text-sm emp">' + self.Describe + '</span>'
        s = '<tr><td style="width:50%;"><span class="text-md">' + self.Name + d + '</span></td><td>' + \
            determine_cost(self.Cost) + '</td><td>' + self.Type + '</td></tr>'
        return s

    def to_string(self):
        return self.Name + ' (' + determine_cost(self.Cost) + ')'


class Art(object):
    materials = [
        ['pewter', 'granite', 'soapstone', 'limestone', 'carved wood', 'ceramic'],
        ['pewter', 'alabaster', 'silver', 'marble', 'bronze'],
        ['pewter', 'alabaster', 'silver', 'marble', 'brass'],
        ['gold', 'adamantine', 'dragonbone', 'crystal']
    ]
    gems = [
        ['n azurite', ' banded agate', ' blue quartz', ' hematite', ' lapis lazuli', ' malachite', ' moss agate',
         'n obsidian piece', ' tiger eye', ' beryl'],
        [' bloodstone', ' carnelian', ' chalcedony', ' citrine', ' jasper', ' moonstone', ' n onyx', ' zircon',
         ' chrysophase'],
        ['n amber', 'n amethyst', ' piece of coral', ' garnet', ' piece of jade', ' pearl', ' spinel', ' tourmaline'],
        ['n alexandrite', 'n aquamarine', ' topaz', ' peridot', ' blue spinel', ' black pearl', ' diamond']
    ]
    filigree = [
        ['copper', 'oak wood', 'tin', 'bronze', 'bone'],
        ['brass', 'maple wood', 'iron', 'glass', 'bone'],
        ['gold', 'mahogany wood', 'glass', 'ivory', 'mythril'],
        ['platinum', 'ironwood', 'mythril', 'ivory']
    ]
    descriptor = ['ugly', 'beautiful', 'ancient', 'old', 'strange', 'antique', 'durable', 'sturdy', 'engraved',
                  'ornate', 'rough', 'ornamental']
    cloth = ['silk', 'wool', 'leather', 'fur', 'angelskin', 'darkleaf', 'griffon mane']
    bad_condition = ['in poor condition', 'of poor craftsmanship', 'of shoddy construction', 'in bad shape',
                     'of low quality']
    figurine = ['a dragon', 'a gryphon', 'a hydra', 'an owlbear', 'a beholder', 'a boar', 'a bear', 'a wolf', 'a fox',
                'a tiger', 'a lion', 'a horse', 'an owl', 'a hawk', 'an eagle', 'a crow', 'a snake', 'a fish',
                'a shark', 'a goblin', 'a skeleton', 'an orc', 'a minotaur', 'a tiefling', 'a warrior', 'a knight',
                'a thief', 'a wizard', 'a ship', 'a castle', 'a tower', 'a boat', 'a king', 'a queen', 'a princess',
                'a god', 'a goddess']
    object = ['ring', 'tankard', 'goblet', 'cup', 'drinking horn', 'crown', 'circlet', 'tiara', 'pendant', 'necklace',
              'amulet', 'medallion', 'bowl', 'plate', 'jewelry box', 'music box', 'brooch', 'chess set', 'mask',
              'holy text', 'hourglass', 'vase']
    magic = ['It glows with a soft blue light', 'It glows with a soft green light', 'It glows with a soft red light',
             'It glows with a soft amber light', 'It glows with a soft violet light', 'It is warm to the touch',
             'It is hot to the touch', 'It is cool to the touch', 'It is cold to the touch',
             'It hums with gentle music', 'It hums with melodic music', 'It hums with soft music',
             'It is wreathed in blue flames', 'It is wreathed in green flames', 'It is wreathed in red flames',
             'It is wreathed in amber flames', 'It is wreathed in violet flames']

    def __init__(self, quality):
        if quality > 5:
            quality %= 6
        c = randint(10)
        if quality == 0:
            c %= 3
            if c == 0:
                self.Description = choice(['Silvered', 'Gilded']) + ' ' + choice(['bottle', 'flask', 'jug']) + \
                                   ' of ' + choice(['dwarven', 'elven', 'Dragonborn']) + ' ' + \
                                   choice(['beer', 'wine', 'ale', 'mead'])
            elif c == 1:
                self.Description = 'Pair of ' + choice(self.descriptor) + ' ' + choice(self.cloth) + ' gloves'
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.cloth) + ' ' + choice(['hat', 'ribbon'])
        elif quality == 1:
            c %= 6
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', ' + choice(self.bad_condition)
            elif c == 1:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', ' + choice(self.bad_condition)
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[0])
            elif c == 3:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[0])
            elif c == 4:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[0])
            elif c == 5:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[0])
        elif quality == 2:
            c %= 2
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.cloth) + ' ' + \
                                   choice(['cloth', 'cloak']) + ' with ' + choice(self.materials[1]) + ' clasps'
            elif c == 1:
                self.Description = choice(self.descriptor) + ' belt with a(n) ' + choice(self.materials[1]) + ' buckle'
        elif quality == 3:
            c %= 8
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 1:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[2])
            elif c == 3:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[2])
            elif c == 4:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 5:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 6:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[2])
            elif c == 7:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[2])
        elif quality == 4:
            c %= 5
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[2])
            elif c == 1:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[2])
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[3])
            elif c == 3:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[3])
            elif c == 4:
                self.Description = choice(self.materials[3]) + ' framed painting of ' + choice(self.figurine)
        elif quality == 5:
            c %= 4
            if c == 0:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 1:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 3:
                self.Description = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[3]) + ' ' + \
                                   choice(self.magic)
        cost_factor = [50, 150, 500, 1000, 5000, 10000, 50000]
        self.Cost = cost_factor[quality + 1]
        self.Rarity = quality

    def __str__(self):
        s = '<tr><td style="width:50%;"><span class="text-md">' + self.Description.title() + '</span></td><td>' + \
            determine_cost(self.Cost) + '</td><td>Grade ' + str(self.Rarity+1) + ' Art</td></tr>'
        return s

    def to_string(self):
        return self.Description.title() + ' (' + determine_cost(self.Cost) + ')'


class Ring(object):
    Spell = Name = ""
    Level = Cost = 0
    Enchantment = None

    def __init__(self, level, spell=None):
        if spell is None:
            if level == 0:
                self.Spell = choice(level_0)
                self.Cost = 13
            elif level == 1:
                self.Spell = choice(level_1)
                self.Cost = 25
            elif level == 2:
                self.Spell = choice(level_2)
                self.Cost = 150
            elif level == 3:
                self.Spell = choice(level_3)
                self.Cost = 375
            elif level == 4:
                self.Spell = choice(level_4)
                self.Cost = 700
            elif level == 5:
                self.Spell = choice(level_5)
                self.Cost = 1125
            elif level == 6:
                self.Spell = choice(level_6)
                self.Cost = 1650
            elif level == 7:
                self.Spell = choice(level_7)
                self.Cost = 2275
            elif level == 8:
                self.Spell = choice(level_8)
                self.Cost = 3000
            elif level == 9:
                self.Spell = choice(level_9)
                self.Cost = 4825

            if self.Spell in odd_price:
                self.Cost = round(self.Cost * odd_price[self.Spell])

            self.Enchantment = Enchant(iSpell=self.Spell, rechargable=True)
        else:
            if find_spell_level(spell) == level:
                self.Spell = spell
                self.Enchantment = Enchant(iSpell=self.Spell)
        self.Name = 'Ring of ' + self.Spell

    def __str__(self):
        # print(self.Enchantment.Level)
        global MasterID
        l = ["Level 0", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8",
             "Level 9", ]

        s = """<tr><td style="width:50%;"><span class="text-md" onclick="show_hide('""" + str(MasterID) + \
            """')" style="color:blue;">""" + self.Name + """</span><br /><span class="text-sm emp" id=\"""" + \
            str(MasterID) + """\" style="display: none;">""" + str(self.Enchantment) + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + l[self.Enchantment.Level] + """</td></tr>"""
        MasterID += 1
        return s

    def to_string(self):
        return self.Name + ' (' + determine_cost(self.Cost) + ')'


class Wondrous(object):
    Name = Aura = Slot = Link = ''
    Cost = CL = Weight = 0

    def __init__(self, cl=-1):
        if cl == -1:
            pick = choice(list(MasterWondrous.keys()))
            self.Name = pick
            self.Link = MasterWondrous[pick]['Link']
            self.Cost = int(MasterWondrous[pick]['Price'])
            self.CL = int(MasterWondrous[pick]['CL'])
            self.Aura = MasterWondrous[pick]['Aura']
            self.Slot = MasterWondrous[pick]['Slot']
            self.Weight = MasterWondrous[pick]['Weight']
        else:
            i = 0
            while True:
                pick = choice(list(MasterWondrous.keys()))
                if cl == int(MasterWondrous[pick]['CL']):
                    self.Name = pick
                    self.Link = MasterWondrous[pick]['Link']
                    self.Cost = int(MasterWondrous[pick]['Price'])
                    self.CL = int(MasterWondrous[pick]['CL'])
                    self.Aura = MasterWondrous[pick]['Aura']
                    self.Slot = MasterWondrous[pick]['Slot']
                    self.Weight = MasterWondrous[pick]['Weight']
                    break
                elif i == 100:
                    i = 0
                    cl = int(MasterWondrous[pick]['CL']) + 1
                else:
                    i += 1

    def __str__(self):
        return '<tr><td style="width:50%;"><span class="text-md"><a href="' + self.Link + '">' + self.Name + \
               '</a></span><br /><span class="text-sm emp">Aura ' + self.Aura + '; CL' + str(self.CL) + '; Weight' + \
               self.Weight + '; Slot ' + self.Slot + '</span></td><td>' + determine_cost(self.Cost) + '</td><td>' + \
               'Wondrous Item</td></tr>'

    def to_string(self):
        return self.Name + ' (' + determine_cost(self.Cost) + ')'


class Whore(object):
    Person = None
    Cost = 0

    def __init__(self, vary=None, cost=-1):
        self.Person = create_person(None)
        self.Cost = random_sample() + .1

    def __str__(self):
        if self.Cost is None or self.Person.Gender is None:
            print(self.Cost)
            print(self.Person.Gender)
        return '<tr><td style="width:50%;"><span class="text-md">' + self.Person.Name + ' (' + self.Person.Race + ')' +\
               '</span><br /><span class="text-sm emp">' + self.Person.Appearance + '; Age ' + str(self.Person.Age) + \
               '</span></td><td>' + determine_cost(self.Cost) + '</td><td>' + self.Person.Gender + '</td></tr>'


def create_book_shop(owner, genres, quan, inflate=1):
    for b in genres:
        if b not in Books.Genres:
            print(b, "Not in genre List. See: ", Books.Genres)
            return None
    if isinstance(inflate, float):
        a = Store(owner, str(Antiques()) + " (Library)", inflate, [0, 9])
    else:
        a = Store(owner, str(Antiques()) + " (Library)", (sum(random_sample(inflate)) / inflate) + .5, [0, 9])
    a.fill_store(Book, quan)
    return a


def create_enchantment_shop(owner, rarity, quan, inflate=1):
    name = str(Enchanter()) + " (Enchantments)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    if quan <= 2:
        quan = 3
    remain = randint(quan)
    a.fill_store(Scroll, remain)
    a.fill_store(Wand, quan - remain)
    return a


def create_enchanter_shop(owner, rarity, quan, inflate=1):
    name = str(Enchanter()) + " (Enchanter)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    for _ in range(quan):
        a.Stock.append(Scroll(randint(rarity[0], rarity[1]), naming=False))
    return a


def create_weapon_shop(owner, rarity, quan, inflate=1):
    name = str(Blacksmith()) + " (Weapon)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    if quan <= 2:
        quan = 3
    a.fill_store(Weapon, quan)
    return a


def create_armor_shop(owner, rarity, quan, inflate=1):
    name = str(Blacksmith()) + " (Armor)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    if quan <= 2:
        quan = 3
    a.fill_store(Armor, quan)
    return a


def create_potion_shop(owner, rarity, quan, inflate=1):
    name = str(Potions()) + " (Alchemist)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    a.fill_store(Potion, quan)
    return a


def create_tavern(owner, qual, rooms, quan, inflate=1):
    # def __init__(self, keeper, name, service, qual, rooms, quan):
    name = str(Tavern()) + " (Inn)"
    if isinstance(inflate, float):
        a = Inn(owner, name, inflate, qual, rooms, quan)
    else:
        a = Inn(owner, name, (sum(random_sample(inflate)) / inflate), qual, rooms, quan)
    return a


def create_jewel_shop(owner, rarity, quan, inflate=1):
    name = str(Jeweller()) + " (Jeweller)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    a.fill_store(Jewel, quan)
    return a


def create_restaurant(owner, rarity, quan, inflate=1):
    name = str(Restaurant()) + " (Restaurant)"
    if isinstance(inflate, float):
        a = Inn(owner, name, inflate, rarity, 0, quan)
    else:
        a = Inn(owner, name, (sum(random_sample(inflate)) / inflate), rarity, 0, quan)
    return a


def create_general_store(owner, rarity, quan, trink, inflate=1):
    name = str(GeneralStore()) + " (General)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    a.fill_store(General, quan)
    for _ in range(trink):
        a.Stock.append(General(0, True))
    return a


def create_brothel(owner, rarity, quan, inflate=1):
    name = str(Brothel()) + " (Brothel)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    a.fill_store(Whore, quan)
    return a


def create_gunsmith(owner, rarity, quan, inflate=1):
    name = str(Gunsmithing()) + ' (Gunsmith)'
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    a.fill_store(Firearm, quan)
    return a


if __name__ == '__main__':
    print(determine_cost(random_sample() * 1000000))
