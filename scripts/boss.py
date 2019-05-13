import bge

MOVEMENT_STEP = 0.025
bge.logic.globalDict['Boss_direction'] = 'DOWN'

def spawn(scene):

    if not 'Boss' in scene.objects:
        scene.addObject('Boss', 'Boss_spawner')

        object_list = scene.objects
        object_list['Boss_HP_bar']['Enabled'] = True
        object_list['Boss_HP_text']['Enabled'] = True

        bge.logic.globalDict['Boss_phase'] = True


def move(controller):
    boss = controller.owner

    if bge.logic.globalDict['Boss_direction'] == 'DOWN':
        if boss.worldPosition.z > -2.2:
            boss.worldPosition.z -= MOVEMENT_STEP

        else:
            bge.logic.globalDict['Boss_direction'] = 'UP'

    else:
        if boss.worldPosition.z < 2.2:
            boss.worldPosition.z += MOVEMENT_STEP

        else:
            bge.logic.globalDict['Boss_direction'] = 'DOWN'


def decrease_life(controller):
    boss_health_bar = controller.owner

    message = controller.sensors["Boss_HP_message"]

    if len(message.bodies) > 0:
        damage = float(message.bodies[0])
        x_scale = float(boss_health_bar.localScale.x)
        new_x_scale = x_scale - damage

        if new_x_scale > 0:
            boss_health_bar.localScale.x = new_x_scale
        else:
            boss_health_bar.localScale.x = 0
            destroy(controller)


def destroy(controller):
    scene = bge.logic.getCurrentScene()

    object_list = scene.objects

    boss_hp_bar = object_list['Boss_HP_bar']
    boss_hp_bar['Enabled'] = False
    boss_hp_bar.localScale.x = 1

    object_list['Boss_HP_text']['Enabled'] = False

    object_list['Boss'].endObject()

    bge.logic.globalDict['Boss_phase'] = False

    bge.logic.sendMessage("enemy_destroyed", '50')
