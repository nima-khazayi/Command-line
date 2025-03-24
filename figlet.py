from pyfiglet import Figlet
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    print(f"Output: \n{figlet.renderText(text)}")


elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        fonts = figlet.getFonts()

        if sys.argv[2] in fonts:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(f"Output: \n{figlet.renderText(text)}")

        else:
            sys.exit(1)

    else:
        sys.exit(1)


else:
    print("Invalid usage")
    sys.exit(1)

