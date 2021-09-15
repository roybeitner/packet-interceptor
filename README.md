Summary:
    Just a little POC of catching a live packet in order to read bytes / mangle / alter packet payload.

    In order to catch the packet inside the python code you'll have to redirect an incoming/outgoing/forwarded packet to the nfqueue.

        Example:
            iptables -A INPUT -j NFQUEUE --queue-num 1

If you have trouble installing "Netfilterqueue" please take a look over here:
    https://stackoverflow.com/questions/61301351/how-do-i-install-netfilterqueue-for-python3
