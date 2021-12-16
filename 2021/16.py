import utils
from functools import reduce

DAY = 16

OPERATIONS = [
    lambda x,y : x+y,           # sum subpackets
    lambda x,y : x*y,           # multiply subpackets
    lambda x,y : min(x,y),      # minimum of subpackets
    lambda x,y : max(x,y),      # maximum of subpackets
    None,                       # value packet
    lambda x,y : int(x>y),      # greater then
    lambda x,y : int(x<y),      # less then
    lambda x,y : int(x==y),     # equal to
]

def decode_value(string :str) -> tuple:
    """returns decimal value and length of string consumed"""
    s = ""
    consumed = 0
    while string[consumed] == "1":  # part A and B of value (if present)
        s += string[consumed+1 : consumed+5]
        consumed = consumed + 5
    s += string[consumed+1 : consumed+5]   # part C of value (end of packet)
    return int(s, 2), consumed + 5


def decode(string :str) -> dict:
    """returns a packet as a dictionary"""
    p_version = int(string[:3], 2)
    p_type = int(string[3:6], 2)
    p_value, p_length, p_operation = 0, 6, None
    p_subpackets = []
    
    if p_type == 4: # value packet
        p_value, length = decode_value(string[6 :])
        p_length += length
    
    else:   # operation packet
        p_length_type = string[6]
        p_operation = OPERATIONS[p_type]

        if p_length_type == "0":    # subpackets defined by length of string
            sub_p_length = int(string[7:22], 2)
            p_length += 16
            while p_length - 22 < sub_p_length:
                p = decode(string[p_length :])
                p_subpackets.append(p)
                p_length += p["length"]
            
        else:   # subpackets defined by number of subpackets
            sub_p_num = int(string[7:18], 2)
            p_length += 12
            while sub_p_num > 0:
                p = decode(string[p_length :])
                p_subpackets.append(p)
                p_length += p["length"]
                sub_p_num -= 1

    return {
        "version": p_version,
        "type" : p_type,
        "subpackets" : p_subpackets,
        "operation" : p_operation,
        "value" : p_value,
        "length" : p_length,
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
    
    packet["value"] = reduce( packet["operation"], map(lambda p : p["value"], packet["subpackets"]) )

    return packet["value"]


message_hex = utils.read_input(DAY)[0]
message_dec = int(message_hex, 16)
message_bin = format(message_dec, f'0>{len(message_hex)*4}b')
packet_hierarchy = decode(message_bin)

# part 1
utils.print_answer(1, sum_versions(packet_hierarchy))
# part 2
utils.print_answer(2, compute(packet_hierarchy))