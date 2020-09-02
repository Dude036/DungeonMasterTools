from numpy.random import random, randint, choice
from resources import masterwork_traits_weapon, masterwork_trait_cost_weapon

# For Armor, See Here: https://www.d20pfsrd.com/magic-items/magic-armor/magic-armor-and-shield-special-abilities/
# For Weapons, See Here: https://www.d20pfsrd.com/magic-items/magic-weapons/magic-weapon-special-abilities/


def special_masterwork_weapon(Weapon, Trait=None):
    if Trait is not None and Trait in masterwork_traits_weapon:
        Weapon.Special = Trait
    else:
        # Get all potential options for our weapon type
        special_options = [
            'Anarchic', 'Axiomatic', 'Bane', 'Beaming', 'Benevolent',
            'Bewildering', 'Breaking', 'Called', 'Conductive', 'Corrosive',
            'Corrosive Burst', 'Dispelling', 'Dispelling Burst', 'Distracting',
            'Greater Distracting', 'Fervent', 'Flaming', 'Flaming Burst',
            'Flying', 'Frost', 'Furyborn', 'Ghost Touch', 'Heartseeker',
            'Heretical', 'Holy', 'Huntsman', 'Icy Burst', 'Igniting',
            'Impervious', 'Kinslayer', 'Limning', 'Lucky', 'Greater Lucky',
            'Merciful', 'Miserable', 'Negating', 'Patriotic', 'Peaceful',
            'Phase Locking', 'Planestriking', 'Redeemed', 'Repositioning',
            'Sacred', 'Shattering', 'Shock', 'Shocking Burst', 'Sneaky',
            'Speed', 'Spell Storing', 'Stalking', 'Summon Bane', 'Thawing',
            'Thundering', 'Toxic', 'Training', 'Treasonous', 'Truthful',
            'Unholy'
        ]
        if Weapon.Class == 'Bows':
            special_options += ['Adaptive', 'Ambushing']
        if Weapon.Class == 'Bows' or Weapon.Class == 'Crossbow':
            special_options += ['Endless Ammunition']
        if Weapon.Class == 'Thrown':
            special_options += ['Anchoring', 'Returning', 'Sharding']
        if Weapon.Class == 'Monk' or Weapon.Class == 'Close':
            special_options += ['Brawling', 'Sapping']
        if Weapon.Class in [
                'Bows', 'Crossbow', 'Thrown', 'Light Blade', 'Close', 'Spear'
        ]:
            special_options += ['Injecting']

        # Firearm Weapons
        if Weapon.Class in ['Pistol', 'Rifle', 'Shotgun', 'Sniper']:
            special_options += [
                'Dazzling', 'Dry Load', 'Reliable', 'Greater Reliable',
                'Sonic Boom'
            ]

        # Not a ranged weapon
        if Weapon.Class not in [
                'Bows', 'Thrown', 'Crossbow', 'Pistol', 'Rifle', 'Shotgun',
                'Sniper'
        ]:
            special_options += [
                'Advancing', 'Answering', 'Allying', 'Countering', 'Courageous',
                'Dazzling Radiance', 'Defending', 'Dueling', 'Exhausting',
                'Fortuitous', 'Furious', 'Glorious', 'Grayflame', 'Growing',
                'Guardian', 'Invigorating', 'Ki Focus', 'Ki Intensifying',
                'Liberating', 'Lifesurge', 'Menacing', 'Mighty Cleaving',
                'Mimetic', 'Neutralizing', 'Ominous', 'Quenching', 'Rusting',
                'Seaborne', 'Sharding', 'Shrinking', 'Spell Siphon',
                'Spell Stealing', 'Throwing', 'Umbral', 'Underwater', 'Unseen'
            ]
            if Weapon.Class not in ['Heavy Axe', 'Heavy Blade']:
                special_options += ['Agile']
            if 'S' in Weapon.Damage or 'P' in Weapon.Damage:
                special_options += [
                    'Bloodsong', 'Culling', 'Debilitating', 'Gory', 'Keen',
                    'Wounding'
                ]
            if 'B' in Weapon.Damage:
                special_options += [
                    'Disruption', 'Impact', 'Legbreaker', 'Quaking', 'Smashing'
                ]
            if Weapon.Class in ['Light Axe', 'Light Blade', 'Close', 'Hammer']:
                special_options += ['Concealed', 'Concealed, Lesser']
            if Weapon.Class in [
                    'Heavy Axe', 'Heavy Blade', 'Light Axe', 'Light Blade',
                    'Polearm'
            ]:
                special_options += ['Deadly', 'Vorpal']

        else:
            special_options += [
                'Conserving', 'Cyclonic', 'Lesser Designating',
                'Greater Designating', 'Distance', 'Driving', 'Glitterwake',
                'Grounding', 'Heart-Piercing', 'Interfering', 'Nimble Shot',
                'Penetrating', 'Phantom Ammunition', 'Plummeting',
                'Second Chance', 'Seeking', 'Shadowshooting', 'Tailwind'
            ]

        Weapon.Special = choice(special_options)

    # Add text to weapon Quality
    get_flavor_text_weapon(Weapon.Special, Weapon)

    # Add the title of the masterwork quality to the weapon
    Weapon.Name = Weapon.Name[:2] + ' ' + Weapon.Special + Weapon.Name[2:]
    Weapon.Cost += (1 + Weapon.Masterwork) * 1000
    return Weapon


