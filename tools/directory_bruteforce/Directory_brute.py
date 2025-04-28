import subprocess
import os

class FUFF:
    def __init__(self):
        pass

    def ffuf(self, host):
        
        check = ["which", "ffuf"]
        check_res = subprocess.run(check, capture_output=True, text=True)

        if check_res.returncode != 0:
            print("[❌] FFUF is not installed on your system.")
            install_permission = input("Do you want to install it? (Y/N): ")

            if install_permission.lower() == 'y':
                os.system("sudo apt install ffuf")
            else:
                print("Skipping installation.")
                return
        else:
            print("[✅] FFUF is already installed.")

        
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

        print("\n[👍] Final command to be executed:")
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

class Feroxbuster:
    def __init__(self):
        pass
    def feroxbuster(self, host):
        check = ['which', 'feroxbuster']
        check_res = subprocess.run(check, capture_output=True, text=True)
        #check_output = check_res.stdout + check_res.stderr

        if check_res.returncode !=0:
            print("![❌] FEROXBUSTER is not installed. Do you want to install it?")
            install_permission = input("Y/N")

            if install_permission.lower()=='y':
                os.system('sudo apt install feroxbuster')
            else:
                print('![+] Skipping the installation')
                return
        else:
            print('[✅] Feroxbuster is installed')
        
        default_wordlist = "../../wordlist/SecLists/Discovery/Web-Content/raft-medium-words.txt"
        print("\nDefault wordlist:")
        print(f"-> {default_wordlist}")
        wordlist = input("Enter custom wordlist path or press Enter to use default: ").strip()

        if wordlist == "":
            wordlist = default_wordlist

        print("\n[Optional] Add any custom feroxbuster flags you want.")
        man = '''
            Response filters:
          -S, --filter-size <SIZE>...                 Filter out messages of a particular size (ex: -S 5120 -S 4927,1970)
          -X, --filter-regex <REGEX>...               Filter out messages via regular expression matching on the response's body/headers (ex: -X '^ignore me$')
          -W, --filter-words <WORDS>...               Filter out messages of a particular word count (ex: -W 312 -W 91,82)
          -N, --filter-lines <LINES>...               Filter out messages of a particular line count (ex: -N 20 -N 31,30)
          -C, --filter-status <STATUS_CODE>...        Filter out status codes (deny list) (ex: -C 200 -C 401)
              --filter-similar-to <UNWANTED_PAGE>...  Filter out pages that are similar to the given page (ex. --filter-similar-to http://site.xyz/soft404)
          -s, --status-codes <STATUS_CODE>...         Status Codes to include (allow list) (default: All Status Codes)
        
        '''
        print(f"{man}")
        custom_flags = input("Enter custom flags or press Enter to skip: ").strip()
        cmd = f"feroxbuster -u {host} -w {wordlist} {custom_flags}"

        print("\n[👍] Final command to be executed:")
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