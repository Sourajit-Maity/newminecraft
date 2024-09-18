
options: {
    /**
    Defines the number of digits that comprise the array of discrete seven-segment displays.
    */
    digits: 1

    /**
    This option controls the display value on the 7seg.  Set this to the numeric value you
    want displayed.  The least significant digit will be rendered in the rightmost seven-segment digit display.
    More significant digits that exceed the limits of the number of digits you configured for the display
    will simply be omitted.
    Setting it to null will blank the display.
    */
    value: null,

    /**
    Set this to true to allow sevenSeg to respond to the mousewheel event, which
    will allow you to change the display value by spinning the mousewheel up or down.
    (The default step is +/- 1, but you can set that in the 'step' option).
    */
    allowInput: false,

    /**
    This setting controls the +/- delta value whenever the sevenSeg is incremented up or down (via mousewheel).
    The allowInput option must be true for this setting to be of use.
    */
    step: 1,

    /**
    This controls the number of decimal places displayed.  The default -1 results in no rounding and displays the value
    as-is.  A value of 0 or more defines the number of fixed decimal places that the numeric value will be rounded to.
    
    If you intend to set display values that are the result of floating point operations, including the
    use of allowInput=true and a fractional step size, then you most definitely want to set this to a specific value to
    avoid overflowing the display from floating point inaccuracies.
    */
    decimalPlaces: -1,

    /**
    Override the default segment "on" color (Red).  
    Note: You can alternatively define a CSS style for the class.sevenSeg-segOn that specifies a 'fill' color.
    */
    colorOn: null,

    /**
    Override the default segment "off" color (#320000).  
    Note: You can alternatively define a CSS style for the class .sevenSeg-svg that specifies a 'fill' color.
    */
    colorOff: null,

    /**
    Override the default background color of the display (Black).  
    Note: You can alternatively define a CSS style for the class .sevenSeg-svg that specifies a 'background-color' color.
    */
    colorBackground: null,
    
    /**
    This option allows skewing the segments to create a slant effect.
    Note: Setting "transform: skew()" in CSS is problematic for SVG. Would be nice to have, but browser support just 
    isn't there yet. So, setting the slant must be done through options.
    */
    slant: 0,  

    /**
    This flag controls the appearance of the decimal point 'dot' in the display.
    The default is to display it (true), but you can set to false to omit it.
    */
    decimalPoint: true
}