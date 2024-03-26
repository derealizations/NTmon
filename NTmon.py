#!/usr/bin/python3
import psutil, time, os

def gettrin():
    interfaces = psutil.net_if_addrs()
    return interfaces.keys()

def gettr(interface):
    counters = psutil.net_io_counters(pernic=True)
    incoming = counters[interface].bytes_recv
    outgoing = counters[interface].bytes_sent
    total = incoming + outgoing
    return incoming, outgoing, total

def btg(bytes):
    gb = bytes / (1024**3)
    return gb

def NTmon():
    interfaces = list(gettrin())

    print("Captured Interfaces:")
    for i, interface in enumerate(interfaces):
        print(f"{i+1}. {interface}")

    selectinter = int(input("Select a network interface: ")) - 1
    intername = interfaces[selectinter]

    while True:
        incoming, outgoing, total = gettr(intername)
        print(f"Monitoring Interface {intername}")
        print(f"Download (incoming): {btg(incoming):.2f} GB")
        print(f"Upload (outgoing): {btg(outgoing):.2f} GB")
        print(f"Total: {btg(total):.2f} GB")
        time.sleep(0.06)
        os.system("clear")
if __name__ == "__main__":
    NTmon()
