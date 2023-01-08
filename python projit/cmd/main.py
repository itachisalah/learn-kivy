import subprocess

while True:
    try:
        command = input("Please Enter System Command > ")
        if command.lower() == "exit" or command.lower() == "stop" or command.lower() == "quite":
            break

        subprocess.run(command)
    except Exception:
        continue

print("Good Bye")

