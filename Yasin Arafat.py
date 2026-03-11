from scapy.all import sniff, IP

# এই ফাংশনটি প্রতিটি প্যাকেট ক্যাপচার করার পর তথ্য প্রদর্শন করবে
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source: {src_ip} | Destination: {dst_ip} | Protocol: {protocol}")

print("Network Sniffer starting... (Press Ctrl+C to stop)")
# প্যাকেট ক্যাপচার শুরু করার কমান্ড
sniff(prn=packet_callback, store=0)