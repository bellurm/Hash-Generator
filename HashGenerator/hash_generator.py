import hashlib

usage = """
Usage: python3 hash_creator.py
"""
print(usage)

operations = """
********** Our Operations! **********
[*]Please choose an operation (1, 2, 3 or 99).
1. Text to MD5
2. Text to SHA256
3. Text to SHA512
99. Exit
"""

def md5():
    textToMd5 = str(input("Give me something: "))
    result_md5 = hashlib.md5(textToMd5.encode()).hexdigest()
    print(f"Your MD5 hash is ready! => {result_md5}")

    while True:
        save_md5 = str(input("[!]Do you want to save the hash? (y/n) => "))
        if save_md5 == "y":
            md5_file = open("/home/kali/Desktop/MD5_hash.txt", "a")
            md5_file.write(textToMd5 + ":" + result_md5 + "\n")
            md5_file.close()
            print(f"[*]Your hash file is saved!")
            break
        elif save_md5 == "n":
            print("[*]Good luck about life!")
            break
        else:
            print("[!]Invalid input!")

def sha256():
    textToSha256 = str(input("Give me something: "))
    result_sha256 = hashlib.sha256(textToSha256.encode()).hexdigest()
    print(f"Your SHA256 hash is ready! => {result_sha256}")

    while True:
        save_sha256 = str(input("[!]Do you want to save the hash? (y/n) => "))
        if save_sha256 == "y":
            sha256_file = open("/home/kali/Desktop/SHA256_hash.txt", "a")
            sha256_file.write(textToSha256 + ":" + result_sha256 + "\n")
            sha256_file.close()
            print(f"[*]Your hash file is saved!")
            break
        elif save_sha256 == "n":
            print("[*]Good luck about life!")
            break
        else:
            print("[!]Invalid input!")

def sha512():
    textToSha512 = str(input("Give me something: "))
    result_sha512 = hashlib.sha512(textToSha512.encode()).hexdigest()
    print(f"Your SHA512 hash is ready! => {result_sha512}")

    while True:
        save_sha512 = str(input("[!]Do you want to save the hash? (y/n) => "))
        if save_sha512 == "y":
            sha512_file = open("/home/kali/Desktop/SHA512_hash.txt", "a")
            sha512_file.write(textToSha512 + ":" + result_sha512 + "\n")
            sha512_file.close()
            print(f"[*]Your hash file is saved!")
            break
        elif save_sha512 == "n":
            print("[*]Good luck about life!")
            break
        else:
            print("[!]Invalid input!")
try:
    print(operations)
    while True:
        choice = int(input("Operation: "))
        if choice == 99:
            break
        elif choice == 1:
            md5()
        elif choice == 2:
            sha256()
        elif choice == 3:
            sha512()
        else:
            print("[!]Invalid input!")
except ValueError:
    print("[!]Please follow the list of operations!")
except KeyboardInterrupt:
    pass
