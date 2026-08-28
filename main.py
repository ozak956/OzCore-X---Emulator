import random

with open("program.txt", "r") as f:
    instrukcje = [linia.strip() for linia in f if linia.strip() != ""]

WORD_MASK = 0xFFFF
RAM_MASK = 0xFF

opcode = ""
arg_1 = 0
arg_2 = 0
arg_3 = 0

a_reg = [0] * 8
b_reg = [0] * 8
a = 0
b = 0
cout = 0

ram = [0] * 256
ram_pointer = 0

io_input = [0] * 16
io_output = [0] * 16

flag_check = True
flag_True = True
flag_0 = False
flag_not0 = False
flag_carryOut = False
flag_notCarryOut = False
flag_Parity = False
flag_notParity = False
flag_A_than_B = False
flag_B_than_A = False
flag_A_equals_B = False
flag_First_Bit_1 = False
flag_Last_Bit_1 = False

main_pointer = 0
running = True

def InstructionToArguments():
    global arg_1, arg_2, arg_3, main_pointer, opcode
    line = instrukcje[main_pointer]
    czesci = line.split()

    opcode = czesci[0]
    arg_1 = int(czesci[1]) if len(czesci) > 1 else 0
    arg_2 = int(czesci[2]) if len(czesci) > 2 else 0
    arg_3 = int(czesci[3]) if len(czesci) > 3 else 0

def RegSave():
    global a, b
    a = a_reg[arg_1]
    b = b_reg[arg_2]

def CoutSave():
    global cout, a_reg, b_reg
    UpdateResultFlags(cout)
    cout &= WORD_MASK
    a_reg[arg_3] = cout
    b_reg[arg_3] = cout

def IntLoad():
    global a_reg, b_reg
    value = arg_1 & WORD_MASK
    a_reg[arg_2] = value
    b_reg[arg_2] = value

def UpdateResultFlags(raw_result):
    global flag_0, flag_not0
    global flag_carryOut, flag_notCarryOut
    global flag_Parity, flag_notParity
    global flag_First_Bit_1, flag_Last_Bit_1

    flag_carryOut = raw_result > WORD_MASK or raw_result < 0
    flag_notCarryOut = not flag_carryOut

    result = raw_result & WORD_MASK

    flag_0 = result == 0
    flag_not0 = result != 0

    flag_Parity = bin(result).count("1") % 2 == 0
    flag_notParity = not flag_Parity

    flag_First_Bit_1 = bool(result & 0x8000)
    flag_Last_Bit_1 = bool(result & 0x0001)

def UpdateCompareFlags():
    global flag_A_than_B, flag_B_than_A, flag_A_equals_B

    flag_A_than_B = a > b
    flag_B_than_A = b > a
    flag_A_equals_B = a == b

def CheckFlag(flag_id):
    if flag_id == 0:
        return flag_True
    elif flag_id == 1:
        return flag_0
    elif flag_id == 2:
        return flag_not0
    elif flag_id == 3:
        return flag_carryOut
    elif flag_id == 4:
        return flag_notCarryOut
    elif flag_id == 5:
        return flag_Parity
    elif flag_id == 6:
        return flag_notParity
    elif flag_id == 7:
        return flag_A_than_B
    elif flag_id == 8:
        return flag_B_than_A
    elif flag_id == 9:
        return flag_A_equals_B
    elif flag_id == 10:
        return flag_First_Bit_1
    elif flag_id == 11:
        return flag_Last_Bit_1

    return False

