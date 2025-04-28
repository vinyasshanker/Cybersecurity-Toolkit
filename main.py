import os
from tools.Secure_System.update_system import Update_System
from tools.Secure_System.update_system import Upgrade_System
from tools.directory_bruteforce.Directory_brute import FUFF
from tools.directory_bruteforce.Directory_brute import Feroxbuster
from tools.info_gathering.info_gather import Nmap
from tools.info_gathering.info_gather import WhatWeb
from tools.info_gathering.info_gather import Sublist3r
from tools.info_gathering.info_gather import amassh
from tools.info_gathering.info_gather import EyeWitness
from tools.password_crack.Password_Crack import JohnTheRipper
from tools.password_crack.Password_Crack import Hashcat
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
            print("[1] Nmap")
            print("[2] WhatWeb")
            print("[3] Sublist3r")
            print("[4] Amass")
            print("[5] EyeWitness")
            print("[99] Back to Main Menu")
            try:
                i3 = int(input("Enter the option: "))
                match i3:
                    case 1:
                        print("\nNmap Scan")
                        print("---------")
                        host = input("Please enter the target URL (e.g., http://example.com or 10.10.11.26): ")
                        updater = Nmap()
                        result = updater.nmap(host)
                        if result is not None:
                            input("\nScan complete. Press Enter to continue...")
                        
                    case 2:
                        print("\nWhatWeb Scan")
                        print("------------")
                        host = input("Please enter the target URL (e.g., http://example.com): ")
                        updater = WhatWeb()
                        result = updater.whatweb(host)
                        if result is not None:
                            input("\nScan complete. Press Enter to continue...")
                        
                    case 3:
                        print("\nSublist3r Scan")
                        print("---------------")
                        host = input("Please enter the target URL (e.g., example.com): ")
                        updater = Sublist3r()
                        result = updater.sublist3r(host)
                        if result is not None:
                            input("\nScan complete. Press Enter to continue...")
                        
                    case 4:
                        print("\nAmass Scan")
                        print("-----------")
                        host = input("Please enter the target URL (e.g., example.com): ")
                        updater = amassh()
                        result = updater.amassh(host)
                        if result is not None:
                            input("\nScan complete. Press Enter to continue...")
                        
                    case 5:
                        print("\nEyeWitness Scan")
                        print("----------------")
                        host = input("Please enter the target URL (e.g., http://example.com): ")
                        updater = EyeWitness()
                        result = updater.eyewitness(host)
                        if result is not None:
                            input("\nScan complete. Press Enter to continue...")
                        
                    case 99:
                        break

                    case _:
                        print("Invalid sub-option selected")
                        input("\nPress Enter to continue...")
            except ValueError:
                print("Please enter a valid number")
                input("\nPress Enter to continue...")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user")
                input("\nPress Enter to continue...")
            except Exception as e:
                print(f"\nAn error occurred: {str(e)}")
                input("\nPress Enter to continue...")

        case 3:
            while True:
                clear_screen()
                print("Directory BruteForce Tool Menu:")
                print("[1] FFUF")
                print("[2] Feroxbuster")
                print("[99] Back to Main Menu")
                try:
                    i2 = int(input("Enter the option: "))

                    match i2:
                        case 1:
                            print("\nFFUF Directory Bruteforce")
                            print("------------------------")
                            host1 = input("Please enter the target URL (e.g., http://example.com): ")
                            updater1 = FUFF()
                            result = updater1.ffuf(host1)
                            if result is not None:
                                input("\nScan complete. Press Enter to continue...")
                            
                        case 2:
                            print("\nFeroxbuster Directory Scan")
                            print("-------------------------")
                            host2 = input("Enter the target URL (e.g., http://example.com): ")
                            updater2 = Feroxbuster()
                            result = updater2.feroxbuster(host2)
                            if result is not None:
                                input("\nScan complete. Press Enter to continue...")
                            
                        case 99:
                            break
                        
                        case _:
                            print("Invalid sub-option selected")
                            input("\nPress Enter to continue...")

                except ValueError:
                    print("Please enter a valid number")
                    input("\nPress Enter to continue...")
                except KeyboardInterrupt:
                    print("\nOperation cancelled by user")
                    input("\nPress Enter to continue...")
                except Exception as e:
                    print(f"\nAn error occurred: {str(e)}")
                    input("\nPress Enter to continue...")

        case 4:
            while True:
                clear_screen()
                print("Password Bruteforce Menu:")
                print("[1] John the Ripper")
                print("[2] Hashcat")
                print("[99] Back to Main Menu")
                try:
                    i4 = int(input("Enter choice: "))
                    match i4:
                        case 1:
                            print("\nJohn the Ripper Selected")
                            tool = JohnTheRipper()
                            tool.crack()
                            input("\nPress Enter to continue...")
                        case 2:
                            print("\nHashcat Selected")
                            tool = Hashcat()
                            tool.crack()
                            input("\nPress Enter to continue...")
                        case 99:
                            break
                        case _:
                            print("Invalid option")
                            input("\nPress Enter to continue...")
                except ValueError:
                    print("Please enter a valid number")
                    input("\nPress Enter to continue...")
                except KeyboardInterrupt:
                    print("\nOperation cancelled by user")
                    input("\nPress Enter to continue...")
                except Exception as e:
                    print(f"\nAn error occurred: {str(e)}")
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
