from scapy.all import *
from netfilterqueue import NetfilterQueue

def intercept(packet):
    pkt = packet.get_payload()
    # Change packet payload here using 'scapy' or pkt.setpayload()...
    print(pkt)
    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, intercept)
try:
    print ("Waiting for a new packet to intercept...")
    nfqueue.run()
except KeyboardInterrupt:
    pass