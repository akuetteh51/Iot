from machine import Pin as p
import time


class Steppa:
    mode=""
    SINGLE_PHASE_FORWARD = 0
    SINGLE_PHASE_BACKWARD = 1
    DOUBLE_PHASE_FORWARD = 2
    DOUBLE_PHASE_BACKWARD = 3
    HALF_STEP_FORWARD = 4
    HALF_STEP_BACKWARD = 5
    modevale=["SINGLE_PHASE_FORWARD","SINGLE_PHASE_BACKWARD","DOUBLE_PHASE_FORWARD","DOUBLE_PHASE_BACKWARD","HALF_STEP_FORWARD","HALF_STEP_BACKWARD","0","1","2","3","4"]
    _PHASE1=22
    _PHASE2=21
    _PHASE3=26
    _PHASE4=18
    
    
     
    def __init__(self,p1=_PHASE1,p2=_PHASE2,p3=_PHASE3,p4=_PHASE4) :
        self.p1 = p(p1, p.OUT)
        self.p2 = p(p2, p.OUT)
        self.p3 = p(p3, p.OUT)
        self.p4 = p(p4, p.OUT)
        self.SinglePhaseForward=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        self.SinglePhaseBackward=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
        self.DoublePhaseForward=[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
        self.DoublePhaseBackward=[[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]
        
        
        self.HalfStepFforward =[

            [1,0,0,0],

            [1,1,0,0],

            [0,1,0,0],

            [0,1,1,0],

            [0,0,1,0],

            [0,0,1,1],

            [0,0,0,1],

            [1,0,0,1]

            ]

       

        self.HalfStepBack = [

            [1,0,0,1],

            [1,0,0,0],

            [1,1,0,0],

            [0,1,0,0],

            [0,1,1,0],

            [0,0,1,0],

            [0,0,1,1],

            [0,0,0,1]

            ]
        
    
    def halfStepBack(self,noOfSteps):
        

        for i in range(self.noOfSteps):
            for s in range(8):
#              
                self.p1.value(self.HalfStepBack[s][0])
                self.p2.value(self.HalfStepBack[s][1])
                self.p3.value(self.HalfStepBack[s][2])
                self.p4.value(self.HalfStepBack[s][3])
                time.sleep_ms(50)
                
    def halfStepforward(self,noOfSteps):
        
        for i in range(self.noOfSteps):
            for s in range(8):            
                self.p1.value(self.HalfStepFforward[s][0])
                self.p2.value(self.HalfStepFforward[s][1])
                self.p3.value(self.HalfStepFforward[s][2])
                self.p4.value(self.HalfStepFforward[s][3])
                time.sleep_ms(50)
                
    def SinglePhase_backward(self,noOfSteps):
       

        for i in range(self.noOfSteps):
            for s in range(4):            
                self.p1.value(self.SinglePhaseBackward[s][0])
                self.p2.value(self.SinglePhaseBackward[s][1])
                self.p3.value(self.SinglePhaseBackward[s][2])
                self.p4.value(self.SinglePhaseBackward[s][3])
                time.sleep_ms(100)
                
    def DoublePhase_forward(self,noOfSteps):
        

        for i in range(self.noOfSteps):
            for s in range(4):            
                self.p1.value(self.DoublePhaseForward[s][0])
                self.p2.value(self.DoublePhaseForward[s][1])
                self.p3.value(self.DoublePhaseForward[s][2])
                self.p4.value(self.DoublePhaseForward[s][3])
                time.sleep_ms(100)

    def DoublePhase_backward(self,noOfSteps):
        

        for i in range(self.noOfSteps):
            for s in range(4):            
                self.p1.value(self.DoublePhaseBackward[s][0])
                self.p2.value(self.DoublePhaseBackward[s][1])
                self.p3.value(self.DoublePhaseBackward[s][2])
                self.p4.value(self.DoublePhaseBackward[s][3])
                time.sleep_ms(100)
    def stepMode(self,mode=None):
        if self.mode not in Steppa.modevale:
            print("you need to Enter A value from the list of mode")
            print(Steppa.modevale)
            
    def move(self,noOfSteps):
        #global self.noOfSteps
        return self.noOfSteps
        

stepper=Steppa()
stepper.mode(0)
# stepper.mode(DoublePhase_forward)
#stepper.halfStepBack(233)
#stepper.halfStepforward(255)
#stepper.SinglePhaseforward(255)
#stepper.SinglePhase_backward(255)
#stepper.DoublePhase_forward(255)
# stepper.DoublePhase_backward(255)