def get_flavor_text_weapon(name, Weapon=None):
    text = ''
    # Add text to weapon Quality
    if name == 'Adaptive':
        text = 'This weapon has a very high tensile strength, requiring a STR of ' + str(randint(10, 31)) + \
                      ' to be able to wield it correct. When wielding this Weapon, you use your Strength modifier' + \
                      ' instead of Dexterity when calculating to Hit or Dexterity.'

    elif name == 'Advancing':
        text = 'This weapon is designed for a frontline fighter. As a free action, you can move an ' + \
                      'additional 10 ft. of movement, but have a -2 to hit on the turn you take that movement in.'

    elif name == 'Agile':
        text = 'This weapon grants the finesse property. You may use your Dexterity instead of your ' + \
                      'Strength for attack and damage with this weapon.'

    elif name == 'Allying':
        text = 'This weapon grants a flanking bonus, to you and an ally. You may take this flanking bonus' + \
                      ' as long as there is an enemy within 5ft of the same creature you\'re attacking.'

    elif name == 'Ambushing':
        text = 'This weapon is designed for Surprise encounters. If you act during a Surprise round, you ' + \
                      'may apply an additional 1d6 points of Sneak Attack Damage on a successful hit.'

    elif name == 'Anarchic':
        text = 'This weapon was created in The Abyss. This weapon cannot be wielded by a Lawful creature.' + \
                      ' Any Lawful creatures attempting to do so, take 2d6 damage every round. Any Chaotic or ' + \
                      'Neutral creatures wielding this weapon deal an additional 2d6 damage against Lawful ' + \
                      'creatures.'

    elif name == 'Anchoring':
        text = 'This weapon is designed to fasten a creature in place. If you make a successful attack ' + \
                      'against the creature with this weapon, they enemy is rendered restrained, and must spend ' + \
                      'a standard action to remove this condition.'

    elif name == 'Answering':
        text = 'This weapon is designed to riposte. Creatures who miss an attack against you, you can use your ' + \
               'reaction to make an attack of opportunity against the creature.'

    elif name == 'Axiomatic':
        text = 'This weapon was created in Mechanus. This weapon cannot be wielded by a Chaotic creature. Any ' + \
               'Chaotic creatures attempting to do so, take 2d6 damage every round. Any Lawful or Neutral creatures' + \
               'wielding this weapon deal an additional 2d6 damage against Chaotic creatures.'

    elif name == 'Bane':
        creatures = choice([
            'aberrations', 'beasts', 'celestials', 'constructs', 'dragons',
            'elementals', 'fey', 'fiends', 'giants', 'monstrosities', 'oozes',
            'plants', 'undead'
        ])
        text = 'This weapon is designed to be destructive to a certain type of foe. Deal an additional 2d6 points ' + \
               'of damage against creatures of the ' + creatures + ' type.'

    elif name == 'Beaming':
        text = 'This weapon has light infused inside of the weapon. You speak the command word of the weapon, and ' + \
               'your weapon acts as if the light spell was cast on it.'

    elif name == 'Benevolent':
        text = 'This weapon allows you to aid another during their attack. If you and an ally are within 30 ft of ' + \
               'each other, you may expend your standard action, to allow your ally to take an attack action ' + \
               'instead of you.'

    elif name == 'Bewildering':
        text = 'This weapon allows the wielder to cast the Confusion spell as part of an attack. If the attack ' + \
               'successfully hits, the target must succeed a Wisdom saving throw of DC 8 + Proficiency + ' + \
               'Strength (or Dexterity).'

    elif name == 'Blood-Hunting':
        creatures = choice([
            'aberrations', 'beasts', 'celestials', 'dragons', 'fey', 'fiends',
            'giants', 'monstrosities'
        ])
        text = 'This weapon is designed to seek the blood of a certain type of foe. Deal an additional 1d6 points ' + \
               'of damage against creatures of the ' + creatures + ' type.'

    elif name == 'Bloodsong':
        text = "This weapon is designed for Barbarians. While a barbarian is raging and using this weapon, it's " + \
               "critical range increases by 1. (i.e. Critical at 20 becomes 19-20). If the wielder makes a " + \
               "critical hit, they gain half the HP dealt as damage as Temporary HP to themselves."

    elif name == 'Brawling':
        text = 'This weapon is designed for up close and personal combat. You gain proficiency with Athletics and ' + \
                'Acrobatics. If you are proficient already, you gain expertise. You also have advantage on attacks ' + \
                'made to grapple a target with this weapon.'

    elif name == 'Breaking':
        text = 'The weapon is designed as a seige weapon. You deals an additional 2d6 damage against Constructs, ' + \
               'Structures, or Objects.'

    elif name == 'Brilliant Energy':
        damage = choice(
            ['Acid', 'Cold', 'Fire', 'Force', 'Lightning', 'Poison', 'Thunder'])
        text = "This weapon was designed to deal " + damage + " damage instead of it's normal damage. You also deal"

    elif name == 'Called':
        text = "This weapon can be teleported back to the wielder's hands. This does not provoke attacks of " + \
               "opportunity. The range of this ability is 100 ft. Any attempt to call the weapon back outside of " + \
               "this range fails."

    elif name == 'Compassionate':
        text = 'This weapon can deal non-lethal damage, rendering a target who drops to 0 HP stable by this ' + \
               'weapon. You must express that you are not doing non-lethal damage before an attack attempt.'

    elif name == 'Concealed':
        text = 'This weapon has the ability to transform into a mundane item, of the same size/dimension. While ' + \
               'in this transformed state, creatures wishing to understand the true nature, must succeed a DC20 ' + \
               'Investigation check. This weapon can remain in its transformed state for 8 hours per day. ' + \
               'Transforming this item takes a standard action.'

    elif name == 'Lesser Concealed':
        text = 'This weapon has the ability to transform into a mundane item, of the same size/dimension. While ' + \
               'in this transformed state, creatures wishing to understand the true nature, must succeed a DC16 ' + \
               'Investigation check. This weapon can remain in its transformed state for 4 hours per day. ' + \
               'Transforming this item takes a standard action.'

    elif name == 'Conductive':
        text = 'This weapon has channels meant for magics. If a creature who can cast spells, uses this weapon, ' + \
               'they can channel a spell through this weapon as part of a melee attack. The spell can be any spell ' + \
               'that takes a bonus action, or a reaction to cast.'

    elif name == 'Conserving':
        text = "This weapon is designed to conserve ammunition. If an attack misses with a ranged attack, the " + \
               "first ammunition returns to it's quiver, case or container."

    elif name == 'Corrosive':
        text = 'This weapon is coated in a thick layer of acid. Attacks made with this weapon deal an additional ' + \
               '1d6 Acid Damage.'

    elif name == 'Corrosive Burst':
        text = "This weapon is coated in a thick layer of acid. Attacks made with this weapon deal an additional " + \
               "1d6 Acid Damage. If the wielder makes a critical hit against a creature, the damage becomes 1d10," + \
               " instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for " + \
               "every number above 2. x3 = 2d10; x7 = 6d10"

    elif name == 'Countering':
        text = 'This weapon is designed to deter enemies who try and disarm you. As a reaction, if a creature ' + \
               'attempts the Disarm action against you, you may make an attack of opportunity against the creature.'

    elif name == 'Courageous':
        text = "This weapon bolster's the wielder's courage. The wielder has advantage on saving throws against " + \
               "being frightened."

    elif name == 'Cruel':
        text = 'This weapon is a twisted tool of death. If a creature is hit with this weapon, the creature must ' + \
               'make a Wisdom Saving throw (DC 8 + Proficiency + Strength modifier) or be frightened. Once the ' + \
               'creature saves against this effect, they are immune to the effects for 24 hours.'

    elif name == 'Culling':
        text = 'This weapon allows the user to cleave through a target. When making an attack, if you succeed on ' + \
               'hitting a creature, you may attack a creature adjacent to the first creature, and within your ' + \
               'range. You make the second attack at disadvantage.'

    elif name == 'Cyclonic':
        text = "This weapon tends to move the air around your projcetiles. The wielder's projectiles are not " + \
               "hindered by Liquid or Gaseous environmental effects, such as Wind Wall."

    elif name == 'Dazzling':
        text = 'This weapon emits an explosive flash that dazzles all foes within a 15 ft cone in the direction of ' + \
               'the projectile. Creatures must succeed a Constitution Saving Throw (DC17) or be blinded for 1d4 rounds.'

    elif name == 'Dazzling Radiance':
        text = 'This weapon emits an explosive flash that dazzles all foes within a 15 ft of the wielder. ' + \
               'Creatures must succeed a Constitution Saving Throw (DC17) or be blinded for 1d4 rounds.'

    elif name == 'Deadly':
        text = 'This weapon instantly kills unsuspecting victims. If an enemy is unaware of the wielder, and the ' + \
               'wielder makes a successful attack against the enemy, roll damage normally. The enemy must make a ' + \
               'Constitution saving throw (DC is the damage dealt by this weapon). On a failed save, the enemy ' + \
               'falls Unconscious.'

    elif name == 'Debilitating':
        text = 'This weapon has wicked ridges, that tear flesh. If a creature is hit with this weapon during a ' + \
               'surprise round, the weapon removes their Dexterity modifier from their AC. This effect does not ' + \
               'work against creatures who have natural armor.'

    elif name == 'Defending':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = 'This weapon is meant to fend off attacks, more than being able to do damage. While wielding this ' + \
               'weapon, you may add +' + t + ' to your AC.'

    elif name == 'Defiant':
        text = 'This weapon is designed to keep its wielder alive in perilous situations. Once per day, if the ' + \
               'wielder of this weapon falls to 0 HP, they can choose to fall to 1 HP instead. This effect can ' + \
               'only done once per long rest'

    elif name == 'Greater Designating':
        text = "This weapon grants the wielder the ability to strike targets successively. Once you've made a " + \
               "successful ranged attack against a creature, you can choose this creature as your Target. If " + \
               "you choose to make another ranged attack against your Target, you have advantage against " + \
               "hitting the Target. You can do this a number of times per day equal to your Wisdom Modifier (min. 1)."

    elif name == 'Lesser Designating':
        text = "This weapon grants the wielder the ability to strike targets successively. Once you've made a " + \
               "successful ranged attack against a creature, you can choose this creature as your Target. If " + \
               "you choose to make another ranged attack against your Target, you can add your proficiency " + \
               "bonus twice against hitting the Target. You can do this a number of times per day equal to half " + \
               "of your Wisdom Modifier, rounded down (min. 1)."

    elif name == 'Dispelling':
        text = 'This weapon has Dispel Magic stored inside of the weapon. Once per day, you can cast Dispel ' + \
               'Magic at 3rd level using this weapon as your focus.'

    elif name == 'Dispelling Burst':
        text = 'This weapon has Dispel Magic stored inside of the weapon. Once per day, you can cast Dispel ' + \
               'Magic at 3rd level using this weapon as your focus. When you choose to do so, all spell effects ' + \
               'within 15 ft. of you also are effected by the spell.'

    elif name == 'Disruption':
        text = 'This weapon is designed to destroy Undead. All undead must make a Wisdom Saving throw (DC 8 + ' + \
               'Proficiency + Wisdom modifier). On a fail, the Undead is frightened. The Undead whose CR is less ' + \
               'than or equal to your highest Level divided by four (rounded down), are destroyed instead of frightened'

    elif name == 'Distance':
        text = 'This weapon is meant for range. Your range incriments are doubled.'

    elif name == 'Distracting':
        text = 'This weapon is meant to deter Spellcasters from using their spells. If you make a successful ' + \
               'attack against a creature who is concentrating, the DC of their Concetration check goes up by 5.'

    elif name == 'Greater Distracting':
        text = 'This weapon is meant to deter Spellcasters from using their spells. If you make a successful ' + \
               'attack against a creature who is concentrating, the DC of their Concetration check goes up by 10.'

    elif name == 'Driving':
        text = 'This weapon is designed to knock enemies away from you. If you make a successful attack against ' + \
               'a creature, they must make a Strength Saving throw (DC 8 + Proficiency + Dexterity modifier). If ' + \
               'they fail, they are knocked 5 ft away from the wielder. If the creature fails by more than 10, ' + \
               'they are knocked prone.'

    elif name == 'Dry Load':
        text = 'The weapon is build for surviving underwater use. This weapon is not rendered broken underwater. ' + \
               'It also allows the wieder to reload and fire the weapon underwater, and is only limited by the ' + \
               'regular rules of underwater combat.'

    elif name == 'Dueling':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = 'This weapon grants the user speed in combat, and deftness in reaction. Add +' + t + ' to your ' + \
               'Initiative while wielding this weapon. You also have advantage on saves against being disarmed.'

    elif name == 'Endless Ammunition':
        text = 'This weapon is designed for users spares of ammunition. Every time you draw an arrow/bolt from a ' + \
               'quiver/container, the same type of arrow/bolt is replicated back into your quiver. The ammunition, ' + \
               'once it hits a target or misses, vanishes from existence.'

    elif name == 'Exhausting':
        text = 'This weapon saps the energy from a target. When this weapon strikes a critical hit, the wielder ' + \
               'can choose to forgo the regular effects of a critical, and inflict 1 level of exhaustion on the target.'

    elif name == 'Fervent':
        text = 'This weapon grants the wielder the ability to channel divinity through their weapon. If you ' + \
               'worship a diety, you gain a proficiency with Religion and Insight checks. If you already have ' + \
               'proficiency, you gain expertise with Religion and Insight.'

    elif name == 'Flaming':
        text = 'This weapon is covered in fire. Attacks made with this weapon deal an additional 1d6 of fire damage.'

    elif name == 'Flaming Burst':
        text = "This weapon is covered in fire. Attacks made with this weapon deal an additional 1d6 of fire " + \
               "damage. If the wielder makes a critical hit against a creature, the damage becomes 1d10, instead " + \
               "of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for every " + \
               "number above 2. x3 = 2d10; x7 = 6d10."

    elif name == 'Flying':
        text = 'This weapon grants the user the ability to fly. While wielding this weapon, the user gains an ' + \
               'innate fly speed equal to half their movement speed.'

    elif name == 'Fortuitous':
        text = 'This grants the wielder lightning fast reactions. The wielder of this weapon can make as many ' + \
               'attacks of opportunity as the like.'

    elif name == 'Frost':
        text = 'This weapon is covered in ice. Attacks made with this weapon deal an additional 1d6 of cold damage.'

    elif name == 'Furious':
        text = 'This weapon contains the spirit of a barbarian. The wielder is granted a Level 1 Barbarian\'s Rage ' + \
               'ability. You may enter a Rage once per Long Rest.'

    elif name == 'Furyborn':
        text = 'This weapon slowly becomes more dangerous against an enemy, the more it gets attacked with it. With' + \
               ' every successful attack against a creature, the wielder gains a +1 to damage, which stacks. This ' + \
               'bonus is lost on a missed attack.'

    elif name == 'Ghost Touch':
        text = 'This weapon seems to be guided towards ghost like creatures. You deal an additional 1d6 Force ' + \
               'Damage against Undead'

    elif name == 'Glitterwake':
        text = 'This weapon helps see invisible creatures. The wielder may target a square, as part of an attack. ' + \
               'All invisible creatures within 15 ft. of that square must make a Dexterity Saving throw (DC 8 + ' + \
               'Proficiency + Dexterity modifier). On a fail, the creature is coated in a glittering dust, and ' + \
               'rendered visible. The wielder can use this ability a number of times equal to their Wisdom modifier' + \
               ' (min 1).'

    elif name == 'Glorious':
        text = "This weapon grants the wielder the ability to charm creatures. All enemies within 30 ft of the " + \
               "wielder must make a Charisma saving throw (DC 8 + Proficiency + Charisma modifier), or be charmed" + \
               " for 1 minute. If the creature is damaged during that minute, the charmed effect is broken. This " + \
               "can be done a number of times equal to the wielders Charisma modifer (min. 1). Creatures who have " + \
               "been affected by this ability in the past 24 hours, or whose CR is greater than the wielder's level" + \
               " are uneffected."

    elif name == 'Gory':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = "This weapon is meant to bleed an enemy of all it's life. On a successful hit, the creature takes " + \
               t + " Bleed damage that stacks. This Bleed occurs on the enemy's turn, and can be cured by any " + \
               "healing effect, or a successful DC15 Medicine Check."

    elif name == 'Grayflame':
        text = 'This weapon is designed for Paladins and Clerics. Whenever the wielder uses a their channel ' + \
               'divinity or applies a Smite to an attack, the weapon deals an additional 1d6 Radiant damage ' + \
               'for the next minute. This ability does not stack with itself.'

    elif name == 'Grounding':
        text = 'This weapon is meant to bring down flying creatures. If a creature is flying when struck by ' + \
               'this weapon, they tak an additional 1d6 damage and have disadvantage on maintaining flight.'

    elif name == 'Growing':
        text = 'This weapon enhances its wielder to grow in size. Once per long rest, the wielder may cast ' + \
               'Enlarge on themselves for the full duration. You may also speak the command word and cause ' + \
               'the weapon to grow a size category. If you are able to wield a weapon of a size category ' + \
               'larger than yourself, you may use this weapon still. When the command word is spoken again, the ' + \
               'weapon returns to normal size.'

    elif name == 'Guardian':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = 'This weapon allows the user to protect themselves against magical effects. The wielder is ' + \
               'granted a +' + t + ' to all their saves while this weapon is equipped.'

    elif name == 'Heart-Piercing':
        text = "This weapon pierces the target's heart. This weapon cannot benefit from abilites that " + \
               "increase it's critical range. On a Critical hit, make another attack roll. If the second attack" + \
               " roll surpasses the AC of the target, the target is dead. On a fail, treat the critical normally."
        if Weapon is not None:
            for c in range(8):
                if 'x' + str(c) in Weapon.Crit:
                    Weapon.Crit = 'x' + str(c)

    elif name == 'Heartseeker':
        text = "This weapon ignores the effects of cover or concealment. If a target is behind three quarters or " + \
               "half cover, this weapon ignores any benefit to their AC. You also ignore obscuring effects such " + \
               "as Fog Cloud."

    elif name == 'Heretical':
        text = "This weapon grants the wielder destructive power against a God. If you worship a God, you cannot " + \
               "choose your God. Choose a God to be against. If an enemy is a follower of that God, you deal an " + \
               "additional 1d6 points of damage against the target."

    elif name == 'Holy':
        text = 'This weapon was created in Mount Celestia. This weapon cannot be wielded by a Evil creature. Any ' + \
               'Evil creatures attempting to do so, take 2d6 damage every round. Any Good or Neutral creatures ' + \
               'wielding this weapon deal an additional 2d6 damage against Evil creatures.'

    elif name == 'Huntsman':
        text = 'This weapon is meant for hunters. If the wielder has made a Survival check to track a creature ' + \
               'within the past 24 hours, the wielder deal an additional 1d6 points of damage to the tracked ' + \
               'target. This weapon also grants proficiency with Survival. If you are proficient with Survival,' + \
               ' you gain expertise with Survival.'

    elif name == 'Icy Burst':
        text = "This weapon is covered in ice. Attacks made with this weapon deal an additional 1d6 of cold " + \
               "damage. If the wielder makes a critical hit against a creature, the damage becomes 1d10, " + \
               "instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for every " + \
               "number above 2. x3 = 2d10; x7 = 6d10."

    elif name == 'Igniting':
        text = 'This weapon is covered in fire. Attacks made with this weapon ignite the enemy on fire. An enemy ' + \
               'on fire takes 1d6 fire damage on their turn for 1 minute, or until put out using a standard ' + \
               'action. You can also be put out by water, or a watery environment.'

    elif name == 'Impact':
        text = 'This weapon deals bludgeoning damage. Attacks made with this weapon deal an additional 1d6 of ' + \
               'bludgeoning damage.'

    elif name == 'Impervious':
        text = "This weapon has a magical resilience against effect that would damage this weapon. This weapon " + \
               "cannot be rusted (if metallic), or warped (if wooden). It also can only be broken by another " + \
               "Impervious weapon."

    elif name == 'Injecting':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = 'This weapon has a hollow point meant to store deadly Poisons. If this is a Melee weapon, you ' + \
               'can store up to ' + t + ' charges of poison that are applied on a successful melee attack. If ' + \
               'this is a Ranged weapon, each projectile can have a dose of poison applied to it.'

    elif name == 'Interfering':
        text = 'This weapon is designed to interfere with Battlefield movement. You may make attacks of ' + \
               'opportunity within 30 ft. or your closest range incriment (whichever is closer).'

    elif name == 'Invigorating':
        text = 'This weapon brings a bloodlust to its wielder. If the wielder drops an enemy to 0 HP, the wielder ' + \
               'is cured of 1 level of exhaustion. If the wielder is not exhausted, the wielder gaina +10 to their ' + \
               'movement speed, and have advantage on all creatures for 1 minute.'

    elif name == 'Keen':
        if Weapon is not None:
            if len(Weapon.Crit) == 2:
                Weapon.Crit = '19-20 ' + Weapon.Crit
            else:
                rang = abs(eval(Weapon.Crit[:-2])) + 1
                rang *= 2
                rang -= 1
                Weapon.Crit = str(20 - rang) + '-20 ' + Weapon.Crit[-2:]
            text = "This weapon's critical range is doubled. This weapon's crit power is now " + Weapon.Crit + '.'
        else:
            text = "This weapon's critical range is doubled. Ex. 19-20 [Range: 2] becomes 17-20 [Range: 4]"

    elif name == 'Ki Focus':
        text = "This weapon is designed for Monks. A Monk is proficient with this weapon, and can channel their " + \
               "Ki through this weapon, using this weapon's damage instead of their unarmed strike."

    elif name == 'Ki Intensifying':
        text = "This weapon is designed for Monks. A Monk is proficient with this weapon, and can channel their " + \
               "Ki through this weapon, using this weapon's damage instead of their unarmed strike. When using an" + \
               " ability that costs 1 Ki point, roll 1d6. On a 5 or a 6, you regain the Ki point."

    elif name == 'Kinslayer':
        text = "This weapon is designed to kill history. Attacks made with this weapon deal an additional 2d6 " + \
               "damage against creatures of the same family line."

    elif name == 'Legbreaker':
        text = 'This weapon slows the advances of creatures. Attacks made with this weapon reduce a creatures ' + \
               'movements speed by 10 for 1d4 rounds. Multiple attacks made do not decrease the speed further ' + \
               'than 10, but do increase the duration of the slow. On a Critical hit, the creatures movement ' + \
               'is reduced to 0 for the duration. A DC15 Medicine check or healing effect removes this penalty.'

    elif name == 'Liberating':
        text = 'This weapon helps a creature unable to move. If the wielder is affected by something that would ' + \
               'impede their movement, they have advantage on the save or check.'

    elif name == 'Lifesurge':
        text = 'This weapon grants resistance to Necrotic Damage. Attacks made with this weapon deal an ' + \
               'additional 1d6 points of damage to Undead.'

    elif name == 'Limning':
        text = "This weapon was built to kill Fae. On a successful attack, the wielder can choose to cast Faerie" + \
               " Fire on the enemy as a free action. the Faerie Fire lasts for the full duration, but uses the " + \
               "wielder's concentration. The wielder can do the a number of times equal to their Wisdom modifier."

    elif name == 'Lucky':
        text = 'This weapon has a lucky charm attached to it. The wielder has 1 Luck point, that they can use to ' + \
               'gain advantage on Saving Throws, Attack Rolls, and Ability Checks. The wielders Lucky points ' + \
               'refresh at the end of a Long Rest.'

    elif name == 'Greater Lucky':
        text = 'This weapon has a greater lucky charm attached to it. The wielder has 3 Luck point, that they can ' + \
               'use to gain advantage on Saving Throws, Attack Rolls, and Ability Checks. The wielders Lucky ' + \
               'points refresh at the end of a Long Rest.'

    elif name == 'Menacing':
        text = 'This weapon grants the wielder advantage on Intimidation checks made while wielding this weapon.'

    elif name == 'Merciful':
        text = 'This weapon deals non-lethal damage. Attacks made with this weapon deal an additional 1d6 points ' + \
               'of non-lethal damage. You can choose to deal lethal damage, but you must express that you want to ' + \
               'deal lethal damage before an attack attempt.'

    elif name == 'Mighty Cleaving':
        text = 'This weapon allows the user to cleave through a target. When making an attack, if you succeed on ' + \
               'hitting a creature, you may attack a creature adjacent to the first creature, and within your ' + \
               'range. You make the second attack normally.'

    elif name == 'Mimetic':
        text = 'This weapon mimics resistance towards damage. When taking damage from one of the following damage ' + \
               'types (Acid, Bludgeoning, Cold, Fire, Lightning, Necrotic, Piercing, Poison, Radiant, Slashing, or ' + \
               'Thunder), you can choose to gain resistance for 1 minute against that damage type. Once this ' + \
               'resistance is active, you cannot change it until the effects wear off.'

    elif name == 'Miserable':
        creatures = choice([
            'aberrations', 'beasts', 'celestials', 'constructs', 'dragons',
            'elementals', 'fey', 'fiends', 'giants', 'monstrosities', 'oozes',
            'plants', 'undead'
        ])
        text = "This weapon is designed to be destructive to a certain type of foe. Deal an additional 2d6 points " + \
               "of damage against creatures of the " + creatures + " type. This weapon cuts through resistances " + \
               "that would otherwise reduce the amount of damage taken. If the enemy has immunities to this type " + \
               "of damage, they instead have resistance. If the enemy has resistances to this type of damage, they" + \
               " take normal damage."

    elif name == 'Negating':
        text = "This weapon cuts through resistances that would otherwise reduce the amount of damage taken. If the" + \
               " enemy has immunities to this type of damage, they instead have resistance against this weapon. If " + \
               "the enemy has resistances to this type of damage, they take normal damage from this weapon."

    elif name == 'Neutralizing':
        text = 'This weapon renders poisons and other toxins innert. This weapon cannot be corroded by Acid. This ' + \
               'weapon also neutralized poisons inside its wielder. The wielder also cannot be poisoned'

    elif name == 'Nimble Shot':
        text = 'This weapon allows the user to make attacks without provoking attacks of opportunity.'

    elif name == 'Ominous':
        text = 'This weapon trails a shadowy haze behind it. All creatures hit by this weapon must make a Wisdom ' + \
               'Saving throw (DC 10 + Proficiency + Charisma modifier). On a failed save, the creature is ' + \
               'frightened for 1 minute, and cannot redo its save for the duration. Creatures affected by this ' + \
               'ability who pass, are immune to its effects for 24 hours.'

    elif name == 'Patriotic':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = "This weapon bleeds for its country. Gain a +" + t + " to History, Insight, Nature, and Survival " + \
               "within the land of the weapon's creation. Attacks made with this weapon deal an additional " + t + \
               " point of damage against enemies of a different nationality."

    elif name == 'Peaceful':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = "This weapon doesn't want to fight. Gain a +" + t + " to Persuasion, Insight, and Deception against" + \
               " creatures who you share a common language."

    elif name == 'Penetrating':
        text = "This weapon fires through enemies. If you make a successful attack against a creature, your " + \
               "ammunition pierces through behinds them. If that second enemy is still within the range of your " + \
               "weapon, and you can draw a straight line between all three enemies, you may make a second attack " + \
               "against the second enemy at disadvantage."

    elif name == 'Phantom Ammunition':
        text = 'This weapon leaves behind no trace of its existence. Any attacks made with these weapons, do normal' + \
               ' damage, but the wounds close and the ammunition disintegrates.'

    elif name == 'Phase Locking':
        text = 'This weapon tethers its enemies to this plane of existence. If you make a successful attack against' + \
               ' a creature, they cannot teleport away by magical means for 1d4 rounds.'

    elif name == 'Planestriking':
        text = 'This weapon is designed to be destructive to a certain type of foe. Deal an additional 1d6 points ' + \
               'of damage against creatures who are not native to the plane this weapon was created on.'

    elif name == 'Plummeting':
        text = 'This weapon is meant to bring down flying creatures. If a creature is flying when struck by this ' + \
               'weapon have disadvantage on maintaining flight.'

    elif name == 'Quaking':
        text = 'This weapon shakes the earth itself. May make an attack on the ground, and all foes within a 5 ft.' + \
               ' Radius, 10 ft. Cone, or 20 ft. Line make a Dexterity saving throw (DC 8 + Proficiency + Strength ' + \
               'modifer). If a creatures fails, they are knocked prone. The wielder has advantage on effects that ' + \
               'would render them prone.'

    elif name == 'Quenching':
        text = 'This weapon is always damp. The wielder can place this weapon into a non magical fire, and ' + \
               'extinguish it. This weapon treats any successful attack against Fire Elementals as Criticals.'

    elif name == 'Redeemed':
        text = 'This weapon was created in Evil, but has since been cleansed of it. This weapon cannot be wielded ' + \
               'by a Evil creature. Any Evil creatures attempting to do so, take 2d6 damage every round. Any Good ' + \
               'or Neutral creatures wielding this weapon deal an additional 2d6 damage against Evil creatures.'

    elif name == 'Reliable':
        text = "This weapon is designed to not jam or misfire. This weapon's misfire chance is reduced by up to 1. " + \
               "This has not been applied to the weapon's current stat block."

    elif name == 'Greater Reliable':
        text = "This weapon is designed to not jam or misfire. This weapon's misfire chance is reduced by up to 4. " + \
               "This has not been applied to the weapon's current stat block."

    elif name == 'Repositioning':
        text = "This weapon is designed to move freely through the Battlefield. You may move 5 ft. without " + \
               "incurring an attack of opportunity from an enemy. You also may take the Disengage action as a " + \
               "bonus action."

    elif name == 'Returning':
        text = 'This weapon flys on its own. On a miss, you make an additional attack without any bonuses against ' + \
               'the target, as the weapon attempts to return to you. On a miss, the projectile is returns to you. ' + \
               'On a hit, the creature only takes the weapon damage, with no modifiers (as if an off-hand weapon)'

    elif name == 'Rusting':
        text = "This weapon constantly sheds flecks of rust. On a critical hit, you can forgo the additional damage" + \
               " to corrode the enemy's weapon you're attacking. This effect is handled similair to how a Rust " + \
               "Monster's 'Rust Metal' ability works."

    elif name == 'Sacred':
        text = 'This weapon acts as a Holy symbol to your diety. Paladins and Clerics may treat this as their ' + \
               'Spellcasting Focus. You gain a proficiency with Religion. If you are already proficient, you gain ' + \
               'expertise in Religion.'

    elif name == 'Sapping':
        text = 'This weapon drains the strength of its enemies. Attacks made with this weapon deal 2d6 points of ' + \
               'non-lethal damage. On a critical, the enemy drops Unconscious for 2d4 rounds.'

    elif name == 'Seaborne':
        text = 'This weapon is at home on the ocean. The wielder of this weapon gains a natural swim speed equal ' + \
               'to half their movement speed rounded up. They also may dash as a bonus action underwater.'

    elif name == 'Second Chance':
        text = 'This weapon seeks its enemies for you. Once on each of your turns when you miss with a weapon ' + \
               'attack, you can make another weapon attack as part of the same action.'

    elif name == 'Seeking':
        text = 'This weapon seeks its enemies for you. The weapon does not have disadvantage when firing at an ' + \
               'invisible creature, into a heavily obscured area, or if environmental effects would otherwise grant' + \
               ' disadvantage. This weapon also treats cover as if it is one level less. Full Cover => Three ' + \
               'Quarters Cover => Half Cover => No Cover.'

    elif name == 'Shadowshooting':
        text = 'This weapon is a rogues best friend. Any attacks made in Darkness, Shade, or Dim Light qualify for ' + \
               'use of Sneak Attack.'

    elif name == 'Sharding':
        text = 'This weapon has a brittle quailty. On a critical hit, the weapon leaves some of itself inside the ' + \
               'enemy. The creature takes minimum damage each round until they spend an action removing the shards,' + \
               ' succeed on a DC 20 Medicine check, or are healed.'

    elif name == 'Shattering':
        text = "This weapon was designed to be destroyed. On a critical hit, deal an additional 1d10 Force Damage " + \
               "per crit multiplier level. (x2 = 1d10 | x5 = 4d10). This damage is NOT included in the weapon's " + \
               "critical. You weapon is destroyed as a result of this action."

    elif name == 'Shock':
        text = 'This weapon crackles with electricity. Attacks made with thise weapon deal an additional 1d6 points' + \
               ' of Lightning damage.'

    elif name == 'Shocking Burst':
        text = "This weapon crackles with electricity. Attacks made with thise weapon deal an additional 1d6 points" + \
               " of Lightning damage. If the wielder makes a critical hit against a creature, the damage becomes " + \
               "1d10, instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for" + \
               " every number above 2. x3 = 2d10; x7 = 6d10"

    elif name == 'Shrinking':
        text = 'This weapon shrinks itself, and its wielder. Once per long rest, you may cast Reduce on yourself ' + \
               'for the full duration. You may also speak the command word, and reduce the weapon to the size of a ' + \
               'dagger. The weapon gains the stats of a regular Dagger of the same material. When the command word ' + \
               'is spoken again, the weapon returns to its normal time.'

    elif name == 'Silencing':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = 'This weapon is silence and deadly. On a successful attack, the enemy is treated as if inside of a ' + \
               'Silence spell for 1 round. On a critical hit, the silence on the creature lasts for an additional ' + \
               '1d4+' + t + ' rounds.'

    elif name == 'Smashing':
        text = 'This weapon breaks things. Attacks made with this weapon deal an additional 2d6 points of damage.'

    elif name == 'Sneaky':
        text = 'This weapon is designed those who want to be Rogues. Attacks deal an additional 1d6 points of ' + \
               'Sneak attack damage as long as attack has advantage, or during a surprise round.'

    elif name == 'Sonic Boom':
        text = 'This weapon has a loudener on it. Attacks made with this weapon deal an additional 1d6 points ' + \
               'of Thunder damage to all enemies in a 15 ft. cone from the wielder.'

    elif name == 'Speed':
        text = 'This weapon is swift. The user gains an additional attack when taking the Attack Action with ' + \
               'this weapon.'

    elif name == 'Spell Siphon':
        text = "This weapon drains Spellcasters. On a successful attack against a Spellcaster, you automatically" + \
               " learn what spells the caster has active. On a critical hit against a Spellcaster, you can attempt" + \
               " to steal a spell slot from them. Enumerate the spell slots and roll approriately to steal. " + \
               "Example: the Enemy has 3 level one spell slots, and 2 level two spell slots. Since there are 5 " + \
               "potential slots to steal, you will roll 1d10. On a 1 or 2, you steal the first level one slot. On " + \
               "a 3 or 4, you steal the second level one slot, and so on. On a 7 or 8, steal the first level two " + \
               "spell slot. On a 9 or 10 steal the second level two spell slot. Leave this to the DM's discretion. " + \
               "The wielder then gains that spell slot, and can use it before they take a long rest."

    elif name == 'Spell Stealing':
        text = 'This weapon leeches knowledge from Spellcasters. On a successful hit, the wielder may learn a ' + \
               'random spell, not a cantrip, from the enemy\'s spellbook, even if the spell is not available to' + \
               ' the wielder normally. If the wielder is a Wizard or Artificer, they may choose to add it to their' + \
               ' spell book before they take a long rest to learn the spell permenantly. If the wielder is any ' + \
               'other Spellcaster, they may choose to swap out one of their known spells for the one they learned.'

    elif name == 'Spell Storing':
        if Weapon is not None:
            if Weapon.Masterwork == 1:
                t = '1st'
            elif Weapon.Masterwork == 2:
                t = '2nd'
            elif Weapon.Masterwork == 3:
                t = "3rd"
            else:
                t = str(Weapon.Masterwork) + 'th'
        else:
            t = '[Your Masterwork Quality]'
        text = "This weapon holds a spell slot. This weapon holds a " + t + " level spell slot. Whatever spell is " + \
               "stored in this weapon, is cast at " + t + " level. To store a slot in this weapon, you cast the " + \
               "spell as if it was a ritual spell, regardless of if the spell has a ritual tag or not. Casting the " + \
               "spell from this weapon is no different from casting the spell normally, other than the spell slot used."

    elif name == 'Stalking':
        text = "This weapon is meant attack known foes. Once per turn, you can spend your bonus action studying a " + \
               "foe's weaknesses. You deal an additional 1d6 points of damage against a foe who has been studied. " + \
               "You may only have one target studied at a time."

    elif name == 'Summon Bane':
        text = 'This weapon is meant to deal with summoned creatures. Attacks made with this weapon deal an ' + \
               'additional 2d6 damage to summoned creatures or companion animals.'

    elif name == 'Tailwind':
        text = 'This weapon gusts wind with each projectile. Every attack made with this weapon acts as if the Gust' + \
               ' cantrip eminates from the projectile.'

    elif name == 'Thawing':
        text = 'This weapon gives a warming heat. Attacks made with this weapon deal an additional 1d6 points of ' + \
               'damage to enemy Elementals who are Icy. This weapon also melts any icy within a 5 ft. square that ' + \
               'it touches.'

    elif name == 'Throwing':
        text = "This weapon is designed to be thrown. If this weapon increases it's throw distance by 10 ft. If the" + \
               " weapon doesn't have throw distance, it is now 10, and gains the Thrown property."

    elif name == 'Thundering':
        text = "This weapon vibrates with a loud low frequency. Attacks made with these weapon deal an additional " + \
               "1d6 points of Thunder damage. If the wielder makes a critical hit against a creature, the damage " + \
               "becomes 1d10, instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra " + \
               "damage for every number above 2. x3 = 2d10; x7 = 6d10"

    elif name == 'Toxic':
        text = "This weapon is designed to deliver poison. If a poison is applied to this weapon, the poison's DC " + \
               "is increased by 2. On a successful attack, roll 1d4. On a 4, the poisonous dose was not completely " + \
               "expended in the attack and the weapon is still poisoned."

    elif name == 'Training':
        feat = choice([
            'Aberrant Dragonmark', 'Actor', 'Alert', 'Athlete',
            'Bountiful Luck', 'Charger', 'Crossbow Expert', 'Defensive Duelist',
            'Dragon Fear', 'Dragon Hide', 'Drow High Magic', 'Dual Wielder',
            'Dungeon Delver', 'Durable', 'Dwarven Fortitude', 'Elemental Adept',
            'Elven Accuracy', 'Fade Away', 'Fey Teleportation',
            'Flames of Phlegethos', 'Grappler', 'Great Weapon Master', 'Healer',
            'Heavily Armored', 'Heavy Armor Master', 'Infernal Constitution',
            'Inspiring Leader', 'Keen Mind', 'Lightly Armored', 'Linguist',
            'Lucky', 'Mage Slayer', 'Magic Initiate', 'Martial Adept',
            'Medium Armor Master', 'Mobile', 'Moderately Armored',
            'Mounted Combatant', 'Observant', 'Orcish Fury', 'Polearm Master',
            'Prodigy', 'Resilient', 'Revenant Blade', 'Ritual Caster',
            'Savage Attacker', 'Second Chance', 'Sentinel', 'Sharpshooter',
            'Shield Master', 'Skilled', 'Skulker', 'Spell Sniper',
            'Squat Nimbleness', 'Svirfneblin Magic', 'Tavern Brawler', 'Tough',
            'War Caster', 'Weapon Master', 'Wood Elf Magic'
        ])
        text = 'This weapon contains a trained feature. This weapon contains the ' + feat + ' feat. You may ' + \
               'consider this feat known, so long as you meet the prerequisites, and have the weapon in your' + \
               ' possesion. '

    elif name == 'Treasonous':
        if Weapon is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Weapon.Masterwork)
        text = "This weapon bleeds against its own country. Gain a +" + t + " to History, Insight, Nature, and " + \
               "Survival within the land of the weapon's creation. Attacks made with this weapon deal an additional" + \
               t + " point of damage against enemies of the same nationality."

    elif name == 'Truthful':
        text = 'This weapon pierces through illusionary magics. The wielder gains advantages on saves against ' + \
               'illusions. Once per long rest, the wielder may cast See Invisibility on themselves for the full' + \
               ' duration.'

    elif name == 'Umbral':
        text = 'This weapon was crafted in the Underdark. The wielder gains darkvision within 60 ft. If the ' + \
               'wielder already has darvision, the range increases by 30 ft. Once per long rest, the weilder may' + \
               ' speak the command work of this weapon to cast Darkness centered around the Blade. The weilder is' + \
               ' able to see through this darkness as long as he holds onto the weapon. If the weapon is sheathed,' + \
               ' dropped, disarmed, or otherwise stowed, the darkness disapates.'

    elif name == 'Underwater':
        text = "This weapon is forged in the Elemental plane of Water. It seemlessly operates in the water, as well" + \
               " as it did in the water. The wielder of this weapon takes no penalties using this weapon underwater."

    elif name == 'Unholy':
        text = 'This weapon was created in the Deepest level of Hell. This weapon cannot be wielded by a Good ' + \
               'creature. Any Good creatures attempting to do so, take 2d6 damage every round. Any Evil or Neutral' + \
               ' creatures wielding this weapon deal an additional 2d6 damage against Good creatures.'

    elif name == 'Unseen':
        text = 'This weapon is nigh invisible. The wielder may speak the command word, and the weapon becomes ' + \
               'invisible. The wielder has advantages on all attacks against all creatures who rely on Natural ' + \
               'vision for the next minute. Creatures who have Tremorsense or True Sight are unaffected. The ' + \
               'wielder can use this ability a number of times equal to their Wisdom modifier.'

    elif name == 'Valiant':
        text = 'This weapon bolsters those unafraid of danger. If a creature uses an ability, spell, or ' + \
               'spell-like ability that would inflict the Frightened Condition, the wielder has advantage against' + \
               ' such an ability. Attacks made with this weapon deal an additional 2d6 damage if the wielder ' + \
               'succeeds on their save.'

    elif name == 'Vampiric':
        text = 'This weapon drains lifeforce from the living. When the wielder of this weapon makes a successful ' + \
               'attack against a creature, the user gains Temporary HP equal to half the damage dealt. If a Good ' + \
               'or Lawful creature attempts to wield this weapon, the have disadvantage on all attack rolls.'

    elif name == 'Greater Vampiric':
        text = 'This weapon drains lifeforce from the living. When the wielder of this weapon makes a successful ' + \
               'attack against a creature, the user gains Temporary HP equal to the damage dealt. If a Good or ' + \
               'Lawful creature attempts to wield this weapon, the have disadvantage on all attack rolls and is ' + \
               'poisoned for 24 hours.'

    elif name == 'Vicious':
        text = 'This weapon deals damage at a cost. Attacks made with this weapon deal an additional 2d6 damage ' + \
               'against the target, and 1d6 damage to the wielder.'

    elif name == 'Vorpal':
        text = "This weapon decapitates the target. This weapon cannot benefit from abilites that increase it's " + \
               "critical range. On a Critical hit, make another attack roll. If the second attack roll surpasses " + \
               "the AC of the target, the target is dead. On a fail, treat the critical normally."

    elif name == 'Wounding':
        text = "This weapon is meant to bleed an enemy of all it's life. On a successful hit, the creature takes " + \
               "1 Bleed damage that stacks. This Bleed occurs on the enemy's turn, and can be cured by any healing " + \
               "effect, or a successful DC15 Medicine Check."

    if Weapon is not None:
        Weapon.Text = '<p>' + text + '</p>'
    else:
        return text


