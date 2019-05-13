import bge
import math

def move(controller):
    spaceship = controller.owner

    # Key retrieval
    w_key = controller.sensors['W']
    s_key = controller.sensors['S']
    d_key = controller.sensors['D']
    a_key = controller.sensors['A']

    STEP = 0.1

    # Rotation
    matrix_rotation = spaceship.worldOrientation
    euler_rotation = matrix_rotation.to_euler()
    ROTATION_STEP = math.radians(4)
    MAX_ROTATION = math.radians(25)

    if w_key.positive and spaceship.worldPosition.z < 3.5 :
        spaceship.worldPosition.z += STEP

        if euler_rotation.x > -MAX_ROTATION:
            euler_rotation.x -= ROTATION_STEP

    if s_key.positive and spaceship.worldPosition.z > -3.5:
        spaceship.worldPosition.z -= STEP

        if euler_rotation.x < MAX_ROTATION:
            euler_rotation.x += ROTATION_STEP

    # reset the X rotation
    if not s_key.positive and not w_key.positive and euler_rotation.x != 0:
        if euler_rotation.x > 0:
            if euler_rotation.x < ROTATION_STEP:
                euler_rotation.x = 0
            else:
                euler_rotation.x -= ROTATION_STEP
        else:
            euler_rotation.x += ROTATION_STEP

    if a_key.positive and spaceship.worldPosition.x > -6:
        spaceship.worldPosition.x -= STEP

        if euler_rotation.z > -MAX_ROTATION:
            euler_rotation.z -= ROTATION_STEP

    if d_key.positive and spaceship.worldPosition.x < 4:
        spaceship.worldPosition.x += STEP

        if euler_rotation.z < MAX_ROTATION:
            euler_rotation.z += ROTATION_STEP

    # reset the Z rotation
    if not a_key.positive and not d_key.positive and euler_rotation.z != 0:
        if euler_rotation.z > 0:
            if euler_rotation.z < ROTATION_STEP:
                euler_rotation.z = 0
            else:
                euler_rotation.z -= ROTATION_STEP
        else:
            euler_rotation.z += ROTATION_STEP

    spaceship.worldOrientation = euler_rotation.to_matrix()


def reduce_life(controller):
    health_bar = controller.owner

    message = controller.sensors["Health_message"]

    if len(message.bodies) > 0:
        lost_life = float(message.bodies[0]) # betweeen 0 and 1

        x_scale = float(health_bar.localScale.x) # between 0 and 1
        print(x_scale)
        new_x_scale = x_scale - lost_life

        if new_x_scale > 0:
            health_bar.localScale.x = new_x_scale
        else:
            health_bar.localScale.x = 0
            # game over
