$(function () {
    $('.rotarySwitch').rotaryswitch({ themeClass: 'big' });
    $('.rotarySwitch2').rotaryswitch({ showMarks: true, themeClass: 'light'});
    var rotarySwitch3a = $('.rotarySwitch3a').rotaryswitch({
        beginDeg: 270,
        lengthDeg: 180,
        minimum: 0,
        maximum: 10,
        step: 0.5,
        showMarks: true
    }),
        rotarySwitch3b = $('.rotarySwitch3b').rotaryswitch({
            minimum: 0,
            maximum: 10,
            step: 0.5,
            hideInput: false
        });

    rotarySwitch3a.on('change', function () {
        rotarySwitch3b.val(rotarySwitch3a.val()).change();
        // console.log('rotarySwitch3a')
    });

    $('.rotarySwitch2').on('change', function () {
        console.log( $('.rotarySwitch2').val())
    });
});
