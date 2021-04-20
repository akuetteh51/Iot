from stepper import steppingMotor
import stepper
step = steppingMotor(22,21,26,18)
step.stepMode(step.HALF_STEP_FORWARD)
# while True:
#     stepper.clrAll() 
#     stepper.move(400)
#     stepper.waitAfterSteps(500)
#
#while True:
step.move(1000)
step.clrAll()
step.waitAfterSteps(500)
#step .waitAfterSteps(500)
