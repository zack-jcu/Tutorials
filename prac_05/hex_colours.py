COLOURS_IN_HEX = {"aliceblue": "#f0f8ff",
                      "antiquewhite": "#faebd7",
                      "antiquewhite1": "#ffefdb",
                      "antiquewhite2": "#eedfcc",
                      "antiquewhite3": "#cdc0b0",
                      "antiquewhite4": "#8b8378",
                      "aquamarine1": "#7fffd4",
                      "aquamarine2": "#76eec6",
                      "aquamarine4": "#458b74",
                      "azure1": "#f0ffff"}

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in COLOURS_IN_HEX:
        print("{} = {} ".format(colour, COLOURS_IN_HEX[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").lower()
