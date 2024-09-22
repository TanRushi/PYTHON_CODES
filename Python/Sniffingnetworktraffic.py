import scapy.all as scapy

def sniff_network(iface):
    sniffed_packets = []
    sniff(prn=lambda x: sniffed_packets.append(x), count=100, iface=iface)
    return sniffed_packets

iface = "eth0"
sniffed_packets = sniff_network(iface)
for packet in sniffed_packets:
    print(packet.summary())