def get_masterwork_level_weapon(name):
    for i in range(1, 6):
        if name in masterwork_trait_cost_weapon[i]:
            return i


def find_masterwork_traits_weapon(stock_list):
    trait_list = set()
    html = ''

    # Find all Traits
    for item in stock_list:
        if item.Special != '':
            trait_list.add(item.Special)
        if item.Masterwork > 0:
            trait_list.add('')

    # Convert to List
    trait_list = list(trait_list)
    if '' in trait_list:
        html += '<p>This Seller is capable of making weapons Masterwork. To make a weapon masterwork, you need to ' + \
                'pay someone time and money to accomplish the goal. It takes 1 day for each 1,000 gp spent on the ' + \
                'upgrade, rounded down. Here is the following table for costs of each upgrade.</p><table><tr><th>' + \
                'Upgrade</th><th>Cost</th><th>Upgrade</th><th>Cost</th></tr>'
        for i in range(1, 11, 2):
            html += '<tr><td>+' + str(i) + '</td><td>' + str(2 * i * i * 1000) + '</td>'
            i += 1
            html += '<td>+' + str(i) + '</td><td>' + str(2 * i * i * 1000) + '</td></tr>'
        html += '</table><br>'

    if len(trait_list) > 1:
        trait_list.remove('')
        html += '<table class="inventory-table" style="width: 100%;"><tr><th>Name</th><th>Effect</th><th>Money Cost' + \
                '</th><th>Prerequisite</th></tr>'
        for item in trait_list:
            level = get_masterwork_level_weapon(item)
            html += '<tr><td>' + item + '</td><td>' + get_flavor_text_weapon(item) + '</td><td>'
            html += str(2 * level * level * 1000) + '</td><td>+' + str(level) + '</td></tr>'
        html += '</table>'

    return html


