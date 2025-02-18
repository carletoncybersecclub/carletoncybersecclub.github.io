from scapy.all import rdpcap
from scapy.layers.inet import TCP
import re

def extract_http_get_requests(pcap_file):
    """
    Extract and print HTTP GET requests from a given pcap file,
    only if the path in the GET request is not empty.
    
    :param pcap_file: Path to the pcap file
    """
    try:
        packets = rdpcap(pcap_file)  # Read packets from the pcap file
        print(f"Loaded {len(packets)} packets from {pcap_file}")
        
        for packet in packets:
            # Check if the packet has a TCP layer
            if packet.haslayer(TCP):
                # Extract the raw payload (if any)
                if hasattr(packet[TCP], 'payload') and packet[TCP].payload:
                    try:
                        # Decode the TCP payload
                        payload = bytes(packet[TCP].payload).decode('utf-8', errors='ignore')
                        
                        # Look for HTTP GET requests
                        if payload.startswith('GET '):
                            # Extract the request line and path
                            request_line = payload.splitlines()[0]
                            request_match = re.match(r'GET\s+(\S+)\s+HTTP', request_line)
                            request_path = request_match.group(1) if request_match else None
                            
                            if request_path and request_path != '/':
                                # Extract host information
                                host_match = re.search(r'Host: (.+)', payload)
                                host = host_match.group(1) if host_match else "Unknown Host"
                                print(f"[HTTP GET] Host: {host}, Request Path: {request_path}")
                    except Exception:
                        
                        continue
    except FileNotFoundError:
        print(f"Error: File '{pcap_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
pcap_file_path = "artifact.pcap"  
extract_http_get_requests(pcap_file_path)

