from pwn import md5sumhex

with open("/usr/share/wordlists/rockyou.txt","r") as f:
	for item in f:
		item = item.strip()
		item = item.encode()
		if md5sumhex(item) == "b1c84f8d672b5d6a84a7a486e81b465a":
			print("Password Found! : " + item.decode())
			break


