/** @Author: Josh Higham
 **
 */

// Field Variables
var chosen_race = "Human";
var normal_types = [
	"Weapon",
	"Armor",
	"Potion",
	"Enchant",
	"Enchanter",
	"Jewel",
	"Guns",
]
var normal_rarity = [ 4, 4, 9, 9, 9, 5, 4 ]

var odd_types = [
	"Books",
	"Tavern",
	"Food",
	"General",
	"Brothel",
	"Variety",
	"Quest",
]

var generate_names = {
	"Weapon": "Weapon Shops",
	"Armor": "Armor Shops",
	"Potion": "Potion Shops",
	"Enchant": "Enchant Shops",
	"Enchanter": "Enchanter Shops",
	"Jewel": "Jewel Shops",
	"Guns": "Gunsmiths",
	"Books": "Book Shops",
	"Tavern": "Tavern Shops",
	"Food": "Food Shops",
	"General": "General Shops",
	"Brothel": "Brothels",
	"Variety": "Variety",
	"Quest": "Quest Boards",
}


// Validate Normal Stores
function normal(name, rarity) {
	// Setup base to eventually modify
	var correct = true;
	var errors = "";

	// Validate Rarity
	var r_low  = parseInt(document.getElementById(name + "RarityLow").value);
	var r_high = parseInt(document.getElementById(name + "RarityHigh").value);
	if (r_low > r_high) {
		correct = false;
		errors += "Rarity Low is higher than Rarity High. ";
	}
	if (r_low > rarity) {
		correct = false;
		errors += "Rarity Low cannot exceed " + rarity + ". ";
	}
	if (r_high > rarity) {
		correct = false;
		errors += "Rarity High cannot exceed " + rarity + ". ";
	}

	// Validate Quantity
	var q_low  = parseInt(document.getElementById(name + "QuantityLow").value);
	var q_high = parseInt(document.getElementById(name + "QuantityHigh").value);
	if (q_low > q_high) {
		correct = false;
		errors += "Quantity Low is higher than Quantity High. ";
	}

	// Validate Inflation
	var check = document.getElementById(name + "Exact").checked;
	var inflate  = parseFloat(document.getElementById(name + "Inflation").value);
	if (check) {
		inflate /= 100
	} else {
		inflate = Math.floor(inflate / 100);
	}

	// Accumulate into JSON object
	var base = {
        "# of Stores": parseInt(document.getElementById(name + "Stores").value),
        "Rarity Low": r_low,
        "Rarity High": r_high,
        "Quantity Low": q_low,
        "Quantity High": q_high,
        "Inflation": inflate
	};

	if (name == "Weapon" || name == "Armor" || name == "Guns") {
		base["Additional Traits"] = parseInt(document.getElementById(name + "AdditionalTraits").value);
	}
	
	// Update Error Codes and return
	document.getElementById(name + "Error").innerHTML = errors;
	return correct ? base : null;
}


// Validate Odd Stores
function odd(name) {
	var base = {
        "# of Stores": parseInt(document.getElementById(name + "Stores").value),
	};
	var correct = true;
	var errors = "";
	switch(name) {
		case "General":
			base["Trinkets"] = parseInt(document.getElementById(name + "Trinkets").value);
			var r_low  = parseInt(document.getElementById(name + "RarityLow").value);
			var r_high = parseInt(document.getElementById(name + "RarityHigh").value);
			if (r_low > r_high) {
				correct = false;
				errors += "Rarity Low is higher than Rarity High. ";
			}
			base["Rarity Low"] = parseInt(document.getElementById(name + "RarityLow").value);
			base["Rarity High"] = parseInt(document.getElementById(name + "RarityHigh").value);

		case "Tavern":
			base["Rooms"] = parseInt(document.getElementById(name + "Rooms").value);

		case "Books":
		case "Food":
		case "Brothel":
		case "Variety":
			var q_low  = parseInt(document.getElementById(name + "QuantityLow").value);
			var q_high = parseInt(document.getElementById(name + "QuantityHigh").value);
			if (q_low > q_high) {
				correct = false;
				errors += "Quantity Low is higher than Quantity High. ";
			}
			
			// Validate Inflation
			var check = document.getElementById(name + "Exact").checked;
			var inflate  = parseFloat(document.getElementById(name + "Inflation").value);
			if (check) {
				inflate /= 100
			} else {
				inflate = Math.floor(inflate / 100);
			}
			base["Quantity Low"] = q_low
			base["Quantity High"] = q_high
			base["Inflation"] = inflate
			break;

		case "Quest":
			var l_low  = parseInt(document.getElementById(name + "LevelLow").value);
			var l_high = parseInt(document.getElementById(name + "LevelHigh").value);
			if (l_low > l_high) {
				correct = false;
				errors += "Level Low is higher than Level High. ";
			}

			base["Level Low"] = l_low;
			base["Level High"] = l_high;
			base["Quantity"] = parseInt(document.getElementById(name + "Quantity").value);
			break;
	}
	if (name == "General") {
		delete base["Rooms"];
	} else if (name == "Tavern") {
		delete base["Rarity High"];
		delete base["Rarity Low"];
	}

	document.getElementById(name + "Error").innerHTML = errors;
	return correct ? base : null;
}


