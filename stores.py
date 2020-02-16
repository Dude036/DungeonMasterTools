from numpy.random import randint, choice, random_sample
from names import Antiques, Books, Enchanter, Potions, Tavern, Restaurant, Jeweller, Blacksmith, GeneralStore, Weapons,\
    Jewelling, Brothel, Gunsmithing
from variance import normalize_dict
from character import create_person
import simplejson as json
from resources import *

with open('spells.json', 'r') as inf:
    MasterSpells = json.load(inf, encoding='utf-8')
with open('wondrous.json', 'r') as inf:
    MasterWondrous = json.load(inf, encoding='utf-8')

MasterID = 1


def find_spell_level(spell):
    l = None
    a = [
        level_0, level_1, level_2, level_3, level_4, level_5, level_6, level_7,
        level_8, level_9
    ]
    for level in range(len(a)):
        if spell in a[level]:
            l = level
    return l


def find_spell_details(spell):
    while spell not in list(MasterSpells.keys()):
        spell = choice(list(MasterSpells.keys()))
    if MasterSpells[spell]['link'] in MasterSpellBlacklist:
        return None
    return MasterSpells[spell]['link'], MasterSpells[spell]['school'], MasterSpells[spell]['casting_time'], \
           MasterSpells[spell]['components'], MasterSpells[spell]['range'], MasterSpells[spell]['description'],


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
            s += str(int(c * 10)) + " sp "
        if int((c * 100) % 10) > 0:
            s += str(int((c * 100) % 10)) + " cp"
    if len(s) == 0:
        s = "0 cp"
    return s


def determine_rarity(q):
    if q[0] == q[1]:
        return q[0]
    l = []
    for x in range(q[0], q[1] + 1):
        l.append((x + 1) * x * x)
    l[0] += 1
    l = l[::-1]
    d = {}
    pos = 0
    for x in range(q[0], q[1] + 1):
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
        self.Inflation = float(service)
        self.Quality = qual
        self.Stock = []

    def fill_store(self, Item, quantity):
        for _ in range(quantity):
            same = True
            while same:
                # qual = randint(self.Quality[0], self.Quality[1] + 1)
                qual = int(determine_rarity(self.Quality))
                i = Item(qual)
                i.Cost = float(i.Cost * self.Inflation)
                if i not in self.Stock:
                    self.Stock.append(i)
                    same = False

    def add_relic(self, Item):
        # qual = randint(self.Quality[0], self.Quality[1] + 1)
        if isinstance(Item, Weapon):
            typ = choice([
                "Axe",
                "Bow",
                "Dagger",
                "Hammer",
                "Mace",
                "Spear",
                "Sword",
            ])
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

    def to_dict(self):
        d = {
            "Shopkeeper": self.Shopkeeper,
            "Store_name": self.Store_name,
            "Quality": self.Quality,
            "Stock_quantity": len(self.Stock),
            "Stock_type": str(type(self.Stock[0]).__name__),
            "Inflation": self.Inflation
        }
        return d

    def from_dict(self, new_self):
        new_stock = []
        new_class = eval(new_self.pop("Stock_type"))
        new_quan = new_self.pop("Stock_quantity")
        self.Stock = []

        self.__dict__.update(new_self)
        self.fill_store(new_class, new_quan)


