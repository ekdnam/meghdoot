import time


class PID:
    def __init__(self, uBias: float = 0, kP: float = 0, kI: float = 0, kD: float = 0):
        self.uBias = uBias
        self.kP = kP
        self.kI = kI
        self.kD = kD

        self.controllerOutput = 0

        self.prevError = 0

        self.prevTime = time.time()

        self.tP = 0
        self.tI = 0
        self.tD = 0

    def setTime(self) -> None:
        self.prevTime = time.time()
        self.currTime = self.prevTime

    def runPID(self, error: float, sleep: float = 0.2) -> float:
        time.sleep(sleep)

        self.currTime = time.time()

        deltaError = error - self.prevError
        deltaTime = self.currTime - self.prevTime

        self.tP = error

        self.tI += self.tP * deltaTime

        if deltaTime > 0:
            self.tD = deltaError / deltaTime
        else:
            self.tD = 0

        self.prevError = error
        self.prevTime = self.currTime

        self.controllerOutput = (
            self.uBias + self.kP * self.tP + self.kI * self.tI + self.kD * self.tD
        )

        return self.controllerOutput
