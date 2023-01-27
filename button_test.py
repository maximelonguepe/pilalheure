from gpiozero import Button


def test():
    print("pressed")


but = Button(20)
while True:
    but.when_pressed = test