// Function to Validate the form
function validate() {
	// Generate basic Info
	var settings = {};
	var generate = {};

	// Sentinel to how everything should be handled
	var correct = true;

	// All input values
	const all_select = document.getElementsByTagName("select");
	const all_inputs = document.getElementsByTagName("input");

	/*********************/
	/* Validate Settings */
	/*********************/
	settings["System"] = document.getElementById("System").value;
	settings["Race"] = chosen_race;
	settings["Population"] = parseInt(document.getElementById("Population").value);
	settings["Variance"] = parseInt(document.getElementById("Variance").value);
	var exotic_list = [];

	for (var i = all_inputs.length - 1; i >= 0; i--) {
		if (all_inputs[i].type == "checkbox" && all_inputs[i].checked && all_inputs[i].value !== "on") {
			exotic_list.push(all_inputs[i].value);
		}
	}
	settings["Exotic"] = exotic_list;


	/*********************/
	/* Validate Stores   */
	/*********************/
	// Normal generations
	for (var i = normal_types.length - 1; i >= 0; i--) {
		var ret = normal(normal_types[i], normal_rarity[i]);
		if (!ret) {
			correct = false;
		} else {
			generate[generate_names[normal_types[i]]] = ret;
		}
	}

	// Odd generators
	for (var i = normal_types.length - 1; i >= 0; i--) {
		var ret = odd(odd_types[i]);
		if (!ret) {
			correct = false;
		} else {
			generate[generate_names[odd_types[i]]] = ret;
		}
	}

	/*********************/
	/* Validate People   */
	/*********************/
	var raw_people_info = document.getElementById("People_List").value.split('\n');
	generate["Occupations"] = raw_people_info.filter((el) => {
		return el != null && el != "";
	})

	var raw_npc_info = document.getElementById("NPC_List").value.split('\n');
	generate["NPCs"] = raw_npc_info.filter((el) => {
		return el != null && el != "";
	})


	/*********************/
	/* Validate Misc     */
	/*********************/
	generate["Allow Pokemon"] = all_select.Pokemon.value;
	generate["Dump Json"] = all_select.DumpJson.value;
	generate["Town Name"] = document.getElementById('TownName').value;

	console.log(settings);
	console.log(generate);
	// If there are no errors, submit everything
	if (correct) {
		eel.submit(settings, generate);
	}

	// document.getElementById("wholeForm").style.display = 'none';
	document.getElementById("mainHeader").innerHTML = 'Form Submitted.';
}


// Make the chosen race unselectable as exotic
function changing_races() {
	// Get new Race
	const new_race_name = document.getElementById("Race").value;
	var inputs = document.getElementsByTagName("input");
	var new_race = null;
	for (var i = inputs.length - 1; i >= 0; i--) {
		if (new_race_name == inputs[i].id) {
			new_race = inputs[i];
			break;
		}
	}

	// Disable new base race
	new_race.setAttribute("disabled", true);
	new_race.checked = false;

	// Make the old race available to add
	var old_race = document.getElementById(chosen_race);
	old_race.removeAttribute("disabled");
	chosen_race = new_race.id;
}


// Show/Hide all of the exotic race pickings
function show_hide(ident){
  var a = document.getElementById(ident);
  if (a.style.display === 'none') {
    a.style.display = 'block';
  } else {
    a.style.display = 'none';
  }
}