def special_masterwork_armor(Armor, Trait=None):
    if Trait is not None and Trait in masterwork_traits_armor:
        Armor.Special = Trait
    else:
        special_options = [
            'Adhesive', 'Arrow Catching', 'Arrow Deflection', 'Arrow-Collecting', 'Assiduous', 'Bastion', 'Benevolent',
            'Billowing', 'Bitter', 'Blinding', 'Buoyant', 'Calming', 'Champion', 'Channeling', 'Clangorous',
            'Cocooning', 'Crusading', 'Cushioned', 'Deceiving', 'Defiant', 'Delving',
        ]

        if Armor.Class == 'Light':
            special_options += ['Balanced', 'Bloodthirsty', 'Brawling', 'Burdenless', 'Creeping', ]
        if Armor.Class == 'Medium':
            special_options += ['Balanced', 'Bloodthirsty', 'Bolstering', 'Burdenless', 'Comfort', 'Corsair', ]
        if Armor.Class == 'Heavy':
            special_options += ['Adamant', 'Advancing', 'Bolstering', 'Burdenless', 'Comfort', 'Corsair', 'Dread Wing', ]
        if Armor.Class == 'Shield':
            special_options += ['Animated', 'Bashing', 'Bolstering', ]

        Armor.Special = choice(special_options)

    get_flavor_text_armor(Armor.Special, Armor)

    Armor.Name = Armor.Name[:2] + ' ' + Armor.Special + Armor.Name[2:]
    Armor.Cost += (1 + Armor.Masterwork) * 1000
    return Armor


