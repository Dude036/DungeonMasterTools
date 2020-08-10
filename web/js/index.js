/** @Author: Josh Higham
 **
 */

// Field Variables
var chosen_race = "Human";

// Clear all errors to start the new run
function clear_errors() {
	var areas = document.getElementsByClassName("error");
	for (var i = areas.length - 1; i >= 0; i--) {
		areas[i].innerHTML = "";
	}
}


// Function to Validate the form
function validate() {
	// Cleanup
	clear_errors();

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
	settings["Race"] = chosen_race;
	settings["Population"] = document.getElementById("Population").value;
	settings["Variance"] = document.getElementById("Variance").value;
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


	/*********************/
	/* Validate People   */
	/*********************/
	var raw_people_info = document.getElementById("People_List").value.split('\n');
	settings["Occupations"] = raw_people_info.filter((el) => {
		return el != null && el != "";
	})

	var raw_npc_info = document.getElementById("NPC_List").value.split('\n');
	settings["NPCs"] = raw_npc_info.filter((el) => {
		return el != null && el != "";
	})


	/*********************/
	/* Validate Misc     */
	/*********************/
	generate["Allow Pokemon"] = all_select.Pokemon.value;
	generate["Dump Json"] = all_select.DumpJson.value;

	console.log(settings);
	console.log(generate);
	// If there are no errors, submit everything
	if (correct) { eel.submit(settings, generate); }
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

