from numpy import multiply
import utils

DAY = 16


def sum_packets(packet :dict):
    tot = 0
    for p in packet["subpackets"]:
        tot += p["value"]
    packet["value"] = tot

def multiply_packets(packet :dict):
    tot = 1
    for p in packet["subpackets"]:
        tot *= p["value"]
    packet["value"] = tot
    
def min_packets(packet :dict):
    mini = float('inf')
    for p in packet["subpackets"]:
        if p["value"] < mini:
            mini = p["value"]
    packet["value"] = mini

def max_packets(packet :dict):
    maxi = float(0)
    for p in packet["subpackets"]:
        if p["value"] > maxi:
            maxi = p["value"]
    packet["value"] = maxi

def greater_packets(packet :dict):
    sub_p = packet["subpackets"]
    packet["value"] = int( sub_p[0]["value"] > sub_p[1]["value"] )
    
def less_packets(packet :dict):
    sub_p = packet["subpackets"]
    packet["value"] = int( sub_p[0]["value"] < sub_p[1]["value"] )

def equal_packets(packet :dict):
    sub_p = packet["subpackets"]
    packet["value"] = int( sub_p[0]["value"] == sub_p[1]["value"] )


OPERATIONS = [ sum_packets, multiply_packets, min_packets, max_packets, None, greater_packets, less_packets, equal_packets ]


def decode_value(string :str) -> tuple:     # returns decimal value and length of string consumed
    s = ""
    consumed = 0
    while string[consumed] == "1":  # part A and B of value (if present)
        s += string[consumed+1 : consumed+5]
        consumed = consumed + 5
    s += string[consumed+1 : consumed+5]   # part C of value (end of packet)
    return int(s, 2), consumed + 5


def decode(string :str) -> dict:
    p_version = int(string[:3], 2)
    p_type = int(string[3:6], 2)
    
    if p_type == 4:
        p_value, p_length = decode_value(string[6 :])
        return {
            "version" : p_version,
            "type" : p_type,
            "value" : p_value,
            "length" : p_length + 6,
            "subpackets" : [],
        }

    else:
        p_length_type = string[6]
        subpackets = []
        
        if p_length_type == "0":
            sub_length = int(string[7:22], 2)
            curr_length = 0
            while curr_length < sub_length:
                p = decode(string[22 + curr_length :])
                subpackets.append(p)
                curr_length += p["length"]
            p_length = curr_length + 22
        
        else:
            sub_num = int(string[7:18], 2)
            curr_length = 0
            while sub_num > 0:
                p = decode(string[18 + curr_length :])
                subpackets.append(p)
                curr_length += p["length"]
                sub_num -= 1
            p_length = curr_length + 18
    
        return {
            "version": p_version,
            "type" : p_type,
            "subpackets" : subpackets,
            "length" : p_length,
            "operation" : OPERATIONS[p_type]
        }


def sum_versions(packet :dict) -> int:
    tot = packet["version"]
    for p in packet["subpackets"]:
        tot += sum_versions(p)
    return tot


def compute(packet :dict) -> int:
    if not packet["subpackets"]:
        return packet["value"]
    
    for p in packet["subpackets"]:
        p["value"] = compute(p)

    packet["operation"](packet)
    return packet["value"]


message_hex = utils.read_input(DAY)[0]
message_dec = int(message_hex, 16)
message_bin = format(message_dec, f'0>{len(message_hex)*4}b')

# part 1
packet_hierarchy = decode(message_bin)
utils.print_answer(1, sum_versions(packet_hierarchy))
utils.print_answer(2, compute(packet_hierarchy))