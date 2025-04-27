import os
from tools.Secure_System.update_system import Update_System
from tools.Secure_System.update_system import Upgrade_System

def clear_screen():
    os.system('clear')

while True:
    clear_screen()
    print("Select option:")
    print("[1] Secure System")
    print("[2] Information Gathering")
    print("[3] Directory Bruteforce")
    print("[4] Password Bruteforce")
    print("[5] Burpsuite Pro")
    print("[6] AI Chatbot")
    print("[99] Exit")

    i = int(input("Please choose an option: "))

    match i:
        case 1:
            while True:
                clear_screen()
                print("Secure System Menu:")
                print("[1] Update System")
                print("[2] Upgrade System")
                print("[99] Back to Main Menu")
                i1 = int(input("Enter choice: "))

                match i1:
                    case 1:
                        print("You chose Update System")
                        updater = Update_System()
                        command = "sudo apt-get update".split()
                        print(updater.run_tool(command))
                        input("\nPress Enter to continue...")

                    case 2:
                        print("You chose Upgrade System")
                        upgrader = Upgrade_System()
                        command = "sudo apt-get full-upgrade".split()
                        print(upgrader.run_tool(command))
                        input("\nPress Enter to continue...")

                    case 99:
                        break

                    case _:
                        print("Invalid sub-option selected")
                        input("\nPress Enter to continue...")

        case 2:
            clear_screen()
            print("Information Gathering Selected")
            input("\nPress Enter to continue...")

        case 3:
            clear_screen()
            print("Directory Bruteforce Selected")
            input("\nPress Enter to continue...")

        case 4:
            clear_screen()
            print("Password Bruteforce Selected")
            input("\nPress Enter to continue...")

        case 5:
            clear_screen()
            print("Burpsuite Pro Selected")
            input("\nPress Enter to continue...")

        case 6:
            clear_screen()
            print("AI Chatbot Selected")
            input("\nPress Enter to continue...")

        case 99:
            print("Exiting program. Goodbye!")
            break

        case _:
            print("Invalid main option selected")
            input("\nPress Enter to continue...")
