from hardware.multiple_servos import enclencher_servo_remplissage_haut, enclencher_servo_prise_haut

if __name__ == '__main__':
    for i in range(7):
        enclencher_servo_remplissage_haut(i)
        enclencher_servo_prise_haut(i)
