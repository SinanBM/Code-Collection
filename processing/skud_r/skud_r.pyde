#skudår funktion


def skudaar(aar):
    # skudår hvis året kan divideres med 4.
    if aar % 4 == 0:
        # skudår hvis året ikke kan divideres med 100 og kan divideres med 400.
        if aar % 100 != 0 or aar % 400 == 0:
            print("Skudaar")
        else:
            print("ikke skudaar")
    else:
        print("ikke skudaar")

skudaar(2000)

   
      