def get_flavor_text_armor(name, Armor=None):
    text = ''
    if name == 'Adamant':
        text = 'Once per day, for a total of 9 rounds, You gain resistance to all Bludgeoning, Piercing, & ' + \
               'Slashing damage from nonmagical weapons.'

    elif name == 'Adhesive':
        text = 'while wearing this armor, you can gain the effects of <a href="https://5e.tools/spells.html#' + \
               'spider\%20climb_phb">Spider Climb</a> for 10 rounds once per day.'

    elif name == 'Advancing':
        text = 'Upon slaying an enemy, your movement speed is doubled for that round.'

    elif name == 'Amorphous':
        text = 'You have advantage on Escaping a Grapple. You also can attempt to Escape as a bonus action.'

    elif name == 'Animated':
        if Armor is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Armor.Masterwork)
        text = 'Once per day, you can throw your shield out, and it operates without you needing to use your ' + \
               'off hand. You gain the ability to weild a weapon with two hands, or wielding two weapons while ' + \
               'also benefiting from the Shield. This lasts for 5 consecutive rounds, and can be done ' + t + \
               ' times a day.'

    elif name == 'Arrow Catching':
        text = 'This armor grants a +1 to AC against ranged attacks.'
        if Armor is not None:
            if Armor.Class == 'Shield':
                if Armor is None:
                    t = '[Your Masterwork Quality]'
                else:
                    t = str(Armor.Masterwork)
                text += ' As a reaction to being shot by a projectile, you can attempt to catch it. Roll 1d10+' + \
                        t + ' and reduce the amount of incoming damage by that amount. You cannot gain HP as a' + \
                        ' of this trait. You cannot use this ability in combat if you have not acted yet.'

    elif name == 'Arrow Deflection':
        text = 'This armor grants a +2 to AC against ranged attacks. As a reaction to being shot by a ' + \
               'projectile, you can attempt to catch it. Roll 1d10+' + t + ' and reduce the amount of ' + \
               'incoming damage by that amount. You cannot gain HP as a of this trait.'

    elif name == 'Arrow-Collecting':
        if Armor is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Armor.Masterwork)
        text = 'When projectiles are fired at this armor, Roll 1d20. On a ' + t + ' or less, the projectile' + \
               ' begins orbiting the armor. The armor can hold up to ' + t + ' projectiles. The wearer can ' + \
               'release all projectiles orbiting the armor as a standard action towards a target. The target' + \
               ' must be within 30 ft. Make a Ranged Attack with each projectile towards the target. ' + \
               'All projectiles deal 1d6 damage.'

    elif name == 'Assiduous':
        text = 'Once per long rest, this armor grants advantage on a saving throw of your choice.'

    elif name == 'Balanced':
        text = 'Any attempt that a creature makes to knock the wearer of this armor prone has disadvantage. ' + \
               ' Likewise, any attempt the wearer of this armor makes to avoid being knocked prone has advantage.'

    elif name == 'Bashing':
        text = 'If you move at least 20 ft in a straight line towards an enemy, you deal an additional 1d6 ' + \
               'bludgeoning damage against the creature, and all attacks of opportunity have disadvantage ' + \
               'whlie moving in that straight line.'

    elif name == 'Bastion':
        text = 'All Allies, including yourself, have advantage against Wisdom, Intelligence, and Charisma ' + \
               'saving throws while within 15 ft of this armor.'

    elif name == 'Benevolent':
        text = 'If you are within 30 ft of an ally, you can use your standard action, to give your ally ' + \
                'your armor\'s AC until the start of your next turn.'

    elif name == 'Billowing':
        if Armor is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Armor.Masterwork)
        text = 'You can use your reaction to avoid taking fall damage. DC20-' + t + ' Dexterity saving ' + \
               'throw. On a success, you only take half of the calculated fall damage.'

    elif name == 'Bitter':
        if Armor is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Armor.Masterwork)
        text = 'Any natural attacks made against this creature must successed a DC8+' + t + ' to not ' + \
               'becomed sickened. Creatures who succeed this save are immune to the armor\'s effects for' + \
               ' 24 hours. Creatures who attempt to swallow the wearer of this armor make the save with disadvantage'

    elif name == 'Blinding':
        text = 'While fighting in bright sunlight, a creature must make a DC 14 Constitution saving throw. ' + \
               'On a failed save, the enemy is blinded for 1d4 rounds.'

    elif name == 'Bloodthirsty':
        text = 'While fighting with this armor, the wearer gains a +1 to AC for 1d4 rounds for each enemy they ' + \
               'have killed. If the wearer is Raging, they instead gain a +3 for 1d4 rounds.'

    elif name == 'Bolstering':
        text = 'If you make a successful attack against an enemy, add your proficiency bonus to all saving throws' + \
               ' made against that enemy. If you already add your proficiency bonus, add it twice.'

    elif name == 'Brawling':
        text = 'Add your proficiency bonus to attack and damage when making natural attacks / unarmed strikes ' + \
               'against enemies. If you already add your proficiency bonus, add it twice.'

    elif name == 'Buoyant':
        text = 'You no longer automatically sink when in water. When wearing this armor, you do not treat water as' + \
               ' difficult terrain when calculating movement.'

    elif name == 'Burdenless':
        text = 'Your carrying capacity is now 30 x Strength Score. Your Drag, Lift, or Haul capacity is now 45 x ' + \
               'Strength Score.'

    elif name == 'Calming':
        text = 'Once per long rest, you can cast <a href="https://5e.tools/spells.html#calm\%20emotions_phb">Calm ' + \
               'Emotions</a> using this armor.'

    elif name == 'Champion':
        text = 'If you do not have the Smite Class ability; Once per day, you can expend your bonus action to deal' + \
               '2d8 Radiant damage to an enemy. If you have the Smite Class ability, your smites now deal an ' + \
               'additional 1d8 Radiant damage.'

    elif name == 'Channeling':
        if Armor is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Armor.Masterwork)
        text = 'You may use this armor as your holy symbol when casting divine spells. If you have the Channel ' + \
               'Divinity class ability, you gain the following method for channeling. All Allies within a 20 ft.' + \
               ' cone gain 2d6+' + t + ' HP. This ability cannot affect Undead or Constructs.'

    elif name == 'Clangorous':
        if Armor is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Armor.Masterwork)
        text = 'As a standard action, you slam your armor with a weapon. All creatures within 50 ft. make a DC8+' + \
               t + '+Proficiency Constitution Saving throw. On a failed save, the creature takes a 1d8 Thunder damage.'

    elif name == 'Cocooning':
        text = 'When you call Unconscious, a thick protective membrane envelops you. All non-targetted spells and ' + \
               ' environmental effects fail against you. This membrane lasts for 1d10 minutes, or until the wearer' + \
               ' regains conscienceness. This ability happens only once per long rest.'

    elif name == 'Comfort':
        text = 'This armor is comfortable enough to sleep in. You take no penalties from wearing this armor while ' + \
               'sleeping or resting'

    elif name == 'Corsair':
        text = 'This armor does not inhibit your movement speed, or other Dexterity based checks, such as stealth.'

    elif name == 'Creeping':
        text = 'Once per day, you speak the command word of this armor, and you treat all Stealth checks as if ' + \
               'you rolled a 17 for the next hour.'

    elif name == 'Crusading':
        text = 'This armor grants an additional +2 to AC against all Undead, Aberations, and Evil Dragons.'

    elif name == 'Cushioned':
        text = 'All fall damage is treated as if it were 20 feet less while wearing this armor.'

    elif name == 'Deathless':
        text = 'Once per long rest, when you fall to 0 HP, you can choose to fall to 1 HP instead. For the next ' + \
               'minute, your AC is increased by 1.'

    elif name == 'Deceiving':
        text = 'The wearer of this armor is not detectable via Detect Magic or Detect Evil and Good. The wearer ' + \
               'is also considered to have an Intelligence of 3 against Detect Thoughts.'

    elif name == 'Defiant':
        if Armor is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Armor.Masterwork)
        creatures = choice([
            'aberrations', 'beasts', 'celestials', 'constructs', 'dragons',
            'elementals', 'fey', 'fiends', 'giants', 'monstrosities', 'oozes',
            'plants', 'undead'
        ])
        text = 'This armor treats all incoming damage from ' + creatures + ' as if it were ' + t + ' less.'

    elif name == 'Delving':
        text = 'You gain a natural burrow movement speed of 10 ft.'

    elif name == 'Determination':
        text = 'Once per long rest, when you fall to 0 HP, you can choose to fall to 1 HP instead.'

    elif name == 'Dread Wing':
        if Armor is None:
            t = '[Your Masterwork Quality]'
        else:
            t = str(Armor.Masterwork)
        text = 'This armor transforms itself into the wings and the claws of a powerful Dragon. You do not gain the benefits of your AC, but you gain a fly speed of 60 ft. and a natural claw attack. It takes 1 minute to transform between your armored state and the dragon state. Your Claw uses your Strength bonus for damage and attack. The claw does 1d10+Strength modifier+' + t + '. You can transform a number of times equal to 2 x ' + t

    elif name == 'Energy Resistance':
        text = '_'

    elif name == 'Greater Energy Resistance':
        text = '_'

    elif name == 'Improved Energy Resistance':
        text = '_'

    elif name == 'Etherealness':
        text = '_'

    elif name == 'Evolving':
        text = '_'

    elif name == 'Expeditious':
        text = '_'

    elif name == 'Folding':
        text = '_'

    elif name == 'Fortification':
        text = '_'

    elif name == 'Frosted':
        text = '_'

    elif name == 'Ghost Spike':
        text = '_'

    elif name == 'Ghost Touch':
        text = '_'

    elif name == 'Glamered':
        text = '_'

    elif name == 'Grinding':
        text = '_'

    elif name == 'Harmonizing':
        text = '_'

    elif name == 'Heraldic':
        text = '_'

    elif name == 'Hosteling':
        text = '_'

    elif name == 'Impervious':
        text = '_'

    elif name == 'Invulnerability':
        text = '_'

    elif name == 'Jarring':
        text = '_'

    elif name == 'Jawbreaker':
        text = '_'

    elif name == 'Jousting':
        text = '_'

    elif name == 'Locksmith':
        text = '_'

    elif name == 'Malevolent':
        text = '_'

    elif name == 'Martyring':
        text = '_'

    elif name == 'Mastering':
        text = '_'

    elif name == 'Mental Focus':
        text = '_'

    elif name == 'Merging':
        text = '_'

    elif name == 'Mind Buttressing':
        text = '_'

    elif name == 'Mirrored':
        text = '_'

    elif name == 'Phantasmal':
        text = '_'

    elif name == 'Phase Lurching':
        text = '_'

    elif name == 'Poison-Resistant':
        text = '_'

    elif name == 'Poisoning':
        text = '_'

    elif name == 'Putrid':
        text = '_'

    elif name == 'Radiant':
        text = '_'

    elif name == 'Radiant Flight':
        text = '_'

    elif name == 'Rallying':
        text = '_'

    elif name == 'Ramming':
        text = '_'

    elif name == 'Rampaging':
        text = '_'

    elif name == 'Rebounding':
        text = '_'

    elif name == 'Reflecting':
        text = '_'

    elif name == 'Restful':
        text = '_'

    elif name == 'Righteous':
        text = '_'

    elif name == 'Sensing':
        text = '_'

    elif name == 'Shadow':
        text = '_'

    elif name == 'Shadow Blending':
        text = '_'

    elif name == 'Greater Shadow':
        text = '_'

    elif name == 'Improved Shadow':
        text = '_'

    elif name == 'Singing':
        text = '_'

    elif name == 'Slick':
        text = '_'

    elif name == 'Greater Slick':
        text = '_'

    elif name == 'Improved Slick':
        text = '_'

    elif name == 'Spell Dodging':
        text = '_'

    elif name == 'Spell Resistance':
        text = '_'

    elif name == 'Spell Storing':
        text = '_'

    elif name == 'Spellrending':
        text = '_'

    elif name == 'Spellsink':
        text = '_'

    elif name == 'Spirit-Bonded':
        text = '_'

    elif name == 'Spiteful':
        text = '_'

    elif name == 'Stanching':
        text = '_'

    elif name == 'Terrain-Striding':
        text = '_'

    elif name == 'Titanic':
        text = '_'

    elif name == 'Trackless':
        text = '_'

    elif name == 'Unbound':
        text = '_'

    elif name == 'Unbowed':
        text = '_'

    elif name == 'Undead Controlling':
        text = '_'

    elif name == 'Unrighteous':
        text = '_'

    elif name == 'Venom-Eating':
        text = '_'

    elif name == 'Vigilant':
        text = '_'

    elif name == 'Volcanic':
        text = '_'

    elif name == 'Vouchsafing':
        text = '_'

    elif name == 'Warding':
        text = '_'

    elif name == 'Weeping':
        text = '_'

    elif name == 'Wild':
        text = '_'

    elif name == 'Withstanding':
        text = '_'

    elif name == 'Wyrmsbreath':
        text = '_'

    if Armor is not None:
        Armor.Text = '<p>' + text + '</p>'
    else:
        return text
