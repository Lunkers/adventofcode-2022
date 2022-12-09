packet_idx = None
message_idx = None
with open("./input.txt") as f:
    data = f.read().rstrip()
    for i in range(len(data)):
        if len(set(data[i:i+4])) == 4 and packet_idx is None:
            packet_idx = i + 4
        if message_idx == None and len(set(data[i:i+14])) == 14:
            message_idx = i +14
        if packet_idx and message_idx:
            break

print(packet_idx)
print(message_idx)
        
