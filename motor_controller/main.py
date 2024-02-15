from motor import Motor
from controller import Controller
from sensor import Sensor
from system import System

pid = Controller("pid")
bldc = Motor("bldc")
posSensor = Sensor("pos")
currentSensor = Sensor("current")

pid.connectOutput(bldc)
bldc.connectOutput(posSensor)
bldc.connectOutput(currentSensor)
posSensor.connectOutput(pid)
currentSensor.connectOutput(pid)

sys = System("system", [pid, bldc, posSensor, currentSensor])