def on_button_pressed_a():
    basic.show_string("DISCO 1")
    for index in range(50):
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        basic.pause(100)
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("disco 2")
    for index2 in range(50):
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.pause(100)
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        basic.pause(100)
        strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
        basic.pause(500)
        strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
        basic.pause(100)
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        basic.pause(200)
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
        basic.pause(500)
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        basic.pause(100)
input.on_button_pressed(Button.B, on_button_pressed_b)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 13, NeoPixelMode.RGB)
strip.set_brightness(100)

def on_forever():
    music.set_built_in_speaker_enabled(True)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            200,
            1,
            255,
            0,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
basic.forever(on_forever)