while running:
    if main_pointer >= len(instrukcje):
        running = False
        break

    InstructionToArguments()
    main_pointer += 1

    if opcode == "NOP":
        print("NOP")

    elif opcode == "ADD":
        print("ADD")
        RegSave()
        cout = a + b
        print(cout)
        CoutSave()

    elif opcode == "SUB":
        print("SUB")
        RegSave()
        cout = a - b
        print(cout)
        CoutSave()

    elif opcode == "AND":
        print("AND")
        RegSave()
        cout = a & b
        print(cout)
        CoutSave()

    elif opcode == "NAD":
        print("NAND")
        RegSave()
        cout = ~(a & b)
        print(cout)
        CoutSave()

    elif opcode == "XOR":
        print("XOR")
        RegSave()
        cout = a ^ b
        print(cout)
        CoutSave()

    elif opcode == "XNR":
        print("XNOR")
        RegSave()
        cout = ~(a ^ b)
        print(cout)
        CoutSave()

    elif opcode == "ORR":
        print("OR")
        RegSave()
        cout = a | b
        print(cout)
        CoutSave()

    elif opcode == "NOR":
        print("NOR")
        RegSave()
        cout = ~(a | b)
        print(cout)
        CoutSave()

    elif opcode == "A++":
        print("A++")
        RegSave()
        cout = a + 1
        print(cout)
        CoutSave()

    elif opcode == "A--":
        print("A--")
        RegSave()
        cout = a - 1
        print(cout)
        CoutSave()

    elif opcode == "NOT":
        print("NOT")
        RegSave()
        cout = ~a
        print(cout)
        CoutSave()

    elif opcode == "RSH":
        print("RSH")
        RegSave()
        cout = a >> 1
        print(cout)
        CoutSave()

    elif opcode == "LSH":
        print("LSH")
        RegSave()
        cout = a << 1
        print(cout)
        CoutSave()

    elif opcode == "INT":
        print("INT")
        IntLoad()

    elif opcode == "MOV":
        print("MOV")
        a_reg[arg_1] = a_reg[arg_2]
        b_reg[arg_1] = b_reg[arg_2]

    elif opcode == "JMP":
        print("JMP")
        flag_check = CheckFlag(arg_2)

        if flag_check:
            main_pointer = arg_1
        else:
            print("Warunek nie spełniony!")

    elif opcode == "JMR":
        print("JMR")
        flag_check = CheckFlag(arg_2)

        if flag_check:
            main_pointer = a_reg[arg_1]
        else:
            print("Warunek nie spełniony!")

    elif opcode == "RND":
        print("RND")
        random_value = random.randint(0, WORD_MASK)
        a_reg[arg_3] = random_value
        b_reg[arg_3] = random_value

    elif opcode == "CLR":
        print("CLR")
        a_reg[arg_3] = 0
        b_reg[arg_3] = 0

    elif opcode == "RIO":
        print("RIO")
        io_output[arg_3] = a_reg[arg_1] & WORD_MASK

    elif opcode == "IOR":
        print("IOR")
        value = io_input[arg_1] & WORD_MASK
        a_reg[arg_3] = value
        b_reg[arg_3] = value

    elif opcode == "RTP":
        print("RTP")
        ram_pointer = a_reg[arg_1] & RAM_MASK

    elif opcode == "CLP":
        print("CLP")
        ram_pointer = 0

    elif opcode == "RP+":
        print("RP+")
        ram_pointer = (ram_pointer + 1) & RAM_MASK

    elif opcode == "RP-":
        print("RP-")
        ram_pointer = (ram_pointer - 1) & RAM_MASK

    elif opcode == "LRR":
        print("LRR")
        value = ram[ram_pointer] & WORD_MASK
        a_reg[arg_3] = value
        b_reg[arg_3] = value

    elif opcode == "SRR":
        print("SRR")
        ram[ram_pointer] = a_reg[arg_1] & WORD_MASK

    elif opcode == "CMP":
        print("CMP")
        RegSave()
        UpdateCompareFlags()
        UpdateResultFlags(a - b)

    elif opcode == "WFE":
        print("Press ENTER to continue...")
        input()

    elif opcode == "END":
        print("END")
        running = False
        print("Program END")

    elif opcode == "MLT":
        print("MLT")
        RegSave()
        cout = a * b
        print(cout)
        CoutSave()

    elif opcode == "DIV":
        print("DIV")
        RegSave()

        if b == 0:
            print("CPU ERROR: DIVISION BY ZERO")
            running = False
        else:
            cout = a // b
            print(cout)
            CoutSave()

    else:
        print(f"UNKNOWN OPCODE: {opcode}")
        running = False