#!/usr/bin/python3
import os
import sys
import hashlib

def get_hash(text, algo):
    match algo:
        case 'md5': return hashlib.md5(text.encode('utf-8')).hexdigest()
        case 'sha1': return hashlib.sha1(text.encode('utf-8')).hexdigest()
        case 'sha224': return hashlib.sha224(text.encode('utf-8')).hexdigest()
        case 'sha256': return hashlib.sha256(text.encode('utf-8')).hexdigest()
        case 'sha512': return hashlib.sha512(text.encode('utf-8')).hexdigest()

help_message = f"""
Usage: hashcracker.py <hash_type> <hash_sum> <wordlist_path>

Current Algorithm Supports:
    md5, sha1, sha224, sha256, sha512

Example:
    python3 {sys.argv[0]} md5 5f4dcc3b5aa765d61d8327deb882cf99 /path/wordlist.txt"""

if len(sys.argv) != 4 :
    print(help_message)
    sys.exit()

mode = sys.argv[1].lower()  # md5
hash2crack = sys.argv[2].lower()    # 0800fc577294c34e0b28ad2839435945
wordlist = sys.argv[3]      # /usr/share/wordlist/rockyou.txt

if not os.path.exists(wordlist):
    print(f"Error: '{wordlist}' does not exist.")
    sys.exit()

try:
    with open(wordlist,"r",encoding="latin-1") as f:
        for text in f:
            text = text.strip()
            text_hash = get_hash(text, mode)
            if text_hash == hash2crack:
                print(f"\nHash Cracked: '{text}'")
                break
        else:
            print("\nHash not found.")
except Exception as e:
    print(e)