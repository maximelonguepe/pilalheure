from adafruit_servokit import ServoKit


def enclencher_servo_remplissage_bas(numero_servo):
    kit = ServoKit(channels=16)
    kit.servo[numero_servo].angle = 120


def enclencher_servo_remplissage_haut(numero_servo):
    kit = ServoKit(channels=16)
    kit.servo[numero_servo].angle = 0


def enclencher_servo_prise_bas(numero_servo):
    kit = ServoKit(channels=16)
    kit.servo[numero_servo + 7].angle = 120


def enclencher_servo_prise_haut(numero_servo):
    kit = ServoKit(channels=16)
    kit.servo[numero_servo + 7].angle = 0
