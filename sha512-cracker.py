import hashlib
import sys

if len(sys.argv) != 2:
	print("Invalid Arguments!")
	print(f">> {sys.argv[0]} '<sha512sum>'")
	exit()

hash_value = sys.argv[1]
attempts = 0

# hash_value = input("Enter the sha256 hash to crack: ")
# hash_value = "65af9da6c376811e7fca4b1c904e19ed3f5c68cf2a658fa761d5767b742f0ca7dc07453b614e98d1cb807dc408d23468978e56cf035f10e02361e9a0610adb72"

with open("/usr/share/wordlists/rockyou.txt","r",encoding='latin-1') as wordlist:
	for item in wordlist:
		attempts += 1
		item = item.strip()
		try:
			item_hash_value = hashlib.sha512(item.encode('utf-8')).hexdigest()

			# sys.stdout.write(f"\r[{attempts}] Password: '{item}'\n")
			# sys.stdout.flush()

			if hash_value == item_hash_value:
				print(f"[+] Password Found: \"{item}\" in {attempts} attempts.")
				exit()
		except Exception as e:
			print(e)
	else:
		print(f"[-] Password not found in this wordlist.")