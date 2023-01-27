from gpiozero import Button


def test():
    print("pressed")


but = Button(21)

but.when_pressed = test
