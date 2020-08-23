from numpy.random import random, randint, choice
from resources import masterwork_traits


def special_masterwork(Weapon, Trait=None):
    if Trait is not None and Trait in masterwork_traits:
        Weapon.Special = Trait
    else:
        selection = int((random() * 1000))
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
    if Weapon.Special == 'Adaptive':
        Weapon.Text = '<p>This weapon has a very high tensile strength, requiring a STR of ' + str(
            randint(10, 31)
        ) + ' to be able to wield it correct. When wielding this Weapon, you use your Strength modifier instead of Dexterity when calculating to Hit or Dexterity.</p>'

    elif Weapon.Special == 'Advancing':
        Weapon.Text = '<p>This weapon is designed for a frontline fighter. As a free action, you can move an additional 10 ft. of movement, but have a -2 to hit on the turn you take that movement in.</p>'

    elif Weapon.Special == 'Agile':
        Weapon.Text = '<p>This weapon grants the finesse property. You may use your Dexterity instead of your Strength for attack and damage with this weapon.</p>'

    elif Weapon.Special == 'Allying':
        Weapon.Text = '<p>This weapon grants a flanking bonus, to you and an ally. You may take this flanking bonus as long as there is an enemy within 5ft of the same creature you\'re attacking.</p>'

    elif Weapon.Special == 'Ambushing':
        Weapon.Text = '<p>This weapon is designed for Surprise encounters. If you act during a Surprise round, you may apply an additional 1d6 points of Sneak Attack Damage on a successful hit.</p>'

    elif Weapon.Special == 'Anarchic':
        Weapon.Text = '<p>This weapon was created in The Abyss. This weapon cannot be wielded by a Lawful creature. Any Lawful creatures attempting to do so, take 2d6 damage every round. Any Chaotic or Neutral creatures wielding this weapon deal an additional 2d6 damage against Lawful creatures.</p>'

    elif Weapon.Special == 'Anchoring':
        Weapon.Text = '<p>This weapon is designed to fasten a creature in place. If you make a successful attack against the creature with this weapon, they enemy is rendered restrained, and must spend a standard action to remove this condition.</p>'

    elif Weapon.Special == 'Answering':
        Weapon.Text = '<p>This weapon is designed to riposte. Creatures who miss an attack against you, you can use your reaction to make an attack of opportunity against the creature.</p>'

    elif Weapon.Special == 'Axiomatic':
        Weapon.Text = '<p>This weapon was created in Mechanus. This weapon cannot be wielded by a Chaotic creature. Any Chaotic creatures attempting to do so, take 2d6 damage every round. Any Lawful or Neutral creatures wielding this weapon deal an additional 2d6 damage against Chaotic creatures.</p>'

    elif Weapon.Special == 'Bane':
        creatures = choice([
            'aberrations', 'beasts', 'celestials', 'constructs', 'dragons',
            'elementals', 'fey', 'fiends', 'giants', 'monstrosities', 'oozes',
            'plants', 'undead'
        ])
        Weapon.Text = '<p>This weapon is designed to be destructive to a certain type of foe. Deal an additional 2d6 points of damage against creatures of the ' + creatures + ' type.</p>'

    elif Weapon.Special == 'Beaming':
        Weapon.Text = '<p>This weapon has light infused inside of the weapon. You speak the command word of the weapon, and your weapon acts as if the light spell was cast on it.</p>'

    elif Weapon.Special == 'Benevolent':
        Weapon.Text = '<p>This weapon allows you to aid another during their attack. If you and an ally are within 30 ft of each other, you may expend your standard action, to allow your ally to take an attack action instead of you.</p>'

    elif Weapon.Special == 'Bewildering':
        Weapon.Text = '<p>This weapon allows the wielder to cast the Confusion spell as part of an attack. If the attack successfully hits, the target must succeed a Wisdom saving throw of DC 8 + Proficiency + Strength (or Dexterity).</p>'

    elif Weapon.Special == 'Blood-Hunting':
        creatures = choice([
            'aberrations', 'beasts', 'celestials', 'dragons', 'fey', 'fiends',
            'giants', 'monstrosities'
        ])
        Weapon.Text = '<p>This weapon is designed to seek the blood of a certain type of foe. Deal an additional 1d6 points of damage against creatures of the ' + creatures + ' type.</p>'

    elif Weapon.Special == 'Bloodsong':
        Weapon.Text = "<p>This weapon is designed for Barbarians. While a barbarian is raging and using this weapon, it's critical range increases by 1. (i.e. Critical at 20 becomes 19-20). If the wielder makes a critical hit, they gain half the HP dealt as damage as Temporary HP to themselves.</p>"

    elif Weapon.Special == 'Brawling':
        Weapon.Text = '<p>This weapon is designed for up close and personal combat. You gain proficiency with Athletics and Acrobatics. If you are proficient already, you gain expertise. You also have advantage on attacks made to grapple a target with this weapon.</p>'

    elif Weapon.Special == 'Breaking':
        Weapon.Text = '<p>The weapon is designed as a seige weapon. You deals an additional 2d6 damage against Constructs, Structures, or Objects.</p>'

    elif Weapon.Special == 'Brilliant Energy':
        damage = choice(
            ['Acid', 'Cold', 'Fire', 'Force', 'Lightning', 'Poison', 'Thunder'])
        Weapon.Text = "<p>This weapon was designed to deal " + damage + " damage instead of it's normal damage.</p>"

    elif Weapon.Special == 'Called':
        Weapon.Text = "<p>This weapon can be teleported back to the wielder's hands. This does not provoke attacks of opportunity. The range of this ability is 100 ft. Any attempt to call the weapon back outside of this range fails.</p>"

    elif Weapon.Special == 'Compassionate':
        Weapon.Text = '<p>This weapon can deal non-lethal damage, rendering a target who drops to 0 HP stable by this weapon. You must express that you are not doing non-lethal damage before an attack attempt.</p>'

    elif Weapon.Special == 'Concealed':
        Weapon.Text = '<p>This weapon has the ability to transform into a mundane item, of the same size/dimension. While in this transformed state, creatures wishing to understand the true nature, must succeed a DC20 Investigation check. This weapon can remain in its transformed state for 8 hours per day. Transforming this item takes a standard action.</p>'

    elif Weapon.Special == 'Lesser Concealed':
        Weapon.Text = '<p>This weapon has the ability to transform into a mundane item, of the same size/dimension. While in this transformed state, creatures wishing to understand the true nature, must succeed a DC16 Investigation check. This weapon can remain in its transformed state for 4 hours per day. Transforming this item takes a standard action.</p>'

    elif Weapon.Special == 'Conductive':
        Weapon.Text = '<p>This weapon has channels meant for magics. If a creature who can cast spells, uses this weapon, they can channel a spell through this weapon as part of a melee attack. The spell can be any spell that takes a bonus action, or a reaction to cast.</p>'

    elif Weapon.Special == 'Conserving':
        Weapon.Text = "<p>This weapon is designed to conserve ammunition. If an attack misses with a ranged attack, the first ammunition returns to it's quiver, case or container.</p>"

    elif Weapon.Special == 'Corrosive':
        Weapon.Text = '<p>This weapon is coated in a thick layer of acid. Attacks made with this weapon deal an additional 1d6 Acid Damage.</p>'

    elif Weapon.Special == 'Corrosive Burst':
        Weapon.Text = "<p>This weapon is coated in a thick layer of acid. Attacks made with this weapon deal an additional 1d6 Acid Damage. If the wielder makes a critical hit against a creature, the damage becomes 1d10, instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for every number above 2. x3 = 2d10; x7 = 6d10</p>"

    elif Weapon.Special == 'Countering':
        Weapon.Text = '<p>This weapon is designed to deter enemies who try and disarm you. As a reaction, if a creature attempts the Disarm action against you, you may make an attack of opportunity against the creature.</p>'

    elif Weapon.Special == 'Courageous':
        Weapon.Text = "<p>This weapon bolster's the wielder's courage. The wielder has advantage on saving throws against being frightened.</p>"

    elif Weapon.Special == 'Cruel':
        Weapon.Text = '<p>This weapon is a twisted tool of death. If a creature is hit with this weapon, the creature must make a Wisdom Saving throw (DC 8 + Proficiency + Strength modifier) or be frightened. Once the creature saves against this effect, they are immune to the effects for 24 hours.</p>'

    elif Weapon.Special == 'Culling':
        Weapon.Text = '<p>This weapon allows the user to cleave through a target. When making an attack, if you succeed on hitting a creature, you may attack a creature adjacent to the first creature, and within your range. You make the second attack at disadvantage.</p>'

    elif Weapon.Special == 'Cyclonic':
        Weapon.Text = "<p>This weapon tends to move the air around your projcetiles. The wielder's projectiles are not hindered by Liquid or Gaseous environmental effects, such as Wind Wall.</p>"

    elif Weapon.Special == 'Dazzling':
        Weapon.Text = '<p>This weapon emits an explosive flash that dazzles all foes within a 15 ft cone in the direction of the projectile. Creatures must succeed a Constitution Saving Throw (DC17) or be blinded for 1d4 rounds.</p>'

    elif Weapon.Special == 'Dazzling Radiance':
        Weapon.Text = '<p>This weapon emits an explosive flash that dazzles all foes within a 15 ft of the wielder. Creatures must succeed a Constitution Saving Throw (DC17) or be blinded for 1d4 rounds.</p>'

    elif Weapon.Special == 'Deadly':
        Weapon.Text = '<p>This weapon instantly kills unsuspecting victims. If an enemy is unaware of the wielder, and the wielder makes a successful attack against the enemy, roll damage normally. The enemy must make a Constitution saving throw (DC is the damage dealt by this weapon). On a failed save, the enemy falls Unconscious.</p>'

    elif Weapon.Special == 'Debilitating':
        Weapon.Text = '<p>This weapon has wicked ridges, that tear flesh. If a creature is hit with this weapon during a surprise round, the weapon removes their Dexterity modifier from their AC. This effect does not work against creatures who have natural armor.</p>'

    elif Weapon.Special == 'Defending':
        Weapon.Text = '<p>This weapon is meant to fend off attacks, more than being able to do damage. While wielding this weapon, you may add +' + str(
            Weapon.Masterwork) + ' to your AC.</p>'

    elif Weapon.Special == 'Defiant':
        Weapon.Text = '<p>This weapon is designed to keep its wielder alive in perilous situations. Once per day, if the wielder of this weapon falls to 0 HP, they can choose to fall to 1 HP instead. This effect can only done once per long rest</p>'

    elif Weapon.Special == 'Greater Designating':
        Weapon.Text = "<p>This weapon grants the wielder the ability to strike targets successively. Once you've made a successful ranged attack against a creature, you can choose this creature as your Target. If you choose to make another ranged attack against your Target, you have advantage against hitting the Target. You can do this a number of times per day equal to your Wisdom Modifier (min. 1).</p>"

    elif Weapon.Special == 'Lesser Designating':
        Weapon.Text = "<p>This weapon grants the wielder the ability to strike targets successively. Once you've made a successful ranged attack against a creature, you can choose this creature as your Target. If you choose to make another ranged attack against your Target, you can add your proficiency bonus twice against hitting the Target. You can do this a number of times per day equal to half of your Wisdom Modifier, rounded down (min. 1).</p>"

    elif Weapon.Special == 'Dispelling':
        Weapon.Text = '<p>This weapon has Dispel Magic stored inside of the weapon. Once per day, you can cast Dispel Magic at 3rd level using this weapon as your focus.</p>'

    elif Weapon.Special == 'Dispelling Burst':
        Weapon.Text = '<p>This weapon has Dispel Magic stored inside of the weapon. Once per day, you can cast Dispel Magic at 3rd level using this weapon as your focus. When you choose to do so, all spell effects within 15 ft. of you also are effected by the spell.</p>'

    elif Weapon.Special == 'Disruption':
        Weapon.Text = '<p>This weapon is designed to destroy Undead. All undead must make a Wisdom Saving throw (DC 8 + Proficiency + Wisdom modifier). On a fail, the Undead is frightened. The Undead whose CR is less than or equal to your highest Level divided by four (rounded down), are destroyed instead of frightened.</p>'

    elif Weapon.Special == 'Distance':
        Weapon.Text = '<p>This weapon is meant for range. Your range incriments are doubled.</p>'

    elif Weapon.Special == 'Distracting':
        Weapon.Text = '<p>This weapon is meant to deter Spellcasters from using their spells. If you make a successful attack against a creature who is concentrating, the DC of their Concetration check goes up by 5.</p>'

    elif Weapon.Special == 'Greater Distracting':
        Weapon.Text = '<p>This weapon is meant to deter Spellcasters from using their spells. If you make a successful attack against a creature who is concentrating, the DC of their Concetration check goes up by 10.</p>'

    elif Weapon.Special == 'Driving':
        Weapon.Text = '<p>This weapon is designed to knock enemies away from you. If you make a successful attack against a creature, they must make a Strength Saving throw (DC 8 + Proficiency + Dexterity modifier). If they fail, they are knocked 5 ft away from the wielder. If the creature fails by more than 10, they are knocked prone.</p>'

    elif Weapon.Special == 'Dry Load':
        Weapon.Text = '<p>The weapon is build for surviving underwater use. This weapon is not rendered broken underwater. It also allows the wieder to reload and fire the weapon underwater, and is only limited by the regular rules of underwater combat.</p>'

    elif Weapon.Special == 'Dueling':
        Weapon.Text = '<p>This weapon grants the user speed in combat, and deftness in reaction. Add +' + str(
            Weapon.Masterwork
        ) + ' to your Initiative while wielding this weapon. You also have advantage on saves against being disarmed.</p>'

    elif Weapon.Special == 'Endless Ammunition':
        Weapon.Text = '<p>This weapon is designed for users spares of ammunition. Every time you draw an arrow/bolt from a quiver/container, the same type of arrow/bolt is replicated back into your quiver. The ammunition, once it hits a target or misses, vanishes from existence.</p>'

    elif Weapon.Special == 'Exhausting':
        Weapon.Text = '<p>This weapon saps the energy from a target. When this weapon strikes a critical hit, the wielder can choose to forgo the regular effects of a critical, and inflict 1 level of exhaustion on the target.</p>'

    elif Weapon.Special == 'Fervent':
        Weapon.Text = '<p>This weapon grants the wielder the ability to channel divinity through their weapon. If you worship a diety, you gain a proficiency with Religion and Insight checks. If you already have proficiency, you gain expertise with Religion and Insight.</p>'

    elif Weapon.Special == 'Flaming':
        Weapon.Text = '<p>This weapon is covered in fire. Attacks made with this weapon deal an additional 1d6 of fire damage.</p>'

    elif Weapon.Special == 'Flaming Burst':
        Weapon.Text = "<p>This weapon is covered in fire. Attacks made with this weapon deal an additional 1d6 of fire damage. If the wielder makes a critical hit against a creature, the damage becomes 1d10, instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for every number above 2. x3 = 2d10; x7 = 6d10.</p>"

    elif Weapon.Special == 'Flying':
        Weapon.Text = '<p>This weapon grants the user the ability to fly. While wielding this weapon, the user gains an innate fly speed equal to half their movement speed.</p>'

    elif Weapon.Special == 'Fortuitous':
        Weapon.Text = '<p>This grants the wielder lightning fast reactions. The wielder of this weapon can make as many attacks of opportunity as the like.</p>'

    elif Weapon.Special == 'Frost':
        Weapon.Text = '<p>This weapon is covered in ice. Attacks made with this weapon deal an additional 1d6 of cold damage.</p>'

    elif Weapon.Special == 'Furious':
        Weapon.Text = '<p>This weapon contains the spirit of a barbarian. The wielder is granted a Level 1 Barbarian\'s Rage ability. You may enter a Rage once per Long Rest.</p>'

    elif Weapon.Special == 'Furyborn':
        Weapon.Text = '<p>This weapon slowly becomes more dangerous against an enemy, the more it gets attacked with it. With every successful attack against a creature, the wielder gains a +1 to damage, which stacks. This bonus is lost on a missed attack.</p>'

    elif Weapon.Special == 'Ghost Touch':
        Weapon.Text = '<p>This weapon seems to be guided towards ghost like creatures. You deal an additional 1d6 Force Damage against Undead</p>'

    elif Weapon.Special == 'Glitterwake':
        Weapon.Text = '<p>This weapon helps see invisible creatures. The wielder may target a square, as part of an attack. All invisible creatures within 15 ft. of that square must make a Dexterity Saving throw (DC 8 + Proficiency + Dexterity modifier). On a fail, the creature is coated in a glittering dust, and rendered visible. The wielder can use this ability a number of times equal to their Wisdom modifier (min 1).</p>'

    elif Weapon.Special == 'Glorious':
        Weapon.Text = "<p>This weapon grants the wielder the ability to charm creatures. All enemies within 30 ft of the wielder must make a Charisma saving throw (DC 8 + Proficiency + Charisma modifier), or be charmed for 1 minute. If the creature is damaged during that minute, the charmed effect is broken. This can be done a number of times equal to the wielders Charisma modifer (min. 1). Creatures who have been affected by this ability in the past 24 hours, or whose CR is greater than the wielder's level are uneffected.</p>"

    elif Weapon.Special == 'Gory':
        Weapon.Text = "<p>This weapon is meant to bleed an enemy of all it's life. On a successful hit, the creature takes " + str(
            Weapon.Masterwork
        ) + " Bleed damage that stacks. This Bleed occurs on the enemy's turn, and can be cured by any healing effect, or a successful DC15 Medicine Check.</p>"

    elif Weapon.Special == 'Grayflame':
        Weapon.Text = '<p>This weapon is designed for Paladins and Clerics. Whenever the wielder uses a their channel divinity or applies a Smite to an attack, the weapon deals an additional 1d6 Radiant damage for the next minute. This ability does not stack with itself.</p>'

    elif Weapon.Special == 'Grounding':
        Weapon.Text = '<p>This weapon is meant to bring down flying creatures. If a creature is flying when struck by this weapon, they tak an additional 1d6 damage and have disadvantage on maintaining flight.</p>'

    elif Weapon.Special == 'Growing':
        Weapon.Text = '<p>This weapon enhances its wielder to grow in size. Once per long rest, the wielder may cast Enlarge on themselves for the full duration. You may also speak the command word and cause the weapon to grow a size category. If you are able to wield a weapon of a size category larger than yourself, you may use this weapon still. When the command word is spoken again, the weapon returns to normal size.</p>'

    elif Weapon.Special == 'Guardian':
        Weapon.Text = '<p>This weapon allows the user to protect themselves against magical effects. The wielder is granted a +' + str(
            Weapon.Masterwork
        ) + ' to all their saves while this weapon is equipped.</p>'

    elif Weapon.Special == 'Heart-Piercing':
        Weapon.Text = "<p>This weapon pierces the target's heart. This weapon cannot benefit from abilites that increase it's critical range. On a Critical hit, make another attack roll. If the second attack roll surpasses the AC of the target, the target is dead. On a fail, treat the critical normally.</p>"
        for c in range(8):
            if 'x' + str(c) in Weapon.Crit:
                Weapon.Crit = 'x' + str(c)

    elif Weapon.Special == 'Heartseeker':
        Weapon.Text = "<p>This weapon ignores the effects of cover or concealment. If a target is behind three quarters or half cover, this weapon ignores any benefit to their AC. You also ignore obscuring effects  such as Fog Cloud.</p>"

    elif Weapon.Special == 'Heretical':
        Weapon.Text = "<p>This weapon grants the wielder destructive power against a God. If you worship a God, you cannot choose your God. Choose a God to be against. If an enemy is a follower of that God, you deal an additional 1d6 points of damage against the target.</p>"

    elif Weapon.Special == 'Holy':
        Weapon.Text = '<p>This weapon was created in Mount Celestia. This weapon cannot be wielded by a Evil creature. Any Evil creatures attempting to do so, take 2d6 damage every round. Any Good or Neutral creatures wielding this weapon deal an additional 2d6 damage against Evil creatures.</p>'

    elif Weapon.Special == 'Huntsman':
        Weapon.Text = '<p>This weapon is meant for hunters. If the wielder has made a Survival check to track a creature within the past 24 hours, the wielder deal an additional 1d6 points of damage to the tracked target. This weapon also grants proficiency with Survival. If you are proficient with Survival, you gain expertise with Survival.</p>'

    elif Weapon.Special == 'Icy Burst':
        Weapon.Text = "<p>This weapon is covered in ice. Attacks made with this weapon deal an additional 1d6 of cold damage. If the wielder makes a critical hit against a creature, the damage becomes 1d10, instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for every number above 2. x3 = 2d10; x7 = 6d10.</p>"

    elif Weapon.Special == 'Igniting':
        Weapon.Text = '<p>This weapon is covered in fire. Attacks made with this weapon ignite the enemy on fire. An enemy on fire takes 1d6 fire damage on their turn for 1 minute, or until put out using a standard action. You can also be put out by water, or a watery environment.</p>'

    elif Weapon.Special == 'Impact':
        Weapon.Text = '<p>This weapon deals bludgeoning damage. Attacks made with this weapon deal an additional 1d6 of bludgeoning damage.</p>'

    elif Weapon.Special == 'Impervious':
        Weapon.Text = "<p>This weapon has a magical resilience against effect that would damge this weapon. This weapon cannot be rusted (if metallic), or warped (if wooden). It also can only be broken by another Impervious weapon.</p>"

    elif Weapon.Special == 'Injecting':
        Weapon.Text = '<p>This weapon has a hollow point meant to store deadly Poisons. If this is a Melee weapon, you can store up to ' + str(
            Weapon.Masterwork
        ) + ' charges of poison that are applied on a successful melee attack. If this is a Ranged weapon, each projectile can have a dose of poison applied to it.</p>'

    elif Weapon.Special == 'Interfering':
        Weapon.Text = '<p>This weapon is designed to interfere with Battlefield movement. You may make attacks of opportunity within 30 ft. or your closest range incriment (whichever is closer).</p>'

    elif Weapon.Special == 'Invigorating':
        Weapon.Text = '<p>This weapon brings a bloodlust to its wielder. If the wielder drops an enemy to 0 HP, the wielder is cured of 1 level of exhaustion. If the wielder is not exhausted, the wielder gaina +10 to their movement speed, and have advantage on all creatures for 1 minute.</p>'

    elif Weapon.Special == 'Keen':
        if len(Weapon.Crit) == 2:
            Weapon.Crit = '19-20 ' + Weapon.Crit
        else:
            rang = abs(eval(Weapon.Crit[:-2])) + 1
            rang *= 2
            rang -= 1
            Weapon.Crit = str(20 - rang) + '-20 ' + Weapon.Crit[-2:]
        Weapon.Text = "<p>This weapon's critical range is doubled. This weapon's crit power is now " + Weapon.Crit + '.</p>'

    elif Weapon.Special == 'Ki Focus':
        Weapon.Text = "<p>This weapon is designed for Monks. A Monk is proficient with this weapon, and can channel their Ki through this weapon, using this weapon's damage instead of their unarmed strike.</p>"

    elif Weapon.Special == 'Ki Intensifying':
        Weapon.Text = "<p>This weapon is designed for Monks. A Monk is proficient with this weapon, and can channel their Ki through this weapon, using this weapon's damage instead of their unarmed strike. When using an ability that costs 1 Ki point, roll 1d6. On a 5 or a 6, you regain the Ki point.</p>"

    elif Weapon.Special == 'Kinslayer':
        Weapon.Text = "<p>This weapon is designed to kill history. Attacks made with this weapon deal an additional 2d6 damage against creatures of the same family line.</p>"

    elif Weapon.Special == 'Legbreaker':
        Weapon.Text = '<p>This weapon slows the advances of creatures. Attacks made with this weapon reduce a creatures movements speed by 10 for 1d4 rounds. Multiple attacks made do not decrease the speed further than 10, but do increase the duration of the slow. On a Critical hit, the creatures movement is reduced to 0 for the duration. A DC15 Medicine check or healing effect removes this penalty.</p>'

    elif Weapon.Special == 'Liberating':
        Weapon.Text = '<p>This weapon helps a creature unable to move. If the wielder is affected by something that would impede their movement, they have advantage on the save or check.</p>'

    elif Weapon.Special == 'Lifesurge':
        Weapon.Text = '<p>This weapon grants resistance to Necrotic Damage. Attacks made with this weapon deal an additional 1d6 points of damage to Undead.</p>'

    elif Weapon.Special == 'Limning':
        Weapon.Text = "<p>This weapon was built to kill Fae. On a successful attack, the wielder can choose to cast Faerie Fire on the enemy as a free action. the Faerie Fire lasts for the full duration, but uses the wielder's concentration. The wielder can do the a number of times equal to their Wisdom modifier.</p>"

    elif Weapon.Special == 'Lucky':
        Weapon.Text = '<p>This weapon has a lucky charm attached to it. The wielder has 1 Luck point, that they can use to gain advantage on Saving Throws, Attack Rolls, and Ability Checks. The wielders Lucky points refresh at the end of a Long Rest.</p>'

    elif Weapon.Special == 'Greater Lucky':
        Weapon.Text = '<p>This weapon has a greater lucky charm attached to it. The wielder has 3 Luck point, that they can use to gain advantage on Saving Throws, Attack Rolls, and Ability Checks. The wielders Lucky points refresh at the end of a Long Rest.</p>'

    elif Weapon.Special == 'Menacing':
        Weapon.Text = '<p>This weapon grants the wielder advantage on Intimidation checks made while wielding this weapon.</p>'

    elif Weapon.Special == 'Merciful':
        Weapon.Text = '<p>This weapon deals non-lethal damage. Attacks made with this weapon deal an additional 1d6 points of non-lethal damage. You can choose to deal lethal damage, but you must express that you want to deal lethal damage before an attack attempt.</p>'

    elif Weapon.Special == 'Mighty Cleaving':
        Weapon.Text = '<p>This weapon allows the user to cleave through a target. When making an attack, if you succeed on hitting a creature, you may attack a creature adjacent to the first creature, and within your range. You make the second attack normally.</p>'

    elif Weapon.Special == 'Mimetic':
        Weapon.Text = '<p>This weapon mimics resistance towards damage. When taking damage from one of the following damage types (Acid, Bludgeoning, Cold, Fire, Lightning, Necrotic, Piercing, Poison, Radiant, Slashing, or Thunder), you can choose to gain resistance for 1 minute against that damage type. Once this resistance is active, you cannot change it until the effects wear off.</p>'

    elif Weapon.Special == 'Miserable':
        creatures = choice([
            'aberrations', 'beasts', 'celestials', 'constructs', 'dragons',
            'elementals', 'fey', 'fiends', 'giants', 'monstrosities', 'oozes',
            'plants', 'undead'
        ])
        Weapon.Text = "<p>This weapon is designed to be destructive to a certain type of foe. Deal an additional 2d6 points of damage against creatures of the " + creatures + " type. This weapon cuts through resistances that would otherwise reduce the amount of damage taken. If the enemy has immunities to this type of damage, they instead have resistance. If the enemy has resistances to this type of damage, they take normal damage.</p>"

    elif Weapon.Special == 'Negating':
        Weapon.Text = "<p>This weapon cuts through resistances that would otherwise reduce the amount of damage taken. If the enemy has immunities to this type of damage, they instead have resistance against this weapon. If the enemy has resistances to this type of damage, they take normal damage from this weapon.</p>"

    elif Weapon.Special == 'Neutralizing':
        Weapon.Text = '<p>This weapon renders poisons and other toxins innert. This weapon cannot be corroded by Acid. This weapon also neutralized poisons inside its wielder. The wielder also cannot be poisoned</p>'

    elif Weapon.Special == 'Nimble Shot':
        Weapon.Text = '<p>This weapon allows the user to make attacks without provoking attacks of opportunity.</p>'

    elif Weapon.Special == 'Ominous':
        Weapon.Text = '<p>This weapon trails a shadowy haze behind it. All creatures hit by this weapon must make a Wisdom Saving throw (DC 10 + Proficiency + Charisma modifier). On a failed save, the creature is frightened for 1 minute, and cannot redo its save for the duration. Creatures affected by this ability who pass, are immune to its effects for 24 hours.</p>'

    elif Weapon.Special == 'Patriotic':
        Weapon.Text = "<p>This weapon bleeds for its country. Gain a +" + str(
            Weapon.Masterwork
        ) + " to History, Insight, Nature, and Survival within the land of the weapon's creation. Attacks made with this weapon deal an additional " + str(
            Weapon.Masterwork
        ) + " point of damage against enemies of a different nationality.</p>"

    elif Weapon.Special == 'Peaceful':
        Weapon.Text = "<p>This weapon doesn't want to fight. Gain a +" + str(
            Weapon.Masterwork
        ) + " to Persuasion, Insight, and Deception against creatures who you share a common language.</p>"

    elif Weapon.Special == 'Penetrating':
        Weapon.Text = "<p>This weapon fires through enemies. If you make a successful attack against a creature, your ammunition pierces through behinds them. If that second enemy is still within the range of your weapon, and you can draw a straight line between all three enemies, you may make a second attack against the second enemy at disadvantage.</p>"

    elif Weapon.Special == 'Phantom Ammunition':
        Weapon.Text = '<p>This weapon leaves behind no trace of its existence. Any attacks made with these weapons, do normal damage, but the wounds close and the ammunition disintegrates.</p>'

    elif Weapon.Special == 'Phase Locking':
        Weapon.Text = '<p>This weapon tethers its enemies to this plane of existence. If you make a successful attack against a creature, they cannot teleport away by magical means for 1d4 rounds.</p>'

    elif Weapon.Special == 'Planestriking':
        Weapon.Text = '<p>This weapon is designed to be destructive to a certain type of foe. Deal an additional 1d6 points of damage against creatures who are not native to the plane this weapon was created on.</p>'

    elif Weapon.Special == 'Plummeting':
        Weapon.Text = '<p>This weapon is meant to bring down flying creatures. If a creature is flying when struck by this weapon have disadvantage on maintaining flight.</p>'

    elif Weapon.Special == 'Quaking':
        Weapon.Text = '<p>This weapon shakes the earth itself. May make an attack on the ground, and all foes within a 5 ft. Radius, 10 ft. Cone, or 20 ft. Line make a Dexterity saving throw (DC 8 + Proficiency + Strength modifer). If a creatures fails, they are knocked prone. The wielder has advantage on effects that would render them prone.</p>'

    elif Weapon.Special == 'Quenching':
        Weapon.Text = '<p>This weapon is always damp. The wielder can place this weapon into a non magical fire, and extinguish it. This weapon treats any successful attack against Fire Elementals as Criticals.</p>'

    elif Weapon.Special == 'Redeemed':
        Weapon.Text = '<p>This weapon was created in Evil, but has since been cleansed of it. This weapon cannot be wielded by a Evil creature. Any Evil creatures attempting to do so, take 2d6 damage every round. Any Good or Neutral creatures wielding this weapon deal an additional 2d6 damage against Evil creatures.</p>'

    elif Weapon.Special == 'Reliable':
        Weapon.Text = "<p>This weapon is designed to not jam or misfire. This weapon's misfire chance is reduced by up to 1. This has not been applied to the weapon's current stat block.</p>"

    elif Weapon.Special == 'Greater Reliable':
        Weapon.Text = "<p>This weapon is designed to not jam or misfire. This weapon's misfire chance is reduced by up to 4. This has not been applied to the weapon's current stat block.</p>"

    elif Weapon.Special == 'Repositioning':
        Weapon.Text = "<p>This weapon is designed to move freely through the Battlefield. You may move 5 ft. without incurring an attack of opportunity from an enemy. You also may take the Disengage action as a bonus action.</p>"

    elif Weapon.Special == 'Returning':
        Weapon.Text = '<p>This weapon flys on its own. On a miss, you make an additional attack without any bonuses against the target, as the weapon attempts to return to you. On a miss, the projectile is returns to you. On a hit, the creature only takes the weapon damage, with no modifiers (as if an off-hand weapon)</p>'

    elif Weapon.Special == 'Rusting':
        Weapon.Text = "<p>This weapon constantly sheds flecks of rust. On a critical hit, you can forgo the additional damage to corrode the enemy's weapon you're attacking. This effect is handled similair to how a Rust Monster's 'Rust Metal' ability works.</p>"

    elif Weapon.Special == 'Sacred':
        Weapon.Text = '<p>This weapon acts as a Holy symbol to your diety. Paladins and Clerics may treat this as their Spellcasting Focus. You gain a proficiency with Religion. If you are already proficient, you gain expertise in Religion.</p>'

    elif Weapon.Special == 'Sapping':
        Weapon.Text = '<p>This weapon drains the strength of its enemies. Attacks made with this weapon deal 2d6 points of non-lethal damage. On a critical, the enemy drops Unconscious for 2d4 rounds.</p>'

    elif Weapon.Special == 'Seaborne':
        Weapon.Text = '<p>This weapon is at home on the ocean. The wielder of this weapon gains a natural swim speed equal to half their movement speed rounded up. They also may dash as a bonus action underwater.</p>'

    elif Weapon.Special == 'Second Chance':
        Weapon.Text = '<p>This weapon seeks its enemies for you. Once on each of your turns when you miss with a weapon attack, you can make another weapon attack as part of the same action.</p>'

    elif Weapon.Special == 'Seeking':
        Weapon.Text = '<p>This weapon seeks its enemies for you. The weapon does not have disadvantage when firing at an invisible creature, into a heavily obscured area, or if environmental effects would otherwise grant disadvantage. This weapon also treats cover as if it is one level less. Full Cover => Three Quarters Cover => Half Cover => No Cover.</p>'

    elif Weapon.Special == 'Shadowshooting':
        Weapon.Text = '<p>This weapon is a rogues best friend. Any attacks made in Darkness, Shade, or Dim Light qualify for use of Sneak Attack.</p>'

    elif Weapon.Special == 'Sharding':
        Weapon.Text = '<p>This weapon has a brittle quailty. On a critical hit, the weapon leaves some of itself inside the enemy. The creature takes minimum damage each round until they spend an action removing the shards, succeed on a DC 20 Medicine check, or are healed.</p>'

    elif Weapon.Special == 'Shattering':
        Weapon.Text = "<p>'This weapon was designed to be destroyed. On a critical hit, deal an additional 1d10 Force Damage per crit multiplier level. (x2 = 1d10 | x5 = 4d10). This damage is NOT included in the weapon's critical.</p>"

    elif Weapon.Special == 'Shock':
        Weapon.Text = '<p>This weapon crackles with electricity. Attacks made with thise weapon deal 1d6 points of Lightning damage.</p>'

    elif Weapon.Special == 'Shocking Burst':
        Weapon.Text = "<p>This weapon crackles with electricity. Attacks made with thise weapon deal 1d6 points of Lightning damage. If the wielder makes a critical hit against a creature, the damage becomes 1d10, instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for every number above 2. x3 = 2d10; x7 = 6d10</p>"

    elif Weapon.Special == 'Shrinking':
        Weapon.Text = '<p>This weapon shrinks itself, and its wielder. Once per long rest, you may cast Reduce on yourself for the full duration. You may also speak the command word, and reduce the weapon to the size of a dagger. The weapon gains the stats of a regualr Dagger of the same material. When the command word is spoken again, the weapon returns to its normal time.</p>'

    elif Weapon.Special == 'Silencing':
        Weapon.Text = '<p>This weapon is silence and deadly. On a successful attack, the enemy is treated as if inside of a Silence spell for 1 round. On a critical hit, the silence on the creature lasts for an additional 1d4+' + Weapon.Crit[-1] + ' rounds.</p>'

    elif Weapon.Special == 'Smashing':
        Weapon.Text = '<p>This weapon breaks things. Attacks made with this weapon deal an additional 2d6 points of damage.</p>'

    elif Weapon.Special == 'Sneaky':
        Weapon.Text = '<p>This weapon is designed those who want to be Rogues. Attacks deal an additional 1d6 points of Sneak attack damage as long as attack has advantage, or during a surprise round.</p>'

    elif Weapon.Special == 'Sonic Boom':
        Weapon.Text = '<p>This weapon has a loudener on it. Attacks made with this weapon deal an additional 1d6 points of Thunder damage to all enemies in a 15 ft. cone from the wielder.</p>'

    elif Weapon.Special == 'Speed':
        Weapon.Text = '<p>This weapon is swift. The user gains an additional attack when taking the Attack Action with this weapon.</p>'

    elif Weapon.Special == 'Spell Siphon':
        Weapon.Text = "<p>This weapon drains Spellcasters. On a successful attack against a Spellcaster, you automatically learn what spells the caster has active. On a critical hit against a Spellcaster, you can attempt to steal a spell slot from them. Enumerate the spell slots and roll approriately to steal. Example: the Enemy has 3 level one spell slots, and 2 level two spell slots. Since there are 5 potential slots to steal, you will roll 1d10. On a 1 or 2, you steal the first level one slot. On a 3 or 4, you steal the second level one slot, and so on. On a 7 or 8, steal the first level two spell slot. On a 9 or 10 steal the second level two spell slot. Leave this to the DM's discretion. The wielder then gains that spell slot, and can use it before they take a long rest.</p>"

    elif Weapon.Special == 'Spell Stealing':
        Weapon.Text = '<p>This weapon leeches knowledge from Spellcasters. On a successful hit, the wielder may learn a random spell, not a cantrip, from the enemy\'s spellbook, even if the spell is not available to the wielder normally. If the wielder is a Wizard or Artificer, they may choose to add it to their spell book before they take a long rest to learn the spell permenantly. If the wielder is any other Spellcaster, they may choose to swap out one of their known spells for the one they learned.</p>'

    elif Weapon.Special == 'Spell Storing':
        if Weapon.Masterwork == 1:
            slot = '1st'
        elif Weapon.Masterwork == 2:
            slot = '2nd'
        elif Weapon.Masterwork == 3:
            slot = "3rd"
        else:
            slot = str(Weapon.Masterwork) + 'th'
        Weapon.Text = "<p>This weapon holds a spell slot. This weapon holds a " + slot + " level spell slot. Whatever spell is stored in this weapon, is cast at " + slot + " level. To store a slot in this weapon, you cast the spell as if it was a ritual spell, regardless of if the spell has a ritual tag or not. Casting the spell from this weapon is no different from casting the spell normally, other than the spell slot used.</p>"

    elif Weapon.Special == 'Stalking':
        Weapon.Text = "<p>This weapon is meant attack known foes. Once per turn, you can spend your bonus action studying a foe's weaknesses. You deal an additional 1d6 points of damage against a foe who has been studied. You may only have one target studied at a time.</p>"

    elif Weapon.Special == 'Summon Bane':
        Weapon.Text = '<p>This weapon is meant to deal with summoned creatures. Attacks made with this weapon deal an additional 2d6 damage to summoned creatures or companion animals.</p>'

    elif Weapon.Special == 'Tailwind':
        Weapon.Text = '<p>This weapon gusts wind with each projectile. Every attack made with this weapon acts as if the Gust cantrip eminates from the projectile.</p>'

    elif Weapon.Special == 'Thawing':
        Weapon.Text = '<p>This weapon gives a warming heat. Attacks made with this weapon deal an additional 1d6 points of damage to enemy Elementals who are Icy. This weapon also melts any icy within a 5 ft. square that it touches.</p>'

    elif Weapon.Special == 'Throwing':
        Weapon.Text = "<p>This weapon is designed to be thrown. If this weapon increases it's throw distance by 10 ft. If the weapon doesn't have throw distance, it is now 10, and gains the Thrown property.</p>"

    elif Weapon.Special == 'Thundering':
        Weapon.Text = "<p>This weapon vibrates with a loud low frequency. Attacks made with thise weapon deal 1d6 points of Thunder damage. If the wielder makes a critical hit against a creature, the damage becomes 1d10, instead of 1d6. If this weapon's critical is greater than x2, it deals 1d10 extra damage for every number above 2. x3 = 2d10; x7 = 6d10</p>"

    elif Weapon.Special == 'Toxic':
        Weapon.Text = "<p>This weapon is designed to deliver poison. If a poison is applied to this weapon, the poison's DC is increased by 2. On a successful attack, roll 1d4. On a 4, the poisonous dose was not completely expended in the attack and the weapon is still poisoned.</p>"

    elif Weapon.Special == 'Training':
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
        Weapon.Text = '<p>This weapon contains a trained feature. This weapon contains the ' + feat + ' feat. You may consider this feat known, so long as you meet the prerequisites, and have the weapon in your possesion. </p>'

    elif Weapon.Special == 'Treasonous':
        Weapon.Text = "<p>This weapon bleeds against its own country. Gain a +" + str(
            Weapon.Masterwork
        ) + " to History, Insight, Nature, and Survival within the land of the weapon's creation. Attacks made with this weapon deal an additional " + str(
            Weapon.Masterwork
        ) + " point of damage against enemies of the same nationality.</p>"

    elif Weapon.Special == 'Truthful':
        Weapon.Text = '<p>This weapon pierces through illusionary magics. The wielder gains advantages on saves against illsions. Once per long rest, the wielder may cast See Invisibility on themselves for the full duration.</p>'

    elif Weapon.Special == 'Umbral':
        Weapon.Text = '<p>This weapon was crafted in the Underdark. The wielder gains darkvision within 60 ft. If the wielder already has darvision, the range increases by 30 ft. Once per long rest, the weilder may speak the command work of this weapon to cast Darkness centered around the Blade. The weilder is able to see through this darkness as long as he holds onto the weapon. If the weapon is sheathed, dropped, disarmed, or otherwise stowed, the darkness disapates.</p>'

    elif Weapon.Special == 'Underwater':
        Weapon.Text = "<p>This weapon is forged in the Elemental plane of Water. It seemlessly operates in the water, as well as it did in the water. The wielder of this weapon takes no penalties using this weapon underwater.</p>"

    elif Weapon.Special == 'Unholy':
        Weapon.Text = '<p>This weapon was created in the Deepest level of Hell. This weapon cannot be wielded by a Good creature. Any Good creatures attempting to do so, take 2d6 damage every round. Any Evil or Neutral creatures wielding this weapon deal an additional 2d6 damage against Good creatures.</p>'

    elif Weapon.Special == 'Unseen':
        Weapon.Text = '<p>This weapon is nigh invisible. The wielder may speak the command word, and the weapon becomes invisible. The wielder has advantages on all attacks against all creatures who rely on Natural vision for the next minute. Creatures who have Tremorsense or True Sight are unaffected. The wielder can use this ability a number of times equal to their Wisdom modifier.</p>'

    elif Weapon.Special == 'Valiant':
        Weapon.Text = '<p>This weapon bolsters those unafraid of danger. If a creature uses an ability, spell, or spell-like ability that would inflict the Frightened Condition, the wielder has advantage against such an ability. Attacks made with this weapon deal an additional 2d6 damage if the wielder succeeds on their save.</p>'

    elif Weapon.Special == 'Vampiric':
        Weapon.Text = '<p>This weapon drains lifeforce from the living. When the wielder of this weapon makes a successful attack against a creature, the user gains Temporary HP equal to half the damage dealt. If a Good or Lawful creature attempts to wield this weapon, the have disadvantage on all attack rolls.</p>'

    elif Weapon.Special == 'Greater Vampiric':
        Weapon.Text = '<p>This weapon drains lifeforce from the living. When the wielder of this weapon makes a successful attack against a creature, the user gains Temporary HP equal to the damage dealt. If a Good or Lawful creature attempts to wield this weapon, the have disadvantage on all attack rolls and is poisoned for 24 hours.</p>'

    elif Weapon.Special == 'Vicious':
        Weapon.Text = '<p>This weapon deals damage at a cost. Attacks made with this weapon deal an additional 2d6 damage against the target, and 1d6 damage to the wielder.</p>'

    elif Weapon.Special == 'Vorpal':
        Weapon.Text = "<p>This weapon decapitates the target. This weapon cannot benefit from abilites that increase it's critical range. On a Critical hit, make another attack roll. If the second attack roll surpasses the AC of the target, the target is dead. On a fail, treat the critical normally.</p>"
        for c in range(8):
            if 'x' + str(c) in Weapon.Crit:
                Weapon.Crit = 'x' + str(c)

    elif Weapon.Special == 'Wounding':
        Weapon.Text = "<p>This weapon is meant to bleed an enemy of all it's life. On a successful hit, the creature takes 1 Bleed damage that stacks. This Bleed occurs on the enemy's turn, and can be cured by any healing effect, or a successful DC15 Medicine Check.</p>"

    # Add the title of the masterwork quality to the weapon
    Weapon.Name = Weapon.Name[:2] + ' ' + Weapon.Special + Weapon.Name[2:]
    return Weapon


if __name__ == '__main__':
    from stores import Weapon
    # Find unused Traits
    for t in masterwork_traits:
    	w = Weapon(4)
    	w.add_masterwork(2)
    	w = special_masterwork(w, Trait=t)
    	if w.Text == '':
    		print(t)
    	# elif w.Text != '_':
    	# 	print('\t- ' + t + ':', w.Text)

    # Test Random Traits
    # for _ in range(1000):
    #     for j in range(5):
    #         for i in range(1, 10):
    #             w = Weapon(j)
    #             w.add_masterwork(i)
    #             print(special_masterwork(w))
    #             print(w.Text, '\n')
