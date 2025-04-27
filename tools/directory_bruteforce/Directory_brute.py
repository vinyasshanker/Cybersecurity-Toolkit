import subprocess
import os

class Dir_Brute:
    def __init__(self):
        pass

    def ffuf(self, host):
        
        check = ["which", "ffuf"]
        check_res = subprocess.run(check, capture_output=True, text=True)

        if check_res.returncode != 0:
            print("[!] FFUF is not installed on your system.")
            install_permission = input("Do you want to install it? (Y/N): ")

            if install_permission.lower() == 'y':
                os.system("sudo apt install ffuf")
            else:
                print("Skipping installation.")
                return
        else:
            print("[+] FFUF is already installed.")

        
        default_wordlist = "../../wordlist/SecLists/Discovery/Web-Content/raft-medium-words.txt"
        print("\nDefault wordlist:")
        print(f"-> {default_wordlist}")
        wordlist = input("Enter custom wordlist path or press Enter to use default: ").strip()

        if wordlist == "":
            wordlist = default_wordlist

        
        print("\n[Optional] Add any custom ffuf flags you want.")
        print("For example: -mc 200, -t 50, -fs 4242, -recursion\n")
        custom_flags = input("Enter custom flags or press Enter to skip: ").strip()

        
        cmd = f"ffuf -u {host}/FUZZ -w {wordlist} -c {custom_flags}"

        print("\n[+] Final command to be executed:")
        print(cmd)

        
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        rc = process.poll()
        return rc

host = "https://nmap.org"
c1=Dir_Brute()
print(c1.ffuf(host))