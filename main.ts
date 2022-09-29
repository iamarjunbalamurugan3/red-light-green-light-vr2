input.onButtonPressed(Button.A, function on_button_pressed_a() {
    strip.showColor(neopixel.colors(NeoPixelColors.Red))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    strip.showColor(neopixel.colors(NeoPixelColors.Green))
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    strip.showColor(neopixel.colors(NeoPixelColors.White))
})
let strip : neopixel.Strip = null
strip = neopixel.create(DigitalPin.P0, 13, NeoPixelMode.RGB)
basic.forever(function on_forever() {
    strip.setBrightness(50)
})
