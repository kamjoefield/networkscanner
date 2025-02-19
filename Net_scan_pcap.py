import subprocess
import time

# Set network subnet (replace with your actual subnet, e.g., "192.168.1.0/24")
subnet = "192.168.1.0/24"

# Set the network interface for packet capture (adjust as needed)
interface = "wlan0"

# Nmap scan command
def run_nmap_scan():
    print(f"Scanning network: {subnet}")
    scan_command = ["nmap", "-sn", subnet]  # -sn for a simple ping scan
    result = subprocess.run(scan_command, capture_output=True, text=True)
    print(result.stdout)

# Start Wireshark packet capture using tshark
def start_tshark_capture():
    print(f"Starting packet capture on {interface}")
    capture_file = "network_capture.pcap"
    tshark_command = ["tshark", "-i", interface, "-w", capture_file]

    tshark_process = subprocess.Popen(tshark_command)
    return tshark_process, capture_file

# Run the scan
run_nmap_scan()

# Start packet capture
tshark_process, capture_file = start_tshark_capture()

# Capture packets for 60 seconds (adjust as needed)
time.sleep(60)

# Stop tshark capture
tshark_process.terminate()
print(f"Packet capture saved to {capture_file}")

# Analyze the capture (optional)
print("Run the following command to analyze captured packets:")
print(f"tshark -r {capture_file}")
