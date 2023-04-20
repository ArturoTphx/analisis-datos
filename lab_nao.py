# -*- encoding: UTF-8 -*-

import sys
import math

from naoqi import ALProxy
import time

def main(robotIP):
    port = 50574    
    try:
        tts = ALProxy("ALTextToSpeech", "127.0.0.1", port)
        posturasProxy = ALProxy("ALRobotPosture", robotIP, port)
        motion_proxy = ALProxy("ALMotion", robotIP, port)
        posturasProxy.goToPosture("StandInit", 2.0)
        arms = 'Arms'
        legs = 'Legs'
        head = 'Head'
    
        arms_names = motion_proxy.getBodyNames(arms)
        legs_names = motion_proxy.getBodyNames(legs)
        head_names = motion_proxy.getBodyNames(head)
        speed = float(0.1)

        
      
        #entre 0 a 1
        #L viene de left, R viene de right
        #motion_proxy.setAngles(#parte del cuerpo,angulos radianes, velocidad)
        #Los grados son radianes ejemplo 30 grados * pi/180
        
        motion_proxy.moveInit()
        motion_proxy.setAngles(arms_names[0],  -0.6, speed)
        time.sleep(2)
        motion_proxy.setAngles(legs_names[5],  0.2, speed)
        time.sleep(2)
        motion_proxy.setAngles(legs_names[5],  -0.2, speed)
        time.sleep(2)
        motion_proxy.setAngles(head_names[0],  0.5, speed)
        time.sleep(2)
        posturasProxy.goToPosture("StandInit", 2.0)
        tts.say("Listo!")
    except Exception, e:
        print "No se pudo crear conexión con el robot"
        print "El error fue: ", e
    
    posturasProxy.goToPosture("StandInit", 2.0)


if __name__ == "__main__":
    robotIp = "127.0.0.1"
    print "Programacion movimiento de python"
    main(robotIp)
    
