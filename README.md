# DungeonMasterTools
A collection of Python scripts to remove tedium from being a dungeon master. This tool is useful for Pathfinder as of now, but I plan on making it just as useful for D&amp;D 5e.

### Installing 
First, you'll need to install *Python 3* and *pip*. Once you have *pip* installed, you'll want to run the following command. This command with install all necessary requirements to run this application. 

    pip install -r requirements.txt

_Window's Users_: You may have to modify the above command with the ```--user``` argument if not under an admin account.

### Running the Application

There are two setting files right now. Settings.json contains the settings for creating the town's population. The four lines in the file are as such;

    "Race": "Human", [The main race from the town. (Any race from the PFSRD)]
    "Population": 5000, [The population of town. (1 to infinite)]
    "Variance": 10, [The degree of change from the main race to all other races. (0% to 100%)]
    "Exotic": 5 [The amount of other races in the town. (0 to 32)]

**Generate.json** contains all the information about the town. Some stores have unique aspects, but each setting explains itself. The last two categories in the JSON are "NPCs" and "Occupations". The difference between the two is that "NPCs" have weapons and stats, while the "Occupation" doesn't. 

These two should contain the name of the position. They will be filled with people based on the **settings.json** file.

Inflation is compatible with both floats and integers. Floats with mean it's exact Percentage of inflation, 1.0 == 100%. An integer will mean some arbitrary amount. The higher the number, the more nominal it will be.

Below has the initial settings file with brackets after. Inside the brackets is the possible range of each setting.

    "Weapon Shops": {
        "# of Stores": 2,       // [0 to Infinte]
        "Rarity Low": 0,        // [0 to 4]
        "Rarity High": 4,       // [Rarity Low to 4]
        "Quantity Low": 15,     // [0 to Infinte]
        "Quantity High": 25,    // [Quantity Low to Infinte]
        "Inflation": 1          // [0.0 to Infinte]
    },
    "Armor Shops": {
        "# of Stores": 2,       // [0 to Infinte]
        "Rarity Low": 0,        // [0 to 4]
        "Rarity High": 4,       // [Rarity Low to 4]
        "Quantity Low": 15,     // [0 to Infinte]
        "Quantity High": 25,    // [Quantity Low to Infinte]
        "Inflation": 1          // [0.0 to Infinte]
    },
    "Potion Shops": {
        "# of Stores": 1,       // [0 to Infinite]
        "Rarity Low": 0,        // [0 to 9]
        "Rarity High": 9,       // [Rarity Low to 9]
        "Quantity Low": 15,     // [0 to Infinte]
        "Quantity High": 20,    // [Quantity Low to Infinte]
        "Inflation": 1          // [0.0 to Infinite]
    },
    "Enchant Shops": {
        "# of Stores": 1,       // [0 to Infinite]
        "Rarity Low": 0,        // [0 to 9]
        "Rarity High": 9,       // [Rarity Low to 9]
        "Quantity Low": 15,     // [0 to Infinte]
        "Quantity High": 20,    // [Quantity Low to Infinte]
        "Inflation": 1          // [0.0 to Infinite]
    },
    "Enchanter Shops": {
        "# of Stores": 1,       // [0 to Infinite]
        "Rarity Low": 0,        // [0 to 9]
        "Rarity High": 9,       // [Rarity Low to 9]
        "Quantity Low": 15,     // [0 to Infinte]
        "Quantity High": 20,    // [Quantity Low to Infinte]
        "Inflation": 1          // [0.0 to Infinite]
    },
    "Book Shops": {
        "# of Stores": 1,       // [0 to Infinite]
        "Quantity Low": 15,     // [0 to Infinite]
        "Quantity High": 25,    // [Quantity Low to Infinite]
        "Inflation": 1          // [0.0 to Infinite]
    },
    "Tavern Shops": {
        "# of Stores": 1,       // [0 to Infinite]
        "Rooms": 3,             // [0 to Infinite]
        "Quantity Low": 10,     // [0 to Infinite]
        "Quantity High": 15,    // [Quantity Low to Infinite]
        "Inflation": 1          // [0.0 to Infinite]
    },
    "Jewel Shops": {
        "# of Stores": 2,       // [0 to Infinte]
        "Rarity Low": 0,        // [0 to 5]
        "Rarity High": 4,       // [Rarity Low to 5]
        "Quantity Low": 15,     // [0 to Infinte]
        "Quantity High": 25,    // [Quantity Low to Infinte]
        "Inflation": 1          // [0.0 to Infinte]
    },
    "Food Shops": {
        "# of Stores": 1,       // [0 to Infinite]
        "Quantity Low": 15,     // [0 to Infinite]
        "Quantity High": 30,    // [Quantity Low to Infinite]
        "Inflation": 1          // [0.0 to Infinite
    },
    "General Shops": {
        "# of Stores": 1,       // [0 to Infinite]
        "Rarity Low": 0,        // [0 to Infinite]
        "Rarity High": 3,       // [Rarity High to Infinite]
        "Quantity Low": 30,     // [0 to Infinite]
        "Quantity High": 40,    // [Rarity Low to Infinite]
        "Trinkets": 2,          // [0 to Infinite]
        "Inflation": 1          // [0.0 to Infinite]
    },
    "Brothels": {
        "# of Stores": 1,       // [0 to Infinite]
        "Quantity Low": 15,     // [0 to Infinite]
        "Quantity High": 20,    // [Quantity Low to Infinite]
        "Inflation": 1          // [0.0 to Infinite]
    },
    "Gunsmiths": {
        "# of Stores": 1,       // [0 to Infinte]
        "Rarity Low": 0,        // [0 to 4]
        "Rarity High": 4,       // [Rarity Low to 4]
        "Quantity Low": 15,     // [0 to Infinte]
        "Quantity High": 20,    // [Quantity Low to Infinte]
        "Inflation": 1          // [0.0 to Infinte]
    },
    "Quest Boards": {
        "# of Stores": 1,       // [0 to Infinte]
        "Level Low": 0,         // [0 to 20]
        "Level High": 5,        // [Level Low to 20]
        "Quantity": 10          // [0 to Infinite]
    },
    "Occupations": [            // Encapsulate with "", and seperate with ,
        "The King",
        "The Cleric"
    ],
    "NPCs": [                   // Encapsulate with "", and seperate with ,
        "Captain of the Guard",
        "The Villain"
    ]

