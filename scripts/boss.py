import bge

MOVEMENT_STEP = 0.025
bge.logic.globalDict['Boss_direction'] = 'DOWN'

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
