# Job Application Tracker

def display_menu():
    print("\n--- Job Application Tracker ---")
    print("1. Submit New Application")
    print("2. Modify Application Status")
    print("3. Show All Applications")
    print("4. Look Up Application by Company")
    print("5. Quit")

# List to store all applications
ApplicationsList = []

menuChoice = 0

while menuChoice != 5:
    display_menu()
    
    try:
        menuChoice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # 1. Add new application
    if menuChoice == 1:
        FirmName = input("Enter Company Name: ")
        PositionTitle = input("Enter Position Title: ")
        AppliedOn = input("Enter Application Date: ")
        CurrentStatus = input("Enter Current Status: ")

        entry = {
            "FirmName": FirmName,
            "PositionTitle": PositionTitle,
            "AppliedOn": AppliedOn,
            "CurrentStatus": CurrentStatus
        }
        ApplicationsList.append(entry)
        print("Application Successfully Saved.")

    # 2. Modify status
    elif menuChoice == 2:
        FirmName = input("Enter Company Name to Update: ")
        found = False

        for entry in ApplicationsList:
            if entry["FirmName"].lower() == FirmName.lower():
                updatedStatus = input("Enter Updated Status: ")
                entry["CurrentStatus"] = updatedStatus
                print("Status Updated Successfully.")
                found = True
                break

        if not found:
            print("Company Not Located.")

    # 3. Display all applications
    elif menuChoice == 3:
        if len(ApplicationsList) == 0:
            print("No Applications Found.")
        else:
            print("\n--- All Applications ---")
            for entry in ApplicationsList:
                print(entry)

    # 4. Lookup by company
    elif menuChoice == 4:
        lookupName = input("Enter Company Name to Search: ")
        found = False

        for entry in ApplicationsList:
            if entry["FirmName"].lower() == lookupName.lower():
                print("Application Found:")
                print(entry)
                found = True
                break

        if not found:
            print("No Matching Application Found.")

    # 5. Quit
    elif menuChoice == 5:
        print("Closing System...")

    else:
        print("Invalid Selection. Please try again.")

print("Program Ended.")
