
$(document).ready(function () {
    var loaderArray = [100, 10, 15, 20, 25, 30, 78, 54, 65, 45, 90, 82, 37];
    var loderArrayMax = 0;
    var loderArrayMin = 0;
    var loaderArrayCurrentValue = 100;
    var bulb_off = true;

    $("#toggleSwithch").click(function () {
        // console.log("toggle")
        if (bulb_off == true) {
            bulb_off = false;
            bulbon();
        } else {
            bulb_off = true;
            bulboff();
            // console.log(bulb_off)
        }

    })

    function bulbon() {
        $("#bulb").attr('src', 'assets/color_arrow.com.png');
    }
    function bulboff() {
        $("#bulb").attr('src', 'assets/arrow.com.png');
    }

    function setLoaderArray() {
        for (let index = 0; index < loaderArray.length; index++) {
            if (loderArrayMax < loaderArray[index]) {
                loderArrayMax = loaderArray[index];
            }
            if (loderArrayMin > loaderArray[index]) {
                loderArrayMin = loaderArray[index];
            }
        }
        $('#progressBar').attr('aria-valuenow', loaderArrayCurrentValue);
        $('#progressBar').attr('aria-valuemin', loderArrayMin);
        $('#progressBar').attr('aria-valuemax', loderArrayMax);
        $('#progressBar').css('width', loaderArrayCurrentValue + '%');
        $('#loaderArrayCurrentValue').html(loaderArrayCurrentValue + '%');

        $('#progressBarVertical').attr('aria-valuenow', loaderArrayCurrentValue);
        $('#progressBarVertical').attr('aria-valuemin', loderArrayMin);
        $('#progressBarVertical').attr('aria-valuemax', loderArrayMax);
        $('#progressBarVertical').css('height', loaderArrayCurrentValue + '%');
        $('#loaderArrayCurrentValueVertical').html(loaderArrayCurrentValue + '%');
        progressBarVertical
    }

    setLoaderArray();

    setInterval(() => {
        loaderArrayCurrentValue = loaderArray[Math.floor(Math.random() * loaderArray.length)];
        setLoaderArray();
    }, 2000);

    $("#exampleArray").sevenSeg({ digits: 6, value: 1012.35 });
});
var CompassRotateAngle = 45;
function SetCompassAngle() {
    $('.main-arrow').css({ 'transform': 'rotate(' + CompassRotateAngle + 'deg)' });
    setChild();
}
childArray = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
function setChild() {
    for (let index = 0; index < childArray.length; index++) {
        const element = childArray[index];
        $(".marks .mark:nth-child(" + index + ")").html(element);
    }
}

