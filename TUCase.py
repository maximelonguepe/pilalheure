from hardware.multiple_servos import enclencher_servo_remplissage_haut, enclencher_servo_remplissage_bas, \
    enclencher_servo_prise_haut, enclencher_servo_prise_bas
import time

for i in range(7):
    enclencher_servo_remplissage_haut(i)
    enclencher_servo_prise_haut(i)
