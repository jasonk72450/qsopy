import os
import random
import sys


def get_random_text(filename):
    file_location = os.path.join('data', filename)
    with open(file_location, "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


def print_and_write_file(_id, content):
    print(f"\nProtocol {_id}:\n")
    print(content)

    filename = f"protocol_{_id}.txt"
    with open(filename, "w") as file:
        file.write(content)


def generate_all():
    print("Generating protocol files with my name =", my_name, "and my call =", my_call)
    other_call = get_random_text("call_signs.txt").upper()
    salutation = get_random_text("salutations.txt").upper()
    rst = get_random_text("rst.txt").upper()
    qth = get_random_text("qth.txt").upper()
    other_name = get_random_text("names.txt").upper()
    rig = get_random_text("rig.txt").upper()
    ant = get_random_text("ant.txt").upper()
    wx = get_random_text("wx.txt").upper()
    key = get_random_text("key.txt").upper()
    rag_chew1 = get_random_text("rag_chew1.txt").upper()
    rag_chew2 = get_random_text("rag_chew2.txt").upper()
    rag_chew3 = get_random_text("rag_chew3.txt").upper()

    text_cq = protocol_cq(other_call)
    print_and_write_file("cq", text_cq)

    text1 = protocol_1(other_call, salutation, rst, qth, other_name)
    print_and_write_file(1, text1)

    text2 = protocol_2(other_call, rig, ant, wx)
    print_and_write_file(2, text2)

    text3 = protocol_3(other_call, key)
    print_and_write_file(3, text3)

    text4 = protocol_4(other_call, rag_chew1, rag_chew2, rag_chew3)
    print_and_write_file(4, text4)

    text5 = protocol_5(other_call)
    print_and_write_file(5, text5)
    

def protocol_cq(other_call):
    return f"""
CQ CQ CQ DE {other_call} {other_call} {other_call} K
    """.strip()


def protocol_1(other_call, salutation, rst, qth, other_name):
    return f"""
{my_call} DE {other_call}
{salutation} ES TNX FER CALL
UR RST {rst} {rst}
QTH {qth} {qth}
NAME {other_name} {other_name}
OK HW? <AR>
{my_call} DE {other_call} <KN>
    """.strip()


def protocol_2(other_call, rig, ant, wx):
    power = random.randrange(5, 1501, 5)  # 5 to 1500, multiples of 5
    height = random.randrange(10, 301, 10)  # 10 to 300, multiples of 10
    temperature = random.randrange(0, 121)  # 0 to 120
    return f"""
{my_call} DE {other_call}
OK {my_name} FB ES TNX FER RPRT
RIG {rig} ES PWR {power} W
ANT {ant} UP {height} FT
WX {wx} ES TEMP {temperature} F
OK HW? <AR>
{my_call} DE {other_call} <KN>
    """.strip()


def protocol_3(other_call, key):
    age = random.randrange(12, 101)  # 12 to 100
    ham_years = random.randrange(1, age - 10)  # 1 to age-11
    return f"""
{my_call} DE {other_call}
RR {my_name} SOLID CPY
AGE {age} YRS
BEEN HAM FER {ham_years} YRS
MY KEY {key}
OK HW? <AR>  
{my_call} DE {other_call} <KN>
    """.strip()


def protocol_4(other_call, rag_chew1, rag_chew2, rag_chew3):
    return f"""
{my_call} DE {other_call}
FB {my_name} TU FER QSO
RETIRED {rag_chew1},
LIKE {rag_chew2} ES {rag_chew3},
HW? <AR> 
{my_call} DE {other_call} <KN>
    """.strip()


def protocol_5(other_call):
    return f"""
{my_call} DE {other_call}
OK {my_name} TNX FER FB QSO
ES HP CUAGN 73 <AR> 
{my_call} DE {other_call} <EE>
    """.strip()





if __name__ == '__main__':
    if len(sys.argv) > 1:
        my_name = sys.argv[1]
        my_call = sys.argv[2]
    else:
        print("App can also be run with 'python3", sys.argv[0], "[NAME] [CALL]'")
        my_name = input("Enter your name: ").upper()
        my_call = input("Enter your call: ").upper()
    generate_all()
