from time import perf_counter
from math import prod

start = perf_counter()

in_time = perf_counter()
with open("day16input.txt", "r") as file_in:
    hex = file_in.readline()
    decode_hex = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }
    bits = str()
    for char in hex:
        bits += decode_hex[char]
    packets = list()

# print(bits, len(bits))


print("input processed in " + str(perf_counter() - in_time) + " seconds")


def read_packet(pos, total_version, subpacket):
    packet = dict()
    packet_end = False
    state = "V"
    while not packet_end:
        # print(pos, state)
        if state == "V":
            version = int(bits[pos:pos+3], base=2)
            packet["version"] = version
            total_version += version
            state = "T"
            pos += 3
        elif state == "T":
            typeID = int(bits[pos:pos+3], base=2)
            packet["type_ID"] = typeID
            if typeID == 4:
                state = "N"
                literal_num = list()
            else:
                state = "I"
            pos += 3
        elif state == "N":
            if bits[pos] == "1":
                literal_num.append(bits[pos+1:pos+5])
                pos += 5
            else:
                literal_num.append(bits[pos+1:pos+5])
                packet["literal_value"] = int(''.join(literal_num), base=2)
                packet_end = True
                pos += 5
        elif state == "I":
            packet["length_type_ID"] = int(bits[pos])
            state = "L"
            pos += 1
        elif state == "L":
            if packet["length_type_ID"] == 1:
                packet["count_subpackets"] = int(bits[pos:pos+11], base=2)
                subpacket_counter = 0
                pos += 11
            else:
                packet["total_length"] = int(bits[pos:pos+15], base=2)
                pos += 15
                subpackets_start_pos = pos
            state = "S"
        elif state == "S":
            if "subpackets" not in packet.keys():
                packet["subpackets"] = list()
            pos, new_packet, total_version = read_packet(
                pos, total_version, subpacket=True)
            packet["subpackets"].append(new_packet)
            if "count_subpackets" in packet.keys():
                subpacket_counter += 1
                # print(subpacket_counter, packet["count_subpackets"])
                if subpacket_counter == packet["count_subpackets"]:
                    packet_end = True
            else:
                if subpackets_start_pos + packet["total_length"] == pos:
                    packet_end = True
        if packet_end and not subpacket:
            if pos % 4 != 0:
                pos += 4 - (pos % 4)
            while pos < len(bits) and hex[int(pos/4)] == "0":
                pos += 4
    # print(packet)
    return pos, packet, total_version


def eval_subpackets(packet):
    if packet["type_ID"] == 4:
        return packet["literal_value"]
    elif packet["type_ID"] == 0:
        # sum
        return sum([eval_subpackets(subpacket) for subpacket in packet["subpackets"]])
    elif packet["type_ID"] == 1:
        # prod
        return prod([eval_subpackets(subpacket) for subpacket in packet["subpackets"]])
    elif packet["type_ID"] == 2:
        # min
        return min([eval_subpackets(subpacket) for subpacket in packet["subpackets"]])
    elif packet["type_ID"] == 3:
        # max
        return max([eval_subpackets(subpacket) for subpacket in packet["subpackets"]])
    elif packet["type_ID"] == 5:
        # greater than
        values = [eval_subpackets(subpacket)
                  for subpacket in packet["subpackets"]]
        return 1 if values[0] > values[1] else 0
    elif packet["type_ID"] == 6:
        # less than
        values = [eval_subpackets(subpacket)
                  for subpacket in packet["subpackets"]]
        return 1 if values[0] < values[1] else 0
    elif packet["type_ID"] == 7:
        # equal to
        values = [eval_subpackets(subpacket)
                  for subpacket in packet["subpackets"]]
        return 1 if values[0] == values[1] else 0


def part_one():
    pos = 0
    total_versions = 0
    while pos < len(bits):
        pos, new_packet, total_versions = read_packet(
            pos, total_versions, subpacket=False)
        # print(new_packet)
        packets.append(new_packet)
    return total_versions


def part_two():
    total_value = 0
    for packet in packets:
        total_value = eval_subpackets(packet)
    return total_value


first = perf_counter()
print(part_one())
print("part one computed in " + str(perf_counter() - first) + " seconds")
second = perf_counter()
print(part_two())
print("part two computed in " + str(perf_counter() - second) + " seconds")

print("completely computed in " + str(perf_counter() - start) + " seconds")
