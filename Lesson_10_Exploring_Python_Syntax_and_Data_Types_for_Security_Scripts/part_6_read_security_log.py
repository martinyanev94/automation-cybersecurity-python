try:
    with open("security_log.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Log reading attempt executed.")
