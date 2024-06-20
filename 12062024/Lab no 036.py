

browser = str(input("Enter the browser name \n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("chrome code excuted")
    case"firefox":
        print("Firefox code excuted")
    case _:
        print("No browser found")