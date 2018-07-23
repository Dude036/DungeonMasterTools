from numpy.random import randint, choice, random_sample
import pickle
from names import Antiques, Books, Enchanter, Potions, Tavern, Restaurant, Jeweller, Blacksmith, GeneralStore, Weapons
from variance import normalize_dict

MasterSpells = {}
with open("spells.pickle", 'rb') as pfile:
    MasterSpells = pickle.load(pfile)

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
    'Bronze': {'Weight': 1, 'AC': 8, 'Cost': .8, 'Type': ['B', 'S', 'P', 'MA', 'HA', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Copper': {'Weight': 1, 'AC': 6, 'Cost': .8, 'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Iron': {'Weight': 1, 'AC': 10, 'Cost': 1, 'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Lead': {'Weight': 1.5, 'AC': 8, 'Cost': 1.1, 'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Steel': {'Weight': 1, 'AC': 10, 'Cost': 1, 'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Oak': {'Weight': .5, 'AC': 2, 'Cost': .25, 'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Yew': {'Weight': .5, 'AC': 2, 'Cost': .25, 'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Hide': {'Weight': .5, 'AC': 8, 'Cost': .8, 'Type': ['LA', 'MA', ], },
    'Leather': {'Weight': .5, 'AC': 8, 'Cost': .8, 'Type': ['LA', 'MA', ], },
}
uncommon_material = {
    'Adamantine': {'Weight': 1, 'AC': 20, 'Cost': 1.8, 'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Bone': {'Weight': 1, 'AC': 6, 'Cost': .8, 'Type': ['B', 'S', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Darkwood': {'Weight': .2, 'AC': 5, 'Cost': 1.05, 'Type': ['B', 'P', 'LA', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Dragonskin': {'Weight': 1, 'AC': 12, 'Cost': 2.25, 'Type': ['LA', 'MA', 'HA'], },
    'Dragonhide': {'Weight': 1, 'AC': 10, 'Cost': 2.5, 'Type': ['LA', 'MA', 'HA', ], },
    'Gold': {'Weight': 1, 'AC': 5, 'Cost': 10, 'Type': ['S', 'P', 'MA', '1', 'Si', 'Ex', 'Ra', 'Ar', ], },
    'Greenwood': {'Weight': .5, 'AC': 2, 'Cost': 1.15, 'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Platinum': {'Weight': .7, 'AC': 15, 'Cost': 5, 'Type': ['S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Silkweave': {'Weight': .15, 'AC': 10, 'Cost': 2, 'Type': ['LA', ], },
    'Silver': {'Weight': 1, 'AC': 8, 'Cost': 1.15, 'Type': ['S', 'P', 'MA', '1', 'Si', 'Ex', 'Ra', 'Ar', ], },
    'Stone': {'Weight': .75, 'AC': 2, 'Cost': .25, 'Type': ['B', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
}
rare_material = {
    'Angelskin': {'Weight': .2, 'AC': 5, 'Cost': 2.75, 'Type': ['LA', 'MA', ], },
    'Cold Iron': {'Weight': 1, 'AC': 10, 'Cost': 2, 'Type': ['S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Dreamstone': {'Weight': .5, 'AC': 10, 'Cost': 2.25, 'Type': ['B', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Elysian Bronze': {'Weight': 1, 'AC': 10, 'Cost': 2, 'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Griffon Mane': {'Weight': .2, 'AC': 1, 'Cost': 2, 'Type': ['LA',  'MA',  'HA', ], },
    'Ironwood': {'Weight': .7, 'AC': 10, 'Cost': 1.8, 'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
    'Obsidian': {'Weight': .75, 'AC': 5, 'Cost': 1.5, 'Type': ['S', 'P', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Viridium': {'Weight': 1, 'AC': 10, 'Cost': 1.5, 'Type': ['S', 'P', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
}
very_rare_material = {
    'Blood Crystal': {'Weight': 1, 'AC': 10, 'Cost': 2.75, 'Type': ['S', 'P', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Darkleaf Cloth': {'Weight': .2, 'AC': 10, 'Cost': 2.75, 'Type': ['LA', ], },
    'Mithral': {'Weight': .5, 'AC': 15, 'Cost': 3, 'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Hot Siccatite': {'Weight': .8, 'AC': 10, 'Cost': 3, 'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Cold Siccatite': {'Weight': .8, 'AC': 10, 'Cost': 3, 'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Wyroot': {'Weight': 1.5, 'AC': 5, 'Cost': 2.5, 'Type': ['B', 'P', '2', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
}
legendary_material = {
    'Horacalcum': {'Weight': 1, 'AC': 15, 'Cost': 5, 'Type': ['B', 'S', 'P', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Mindglass': {'Weight': 1, 'AC': 10, 'Cost': 4, 'Type': ['B', 'S', 'P', 'LA', 'MA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Noqual': {'Weight': .5, 'AC': 10, 'Cost': 3, 'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Umbrite': {'Weight': 1, 'AC': 18, 'Cost': 3, 'Type': ['B', 'S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Voidglass': {'Weight': .5, 'AC': 10, 'Cost': 3.25, 'Type': ['S', 'P', 'LA', 'MA', 'HA', '2', '1', 'Si', 'Ma', 'Ex', 'Ar', ], },
    'Whipwood': {'Weight': .2, 'AC': 9, 'Cost': 3, 'Type': ['B', 'P', 'LA', '2', '1', 'Si', 'Ma', 'Ex', 'Ra', ], },
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
    if isinstance(type(c), type(0)):
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
        'Double': ['bo staff', 'Boarding gaff', 'chain-hammer', 'chain spear', 'dire flail', 'double walking stick katana', 'double-chained kama', 'dwarven urgrosh', 'gnome battle ladder', 'gnome hooked hammer', 'kusarigama', 'monk’s spade', 'orc double axe', 'quarterstaff', 'taiaha', 'two-bladed sword', 'weighted spear',],
        'Flail': ['battle poi', 'bladed scarf', 'Cat-o’-nine-tails', 'chain spear', 'dire flail', 'double chained kama', 'dwarven dorn-dergar', 'flail', 'flying talon', 'gnome pincher', 'halfling rope-shot', 'heavy flail', 'kusarigama', 'kyoketsu shoge', 'meteor hammer', 'morningstar', 'nine-section whip', 'nunchaku', 'sansetsukon', 'scorpion whip', 'spiked chain', 'urumi', 'whip',],
        'Hammer': ['aklys', 'battle aspergillum', 'Chain-hammer', 'club', 'gnome piston maul', 'greatclub', 'heavy mace', 'lantern staff', 'light hammer', 'light mace', 'mere club', 'planson', 'taiaha', 'tetsubo', 'wahaika', 'warhammer',],
        'Monk': ['bo staff', 'brass knuckles', 'butterfly sword', 'cestus', 'dan bong', 'deer horn knife', 'double chained kama', 'double chicken saber', 'emei piercer', 'fighting fan', 'hanbo', 'jutte', 'kama', 'kusarigama', 'kyoketsu shoge', 'lungshuan tamo', 'monk’s spade', 'nine-ring broadsword', 'nine-section whip', 'nunchaku', 'quarterstaff', 'rope dart', 'sai', 'sanpkhang', 'sansetsukon', 'seven-branched sword', 'shang gou', 'shuriken', 'siangham', 'temple sword', 'tiger fork', 'tonfa', 'tri-point double-edged sword', 'urumi', 'wushu dart',],
        'Polearm': ['bardiche', 'bec de corbin', 'bill', 'Boarding gaff', 'crook', 'fauchard', 'glaive', 'glaive-guisarme', 'gnome ripsaw glaive', 'guisarme', 'halberd', 'hooked lance', 'lucerne hammer', 'mancatcher', 'monk’s spade', 'naginata', 'nodachi', 'ranseur', 'rhomphaia', 'tepoztopilli', 'tiger fork',],
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
            self.Class = choice(list(self.possible_melee[requirement]))
            self.Name = choice(list(self.possible_melee[self.Class])).title()

        elif requirement in list(self.possible_ranged.keys()):
            self.Class = choice(list(self.possible_ranged[requirement]))
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
        if self.Class == 'Bows' or self.Class == 'Crossbow':
            self.Damage = ['Ra', 'P']
        elif self.Class == 'Thrown':
            self.Damage = ['Ar', 'P', 'S']
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
        else:
            print("This Item is already Masterwork")

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

    def print_item(self):
        print(['Name' + (' ' * (len(self.Name) - 10)), 'Weight', 'Cost', 'Rarity', 'Class', 'Dice', 'Crit', 'Damage'])
        print([self.Name, self.Weight, self.Cost, self.Rarity, self.Class, self.Dice, self.Crit, self.Damage])


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
        else:
            print("This Item is already Masterwork")

    def print_item(self):
        print("""Weight | Cost | Rarity | AC | Name | Class | Metal""")
        print(self.Weight, "|", self.Cost, "|", self.Rarity, "| +", self.AC, "|", self.Name, "|", self.Class, "|", self.Metal)


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
        self.Name = Books.Get(Books, self.Genre)
        self.Cost = 0.5 + random_sample()

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Name + \
            """</span></td><td>""" + determine_cost(self.Cost) + """</td><td>""" + \
            self.Genre + """</td></tr>"""
        return s


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
    f1 = ['Açaí Berry', 'Apple', 'Apricot', 'Banana', 'Blackberry', 'Blueberry', 'Boysenberry', 'Crab Apple', 'Cherry',
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
             'Marjoram', 'Oregano', 'Parsley', 'Rosemary', 'Sage', 'Thyme', 'Garlic', 'Chili Pepper', 'Jalapeño',
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
          'Water', 'Water', 'Açaí Juice', 'Apple Juice', 'Apricot Juice', 'Banana Juice', 'Blackberry Juice',
          'Blueberry Juice', 'Boysenberry Juice', 'Crab Apples Juice', 'Cherry Juice', 'Cloudberry Juice',
          'Coconut Juice', 'Cranberry Juice', 'Grape Juice', 'Grapefruit Juice', 'Guava Juice', 'Honeyberry Juice',
          'Huckleberry Juice', 'Kiwi Juice', 'Lemon Juice', 'Lime Juice', 'Mango Juice', 'Melon Juice',
          'Cantaloupe Juice', 'Honeydew Juice', 'Watermelon Juice', 'Nectarine Juice', 'Orange Juice', 'Papaya Juice',
          'Peach Juice', 'Pear Juice', 'Pineapple Juice', 'Pomegranate Juice', 'Raspberry Juice', 'Strawberry Juice',
          'Açaí Contentrate', 'Apple Contentrate', 'Apricot Contentrate', 'Banana Contentrate',
          'Blackberry Contentrate', 'Blueberry Contentrate', 'Boysenberry Contentrate', 'Crab Apples Contentrate',
          'Cherry Contentrate', 'Cloudberry Contentrate', 'Coconut Contentrate', 'Cranberry Contentrate',
          'Grape Contentrate', 'Grapefruit Contentrate', 'Guava Contentrate', 'Honeyberry Contentrate',
          'Huckleberry Contentrate', 'Kiwi Contentrate', 'Lemon Contentrate', 'Lime Contentrate', 'Mango Contentrate',
          'Melon Contentrate', 'Cantaloupe Contentrate', 'Honeydew Contentrate', 'Watermelon Contentrate',
          'Nectarine Contentrate', 'Orange Contentrate', 'Papaya Contentrate', 'Peach Contentrate', 'Pear Contentrate',
          'Pineapple Contentrate', 'Pomegranate Contentrate', 'Raspberry Contentrate', 'Strawberry Contentrate',
          'Açaí Cider', 'Apple Cider', 'Apricot Cider', 'Banana Cider', 'Blackberry Cider', 'Blueberry Cider',
          'Boysenberry Cider', 'Crab Apples Cider', 'Cherry Cider', 'Cloudberry Cider', 'Coconut Cider',
          'Cranberry Cider', 'Grape Cider', 'Grapefruit Cider', 'Guava Cider', 'Honeyberry Cider', 'Huckleberry Cider',
          'Kiwi Cider', 'Lemon Cider', 'Lime Cider', 'Mango Cider', 'Melon Cider', 'Cantaloupe Cider', 'Honeydew Cider',
          'Watermelon Cider', 'Nectarine Cider', 'Orange Cider', 'Papaya Cider', 'Peach Cider', 'Pear Cider',
          'Pineapple Cider', 'Pomegranate Cider', 'Raspberry Cider', 'Strawberry Cider', 'Açaí Soda', 'Apple Soda',
          'Apricot Soda', 'Banana Soda', 'Blackberry Soda', 'Blueberry Soda', 'Boysenberry Soda', 'Crab Apples Soda',
          'Cherry Soda', 'Cloudberry Soda', 'Coconut Soda', 'Cranberry Soda', 'Grape Soda', 'Grapefruit Soda',
          'Guava Soda', 'Honeyberry Soda', 'Huckleberry Soda', 'Kiwi Soda', 'Lemon Soda', 'Lime Soda', 'Mango Soda',
          'Melon Soda', 'Cantaloupe Soda', 'Honeydew Soda', 'Watermelon Soda', 'Nectarine Soda', 'Orange Soda',
          'Papaya Soda', 'Peach Soda', 'Pear Soda', 'Pineapple Soda', 'Pomegranate Soda', 'Raspberry Soda',
          'Strawberry Soda', 'Açaí Infusion', 'Apple Infusion', 'Apricot Infusion', 'Banana Infusion',
          'Blackberry Infusion', 'Blueberry Infusion', 'Boysenberry Infusion', 'Crab Apples Infusion',
          'Cherry Infusion', 'Cloudberry Infusion', 'Coconut Infusion', 'Cranberry Infusion', 'Grape Infusion',
          'Grapefruit Infusion', 'Guava Infusion', 'Honeyberry Infusion', 'Huckleberry Infusion', 'Kiwi Infusion',
          'Lemon Infusion', 'Lime Infusion', 'Mango Infusion', 'Melon Infusion', 'Cantaloupe Infusion',
          'Honeydew Infusion', 'Watermelon Infusion', 'Nectarine Infusion', 'Orange Infusion', 'Papaya Infusion',
          'Peach Infusion', 'Pear Infusion', 'Pineapple Infusion', 'Pomegranate Infusion', 'Raspberry Infusion',
          'Strawberry Infusion', ]
    d2 = ['Absinthe', 'Cognac', 'Gin', 'Pale Ale', 'Pilsner', 'Amber Ale', 'Wheat Beer', 'Ale', 'Porter', 'Märzen',
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
    j1 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
          "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
          "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
          "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
          "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Adamantine ", "Amaranth ", "Amber ",
          "Amethyst ", "Apricot ", "Aquamarine ", "Azure ", "Baby Blue ", "Beige ", "Black ", "Blue ", "Blue-Green ",
          "Blue-Violet ", "Blush ", "Brilliance ", "Brilliant ", "Bronze ", "Brown ", "Burgundy ", "Byzantium ",
          "Carmine ", "Cerise ", "Cerulean ", "Champagne ", "Chartreuse Green ", "Chocolate ", "Cobalt Blue ",
          "Coffee ", "Copper ", "Coral ", "Crimson ", "Crystalline ", "Cyan ", "Dazzling ", "Desert Sand ",
          "Electric Blue ", "Emerald ", "Erin ", "Facet ", "Flashing ", "Gilty ", "Gleaming ", "Glinting ", "Glinty ",
          "Glittering ", "Gold ", "Gray ", "Green ", "Harlequin ", "Indigo ", "Ivory ", "Jade ", "Jungle Green ",
          "Lavender ", "Lemon ", "Lilac ", "Lime ", "Magenta ", "Magenta rose ", "Maroon ", "Mauve ", "Multifaceted ",
          "Navy Blue ", "Ocher ", "Olive ", "Orange ", "Orange-Red ", "Orchid ", "Peach ", "Pear ", "Periwinkle ",
          "Persian Blue ", "Pink ", "Plum ", "Prussian Blue ", "Puce ", "Purple ", "Raspberry ", "Red ", "Red-Violet ",
          "Rose ", "Salmon ", "Sangria ", "Sapphire ", "Scarlet ", "Scintillant ", "Scintillating ", "Silver ",
          "Slate Gray ", "Sparkling ", "Spring Bud ", "Spring Green ", "Tan ", "Taupe ", "Teal ", "Turquoise ",
          "Twinkling ", "Violet ", "Viridian ", "White ", "Yellow ", ]
    j2 = ["Abe", "Abel", "Aben", "Aber", "Abh", "Abhu", "Abs", "Absw", "Aca", "Acan", "Ach", "Achr", "Act", "Acti",
          "Acu", "Acum", "Ada", "Adam", "Ade", "Adel", "Adm", "Admo", "Aeg", "Aegi", "Aen", "Aeni", "Aer", "Aeri",
          "Aeru", "Aes", "Aesc", "Afg", "Afgh", "Afw", "Afwi", "Aga", "Agar", "Agat", "Agr", "Agre", "Agri", "Agu",
          "Agui", "Ahe", "Ahey", "Ahl", "Ahlf", "Aik", "Aiki", "Ajo", "Ajoi", "Aka", "Akag", "Akat", "Akd", "Akda",
          "Ake", "Aker", "Aks", "Aksa", "Ala", "Alab", "Alam", "Alar", "Alb", "Albi", "Ald", "Alde", "Ale", "Alex",
          "Alf", "Alfo", "Alg", "Algo", "Ali", "Alie", "All", "Alla", "Alli", "Allo", "Alm", "Alma", "Als", "Alst",
          "Alt", "Alta", "Alu", "Alum", "Alun", "Ama", "Amaz", "Amb", "Ambe", "Ambl", "Ame", "Ameg", "Amet", "Amm",
          "Ammo", "Amo", "Amos", "Amp", "Amph", "Ana", "Anal", "Anap", "Anat", "And", "Anda", "Ande", "Andr", "Ang",
          "Angl", "Anh", "Anhy", "Ank", "Anke", "Ann", "Anna", "Ano", "Anor", "Ant", "Anth", "Anti", "Antl", "Anto",
          "Any", "Anyo", "Apa", "Apat", "Apo", "Apop", "Aqu", "Aqua", "Ara", "Arag", "Arc", "Arch", "Arct", "Arcu",
          "Arf", "Arfv", "Arg", "Arge", "Argu", "Arm", "Arma", "Ars", "Arse", "Art", "Arth", "Arti", "Artr", "Asb",
          "Asbe", "Ash", "Ashb", "Asi", "Asis", "Ast", "Astr", "Ata", "Atac", "Ath", "Athe", "Aub", "Aube", "Aug",
          "Auge", "Augi", "Aur", "Auri", "Auro", "Aut", "Autu", "Ava", "Aval", "Ave", "Aven", "Axi", "Axin", "Azu",
          "Azur", "Bab", "Babi", "Bad", "Badd", "Bao", "Baot", "Bar", "Bari", "Bars", "Bary", "Bas", "Bast", "Bau",
          "Baux", "Baz", "Bazz", "Bec", "Beck", "Ben", "Beni", "Bens", "Bent", "Ber", "Berr", "Bert", "Bery", "Bio",
          "Biot", "Bir", "Birn", "Bis", "Bism", "Bix", "Bixb", "Blo", "Blod", "Bloo", "Blos", "Bob", "Bobf", "Boe",
          "Boeh", "Bor", "Bora", "Born", "Bot", "Botr", "Bou", "Boul", "Bour", "Bow", "Bowe", "Bra", "Bram", "Bras",
          "Brau", "Braz", "Bre", "Brei", "Brew", "Bri", "Bria", "Bro", "Broc", "Brom", "Bron", "Broo", "Bru", "Bruc",
          "Brus", "Bud", "Budd", "Bue", "Buer", "Buk", "Buko", "Bul", "Bult", "Byt", "Byto", "Cab", "Cabr", "Cad",
          "Cadm", "Caf", "Cafe", "Cal", "Cala", "Calc", "Cald", "Cale", "Cali", "Can", "Canc", "Canf", "Car", "Carn",
          "Caro", "Carr", "Cary", "Cas", "Cass", "Cav", "Cava", "Cel", "Cela", "Cele", "Cels", "Cem", "Ceme", "Cer",
          "Ceri", "Ceru", "Ces", "Cesb", "Cey", "Ceyl", "Cha", "Chab", "Chal", "Chao", "Chap", "Char", "Chi", "Chil",
          "Chl", "Chlo", "Cho", "Chon", "Chr", "Chro", "Chry", "Cin", "Cinn", "Cit", "Citr", "Cla", "Clar", "Cle",
          "Clev", "Cli", "Clin", "Cob", "Coba", "Coe", "Coes", "Cof", "Coff", "Col", "Cole", "Coll", "Colo", "Colt",
          "Colu", "Com", "Comb", "Con", "Conc", "Conn", "Coo", "Coop", "Cop", "Copa", "Copi", "Copp", "Cor", "Cora",
          "Cord", "Coru", "Cov", "Cove", "Cre", "Cree", "Cri", "Cris", "Cro", "Croc", "Cron", "Croo", "Cros", "Cry",
          "Cryo", "Cum", "Cumb", "Cumm", "Cup", "Cupr", "Cya", "Cyan", "Cyl", "Cyli", "Cym", "Cymo", "Cyp", "Cypr",
          "Dan", "Danb", "Dat", "Dato", "Dav", "Davi", "Daw", "Daws", "Del", "Dele", "Delv", "Dem", "Dema", "Des",
          "Desc", "Dia", "Diab", "Diad", "Diam", "Dias", "Diat", "Dic", "Dick", "Dig", "Dige", "Dio", "Diop", "Dju",
          "Djur", "Dol", "Doll", "Dolo", "Dom", "Dome", "Dra", "Drav", "Dum", "Dumo", "Edi", "Edin", "Eka", "Ekan",
          "Elb", "Elba", "Els", "Elsm", "Eme", "Emer", "Emp", "Empr", "Ena", "Enar", "Ens", "Enst", "Eos", "Eosp",
          "Epi", "Epid", "Eps", "Epso", "Ery", "Eryt", "Esp", "Espe", "Ett", "Ettr", "Euc", "Euch", "Eucl", "Eucr",
          "Eud", "Eudi", "Eux", "Euxe", "Fab", "Fabi", "Fas", "Fass", "Fay", "Faya", "Fel", "Feld", "Fer", "Ferb",
          "Ferg", "Fero", "Ferr", "Fic", "Fich", "Flu", "Fluo", "For", "Forn", "Fors", "Fou", "Foug", "Fra", "Fran",
          "Fre", "Frei", "Fres", "Fuk", "Fuku", "Gad", "Gado", "Gah", "Gahn", "Gal", "Gala", "Gale", "Gar", "Garn",
          "Gat", "Gate", "Gay", "Gayl", "Ged", "Geda", "Geh", "Gehl", "Gei", "Geig", "Geo", "Geoc", "Geor", "Ger",
          "Germ", "Gers", "Gib", "Gibb", "Gis", "Gism", "Gla", "Glau", "Gle", "Gles", "Gme", "Gmel", "Goe", "Goet",
          "Gol", "Gold", "Gos", "Gosh", "Gosl", "Gra", "Graf", "Grap", "Gre", "Gree", "Grei", "Gro", "Gros", "Gru",
          "Grun", "Gum", "Gumm", "Gun", "Gunn", "Gyp", "Gyps", "Hac", "Hack", "Hag", "Hagg", "Hai", "Haid", "Hal",
          "Hali", "Hall", "Halo", "Han", "Hank", "Hap", "Hapk", "Har", "Hard", "Harm", "Hau", "Haue", "Haus", "Hauy",
          "Haw", "Hawl", "Hax", "Haxo", "Haz", "Haze", "Hea", "Heaz", "Hec", "Hect", "Hed", "Hede", "Hel", "Heli",
          "Hell", "Hem", "Hema", "Hemi", "Her", "Herb", "Herd", "Hes", "Hess", "Heu", "Heul", "Hib", "Hibo", "Hid",
          "Hidd", "Hil", "Hilg", "His", "Hisi", "Hol", "Holm", "Hom", "Homi", "Hop", "Hope", "Hor", "Horn", "How",
          "Howl", "Hue", "Huem", "Hum", "Humi", "Hut", "Hutc", "Hya", "Hyal", "Hyd", "Hydr", "Hyp", "Hype", "Ido",
          "Idoc", "Idr", "Idri", "Ika", "Ikai", "Ill", "Illi", "Ilm", "Ilme", "Ilv", "Ilva", "Inc", "Incl", "Ind",
          "Indi", "Iny", "Inyo", "Iod", "Ioda", "Iol", "Ioli", "Jac", "Jaco", "Jad", "Jada", "Jade", "Jam", "Jame",
          "Jar", "Jaro", "Jas", "Jasp", "Jef", "Jeff", "Jen", "Jenn", "Jer", "Jerr", "Jun", "Juni", "Juo", "Juon",
          "Jur", "Jurb", "Kaa", "Kaat", "Kad", "Kady", "Kai", "Kain", "Kal", "Kali", "Kals", "Kam", "Kama", "Kamb",
          "Kamp", "Kan", "Kank", "Kao", "Kaol", "Kas", "Kass", "Kei", "Keil", "Ker", "Kerm", "Kern", "Kero", "Kie",
          "Kies", "Kin", "Kino", "Kne", "Kneb", "Kno", "Knor", "Kob", "Kobe", "Kog", "Koga", "Kol", "Kolb", "Kor",
          "Korn", "Kra", "Kran", "Krat", "Kre", "Krem", "Kren", "Kuk", "Kukh", "Kun", "Kunz", "Kut", "Kutn", "Kya",
          "Kyan", "Lab", "Labr", "Lan", "Lana", "Lang", "Lans", "Lant", "Lap", "Lapi", "Lar", "Lari", "Lau", "Laum",
          "Laur", "Law", "Laws", "Laz", "Lazu", "Lea", "Lead", "Lec", "Lech", "Leg", "Legr", "Lep", "Lepi", "Leu",
          "Leuc", "Lev", "Levy", "Lib", "Libe", "Lid", "Lidd", "Lig", "Lign", "Lim", "Limo", "Lin", "Lina", "Lip",
          "Lips", "Lir", "Liro", "Lit", "Lith", "Liv", "Livi", "Liz", "Liza", "Lod", "Lode", "Lol", "Loll", "Lon",
          "Lons", "Lop", "Lopa", "Lope", "Lor", "Lora", "Lore", "Lub", "Lubl", "Lud", "Ludw", "Lyo", "Lyon", "Mac",
          "Macd", "Mack", "Mag", "Magh", "Magn", "Maj", "Majo", "Mal", "Mala", "Man", "Mang", "Mar", "Marc", "Marg",
          "Mari", "Mas", "Masc", "Mass", "Mat", "Matl", "Mck", "Mcke", "Mee", "Meer", "Mei", "Meio", "Mel", "Mela",
          "Meli", "Melo", "Men", "Mend", "Mene", "Meni", "Mer", "Merc", "Mes", "Meso", "Mess", "Met", "Meta", "Mia",
          "Miar", "Mic", "Mica", "Micr", "Mil", "Milk", "Mill", "Mim", "Mime", "Min", "Mini", "Mir", "Mira", "Mix",
          "Mixi", "Mog", "Moga", "Moh", "Mohi", "Moi", "Mois", "Mol", "Moly", "Mon", "Mona", "Mono", "Mont", "Moo",
          "Mool", "Moon", "Mor", "Mord", "Morg", "Mot", "Mott", "Motu", "Mul", "Mull", "Mur", "Murd", "Mus", "Musc",
          "Nab", "Nabe", "Nac", "Nacr", "Nag", "Nagy", "Nah", "Nahc", "Nat", "Nati", "Natr", "Nek", "Nekr", "Nel",
          "Nele", "Nen", "Nena", "Nep", "Neph", "Nept", "Nic", "Nick", "Nie", "Nied", "Nin", "Nini", "Nio", "Niob",
          "Nis", "Niss", "Nit", "Nitr", "Non", "Nont", "Nor", "Norm", "Nos", "Nose", "Nsu", "Nsut", "Nye", "Nyer",
          "Olg", "Olgi", "Oli", "Olig", "Oliv", "Omp", "Omph", "Ony", "Onyx", "Opa", "Opal", "Ord", "Ordo", "Ore",
          "Oreg", "Orp", "Orpi", "Ort", "Orth", "Osa", "Osar", "Osm", "Osmi", "Osu", "Osum", "Ota", "Otav", "Ott",
          "Ottr", "Ove", "Over", "Pai", "Pain", "Pal", "Pala", "Pall", "Paly", "Pan", "Pang", "Pap", "Papa", "Par",
          "Para", "Pari", "Part", "Pas", "Pasc", "Pea", "Pear", "Pec", "Peco", "Pect", "Pen", "Pent", "Per", "Peri",
          "Perl", "Pero", "Pet", "Peta", "Petz", "Pez", "Pezz", "Pha", "Phar", "Phe", "Phen", "Phi", "Phil", "Phl",
          "Phlo", "Pho", "Phoe", "Phos", "Pig", "Pige", "Pit", "Pitc", "Pla", "Plag", "Plat", "Ple", "Ples", "Pol",
          "Pola", "Poll", "Poly", "Pot", "Pota", "Pou", "Poud", "Pow", "Powe", "Pra", "Pras", "Pre", "Preh", "Pro",
          "Prou", "Psi", "Psil", "Pum", "Pumi", "Pump", "Pur", "Purp", "Pyr", "Pyra", "Pyri", "Pyro", "Pyrr", "Qua",
          "Quah", "Quar", "Que", "Quen", "Ram", "Ramb", "Ramm", "Rap", "Rapi", "Ras", "Rasp", "Rea", "Real", "Rei",
          "Reis", "Ren", "Reni", "Rhe", "Rhen", "Rho", "Rhod", "Rhom", "Ric", "Rick", "Rie", "Rieb", "Rob", "Robe",
          "Roc", "Rock", "Rom", "Roma", "Ros", "Rosa", "Rosc", "Rose", "Rou", "Roum", "Rout", "Rub", "Rube", "Ruby",
          "Rui", "Ruiz", "Rut", "Ruth", "Ruti", "Ryn", "Ryne", "Sab", "Saba", "Sabi", "Saf", "Saff", "Sal", "Sali",
          "Sam", "Sama", "Sams", "San", "Sanb", "Sane", "Sani", "Sant", "Sap", "Sapo", "Sapp", "Sar", "Sard", "Sark",
          "Sas", "Sass", "Sat", "Sati", "Sau", "Sauc", "Sca", "Scap", "Sch", "Sche", "Scho", "Schr", "Schw", "Sco",
          "Scol", "Scor", "Sea", "Seam", "See", "Seel", "Seg", "Sege", "Sek", "Seka", "Sel", "Sele", "Seli", "Sell",
          "Sen", "Sena", "Sep", "Sepi", "Ser", "Sera", "Serp", "Sha", "Shat", "Shi", "Shig", "Shu", "Shun", "Sid",
          "Side", "Sie", "Sieg", "Sil", "Sili", "Sill", "Silv", "Sim", "Sime", "Simo", "Sin", "Sink", "Sku", "Skut",
          "Sma", "Smal", "Sme", "Smec", "Smi", "Smit", "Smo", "Smok", "Soa", "Soap", "Sod", "Soda", "Son", "Sono",
          "Spe", "Spec", "Sper", "Spes", "Sph", "Spha", "Sphe", "Spi", "Spin", "Spo", "Spod", "Spu", "Spur", "Sta",
          "Stan", "Stau", "Ste", "Stea", "Step", "Sti", "Stib", "Stic", "Stil", "Sto", "Stol", "Str", "Stro", "Stru",
          "Stu", "Stud", "Sug", "Sugi", "Sul", "Sulf", "Sun", "Suns", "Sur", "Surs", "Sus", "Suss", "Syl", "Sylv",
          "Tac", "Tach", "Tae", "Taen", "Tal", "Talc", "Tan", "Tant", "Tanz", "Tar", "Tara", "Tarb", "Tas", "Tash",
          "Tau", "Taus", "Tea", "Teal", "Tel", "Tell", "Tem", "Tema", "Ten", "Tenn", "Teno", "Tep", "Teph", "Ter",
          "Terl", "Teru", "Tet", "Tetr", "Tha", "Thau", "The", "Then", "Tho", "Thom", "Thor", "Thu", "Thul", "Tie",
          "Tiem", "Tig", "Tige", "Tin", "Tinc", "Tit", "Tita", "Tob", "Tobe", "Tod", "Todo", "Tok", "Toky", "Top",
          "Topa", "Tor", "Torb", "Tou", "Tour", "Tra", "Trav", "Tre", "Trem", "Trev", "Tri", "Trid", "Trip", "Tro",
          "Tron", "Tsa", "Tsav", "Tsc", "Tsch", "Tug", "Tugt", "Tun", "Tung", "Tur", "Turq", "Tus", "Tusi", "Tyr",
          "Tyro", "Tyu", "Tyuy", "Uch", "Uchu", "Ukl", "Uklo", "Ule", "Ulex", "Ull", "Ullm", "Ult", "Ultr", "Ulv",
          "Ulvo", "Uma", "Uman", "Umb", "Umbe", "Umbi", "Una", "Unak", "Upa", "Upal", "Ura", "Ural", "Uran", "Uva",
          "Uvar", "Vae", "Vaes", "Val", "Vale", "Van", "Vana", "Var", "Vari", "Vat", "Vate", "Vau", "Vauq", "Vaux",
          "Ver", "Verd", "Verm", "Ves", "Vesu", "Vil", "Vill", "Vio", "Viol", "Viv", "Vivi", "Vol", "Volb", "Wad",
          "Wag", "Wagn", "War", "Ward", "Wari", "Warw", "Was", "Wass", "Wav", "Wave", "Wed", "Wedd", "Wei", "Weil",
          "Weis", "Wel", "Welo", "Whe", "Whew", "Whi", "Whit", "Wil", "Will", "Wilu", "Wit", "With", "Wol", "Wolf",
          "Woll", "Wul", "Wulf", "Wur", "Wurt", "Wya", "Wyar", "Xen", "Xeno", "Xif", "Xife", "Xon", "Xono", "Ytt",
          "Yttr", "Zab", "Zabu", "Zac", "Zacc", "Zah", "Zahe", "Zaj", "Zaja", "Zak", "Zakh", "Zan", "Zana", "Zar",
          "Zara", "Zek", "Zekt", "Zeo", "Zeol", "Zha", "Zhan", "Zhar", "Zho", "Zhon", "Zie", "Zies", "Zim", "Zimb",
          "Zin", "Zina", "Zinc", "Zink", "Zinn", "Zip", "Zipp", "Zir", "Zirc", "Zirk", "Zoi", "Zois", "Zul", "Zult",
          "Zun", "Zuny"]
    j3 = ["a", "abar", "abergite", "abilite", "abogdanite", "abweite", "achite", "achrysotile", "acinnabarite", "acite",
          "acolite", "acyite", "adinite", "adite", "adium", "adkevichite", "adonite", "adorite", "adymite", "agamite",
          "agite", "agnaite", "agnite", "agoite", "agonite", "ahedrite", "aiba", "aite", "akiite", "akite", "al",
          "alaite", "alcolite", "alconite", "ald", "aldaite", "alerite", "alite", "allite", "alsite", "altite",
          "alusite", "alyte", "amarine", "amite", "amunite", "an", "andine", "andite", "andrite", "anechite", "aneite",
          "angerite", "aninaite", "anite", "ankasite", "annite", "anocolumbite", "anotantalite", "anowodginite",
          "ansite", "antite", "antoid", "anvesuvianite", "apacaite", "apite", "ardite", "arealgar", "arenkoite", "arge",
          "argyrite", "aritasite", "arite", "arkite", "arkoite", "armontite", "arovite", "arskite", "artite",
          "asclarkite", "ase", "aseite", "asite", "asovite", "assite", "assium", "aster", "astonite", "atelierite",
          "atierite", "atine", "atite", "atorbernite", "auxite", "averite", "ax", "axite", "az", "azite", "azziite",
          "babweite", "baldaite", "bandite", "banite", "basite", "baster", "bazite", "bbiite", "bdenite", "beckite",
          "beinite", "beite", "belite", "bergite", "berite", "berlandite", "bernite", "bertsmithite", "bilite",
          "bisite", "bite", "blende", "bnite", "boclase", "bogdanite", "boleite", "bornite", "borthite", "bronite",
          "bsite", "burite", "burtonite", "buttite", "byite", "c", "cagnaite", "cagnite", "calconite", "camite",
          "canthite", "casite", "cate", "cchacuaite", "cedony", "ch pearl", "chalcite", "chantite", "chblende",
          "chikhite", "chilite", "chinsonite", "chite", "chlore", "chrysotile", "chtite", "chynite", "cidolite",
          "cinnabarite", "cite", "cite ", "ckeite", "clase", "clasite", "clipscombite", "cloizite", "cobotryogen",
          "cochroite", "cochromite", "cocite", "codot", "coelite", "coite", "colite", "combite", "con", "conite",
          "conolite", "cophane", "cophanite", "cophoenicite", "cophyllite", "copyrite", "covite", "crase", "crinite",
          "cronite", "ctite", "ctrolite", "cupride", "cury", "cyite", "d", "daleite", "dcreekite", "deleyite",
          "dellite", "denite", "derite", "dermayrite", "deroite", "dhillite", "dicoatite", "dierite", "dine",
          "dingerite", "dingtonite", "dinite", "dite", "dium", "dkevichite", "dochite", "dochrosite", "docrocite",
          "dolite", "donaldite", "donite", "donyx", "dorffite", "dot", "dote", "dozite", "drenite", "dretteite",
          "drite", "drodite", "dspar", "dspathoid", "dstone", "dtite", "dumene", "dymite", "dystonite", "e", "ean",
          "ecite", "eckite", "edite", "edonite", "edsonite", "eelite", "eghinite", "ehouseite", "eibersite", "eite",
          "el", "eldite", "elerite", "eleyite", "elian", "eline", "elite", "ellite", "ellyite", "elsbergite",
          "elveyite", "emanite", "emite", "ena", "enbergite", "ene", "eneite", "engite", "enic", "enicochroite",
          "enite", "enium", "enockite", "enoclasite", "enopyrite", "enovite", "entine", "entinite", "entite",
          "enzenite", "eolite", "eonite", "epite", "er", "ereite", "ereye", "erfordine", "ergite", "ergusonite",
          "erite", "erlandite", "ermanite", "ermayrite", "ermigite", "ermorite", "ernite", "erocobaltite", "eroite",
          "erotil", "ersite", "ersonite", "ersthene", "ertine", "ertite", "ertmannite", "ertsite", "ertsmithite",
          "ertyite", "erupine", "esia", "esine", "esioferrite", "esite", "eslebenite", "esonite", "essite", "estine",
          "estone", "estos", "et", "ethenite", "etite", "ettite", "exite", "eyite", "eykite", "ezite", "feldite",
          "fenite", "fergusonite", "fersonite", "fieldite", "finite", "fite", "florite", "fonteinite", "fordite",
          "fornite", "framite", "ftonite", "fur", "gaite", "gamite", "ganeite", "ganite", "ganocolumbite",
          "ganotantalite", "ganvesuvianite", "gar", "gardite", "garitasite", "garite", "gbeinite", "genite", "gerite",
          "gerobinsonite", "gertyite", "ggite", "ghengite", "ghinite", "ghuacerite", "gioclase", "gite", "gmannite",
          "gmatite", "goclase", "goite", "gonite", "gopite", "gorite", "gorskite", "gstite", "gtonite", "guite",
          "gusonite", "gyrite", "h pearl", "hacite", "halite", "hanite", "hantite", "harenkoite", "harge", "harovite",
          "hatelierite", "hauite", "hblende", "heite", "heline", "hemite", "henite", "henium", "herfordine", "herite",
          "hermigite", "hibole", "hierite", "hillite", "hinite", "hinsonite", "hiophilite", "hire", "hirine", "hite",
          "hmarine", "hmite", "hnite", "hochrysotile", "hoclase", "hog", "hophyllite", "horite", "hotite", "houseite",
          "hrite", "hroite", "hsonite", "htelite", "htite", "hurite", "hwater pearl", "hydrocalcite", "hyhydrite",
          "hylite", "hyllite", "hynite", "hyst", "ialaite", "ialite", "ialyte", "ian", "ianite", "iapite", "iaumite",
          "iba", "ibergite", "ibole", "icate", "icellite", "ichalcite", "icite", "ickite", "iclase", "icoatite",
          "icolite", "icot", "icrete", "iculite", "icupride", "idcreekite", "idine", "idite", "idocrocite", "idolite",
          "idot", "ieite", "ieldite", "ierite", "ieslebenite", "ifornite", "igerite", "igite", "igmannite", "igmatite",
          "igorite", "ihydrite", "iite", "ikahnite", "ilarite", "ile", "ilianite", "ilite", "illite", "imanite", "imar",
          "iment", "imony", "imorphite", "inaite", "inawite", "indrite", "ine", "ingerite", "ingite", "ingstonite",
          "ingtonite", "inguaite", "inierite", "ininite", "inite", "inium", "inolite", "insite", "inspar", "inum",
          "ioclase", "iodor", "iolite", "ionite", "iophilite", "iotite", "iotrope", "iposite", "irine", "is", "iscite",
          "isite", "itaenite", "ite", "ite ", "iterite", "ithauptite", "itoite", "ium", "ive", "iz", "izawaite", "k",
          "kahnite", "kankasite", "kardite", "keite", "kel", "keline", "kelite", "kenite", "kerite", "kesite",
          "khawthorneite", "kinawite", "kinite", "kite", "klinite", "kmanite", "koreaite", "ksite", "ky", "l",
          "lacolloite", "ladium", "laite", "landite", "langerite", "larite", "lase", "laseite", "lastonite", "lbite",
          "lcanthite", "lcedony", "lcite", "lcocite", "lcolite", "lcopyrite", "ldrenite", "le", "lecite", "leite",
          "lemite", "lenite", "lerite", "lesite", "lewoodite", "leyite", "lgar", "lhauite", "li", "liaumite",
          "ligerite", "limanite", "ling", "lingite", "linguaite", "linite", "linsite", "lipscombite", "lipsite", "lite",
          "llacolloite", "lleite", "llipsite", "llite", "llonite", "lockite", "loidite", "loizite", "lomelane",
          "lonite", "looite", "lophane", "lorite", "loysite", "lsite", "lsonite", "ltite", "lucite", "lurite", "lurium",
          "lurobismuthite", "lusion", "lusite", "lussite", "lveyite", "lybite", "lyerite", "lygonite", "lzite", "m",
          "macosiderite", "maline", "mallite", "mandite", "manite", "mannite", "mar", "margyrite", "marine",
          "masclarkite", "masite", "mbite", "mboclase", "mellite", "melsbergite", "ment", "mersite", "mesite",
          "meyerite", "miculite", "milite", "mingtonite", "minite", "minium", "mite", "mium", "mmallite", "molite",
          "mond", "mondine", "montite", "mony", "moreite", "morillonite", "morphite", "mosite", "motome", "mquistite",
          "msenolite", "msite", "mulite", "muth", "muthinite", "na", "nabar", "nacite", "naite", "nakiite", "nakite",
          "nallite", "nantite", "nardite", "nasite", "nathyite", "nbergite", "nblende", "nckeite", "ndine", "ndite",
          "ndrite", "ndrodite", "ndum", "ne", "nechite", "neite", "nel", "nelian", "nellite", "nerite", "nerupine",
          "nesia", "nesioferrite", "nesite", "nessite", "net", "netite", "nezite", "ngerite", "nghengite",
          "nghuacerite", "ngite", "ngstonite", "ngtonite", "nic", "nicochroite", "nierite", "niite", "ninaite",
          "ningite", "ninite", "nite", "nium", "nkhawthorneite", "nklinite", "nnerite", "nniite", "nnite",
          "nochrysotile", "nockite", "noclase", "noclasite", "nogen", "nohedrite", "nohorite", "nohumite", "nolite",
          "nonite", "nophane", "nopilite", "noptilolite", "nopyrite", "notite", "notrichite", "novite", "nowodginite",
          "nozoisite", "nsite", "nskovite", "nspar", "nstedtite", "nstone", "nthite", "ntianite", "ntienite", "ntinite",
          "ntite", "ntoid", "ntonite", "nturine", "ntzite", "nwaldite", "nzenite", "nzite", "o", "obbiite",
          "obotryogen", "obsite", "ocerite", "ochite", "ochlore", "ochromite", "ochrosite", "ochrysotile", "ochvilite",
          "ockite", "oclase", "oclasite", "ocline", "ocolumbite", "oconite", "odite", "odonite", "odor", "odstone",
          "oeite", "oelite", "oepite", "og", "oganite", "ogen", "ogopite", "ogrossular", "ohedrite", "ohorite",
          "ohortonolite", "ohumite", "ohydrocalcite", "oite", "okesite", "okite", "oleite", "olinite", "olite",
          "ollite", "olusite", "omagnesite", "omelane", "omeyerite", "omite", "omium", "omorphite", "on", "onaldite",
          "ond", "ondine", "onellite", "onezite", "onite", "onolite", "onskovite", "ontianite", "ontite", "onyx",
          "ooite", "ope", "opericlase", "ophane", "ophanite", "ophilite", "ophoenicite", "ophyllite", "opilite",
          "optilolite", "oradoite", "orapatite", "orargyrite", "orastrolite", "orcaphite", "oreite", "oriate",
          "orichterite", "orite", "oritoid", "orl", "ornite", "orokite", "orsite", "orspar", "orthite", "ortierite",
          "osewichite", "osite", "ospinel", "ostibite", "otantalite", "ote", "otime", "otite", "otlite", "otome",
          "otrichite", "otrope", "ottaite", "ovite", "ovskite", "ovskyite", "ownite", "oxene", "oxferroite", "oxyhyte",
          "oxylapatite", "oysite", "ozincite", "ozite", "ozoisite", "ozonite", "pacaite", "paite", "pe", "peite",
          "pellyite", "pentine", "per", "perite", "pfite", "phane", "phanite", "phire", "phirine", "phite",
          "phophyllite", "phorite", "phylite", "phyllite", "pite", "plite", "ploidite", "pmanite", "polite", "pore",
          "posite", "pside", "pstone", "ptase", "puhyite", "purite", "quelinite", "quistite", "quoise", "r", "radite",
          "radoite", "radorite", "radymite", "rahedrite", "rald", "ramarine", "ramite", "randite", "rapatite",
          "rargyrite", "rase", "rasovite", "rastrolite", "ratine", "rcaphite", "rchikhite", "rdite", "re", "realgar",
          "reibersite", "relite", "rereite", "ressite", "retteite", "reye", "rgerite", "rgerobinsonite", "rgite",
          "rgyrite", "rhotite", "rialite", "rianite", "riate", "richterite", "ricrete", "rierite", "rihydrite", "riite",
          "rine", "ringite", "rinite", "rite", "ritoid", "rizawaite", "rkeite", "rkite", "rkoite", "rl", "rleite",
          "rmacosiderite", "rmaline", "rmanite", "rmontite", "rmorite", "rnathyite", "rnonite", "ro", "rocerite",
          "rocline", "rocobaltite", "rocolumbite", "rodite", "roeite", "rogrossular", "rohortonolite", "roite",
          "rokite", "rolite", "rollite", "romagnesite", "ron", "ronite", "ropericlase", "rophilite", "rophyllite",
          "rotantalite", "rotil", "rovite", "roxylapatite", "rozincite", "rringite", "rrite", "rrylite", "rschaum",
          "rsite", "rskite", "rsonite", "rspar", "rsthene", "rthite", "rthoclase", "rtierite", "rtite", "rtsite",
          "rtveitite", "rtz", "ry", "rygibbsite", "ryite", "rylite", "ryogen", "ryptite", "rzalite", "s", "saite",
          "sanite", "sartite", "sassite", "schaum", "scite", "scombite", "sdaleite", "sdorffite", "selite", "senolite",
          "seolite", "serite", "sewichite", "sexite", "sfordite", "sgenite", "shite", "shwater pearl", "sian", "sicot",
          "side", "silite", "sine", "siolite", "site", "siterite", "sling", "smannite", "soberyl", "socolla", "solite",
          "sonite", "soprase", "sotile", "spar", "spathoid", "sphophyllite", "sphorite", "spinel", "spore", "ssanite",
          "ssartite", "ssite", "ssium", "ssular", "stedtite", "sterite", "stibite", "stine", "stite", "stobalite",
          "stone", "stonite", "stos", "stowite", "sular", "sum", "taenite", "tagonite", "talite", "tan", "tanite",
          "tase", "tatite", "te", "telite", "terite", "terudite", "tfonteinite", "thanite", "thauptite", "theite",
          "thenite", "thierite", "thite", "thoclase", "thrite", "thsonite", "thyst", "tialaite", "ticellite", "tienite",
          "tierite", "time", "tinum", "tite", "tlandite", "tlite", "tlockite", "tmorillonite", "tnasite", "tobalite",
          "tocalcite", "tochvilite", "toite", "tolite", "tomite", "tone", "tonite", "torbernite", "toreite", "torite",
          "towite", "tramite", "trandite", "trichite", "trine", "trolite", "tronite", "tterudite", "ttite", "ttuckite",
          "tuckite", "tunite", "tupite", "turine", "tveitite", "tz", "tzerite", "tzite", "uberite", "ubisite",
          "ucchacuaite", "uchilite", "ucite", "ucochroite", "ucodot", "uconite", "ucophane", "uelinite", "uggite",
          "ugite", "uhyite", "uite", "ukoreaite", "uli", "ulite", "um", "umasite", "umbite", "umene", "undum", "unite",
          "uoise", "upite", "ur", "urite", "urium", "urmbachite", "urobismuthite", "urolite", "urtonite", "ury",
          "usion", "usonite", "ussite", "ustite", "uth", "uthinite", "utite", "uttite", "uvianite", "uvite", "uyelite",
          "vanite", "vauxite", "ve", "vedsonite", "veite", "venite", "ver", "verite", "vertine", "vianite", "vine",
          "vite", "vorite", "vskite", "vskyite", "waldite", "wellite", "wertmannite", "wickite", "wigite", "wnite",
          "wsterite", "wurmbachite", "x", "xandrite", "xene", "xferroite", "xite", "xyhyte", "y", "yagite", "yamunite",
          "ybasite", "ybdenite", "ybite", "ycrase", "ydrite", "ydymite", "yelite", "yerite", "ygibbsite", "ygonite",
          "ygorskite", "yhalite", "yhydrite", "yite", "ykite", "yl", "ylite", "yllonite", "ymite", "yne", "yogen",
          "yoite", "yopilite", "yptite", "yrelite", "ysoberyl", "ysocolla", "ysoprase", "ysotile", "ystonite", "yte",
          "ytocalcite", "z", "zalite", "zanite", "zerite", "zilianite", "zite", "zlewoodite", "zonite", "zottaite",
          "zziite"]
    value = [10, 50, 100, 500, 1000, 5000, ]
    Name = ""
    Cost = Rarity = 0

    def __init__(self, rarity):
        self.Name = self.j1[randint(len(self.j1))] + self.j2[randint(len(self.j2))] + self.j3[randint(len(self.j3))]
        if rarity >= 5:
            rarity %= 5
        self.Rarity = rarity
        self.Cost = self.value[self.Rarity] * (random_sample() + 1)

    def __str__(self):
        l = ['Low Quality Gems', 'Semi Precious Gems', 'Medium Quality Gemstones', 'High Quality Gemstones', 'Jewels', 'Grand Jewels']
        s = '<tr><td style="width:50%;"><span class="text-md">' + self.Name + '</span></td><td>' + \
            determine_cost(self.Cost) + '</td><td>' + l[self.Rarity] + '</td></tr>'
        return s


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


def create_book_shop(owner, genres, quan, inflate=1):
    for b in genres:
        if b not in Books.Genres:
            print(b, "Not in genre List. See: ", Books.Genres)
            return None
    a = Store(owner, str(Antiques()) + " (Library)", (sum(random_sample(inflate)) / inflate) + .5, [0, 9])
    a.fill_store(Book, quan)
    return a


def create_enchantment_shop(owner, rarity, quan, inflate=1):
    name = str(Enchanter())
    a = Store(owner, name + " (Enchantments)", (sum(random_sample(inflate)) / inflate) + .5, rarity)
    if quan <= 2:
        quan = 3
    remain = randint(quan)
    a.fill_store(Scroll, remain)
    a.fill_store(Wand, quan - remain)
    return a


def create_enchanter_shop(owner, rarity, quan, inflate=1):
    name = str(Enchanter())
    a = Store(owner, name + " (Enchanter)", (sum(random_sample(inflate)) / inflate) + .5, rarity)
    for _ in range(quan):
        a.Stock.append(Scroll(randint(rarity[0], rarity[1]), naming=False))
    return a


def create_weapon_shop(owner, rarity, quan, inflate=1):
    name = str(Blacksmith()) + " (Weapon)"
    a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    if quan <= 2:
        quan = 3
    a.fill_store(Weapon, quan)
    return a


def create_armor_shop(owner, rarity, quan, inflate=1):
    name = str(Blacksmith()) + " (Armor)"
    a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    if quan <= 2:
        quan = 3
    a.fill_store(Armor, quan)
    return a


def create_potion_shop(owner, rarity, quan, inflate=1):
    name = str(Potions())
    a = Store(owner, name + " (Alchemist)", (sum(random_sample(inflate)) / inflate) + .5, rarity)
    a.fill_store(Potion, quan)
    return a


def create_tavern(owner, qual, rooms, quan, inflate=1):
    # def __init__(self, keeper, name, service, qual, rooms, quan):
    name = str(Tavern()) + " (Inn)"
    return Inn(owner, name, (sum(random_sample(inflate)) / inflate), qual, rooms, quan)


def create_jewel_shop(owner, rarity, quan, inflate=1):
    name = str(Jeweller()) + " (Jeweller)"
    a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    a.fill_store(Jewel, quan)
    return a


def create_restaurant(owner, rarity, quan, inflate=1):
    name = str(Restaurant()) + " (Restaurant)"
    return Inn(owner, name, (sum(random_sample(inflate)) / inflate), rarity, 0, quan)


def create_general_store(owner, rarity, quan, trink, inflate=1):
    name = str(GeneralStore()) + " (General)"
    a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5, rarity)
    a.fill_store(General, quan)
    for _ in range(trink):
        a.Stock.append(General(0, True))
    return a


def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


if __name__ == '__main__':
    # for _ in range(15):
    #    Weapon(0).print_item()

    # for _ in range(15):
    #    Weapon(1).print_item()

    # for _ in range(15):
    #    Weapon(2).print_item()

    # for _ in range(15):
    #    Weapon(3).print_item()

    # for _ in range(15):
    #    Weapon(4).print_item()

    # print(Weapon(0))
    # print(Weapon(1))
    # print(Weapon(2))
    # print(Weapon(3))
    # print(Weapon(4))

    # st = create_weapon_shop(None, 1)
    # print(st.Store_name)
    # for item in st.Stock:
    #    item.print_item()

    # for _ in range(15):
    #    s = Scroll(0)
    #    print(s.Name, s.Price, s.Spell)

    # print(Armor(0))
    # for _ in range(50):
    #     print(Armor(0, 'Light'))
    # Armor(1).print_item()
    # Armor(2).print_item()
    # Armor(3).print_item()
    # Armor(4).print_item()

    # import pprint
    # pprint.PrettyPrinter(indent=4).pprint(list(MasterSpells.values()))

    # import re
    # for spell in list(MasterSpells.keys()):
    #     lowest = re.findall(r'\d+', MasterSpells[spell][0]['level'])
    #     print(spell, lowest)
    #     print(min(lowest))

    print(determine_cost(54591.23))

    # for level in [level_0, level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9]:
    #     for spell in level:
    #         try:
    #             test = MasterSpells[spell]
    #         except KeyError:
    #             print(spell)
