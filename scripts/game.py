import bge

from . import boss

bge.logic.globalDict['Music'] = True

POINTS_TO_BOSS = 300

def menu(controller):
	scene = bge.logic.getCurrentScene()

	up     = controller.sensors['Up']
	down   = controller.sensors['Down']
	select = controller.sensors['Select']

	sound = controller.actuators['Sound']

	spaceship = controller.owner
	start_y_position = 0
	exit_y_position  = -3

	if down.positive and spaceship.worldPosition.y == start_y_position:
		spaceship.worldPosition.y -= 3
		controller.activate(sound)

	if up.positive and spaceship.worldPosition.y == exit_y_position:
		spaceship.worldPosition.y += 3
		controller.activate(sound)

	if select.positive:
		if spaceship.worldPosition.y == start_y_position:
			scene.replace('Game')

		if spaceship.worldPosition.y == exit_y_position:
			bge.logic.endGame()


def add_points(controller):
	text_points = controller.owner

	message = controller.sensors["Points_message"]
	bge.logic.getCurrentController().actuators['Explosion_sound'].startSound()

	if len(message.bodies) > 0:
		points_to_add = int(message.bodies[0])

		current_points = int(text_points['Text'])
		current_points += points_to_add
		text_points['Text'] = current_points

		if current_points % POINTS_TO_BOSS == 0:
			scene = bge.logic.getCurrentScene()
			boss.spawn(scene)


def load_points(controller):
	text_points = controller.owner

	if 'Points' in bge.logic.globalDict:
		text_points['Text'] = bge.logic.globalDict['Points'] + ' POINTS'


def restart(controller):
	bge.logic.getCurrentScene().replace('Game')


def exit(controller):
    bge.logic.endGame()


def load_menu(controller):
	bge.logic.getCurrentScene().replace('Menu')


def play_music(controller):
	if bge.logic.globalDict['Music'] == True:
		music = bge.logic.getCurrentController().actuators['Music']
		music.startSound()


def toggle_music(controller):
	music = bge.logic.getCurrentController().actuators['Music']

	bge.logic.globalDict['Music'] = not bge.logic.globalDict['Music']

	if bge.logic.globalDict['Music']:
		music.startSound()

	else:
		music.stopSound()
