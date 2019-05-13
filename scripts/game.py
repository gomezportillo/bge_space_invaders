import bge

def menu(controller):
	scene = bge.logic.getCurrentScene()

	up     = controller.sensors['Up']
	down   = controller.sensors['Down']
	select = controller.sensors['Select']

	sound = controller.actuators['Sound']

	spaceship = controller.owner
	start_y_position = 0
	exit_y_position  = -2

	if down.positive and spaceship.worldPosition.y == start_y_position:
		spaceship.worldPosition.y -= 2
		controller.activate(sound)

	if up.positive and spaceship.worldPosition.y == exit_y_position:
		spaceship.worldPosition.y += 2
		controller.activate(sound)

	if select.positive:
		if spaceship.worldPosition.y == start_y_position:
			scene.replace('Game')

		if spaceship.worldPosition.y == exit_y_position:
			bge.logic.endGame()


def add_points(controller):
	text_points = controller.owner

	message = controller.sensors["Points_message"]

	if len(message.bodies) > 0:
		points_to_add = int(message.bodies[0])

		current_points = int(text_points['Text'])
		current_points += points_to_add
		text_points['Text'] = current_points