class Weapon(object):
    """
    Cost should be in GP
    Rarity [0, 4] - Common, Uncommon, Rare, Very Rare, Legendary
        Rarity will also determine what types of material to use as well as the
            price for an item. Also note, that the prices are how much they cost
            to make, not the cost they'll be sold for.
    """
    Weight = Cost = Rarity = Masterwork = 0
    Name = Dice = Crit = Class = ''
    Damage = []
    Enchantment = None

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
        if requirement is None:
            # Make a pick with each weapon type
            if randint(2):
                self.Class = choice(list(possible_melee.keys()))
                self.Name = choice(list(possible_melee[self.Class])).title()
            else:
                self.Class = choice(list(possible_ranged.keys()))
                self.Name = choice(list(possible_ranged[self.Class])).title()
        # Existing requirement
        elif requirement in list(possible_melee.keys()):
            self.Class = requirement
            self.Name = choice(list(possible_melee[self.Class])).title()

        elif requirement in list(possible_ranged.keys()):
            self.Class = requirement
            self.Name = choice(list(possible_ranged[self.Class])).title()

        else:
            print("The requirement is not in the list of possible weapons.")
            return None

        # We have a class of weapon. Get weapon Damage
        self.Dice = str(int(self.Rarity / 2) + 1) + 'd' + str(
            choice(die_values[self.Class]))

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
            self.Damage = [
                'Ra', 'P',
                choice(['30', '40', '50', '60', '70', '80', '90', '100', '110', '120']) +
                ' ft.'
            ]
        elif self.Class == 'Crossbow':
            self.Damage = [
                'Ra', 'P',
                choice(['60', '70', '80', '90', '100', '110', '120']) + ' ft.'
            ]
        elif self.Class == 'Thrown':
            self.Damage = [
                'Ar', 'P', 'S',
                choice(['15', '20', '25', '30', '35', '40']) +
                ' ft.'
            ]
        return

    def __choose_metal(self):
        if self.Rarity > 4:
            self.Rarity %= 4

        if self.Rarity == 1:  # Uncommon Materials
            m = self.__verify_metal(uncommon_material)

        elif self.Rarity == 2:  # Rare Materials
            m = self.__verify_metal(rare_material)

        elif self.Rarity == 3:  # Very Rare Materials
            m = self.__verify_metal(very_rare_material)

        elif self.Rarity == 4:  # Legendary Materials
            m = self.__verify_metal(legendary_material)

        else:  # Common Materials
            m = self.__verify_metal(common_material)

        self.Name = m[0] + ' ' + self.Name
        self.__weigh(m[0], m[1])

    def __verify_metal(self, cl):
        metal = None
        while metal is None:
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
        if chance < 80:
            self.Crit = 'x2'
        elif chance < 92:
            self.Crit = '19-20 x2'
        elif chance < 97:
            self.Crit = '18-20 x2'
        elif chance < 100:
            self.Crit = 'x3'
        elif chance < 130:
            self.Crit = '19-20 x3'
        else:
            self.Crit = '18-20 x3'
        return chance

    def __weigh(self, metal, cl):
        dice_incriment = int(eval(self.Dice.split('d')[1]) / 2) * 2**eval(self.Dice.split('d')[0])
        crit_val = (self.__crit() // 20)
        cost_factor = max([weapon_cost_and_weight[self.Class][0], dice_incriment * crit_val])

        self.Cost = round(cost_factor * cl[metal]['Cost'] * (self.Rarity + 1)**self.Rarity, 2)
        self.Weight = round(weapon_cost_and_weight[self.Class][1] * cl[metal]['Weight'] * 14, 1)

    def add_enchantment(self, ench):
        if self.Enchantment is None:
            self.Enchantment = ench
            self.Cost = float(self.Cost + self.Enchantment.Cost)
        else:
            print("This Item is already enchanted.")

    def add_masterwork(self, mlevel):
        if mlevel > 10:
            mlevel %= 9
        if self.Masterwork == 0:
            self.Masterwork = int(mlevel)
            self.Cost += (1 + mlevel) * 1000
            self.Name = "+" + str(mlevel) + ' ' + self.Name
            self.Dice += "+" + str(mlevel)

    def __str__(self):
        global MasterID
        r = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary']
        l = [
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
        ]
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
        'Pistol': [
            'Akdal Ghost TR01',
            'ALFA Combat',
            'ALFA Defender',
            'AMT AutoMag II',
            'AMT AutoMag III',
            'AMT AutoMag IV',
            'AMT Backup',
            'AMT Hardballer',
            'AMT Lightning pistol',
            'AMT Skipper',
            'Armatix iP1',
            'Arsenal P-M02',
            'Ashani',
            'ASP pistol',
            'Paris Theodore',
            'Astra 400',
            'Astra 600',
            'Astra Model 900',
            'Astra Model 903',
            'Astra A-60',
            'Astra A-80',
            'Astra A-100',
            'Ballester-Molina',
            'Bauer Automatic',
            'Bayard 1908',
            'Anciens Etablissements Pieper',
            'Bechowiec-1',
            'Bataliony Chiopskie',
            'Beholla pistol',
            'Benelli B76',
            'Benelli MP 90S',
            'Benelli MP 95E',
            'Beretta M9',
            'Beretta 21A Bobcat',
            'Beretta 70',
            'Beretta 90two',
            'Beretta 92',
            'Beretta 92G-SD/96G-SD',
            'Beretta 93R',
            'Beretta 418',
            'Beretta 950',
            'Beretta 3032 Tomcat',
            'Beretta 8000',
            'Beretta 9000',
            'Beretta Cheetah',
            'Beretta M1923',
            'Beretta M1934',
            'Beretta M1935',
            'Beretta M1951',
            'Beretta Nano',
            'Beretta Pico',
            'Beretta Px4 Storm',
            'Beretta U22 Neos',
            'Bersa 83',
            'Bersa Thunder 9',
            'Bersa Thunder 380',
            'Bergmann-Bayard',
            'Theodor Bergmann',
            'Bren Ten',
            'FN Herstal',
            'Browning BDM',
            'Browning Buck Mark',
            'Browning Hi-Power',
            'FN Herstal',
            'Brugger & Thomet MP9',
            'BUL Cherokee',
            'BUL Transmark',
            'BUL M-5',
            'BUL Transmark',
            'BUL Storm',
            'BUL Transmark',
            'Calico M950',
            'Campo Giro',
            'Caracal pistol',
            'Claridge Hi-Tec/Goncz Pistol',
            'Colt Delta Elite',
            'Colt Mustang',
            'Colt OHWS',
            'Colt SCAMP',
            'CZ vz. 27',
            'CZ vz. 38',
            'CZ vz. 50 / CZ vz. 70',
            'CZ 52',
            'CZ 85',
            'CZ 97B',
            'Daewoo Precision Industries K5',
            'Danuvia VD-01',
            'Davis Warner Infallible',
            'Deer gun',
            'Dreyse M1907',
            'Rheinische Metallwaaren- und Maschinenfabrik AG',
            'FB P-64',
            'FeG 37M Pistol',
            'Fegyver- es Gepgyar',
            'FEG PA-63',
            'Fegyver- es Gepgyar',
            'RPC Fort',
            'Fort-17',
            'RPC Fort',
            'FN Baby Browning',
            'FN M1900',
            'FN Model 1903',
            'FN M1905',
            'FN Model 1910',
            'FN Forty-Nine',
            'FN Five-seven',
            'FN FNP',
            'FN FNS',
            'FN FNX',
            'FP-45 Liberator',
            'Fegyver- es Gepgyar',
            'Gaztanaga Destroyer',
            'Gaztanaga',
            'Glisenti Model 1910',
            'Glock Ges.m.b.H.',
            'Grand Power K100',
            'GSh-18',
            'Guncrafter Industries Model No. 1',
            'Gyrojet',
            'Hamada Type pistol',
            'Harper\'s Ferry Model 1805',
            'Harpers Ferry Armory',
            'Hi-Point C-9',
            'Hi-Point CF-380',
            'Hi-Point Model JCP',
            'Hi-Point Model JHP',
            'High Standard HDM',
            'Howdah pistol',
            'HS2000',
            'HS Produkt',
            'Intratec TEC-22',
            'Intratec',
            'JO.LO.AR.',
            'Kahr K series',
            'Kahr MK series',
            'Kahr P series',
            'Kahr PM series',
            'Kel-Tec P-3AT',
            'Kel-Tec P-11',
            'Kel-Tec P-32',
            'Kel-Tec PF-9',
            'Kel-Tec PLR-16',
            'Kel-Tec PMR-30',
            'Kimber Aegis',
            'Kimber Custom',
            'Kimber Eclipse',
            'Kimel AP-9',
            'Kongsberg Colt',
            'Korovin',
            'Krag-Jorgensen',
            'KRISS KARD',
            'Lahti L-35',
            'Valtion Kivaaritehdas',
            'Lancaster pistol',
            'Lercker pistol',
            'Italy',
            'Liliput pistol',
            'Llama M82',
            'Luger pistol',
            'Deutsche Waffen und Munitionsfabriken',
            'M15 pistol',
            'Rock Island Arsenal',
            'MAB Model A',
            'MAB PA-15 pistol',
            'MAC Mle 1950',
            'MAC-10',
            'MAC-11',
            'Makarov pistol',
            'Makarych',
            'Mamba Pistol',
            'Mars Automatic Pistol',
            'Mauser C96',
            'Mauser',
            'Mauser HSc',
            'Mauser',
            'MGP-15 submachine gun',
            'Minebea PM-9',
            'Minebea',
            'Modele 1935 pistol',
            'MP-443 Grach',
            'Musgrave Pistol',
            'NAACO Brigadier',
            'Obregon pistol',
            'Ortgies Semi-Automatic Pistol',
            'OTs-02 Kiparis',
            'OTs-23 Drotik',
            'OTs-33 Pernach',
            'P9RC',
            'Fegyver- es Gepgyar',
            'PAMAS modele G1',
            'Para-Ordnance P14-45',
            'Para USA',
            'Pardini GT9',
            'Pindad G2',
            'Pindad P3',
            'Pindad',
            'Pindad PS-01',
            'Pindad',
            'Pistol model 2000',
            'Pistole vz. 22',
            'PP-2000',
            'Prilutsky M1914',
            'PSM pistol',
            'QSW-06',
            'QSZ-92',
            'Remington 1911 R1',
            'Remington Model 51',
            'Remington R51',
            'Remington Rider Single Shot Pistol',
            'Remington XP-100',
            'Remington Zig-Zag Derringer',
            'Rock Island Armory 1911 series',
            'Rohrbaugh R9',
            'Ruby pistol',
            'Ruger Hawkeye',
            'Ruger LCP',
            'Ruger LC9',
            'Ruger MP9',
            'Ruger SR1911',
            'Sauer 38H',
            'Savage Model 1907',
            'Schwarzlose Model 1898',
            'Schonberger-Laumann 1892',
            'SP-21 Barak',
            'SPP-1 underwater pistol',
            'Star Firestar M43',
            'Star Model 14',
            'Star Model S',
            'Star Ultrastar',
            'Steyr GB',
            'Steyr M',
            'Steyr TMP',
            'Steyr M1912',
            'Sugiura pistol',
            'Tanfoglio Force',
            'Tanfoglio',
            'Tanfoglio GT27',
            'Tanfoglio',
            'Tanfoglio T95',
            'Tanfoglio',
            'Taurus PT92',
            'Taurus Millennium series',
            'Taurus PT1911',
            'TEC-9',
            'Intratec',
            'TP-82',
            'TT pistol',
            'Tokarev TT-33',
            'Fedor Tokarev',
            'Trejo pistol',
            'Type 14 Nambu',
            'Type 64 pistol',
            'Type 77 pistol',
            'Israel Military Industries',
            'Vektor CP1',
            'Vektor SP1',
            'Viper Jaws pistol',
            'Volkspistole',
            'Mauser',
            'Walther CCP',
            'Walther HP',
            'Walther Model 9',
            'Walther P5',
            'Walther P22',
            'Walther P38',
            'Walther P88',
            'Walther P99',
            'Walther PP',
            'Walther PK380',
            'Walther PPQ',
            'Walther PPS',
            'Walther TPH',
            'Webley Self-Loading Pistol',
            'Welrod',
            'Werder pistol model 1869',
            'Johann Ludwig Werder',
            'Whitney Wolverine',
            'Wildey',
            'WIST-94',
            'Zaragoza Corla',
            'Zastava P25',
            'Zastava M57',
            'Zastava M70',
            'Zastava M88',
            'Zastava PPZ',
        ],
        'Rifle': [
            '1792 contract rifle',
            'Advanced Combat Rifle',
            'ArmaLite AR-5',
            'ArmaLite AR-7',
            'ArmaLite AR-10',
            'ArmaLite AR-30',
            'Barrett REC7',
            'Barrett XM109',
            'Barrett XM500',
            'Bendix Hyde carbine',
            'Berdan rifle',
            'Browning BLR',
            'Burnside carbine',
            'Bushmaster Arm Pistol',
            'Bushmaster M4-type Carbine',
            'Bushmaster M17S',
            'CAR-15',
            'Close Quarters Battle Receiver',
            'CMMG Mk47 Mutant',
            'Advanced Colt Carbine-Monolithic',
            'Colt Advanced Piston Carbine',
            'Colt Lightning Carbine',
            'Colt Model 1839 Carbine',
            'Colt Ring Lever rifles',
            'Colt-Burgess rifle',
            'Crazy Horse rifle',
            'Demro TAC-1',
            'Frank Wesson Rifles',
            'Grendel R31',
            'Harpers Ferry Model 1803',
            'Hawken rifle',
            'Henry rifle',
            'Hi-Point Carbine',
            'Hillberg carbine',
            'Individual Carbine',
            'Iver Johnson AMAC-1500',
            'Krag-Jorgensen',
            'M1 Garand',
            'M4 carbine',
            'M14 rifle',
            'M16 rifle',
            'M21 Sniper Weapon System',
            'M27 Infantry Automatic Rifle',
            'M86 Rifle',
            'M231 Firing Port Weapon',
            'M1819 Hall rifle',
            'M1885 Remington-Lee',
            'M1895 Lee Navy',
            'M1903 Springfield',
            'M1917 Enfield',
            'M1918 Browning Automatic Rifle',
            'M1922 Bang rifle',
            'M1941 Johnson rifle',
            'M1944 Hyde Carbine',
            'M1947 Johnson auto carbine',
            'Marlin Levermatic',
            'Marlin Model 20',
            'Marlin Model 60',
            'Marlin Model 70P',
            'Marlin Model 336',
            'Marlin Model 780',
            'Marlin Model 795',
            'Marlin Model 1894',
            'Marlin Model Golden 39A',
            'Marlin Model XT-22',
            'Maynard carbine',
            'Mk 14 Enhanced Battle Rifle',
            'Model 1814 common rifle',
            'Model 1817 common rifle',
            'Mosin-Nagant',
            'Mossberg 464',
            'Mossberg Plinkster',
            'Palmer carbine',
            'Pedersen rifle',
            'Precision Sniper Rifle',
            'PTR rifle',
            'Remington ACR',
            'Remington Model 5',
            'Remington Model 241',
            'Remington Model 572',
            'Remington Model 600',
            'Remington Model 660',
            'Remington Model 673',
            'Remington Model 700',
            'Remington Model 721',
            'Remington Model 750',
            'Remington Model 760',
            'Remington Model 770',
            'Remington Model 7400',
            'Remington Model 7600',
            'Remington Rolling Block rifle',
            'Ruger American Rifle',
            'Ruger M77',
            'Ruger SR-556',
            'Savage Model 99',
            'Savage Model 110',
            'SEAL Recon Rifle',
            'Sharps & Hankins Model 1862 Carbine',
            'Sharps rifle',
            'Smith & Wesson M&P10',
            'Smith & Wesson M&P15',
            'Smith & Wesson M&P15-22',
            'Smith & Wesson Model 1940 Light Rifle',
            'Spencer repeating rifle',
            'Springfield Model 1865',
            'Springfield Model 1866',
            'Springfield Model 1868',
            'Springfield Model 1869',
            'Springfield model 1870',
            'Springfield model 1870 Remington-Navy',
            'Springfield model 1871',
            'Springfield model 1873',
            'Springfield Model 1875',
            'Springfield Model 1877',
            'Springfield model 1880',
            'Springfield Model 1882',
            'Springfield model 1884',
            'Springfield Model 1886',
            'Springfield Model 1888',
            'Springfield Model 1892-99',
            'Springfield Model 1922',
            'Springfield rifle',
            'Starr carbine',
            'Stoner 63',
            'T48 rifle',
            'Thompson Autorifle',
            'Thompson Light Rifle',
            'Tubb 2000',
            'United States Army Squad Designated Marksman Rifle',
            'United States Marine Corps Designated Marksman Rifle',
            'Volcanic Repeating Arms',
            'Winchester Hotchkiss',
            'Winchester Model 67',
            'Winchester Model 68',
            'Winchester Model 69',
            'Winchester Model 1886',
            'Winchester Model 1890',
            'Winchester Model 1892',
            'Winchester Model 1894',
            'Winchester Model 1895',
            'Winchester Model 1906',
            'Winchester Model 1907',
            'Winchester rifle',
            'Winder musket',
            'AAC Honey Badger',
            'AAI ACR',
            'Adcor A-556',
            'ADS amphibious rifle',
            'Advanced Combat Rifle',
            'Advanced Individual Combat Weapon',
            'AG-043',
            'AK-9',
            'AK-12',
            'AK-47',
            'AK-63',
            'AK-74',
            'AK-100 (rifle family)',
            'AK-103',
            'AK-104',
            'AK-105',
            'AKM',
            'AKMSU',
            'AL-7',
            'AMD-65',
            'AMP-69',
            'AMR-69',
            'AO-27 rifle',
            'AO-35 assault rifle',
            'AO-38 assault rifle',
            'AO-46 (firearm)',
            'AO-63 assault rifle',
            'APS underwater rifle',
            'AR-M1',
            'Ares Shrike 5.56',
            'ArmaLite AR-15',
            'Armtech C30R',
            'AS Val',
            'AS-44',
            'ASh-12.7',
            'ASM-DT amphibious rifle',
            'Barrett M468',
            'Bendix Hyde carbine',
            'Beretta AS70/90',
            'BSA 28P',
            'CAR 816',
            'CEAM Modele 1950',
            'CETME',
            'CETME rifle',
            'Close Quarters Battle Receiver',
            'CMMG Mk47 Mutant',
            'Colt ACR',
            'Colt Advanced Piston Carbine',
            'Comparison of the AK-47 and M16',
            'Conventional Multirole Combat Rifle',
            'CornerShot',
            'Cristobal Carbine',
            'CZ 807',
            'CZ 2000',
            'Dlugov assault rifle',
            'EM-2 rifle',
            'EM-4 rifle',
            'EMERK',
            'FA-MAS Type 62',
            'FB Mini-Beryl',
            'FB Onyks',
            'FB Tantal',
            'Featureless rifles',
            'Floro PDW',
            'Gahendra Rifle',
            'Grad AR',
            'GRAM 63 battle rifle',
            'Grossfuss Sturmgewehr',
            'Heckler & Koch G11',
            'Heckler & Koch G36',
            'Heckler & Koch HK36',
            'Heckler & Koch HK416',
            'Howa Type 64',
            'Howa Type 89',
            'IWI Tavor 7',
            'Interdynamics MKR',
            'Interdynamics MKS',
            'IWI ACE',
            'IWI Tavor X95',
            'Kalashnikov rifle',
            'Kbkg wz. 1960',
            'L64/65',
            'LAPA FA-03',
            'Lightweight Small Arms Technologies',
            'LR-300',
            'LSAT rifle',
            'LVOA-C',
            'LWRC M6',
            'M4 carbine',
            'M4-WAC-47',
            'M231 Firing Port Weapon',
            'M1944 Hyde Carbine',
            'Madsen LAR',
            'MPT-76',
            'MR-C',
            'MSBS rifle',
            'Multi Caliber Individual Weapon System',
            'Nesterov assault rifle',
            'Norinco Type 86S',
            'Objective Individual Combat Weapon',
            'OTs-12 Tiss',
            'OTs-14 Groza',
            'PAPOP',
            'Pindad SS3',
            'Pistol Mitraliera model 1963/1965',
            'POF Eye',
            'Project Abakan',
            'Pusca Automata model 1986',
            'QBZ-03',
            'QTS-11',
            'RK 62',
            'RK 95 TP',
            'SA M-7',
            'SIG Sauer SIG516',
            'SIG Sauer SIGM400',
            'SLEM-1',
            'SR-3 Vikhr',
            'Steyr ACR',
            'STG-556',
            'Sturmgewehr 52',
            'Sturmgewehr 58',
            'Thompson Light Rifle',
            'TKB-010',
            'TKB-011',
            'TKB-022PM',
            'TKB-059',
            'TKB-072',
            'TKB-0146',
            'TKB-408',
            'TKB-517',
            'Type 56 assault rifle',
            'Type 58 assault rifle',
            'Type 63 assault rifle',
            'Type 81 assault rifle',
            'United States Army Squad Designated Marksman Rifle',
            'VAHAN (firearm)',
            'VB Berapi LP06',
            'Vepr',
            'Vollmer M35',
            'Vz. 58',
            'Maschinenkarabiner 42(W)',
            'WASR-series rifles',
            'Wimmersperg Spz',
            'Winchester LMR',
            'Zastava M70',
            'Zastava M77 B1',
            'Zastava M90',
        ],
        'Sniper': [
            'Anzio 20mm rifle',
            'Barrett M82',
            'Barrett M90',
            'Barrett M95',
            'Barrett Model 98B',
            'Barrett MRAD',
            'CheyTac Intervention',
            'Desert Tech HTI',
            'Desert Tech SRS',
            'EDM Arms Windrunner',
            'Grizzly Big Boar',
            'H-S Precision Pro Series 2000 HTR',
            'Harris Gun Works M-96',
            'Knight\'s Armament Company SR-25',
            'Longbow T-76',
            'M1 Garand',
            'M24 Sniper Weapon System',
            'M25 Sniper Weapon System',
            'M39 Enhanced Marksman Rifle',
            'M40 rifle',
            'M110 Semi-Automatic Sniper System',
            'M1903 Springfield',
            'McMillan TAC-50',
            'MICOR Leader 50',
            'Mk 12 Special Purpose Rifle',
            'Pauza P-50',
            'Precision-guided firearm',
            'Remington Model 700',
            'Remington MSR',
            'Remington Semi Automatic Sniper System',
            'Robar RC-50',
            'Savage 10FP',
            'Savage 110 BA',
            'United States Marine Corps Squad Advanced Marksman Rifle',
            'M2010 Enhanced Sniper Rifle',
        ],
        'Shotgun': [
            'Blunderbuss',
            'Cynergy Shotgun',
            'TOZ-106',
            'Ithaca Mag-10',
            'Remington Model SP-10',
            'Winchester Model 1200',
            'Marlin Model 55',
            'Akdal MKA',
            'Armsel Striker',
            'Atchisson Assault Shotgun',
            'Baikal MP-153',
            'Bandayevsky RB-12',
            'Benelli M4',
            'Benelli Raffaello',
            'Benelli Supernova',
            'Benelli Vinci',
            'Beretta FP',
            'Beretta A303',
            'Beretta DT-10',
            'Beretta Xtrema 2',
            'Browning Double Automatic Shotgun',
            'FN Herstal',
            'Ciener Ultimate Over/Under',
            'ENARM Pentagun',
            'Fabarm SDASS Tactical',
            'FN SLP',
            'FN TPS',
            'FN SC-1',
            'Franchi SPAS-12',
            'Franchi SPAS-15',
            'Heckler & Koch FABARM FP6',
            'Heckler & Koch HK CAWS',
            'High Standard Model 10',
            'KAC Masterkey',
            'Kel-Tec KSG',
            'M26 Modular Accessory Shotgun System',
            'MAG-7',
            'MAUL (shotgun)',
            'Mossberg 930',
            'NeoStead',
            'Norinco HP9-1',
            'Pancor Jackhammer',
            'Remington Model 10',
            'Remington Model 878',
            'Remington Model 887',
            'Remington Spartan 453',
            'RMB-93',
            'Ruger Gold Label',
            'Sjogren shotgun',
            'TOZ-194',
            'USAS-12',
            'Valtro PM-5/PM-5-350',
            'Weatherby Orion',
            'Winchester Model',
            'Browning BSS',
            'Molot Bekas-M',
            'Browning Auto-5',
            'Browning Superposed',
            'Remington Model 11',
            'Remington Model 31',
            'Remington Model 58',
            'Stevens Model 520/620',
            'Winchester Model 1897',
            'Stoeger Condor',
            'Ithaca 37',
            'Winchester Model 1897',
            'Winchester Model 1887',
            'Browning Citori',
            'Cooey 84',
            'Remington Model 11-48',
            'Remington Model 870',
            'Remington Model 1912',
            'Winchester Model 21',
            'Winchester Model 37',
            'Benelli M1',
            'Benelli M3',
            'Benelli Nova',
            'Beretta AL391',
            'H&R Ultraslug Hunter',
            'Remington Model 11-87',
            'Weatherby SA-08',
            'Mossberg 500',
            'Mossberg 590',
            'Remington Spartan 100',
            'Saiga-12',
            'Stoeger Coach Gun',
            'Blaser F3',
            'Beretta 682',
            'Beretta Silver Pigeon',
            'Remington Spartan 310',
            'MTs-255',
            'Remington Model 17',
            'Franchi AL-48',
            'KS-23',
            'RGA-86',
            'Winchester Model 20',
            'Vepr-12',
        ],
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
        if rarity > 4:
            rarity %= 4
        self.Rarity = rarity
        self.Crit = 'x' + str(randint(2, 5))
        self.__choose_metal()
        self.Name += choice(self.possible[self.Class])

        if self.Class == 'Pistol':
            self.Capacity = int(choice([1, 2, 4, 6, 8]))
            self.Range = 10 + randint(1, 4) * 5 * (self.Rarity + 1)
            self.Dice = str(int(
                (self.Rarity + 2) / 2)) + 'd' + str(choice([4, 6, 8]))

        elif self.Class == 'Rifle':
            self.Capacity = int(10 + randint(1, 8) * 5)
            self.Range = 10 + randint(1, 6) * 5 * (self.Rarity + 1)
            self.Dice = str(int(
                (self.Rarity + 2) / 2)) + 'd' + str(choice([4, 6, 8, 10]))

        elif self.Class == 'Shotgun':
            self.Capacity = int(choice([1, 2, 4, 6, 8, 10, 12]))
            self.Range = randint(3, 6) * 5 * (self.Rarity + 1)
            self.Dice = str(int(
                (self.Rarity + 2) / 2)) + 'd' + str(choice([6, 8, 10, 12]))

        elif self.Class == 'Sniper':
            self.Capacity = int(choice([1, 2, 4]))
            self.Range = 30 + randint(3, 7) * 10 * (self.Rarity + 1)
            self.Dice = str(int(
                (self.Rarity + 2) / 2)) + 'd' + str(choice([8, 10, 12]))

        if iName is not None:
            self.Name = iName

        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_enchantment(Enchant())
        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_masterwork(determine_rarity([1, 9]))

    def __choose_metal(self):
        if self.Rarity > 4:
            self.Rarity %= 4

        cl = [
            common_material, uncommon_material, rare_material,
            very_rare_material, legendary_material
        ][self.Rarity]
        metal = None
        while metal is None:
            metal = choice(list(cl.keys()))
            if 'HA' in cl[metal]['Type'] and 'P' in cl[metal]['Type']:
                self.Name += metal + ' '
            else:
                metal = None
        self.Cost = self.cost_and_weight[self.Class][0] * cl[metal]['Cost'] * (
            self.Rarity + 1)**self.Rarity
        self.Weight = round(
            self.cost_and_weight[self.Class][1] * cl[metal]['Weight'] * 4, 1)

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
            self.Masterwork = int(mlevel)
            self.Cost += (1 + mlevel) * (1 + mlevel) * 1000
            self.Name = "+" + str(mlevel) + ' ' + self.Name
            self.Dice += "+" + str(mlevel)
        # else:
        #     print("This Item is already Masterwork")

    def __str__(self):
        global MasterID
        r = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary']
        l = [
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
        ]
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
        'Padded': [5, 1, 5, 10],
        'Leathered': [10, 1, 10, 15],
        'Studded': [15, 2, 25, 20],
        'Chained': [20, 2, 100, 25],
    }
    medium_armor = {
        # Name	: 			HP, AC, Cost, Weight
        'Hide': [
            15,
            2,
            15,
            25,
        ],
        'Scale mail': [
            20,
            2,
            50,
            30,
        ],
        'Chainmail': [
            25,
            3,
            150,
            40,
        ],
        'Breastplate': [
            25,
            3,
            200,
            30,
        ],
    }
    heavy_armor = {
        # Name	: 			HP, AC, Cost, Weight
        'Splint mail': [
            30,
            3,
            200,
            45,
        ],
        'Banded mail': [
            30,
            3,
            250,
            35,
        ],
        'Half-plate': [
            35,
            4,
            600,
            50,
        ],
        'Full plate': [
            40,
            4,
            1500,
            50,
        ],
    }
    shield = {
        # Name	: 			HP, AC, Cost, Weight
        'Buckler': [
            5,
            1,
            5,
            5,
        ],
        'Light Shield': [
            10,
            1,
            9,
            6,
        ],
        'Heavy Shield': [
            20,
            2,
            20,
            15,
        ],
        'Tower Shield': [
            20,
            4,
            30,
            45,
        ],
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
        if self.Class not in ['Light', 'Medium', 'Heavy', 'Shield'
                              ] or self.Class is None:
            self.Class = choice(['Light', 'Medium', 'Heavy', 'Shield'])
        if self.Class == 'Light':
            c = choice(list(self.light_armor.keys()))
            self.AC += self.light_armor[c][1]
            self.Cost = round(self.Cost * self.light_armor[c][2] *
                              (self.Rarity + 1)**self.Rarity)
            self.Weight *= round(self.light_armor[c][3], 1)
            self.Name = c + " " + self.Metal
            if c == 'Leathered' and self.Metal == "Leather":
                self.Name = "Leather"
        elif self.Class == 'Medium':
            c = choice(list(self.medium_armor.keys()))
            self.AC += self.medium_armor[c][1]
            self.Cost = round(self.Cost * self.medium_armor[c][2] *
                              (self.Rarity + 1)**self.Rarity)
            self.Weight *= round(self.medium_armor[c][3], 1)
            self.Name = self.Metal + " " + c
        elif self.Class == 'Heavy':
            c = choice(list(self.heavy_armor.keys()))
            self.AC += self.heavy_armor[c][1]
            self.Cost = round(self.Cost * self.heavy_armor[c][2] *
                              (self.Rarity + 1)**self.Rarity)
            self.Weight *= round(self.heavy_armor[c][3], 1)
            self.Name = self.Metal + " " + c
        else:
            c = choice(list(self.shield.keys()))
            self.AC += self.shield[c][1]
            self.Cost = round(
                self.Cost * self.shield[c][2] * (self.Rarity + 1)**self.Rarity)
            self.Weight *= round(self.shield[c][3], 1)
            self.Name = self.Metal + " " + c
        # print(c)

    def __str__(self):
        global MasterID
        r = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary']
        l = [
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
        ]
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
            self.Masterwork = int(mlevel)
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
                self.Enchantment = Enchant(
                    iSpell=self.Spell, rechargable=False)

        if naming:
            self.Name = Scroll_Name_Potential[randint(len(Scroll_Name_Potential))] + self.Spell
        else:
            self.Name = self.Spell
            self.Add = '+'

    def __str__(self):
        # print(self.Enchantment.Level)
        global MasterID
        l = [
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
        ]

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
            self.Level = int(
                choice(list(level_likelihood.keys()), p=list(level_likelihood.values())))
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
            self.Uses = int(choice([2, 4, 6, 8, 10, 12], p=[.35, .3, .15, .1, .05, .05]))
            self.Cost += self.Uses * (self.Level + 1)**self.Level
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
                self.Enchantment = Enchant(
                    iSpell=self.Spell, rechargable=False)

        self.Name = Potion_Name_Potential[randint(len(Potion_Name_Potential))] + self.Spell

    def __str__(self):
        # print(self.Enchantment.Level)
        global MasterID
        l = [
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
        ]

        s = """<tr><td style="width:50%;"><span class="text-md" onclick="show_hide('""" + str(MasterID) + \
            """')" style="color:blue;">""" + self.Name + """</span><br /><span class="text-sm emp" id=\"""" + \
            str(MasterID) + """\" style="display: none;">""" + str(self.Enchantment) + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + l[self.Enchantment.Level] + """</td></tr>"""
        MasterID += 1
        return s

    def to_string(self):
        return self.Name + ' (' + determine_cost(self.Cost) + ')'


class Wand(object):
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
        self.Name = Wand_Name_Potential[randint(len(Wand_Name_Potential))] + self.Spell

    def __str__(self):
        # print(self.Enchantment.Level)
        global MasterID
        l = [
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
        ]

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

    def __init__(self, keeper, name, service, rooms, quan):
        self.Shopkeeper = keeper
        self.Store_name = name
        self.Inflation = service
        self.Stock = []

        self.__fill_rooms(rooms)
        self.__fill_stock(quan)

    def __fill_rooms(self, rooms):
        self.Rooms = []
        for n in range(1, rooms + 1):
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

    def from_dict(self, new_self):
        rooms = new_self.pop('Rooms')
        if rooms:
            num_rooms = max([v['Beds'] for v in rooms])
            self.__fill_rooms(num_rooms)
        stock = new_self.pop('Stock')
        self.__fill_stock(len(stock))
        self.__dict__.update(new_self)


class Food(object):
    String = Descriptor = ''
    Cost = 0

    def __init__(self, rarity):
        s = ""
        meal_option = randint(15) + rarity
        if meal_option <= 10:
            self.Descriptor = "Meat, Bread"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(
                len(Food_m2))] + " " + Food_m3[randint(
                    len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(
                len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
        elif meal_option == 11:
            self.Descriptor = "Meat, Bread, Fruit"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(
                len(Food_m2))] + " " + Food_m3[randint(
                    len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(
                len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_f1[randint(
                len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]

        elif meal_option == 12:
            self.Descriptor = "Meat, Bread, Vegetable"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(
                len(Food_m2))] + " " + Food_m3[randint(
                    len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(
                len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_v1[randint(
                len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        elif meal_option == 13:
            self.Descriptor = "Vegetable, Bread, Fruit"
            s += Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(
                len(Food_v2))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(
                len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_f1[randint(
                len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
        elif meal_option == 14:
            self.Descriptor = "Meat, Fruit, Vegetable"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(
                len(Food_m2))] + " " + Food_m3[randint(len(Food_m3))]
            s += " with " + Food_f1[randint(
                len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
            s += " and " + Food_v1[randint(
                len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        else:
            self.Descriptor = "Meat, Fruit, Vegetable, Bread"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(
                len(Food_m2))] + " " + Food_m3[randint(
                    len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(
                len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " with " + Food_f1[randint(
                len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
            s += " and " + Food_v1[randint(
                len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        self.String = s
        if meal_option == 0:
            self.Cost = (len(s) * random_sample() + .5) // 10
        else:
            self.Cost = (len(s) *
                         (sum(random_sample(meal_option)) / meal_option)) // 10

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.String + """</span></td><td>""" + \
            determine_cost(self.Cost) + """</td><td>""" + self.Descriptor + """</td></tr>"""
        return s


class Drink(object):
    String = Descriptor = ''
    Cost = 0

    def __init__(self, level):
        s = ''
        num = randint(4) + level
        if num < 2:
            self.Descriptor = "Non-Alcoholic"
            s += Drink_d1[randint(len(Drink_d1))]
        else:
            self.Descriptor = "Alcoholic"
            s += Drink_d2[randint(len(Drink_d2))]
        self.String = s
        if num == 0:
            self.Cost = (len(s) * random_sample() + .5) / 10
        else:
            self.Cost = (len(s) * (sum(random_sample(num)) / num)) / 10

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
        self.Cost = 0.5 * (qual + 1) * beds

    def __str__(self):
        s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Name + ' (Room Rental)</span></td><td>' + \
            determine_cost(self.Cost) + """</td><td>Lodging</td></tr>"""
        return s


class Jewel(object):
    value = [
        10,
        50,
        100,
        500,
        1000,
        5000,
    ]
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
        l = [
            'Low Quality Gems', 'Semi Precious Gems',
            'Medium Quality Gemstones', 'High Quality Gemstones', 'Jewels',
            'Grand Jewels'
        ]
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
        c = choice(
            list(options.keys()), p=list(normalize_dict(options).values()))
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
    materials = [[
        'pewter', 'granite', 'soapstone', 'limestone', 'carved wood', 'ceramic'
    ], ['pewter', 'alabaster', 'silver', 'marble', 'bronze'],
                 ['pewter', 'alabaster', 'silver', 'marble', 'brass'],
                 ['gold', 'adamantine', 'dragonbone', 'crystal']]
    gems = [[
        'n azurite', ' banded agate', ' blue quartz', ' hematite',
        ' lapis lazuli', ' malachite', ' moss agate', 'n obsidian piece',
        ' tiger eye', ' beryl'
    ],
            [
                ' bloodstone', ' carnelian', ' chalcedony', ' citrine',
                ' jasper', ' moonstone', ' n onyx', ' zircon', ' chrysophase'
            ],
            [
                'n amber', 'n amethyst', ' piece of coral', ' garnet',
                ' piece of jade', ' pearl', ' spinel', ' tourmaline'
            ],
            [
                'n alexandrite', 'n aquamarine', ' topaz', ' peridot',
                ' blue spinel', ' black pearl', ' diamond'
            ]]
    filigree = [['copper', 'oak wood', 'tin', 'bronze', 'bone'],
                ['brass', 'maple wood', 'iron', 'glass', 'bone'],
                ['gold', 'mahogany wood', 'glass', 'ivory', 'mythril'],
                ['platinum', 'ironwood', 'mythril', 'ivory']]
    descriptor = [
        'ugly', 'beautiful', 'ancient', 'old', 'strange', 'antique', 'durable',
        'sturdy', 'engraved', 'ornate', 'rough', 'ornamental'
    ]
    cloth = [
        'silk', 'wool', 'leather', 'fur', 'angelskin', 'darkleaf',
        'griffon mane'
    ]
    bad_condition = [
        'in poor condition', 'of poor craftsmanship', 'of shoddy construction',
        'in bad shape', 'of low quality'
    ]
    figurine = [
        'a dragon', 'a gryphon', 'a hydra', 'an owlbear', 'a beholder',
        'a boar', 'a bear', 'a wolf', 'a fox', 'a tiger', 'a lion', 'a horse',
        'an owl', 'a hawk', 'an eagle', 'a crow', 'a snake', 'a fish',
        'a shark', 'a goblin', 'a skeleton', 'an orc', 'a minotaur',
        'a tiefling', 'a warrior', 'a knight', 'a thief', 'a wizard', 'a ship',
        'a castle', 'a tower', 'a boat', 'a king', 'a queen', 'a princess',
        'a god', 'a goddess'
    ]
    object = [
        'ring', 'tankard', 'goblet', 'cup', 'drinking horn', 'crown',
        'circlet', 'tiara', 'pendant', 'necklace', 'amulet', 'medallion',
        'bowl', 'plate', 'jewelry box', 'music box', 'brooch', 'chess set',
        'mask', 'holy text', 'hourglass', 'vase'
    ]
    magic = [
        'It glows with a soft blue light', 'It glows with a soft green light',
        'It glows with a soft red light', 'It glows with a soft amber light',
        'It glows with a soft violet light', 'It is warm to the touch',
        'It is hot to the touch', 'It is cool to the touch',
        'It is cold to the touch', 'It hums with gentle music',
        'It hums with melodic music', 'It hums with soft music',
        'It is wreathed in blue flames', 'It is wreathed in green flames',
        'It is wreathed in red flames', 'It is wreathed in amber flames',
        'It is wreathed in violet flames'
    ]

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
                self.Description = 'Pair of ' + choice(
                    self.descriptor) + ' ' + choice(self.cloth) + ' gloves'
            elif c == 2:
                self.Description = choice(self.descriptor) + ' ' + choice(
                    self.cloth) + ' ' + choice(['hat', 'ribbon'])
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
                self.Description = choice(
                    self.descriptor) + ' belt with a(n) ' + choice(
                        self.materials[1]) + ' buckle'
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
                self.Description = choice(
                    self.materials[3]) + ' framed painting of ' + choice(
                        self.figurine)
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
        return self.Description.title() + ' (' + determine_cost(
            self.Cost) + ')'


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
        l = [
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
        ]

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

    def __init__(self, useless):
        # Even though this has an argument, It needs it, but it's useless
        self.Person = create_person(None)
        self.Cost = random_sample() + .1

    def __str__(self):
        if self.Cost is None or self.Person.Gender is None:
            print(self.Cost)
            print(self.Person.Gender)
        return '<tr><td style="width:50%;"><span class="text-md">' + self.Person.Name + ' (' + self.Person.Race + ')' +\
               '</span><br /><span class="text-sm emp">' + self.Person.Appearance + '; Age ' + str(self.Person.Age) + \
               '</span></td><td>' + determine_cost(self.Cost) + '</td><td>' + self.Person.Gender + ' wanting ' +\
               self.Person.Orientation + '</td></tr>'


def create_variety_shop(owner, quan, inflate=1):
    if isinstance(inflate, float):
        inflation = (sum(random_sample(inflate)) / inflate) + .5
    else:
        inflation = inflate

    a = Store(owner, "Travelling Salesmen (Variety)", inflation, [0, 0])
    for _ in range(quan):
        item = None
        num = randint(0, 12)

        if num == 0:
            item = Weapon(randint(1, 5))
        elif num == 1:
            item = Armor(randint(1, 5))
        elif num == 2:
            item = Firearm(randint(1, 5))
        elif num == 3:
            item = Ring(randint(1, 10))
        elif num == 4:
            item = Scroll(randint(1, 10))
        elif num == 5:
            item = Wand(randint(1, 10))
        elif num == 6:
            item = Potion(randint(1, 10))
        elif num == 7:
            item = Book(randint(1, 10))
        elif num == 8:
            item = Wondrous()
        elif num == 9:
            item = Food(randint(1, 10))
        elif num == 10:
            item = Drink(randint(1, 10))
        elif num == 11:
            item = Jewel(randint(1, 10))

        a.Stock.append(item)

    return a


def create_book_shop(owner, genres, quan, inflate=1):
    for b in genres:
        if b not in Books.Genres:
            print(b, "Not in genre List. See: ", Books.Genres)
            return None
    if isinstance(inflate, float):
        a = Store(owner, str(Antiques()) + " (Library)", inflate, [0, 9])
    else:
        a = Store(owner,
                  str(Antiques()) + " (Library)",
                  (sum(random_sample(inflate)) / inflate) + .5, [0, 9])
    a.fill_store(Book, quan)
    return a


def create_enchantment_shop(owner, rarity, quan, inflate=1):
    name = str(Enchanter()) + " (Enchantments)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  rarity)
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
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  rarity)
    for _ in range(quan):
        item = Scroll(randint(rarity[0], rarity[1]), naming=False)
        item.Cost *= inflate
        a.Stock.append(item)
    return a


def create_weapon_shop(owner, rarity, quan, inflate=1):
    name = str(Blacksmith()) + " (Weapon)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  rarity)
    if quan <= 2:
        quan = 3
    a.fill_store(Weapon, quan)
    return a


def create_armor_shop(owner, rarity, quan, inflate=1):
    name = str(Blacksmith()) + " (Armor)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  rarity)
    if quan <= 2:
        quan = 3
    a.fill_store(Armor, quan)
    return a


def create_potion_shop(owner, rarity, quan, inflate=1):
    name = str(Potions()) + " (Alchemist)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  rarity)
    a.fill_store(Potion, quan)
    return a


def create_tavern(owner, rooms, quan, inflate=1):
    # def __init__(self, keeper, name, service, qual, rooms, quan):
    name = str(Tavern()) + " (Inn)"
    if isinstance(inflate, float):
        a = Inn(owner, name, inflate, rooms, quan)
    else:
        a = Inn(owner, name, (sum(random_sample(inflate)) / inflate), rooms,
                quan)
    return a


def create_jewel_shop(owner, rarity, quan, inflate=1):
    name = str(Jeweller()) + " (Jeweller)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  rarity)
    a.fill_store(Jewel, quan)
    return a


def create_restaurant(owner, quan, inflate=1):
    name = str(Restaurant()) + " (Restaurant)"
    if isinstance(inflate, float):
        a = Inn(owner, name, inflate, 0, quan)
    else:
        a = Inn(owner, name, (sum(random_sample(inflate)) / inflate), 0, quan)
    return a


def create_general_store(owner, rarity, quan, trink, inflate=1):
    name = str(GeneralStore()) + " (General)"
    if trink < 0:
        trink = 0
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  rarity)
    a.fill_store(General, quan)
    for _ in range(trink):
        a.Stock.append(General(0, True))
    return a


def create_brothel(owner, quan, inflate=1):
    name = str(Brothel()) + " (Brothel)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, [0, 0])
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  [0, 0])
    a.fill_store(Whore, quan)
    return a


def create_gunsmith(owner, rarity, quan, inflate=1):
    name = str(Gunsmithing()) + ' (Gunsmith)'
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate)) / inflate) + .5,
                  rarity)
    a.fill_store(Firearm, quan)
    return a


if __name__ == '__main__':
    from pprint import pprint
    totals = {}
    cap = 10000
    for i in range(5):
        dice = weapon = largest = average = 0
        smallest = 99999
        for _ in range(cap):
            item = Weapon(i)
            if item.info.index(max(item.info)) == 0:
                weapon += 1
            else:
                dice += 1
            if largest < max(item.info):
                largest = max(item.info)
            elif smallest > min(item.info):
                smallest = min(item.info)
            average += item.Cost
        average /= cap
        totals[i] = {"Dice": dice, "Weapon": weapon, "Max": largest, "Min": smallest, "Average": average / cap}

    pprint(totals)
