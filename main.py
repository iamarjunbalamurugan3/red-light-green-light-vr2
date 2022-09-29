def on_button_pressed_a():
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 13, NeoPixelMode.RGB)

def on_forever():
    strip.set_brightness(50)
basic.forever(on_forever)
