#                             Media File Downloader (Self Created.)

import requests
import os

url = input("Enter the url of media: ")
#url = "https://images.pexels.com/photos/1366957/pexels-photo-1366957.jpeg"

chunks = url.split("/")
media_index = len(chunks)-1
media_name = chunks[media_index]
ext_index = media_name.split(".")
ext = ext_index[1]
media = ext_index[0]
i = ''
n = 1
r = requests.get(url)

while True:
    try:
        with open(f"/home/kali/Python/Download_Python/{media}{i}.{ext}","rb") as f1:
            f1.read()
            n+=1
            i = f"_{n}"

    except Exception as e:

        with open(f"/home/kali/Python/Download_Python/{media}{i}.{ext}","wb") as f2:
            f2.write(r.content)

            if os.path.exists(f"/home/kali/Python/Download_Python/{media}{i}.{ext}"):

                print(f"{media}{i}.{ext} Downloaded Successfully.")
            else:
                print(e)
            break

print("\nThanks for using :)")