After you've modified your settings, run the main application to generate a town. There are a few testing protocols that can be run that I have used for testing. Here are those;

| File               | Purpose       |
| ------------------ | ------------- |
| beastiary.py       | Build all monsters into the beasts folder to verify they all look fine. |
| name_generator.py  | Generate several names of each possible race to verify sound and error check names. |
| PC.py              | Print to the console a Playable character in HTML. |
| quests.py          | Generate a threaded task to average out several thousand quest rewards from level 1 to 55. **WARNING:** This will take a VERY long time and heat up your computer immensely. I do NOT recommend you do this. |
| test_scripts.py    | Unit Tests to verify all things are working correctly. |
| town_generator.py  | Generate a Sample town. |
| treasure.py        | Generate solely the treasure from a monster based on CR or on the name of the Monster. |

### Contributing

If you're interesting in contributing to this repository, I'm currently trying to get a character generator fully flushed out. I need to get all the data HTML friendly for basically all the classes in both Pathfinder and D&D 5e. The files that need those are `5e_class_feats.json` and `pathfinder_class_feats.json`.

The next big task is to get settings files setup for generating things for D&D and Pathfinder. D&D doesn't have canon rules for weapon creation, so that may be a little difficult to determine the best course of action.

I would also like to refactor some code, so `stores.py` isn't so bloated.

I'd also like to rework weapon damage types. Adding potentially different damage types, and add some variation on material. i.e. Hot Siccate should also deal fire damage for an average half if it's damage.