import vrep as v


class PioneerAsync:
    def __init__(self, client_id):
        self.clientID = client_id
        error, self.left_motor = v.simxGetObjectHandle(self.clientID, 'Pioneer_p3dx_leftMotor', v.simx_opmode_blocking)
        error, self.right_motor = v.simxGetObjectHandle(self.clientID, 'Pioneer_p3dx_rightMotor', v.simx_opmode_blocking)

    def set_motors(self, left_speed, right_speed):
        v.simxSetJointTargetVelocity(self.clientID, self.left_motor, left_speed, v.simx_opmode_oneshot)
        v.simxSetJointTargetVelocity(self.clientID, self.right_motor, right_speed, v.simx_opmode_oneshot)

