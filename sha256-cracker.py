import hashlib
import sys

if len(sys.argv) != 2:
	print("Invalid Arguments!")
	print(f">> {sys.argv[0]} '<sha256sum>'")
	exit()

hash_value = sys.argv[1]
attempts = 0

# hash_value = input("Enter the sha256 hash to crack: ")
# hash_value = "ee286ba3370879a600b35ef67cf90c68d88e01e3fbf6181d50987cc6450d279c"

with open("/home/kali/wordlist.txt","r",encoding='latin-1') as wordlist:
	for item in wordlist:
		attempts += 1
		item = item.strip()
		try:
			item_hash_value = hashlib.sha256(item.encode('utf-8')).hexdigest()

			# sys.stdout.write(f"\r[{attempts}] Password: '{item}'\n")
			# sys.stdout.flush()

			if hash_value == item_hash_value:
				print(f"[+] Password Found: \"{item}\" in {attempts} attempts.")
				exit()
		except Exception as e:
			print(e)
	else:
		print(f"[-] Password not found in this wordlist.")