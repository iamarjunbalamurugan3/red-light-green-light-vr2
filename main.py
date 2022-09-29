def on_button_pressed_a():
    if 0 < 1:
        for index in range(10):
            strip.show_color(neopixel.colors(NeoPixelColors.RED))
            basic.pause(100)
            strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
            basic.pause(100)
            strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
            basic.pause(100)
            strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
            basic.pause(100)
            strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
            basic.pause(100)
            strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
            basic.pause(100)
            strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
            basic.pause(100)
            strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
            basic.pause(100)
            strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    else:
        strip.clear()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 13, NeoPixelMode.RGB)

def on_forever():
    strip.set_brightness(200)
basic.forever(on_forever)
