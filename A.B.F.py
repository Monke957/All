import pyzipper
import os

number = 0

os.system('cls' if os.name == 'nt' else 'clear')

print("File path = ", end="")
zip_p = input("").strip()

# remove any quotes
zip_p = zip_p.replace('"', '').replace("'", "")


print("Password list = ", end="")
pass_list = input("").strip()
print("\n\n")


# remove any quotes
pass_list = pass_list.replace('"', '').replace("'", "")

zip_path = zip_p

with pyzipper.AESZipFile(zip_path, 'r') as zip_file:
    with open(pass_list, "r", errors="ignore") as file:
        for line in file:
            number += 1
            password = line.strip()
            print(f"Testing: {password}" ,end="")

            try:
                zip_file.extractall(pwd=password.encode("utf-8"))
                print("\nArchive.Unlock(success)")
                print(f"Password({password})\n")
                print(f"Attempts: {number}")
                print("Press enter to exit...")
                input("")
                break

            except:
                print("...Archive.Unlock(failed))")
                pass
