from gpiozero import LED


def init():
    return LED(12)


def led_on():
    led = init()
    led.on()


def led_off():
    led = init()
    led.off()
