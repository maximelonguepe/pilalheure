from gpiozero import Button


def test():
    print("pressed")


but = Button(21)
while True:
    but.when_pressed = test
