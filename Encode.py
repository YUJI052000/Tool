import os
import sys

def get_admin():
    try:
        if sys.argv[-1] == "elevate":
            del sys.argv[-1]
        else:
            sys.exit("Script must be run as administrator")
    except IndexError:
        sys.exit("Script must be run as administrator")

def unblock_ip(ip_address):
    command = f'netsh advfirewall firewall delete rule name="Blocked IP: {ip_address}"'
    os.system(command)

def main():
    get_admin()
    ip_address = input("Enter the IP address you want to unblock: ")
    unblock_ip(ip_address)
    print(f"Successfully unblocked IP address: {ip_address}")

if __name__ == "__main__":
    main()
