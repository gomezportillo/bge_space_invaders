import bge
import random

random.seed(123)

def spawn_enemy(controller):
	spawner = controller.owner
	scene = bge.logic.getCurrentScene()

    # random Z position
	spawner.worldPosition.z = random.uniform(3, -3)

	scene.addObject("Enemy", "Enemy_spawner", 350)

def collision(controller):
	enemy = controller.owner

	enemy.sendMessage("enemy_destroyed", "10")
	enemy.endObject()
