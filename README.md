# DungeonMasterTools
A collection of Python scripts to remove tedium from being a dungeon master. This tool is useful for Pathfinder as of now, but I plan on making it just as useful for D&amp;D 5e.

### Installing 
First, you'll need to install *Python 3* and *pip*. Once you have *pip* installed, you'll want to run the following command. This command with install all necessary requirements to run this application. 

    pip install -r requirements.txt


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
