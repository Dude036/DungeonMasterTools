# DungeonMasterTools
A collection of Python scripts to remove tedium from being a dungeon master. This tool is useful for Pathfinder as of now, but I plan on making it just as useful for D&amp;D 5e.

### Installing 
First, you'll need to install *Python 3* and *pip*. Once you have *pip* installed, you'll want to run the following command. This command with install all necessary requirements to run this application. 

    pip install -r requirements.txt


### Running the Application

There are two setting files right now. Settings.txt contains the settings for creating the town's population. The four lines in the file are as such;

    1: Base population. I used all possible races from Pathfinder's SRD
    2: Population Size. Range: [1, Infinite). 
    3: Core Population Variance. Range: [0, 100] | 0 = No population Varience, 100 = All Diverse Races
    4: Exotic Populations. Range: [0, 32] | 0 = No Exotic Races, 32 = All Exotic Races


Generate.txt has all the information about the town. Every store has some unique aspects. Once the ten lines are filled out, you may add as many lines contianing at least a single letter for positions of notoriety in your town. Inflation is compatible with both floats and integers. Floats with mean it's exact Percentage of inflation, 1.0 == 100%. An integer will mean some arbitraty amount. The higher the number, the more nominal it will be.

    1: Write Weapon Shop(s) 
        [# of Stores (0 to infinite), Rarity Low (0 to 4), Rarity High (Rarity Low+1 to 4), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    2: Write Armor Shop(s) 
        [# of Stores (0 to infinite), Rarity Low (0 to 4), Rarity High (Rarity Low+1 to 4), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    3: Write Potion Shop(s) 
        [# of Stores (0 to infinite), Rarity Low (0 to 9), Rarity High (Rarity Low+1 to 9), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    4: Write Enchant Shop(s) 
        [# of Stores (0 to infinite), Rarity Low (0 to 9), Rarity High (Rarity Low+1 to 9), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    5: Write Enchanter Shop(s) 
        [# of Stores (0 to infinite), Rarity Low (0 to 9), Rarity High (Rarity Low+1 to 9), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    6: Write Book Shop(s) 
        [# of Stores (0 to infinite), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    7: Write Tavern Shop(s) 
        [# of Stores (0 to infinite), Rarity (0 to infinite), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    8: Write Jewel Shop(s) 
        [# of Stores (0 to infinite), Rarity Low (0 to 5), Rarity High (Rarity Low+1 to 5), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite, Inflation (0.00 to infinite))]
    9: Write Food Shop(s) 
        [# of Stores (0 to infinite), Rarity (0 to infinite), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    10: Write General Shop(s) 
        [# of Stores (0 to infinite), Rarity Low (0 to 3), Rarity High (Rarity Low+1 to 3), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite), Trinkets (0 to infinite), Inflation (0.00 to infinite)]
    11: White Brothel(s)
        [# of Stores (0 to infinite), Rarity Low (0 to 3), Rarity High (Rarity Low+1 to 3), Quantity Low (0 to infinite), Quantity High (Quantity Low+1 to infinite), Inflation (0.00 to infinite)]
    12+: Town Positions - Create notable people with a certain profession in the town.


