const scene = document.querySelector('#scene');

// Change the number of device when user moves the slider
const numDiceInput = document.querySelector('input[name="numDice"]');
function updateNumDice(value = null) {
	// Determine old and new values
	const oldNumDice = scene.children.length;
	const newNumDice = parseInt(value == null ? numDiceInput.value : value, 10);


	// Hint for CSS
	scene.dataset.diceNum = newNumDice;

	// Save configuration
	localStorage.setItem('numDice', newNumDice);
}
//numDiceInput.addEventListener('change', () => updateNumDice());
updateNumDice(localStorage.getItem('numDice'));

// Save/load sound option
const soundCheckbox = document.querySelector('input[name="sound"]');
function setSoundOption(value = null) {
	const newValue = value == null ? soundCheckbox.checked : value;
	soundCheckbox.checked = newValue;
	localStorage.setItem('sound', newValue ? 'true' : 'false');
}
soundCheckbox.addEventListener('change', () => setSoundOption(soundCheckbox.checked));
setSoundOption(localStorage.getItem('sound') === 'true');

// Roll the dice
let rollCount = 0;
const sound = document.querySelector('#sound');
const rollButton = document.querySelector('#roll');

function roll() {
	scene.dataset.rollCountMod5 = ++rollCount % 5;
	const rolls = [];
	for (const die of scene.querySelectorAll('.die')) {
		const roll = Math.floor(Math.random() * 6) + 1;
		rolls.push(roll);
		die.dataset.result = roll;
	}

	contHouses = rolls;

	return rolls[0];

	addToHistory(rolls);

}
scene.addEventListener('click', roll);


// Update roll history
const rollHistoryList = document.querySelector('#history ol');

function addToHistory(rolls) {

	console.log(rolls[0]);

	
}

// Change the visual number style on the dice when the user changes the option
function updateNumberStyle(value = null) {
	const newValue = value == null ? document.querySelector('input[name="numberStyle"]:checked').value : value;
	scene.dataset.numberStyle = newValue;
	document.querySelector(`input[name="numberStyle"][value="${newValue}"]`).checked = true;
	localStorage.setItem('numberStyle', newValue);
}
for (const radio of document.querySelectorAll('input[name="numberStyle"]')) {
	radio.addEventListener('change', () => updateNumberStyle());
}
updateNumberStyle(localStorage.getItem('numberStyle'));

// Go to fullscreen mode on user command
const fullscreenButton = document.querySelector('#fullscreen');
const fullscreenArea = document.querySelector('#fullscreenArea');


// Handle shake-to-roll
const shakeCheckbox = document.querySelector('input[name="shake"]');
if (window.DeviceMotionEvent) {
	const ACCELERATION_THRESHOLD_RANGE = [8, 14];
	const ROTATION_THRESHOLD_RANGE = [40, 80];
	const TURNS_PER_SECOND_THRESHOLD = 5;
	const SHAKE_COOLOFF = 1e3;

	let lastShakeTime = null;
	let noMotionTimeout;

	const turns = {
		// Changes of linear acceleration direction
		x: [],
		y: [],
		z: [],

		// Changes of rotation direction
		alpha: [],
		beta: [],
		gamma: [],
	};

	function handleMotion(event) {
		const time = new Date();
		const minTime = time - 1e3;

		clearTimeout(noMotionTimeout);

		// See if we've changed direction in any of the six dimensions
		for (const [dim, value, thresholdRange] of [
			['x', event.acceleration.x, ACCELERATION_THRESHOLD_RANGE],
			['y', event.acceleration.y, ACCELERATION_THRESHOLD_RANGE],
			['z', event.acceleration.z, ACCELERATION_THRESHOLD_RANGE],
			['alpha', event.rotationRate.alpha, ROTATION_THRESHOLD_RANGE],
			['beta', event.rotationRate.alpha, ROTATION_THRESHOLD_RANGE],
			['gamma', event.rotationRate.gamma, ROTATION_THRESHOLD_RANGE]
		]) {
			// Abort if it's outside the threshold range
			if (Math.abs(value) < thresholdRange[0] || Math.abs(value) > thresholdRange[1]) continue;

			// Abort if direction is the same as the last recording
			if (turns[dim].length > 0) {
				const prevValue = turns[dim][turns[dim].length - 1].value;
				if (value > 0 && prevValue > 0 || value < 0 && prevValue < 0) {
					// Same direction
					continue;
				}
			}

			// Remove old or irrelevant direction changes
			if (turns[dim].length > TURNS_PER_SECOND_THRESHOLD) {
				turns[dim] = turns[dim].slice(-TURNS_PER_SECOND_THRESHOLD);
			}
			for (let i = turns[dim].length - 1; i >= 0; i--) {
				if (turns[dim][i].time <= minTime) {
					turns[dim] = turns[dim].slice(i);
					break;
				}
			}

			// Log the direction change
			turns[dim].push({
				time,
				value,
			});

			// Has it been long enough since the last shake?
			if (lastShakeTime != null && time - lastShakeTime < SHAKE_COOLOFF) continue;

			// Have we shaken fast enough?
			if (turns[dim].length > TURNS_PER_SECOND_THRESHOLD) {
				roll();
				lastShakeTime = time;
				break;
			}
		}
	}

	function setRollOnShakeOption(value) {
		shakeCheckbox.checked = value;
		if (value) {
			window.addEventListener('devicemotion', handleMotion);

			// If we don't get any motion event within a short time,
			// likely it isn't supported after all
			noMotionTimeout = setTimeout(() => {
				shakeNotSupported();
				window.removeEventListener('devicemotion', handleMotion);
			}, 1e3);
		} else {
			clearTimeout(noMotionTimeout);
			window.removeEventListener('devicemotion', handleMotion);
		}
		localStorage.setItem('shake', value ? 'true' : 'false');
	}
	shakeCheckbox.addEventListener('change', () => setRollOnShakeOption(shakeCheckbox.checked));
	setRollOnShakeOption(localStorage.getItem('shake') === 'true');
} else {
	// Motion not supported; advise the user
	shakeNotSupported();
}
function shakeNotSupported() {
	shakeCheckbox.disabled = true;
	shakeCheckbox.closest('li').append(" (not available on this browser)");
}
