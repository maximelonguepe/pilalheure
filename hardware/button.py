from gpiozero import Button


def init():
    return Button(20)


def wait_for_press():
    button = init()
    button.wait_for_press()
