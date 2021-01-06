radio.onReceivedValue(function (name, value) {
	
})
basic.forever(function () {
    basic.showIcon(IconNames.No)
    basic.showLeds(`
        # . . . #
        # # . # #
        # . # . #
        # . . . #
        # . . . #
        `)
    basic.showString("music")
    basic.showNumber(234)
    music.playMelody("A G A C5 G C5 F A ", 120)
    music.setVolume(185)
})
