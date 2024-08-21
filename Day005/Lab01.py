# Broswer
browser = str(input("Enter the Broswer Name!\n"))
browser = browser.lower()
match browser:
    case "Chrome":
        print("Chrome code executed")
    case "FireFox":
        print("Firfox code executed")
    case "_":
        print("No Browser Found")

