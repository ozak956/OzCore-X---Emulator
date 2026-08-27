import random
#Ładowanie programu
with open("program.txt", "r") as f:
    instrukcje = [
        linia.strip()
        for linia in f
        if linia.strip() != ""
    ]

# Argumenty
opcode = ""
arg_1 = 0
arg_2 = 0
arg_3 = 0

# Rejestry

a_reg = [0,4,0,0,0,0,0,0]  # Rejestr główny A
b_reg = [0,3,0,0,0,0,0,0]  # Rejestr główny B

a = 0 #Rejestr pomocnicyz
b = 0 #Rejestr pomocnicyz
cout = 0
#Cache
cache = [0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0 ]
#RAM
ram = [0] * 256
ram_pointer = 0

#I/O

io_input = [0] * 16
io_output = [0] * 16

#Flagi
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
# Inne
main_pointer = 0
running = True


def InstructionToArguments():
    global arg_1, arg_2, arg_3, main_pointer, line , opcode

    line = instrukcje[main_pointer]
    czesci = line.split()
    
    opcode = czesci[0]
    arg_1 = int(czesci[1]) if len(czesci) > 1 else 0
    arg_2 = int(czesci[2]) if len(czesci) > 2 else 0
    arg_3 = int(czesci[3]) if len(czesci) > 3 else 0
def RegSave():
    global a ,b
    a = a_reg[arg_1]
    b = b_reg[arg_2]
def CoutSave():
    global cout, a_reg , b_reg
    cout &= 0xFFFF
    a_reg[arg_3] = cout
    b_reg[arg_3] = cout   
def IntLoad():
    global a_reg , b_reg
    a_reg[arg_2] = arg_1
    b_reg[arg_2] = arg_1

while running:
    if main_pointer >= len(instrukcje):
        running = False
        break
    InstructionToArguments()
    main_pointer += 1
    

    # Sprawdzanie instrukcji
    if opcode == "NOP": #0
        print("NOP")
    elif opcode == "ADD": #1
        print("ADD")
        RegSave()
        cout = a + b
        print(cout)
        CoutSave()
    elif opcode == "SUB": #2
        print("SUB")
        RegSave()
        cout = a - b
        print(cout)
        CoutSave()
    elif opcode == "AND": #3
        print("AND")
        RegSave()
        cout = a & b
        print(cout)
        CoutSave()
    elif opcode == "NAD":#4
        print("NAND")
        RegSave()
        cout = ~(a & b)
        print(cout)
        CoutSave()
    elif opcode == "XOR":#5
        print("XOR")
        RegSave()
        cout = a ^ b
        print(cout)
        CoutSave()
    elif opcode == "XNR":#6
        print("XNOR")
        RegSave()
        cout = ~(a ^ b) 
        print(cout)
        CoutSave()
    elif opcode == "ORR":#7
        print("OR")
        RegSave()
        cout = a | b
        print(cout)
        CoutSave()
    elif opcode == "NOR":#8
        print("NOR")
        RegSave()
        cout = ~(a | b) 
        print(cout)
        CoutSave()
    elif opcode =="A++":#9
        print("A++")
        RegSave()
        cout = a + 1
        print(cout)
        CoutSave()
    elif opcode =="A--":#10
        print("A--")
        RegSave()
        cout = a - 1
        print(cout)
        CoutSave()
    elif opcode == "NOT":#11
        print("NOT")
        RegSave()
        cout = ~a
        print(cout)
        CoutSave()
    elif opcode == "RSH":#12
        print("RSH")
        RegSave()
        cout = a >> 1
        print(cout)
        CoutSave()
    elif opcode == "LSH":#13
        print("LSH")
        RegSave()
        cout = a << 1
        print(cout)
        CoutSave()
    elif opcode == "INT":#14
        print("INT")
        IntLoad()
    elif opcode == "MOV":#15
        print("MOV")
        a_reg[arg_1] = a_reg[arg_2]
        b_reg[arg_1] = b_reg[arg_2]
    elif opcode == "JMP":#16
            if flag_check == True:
                main_pointer = arg_1
            else:
                print("Warunek nie spełniony!")
    elif opcode == "JMR":#17
        print("JMR")
        if flag_check == True:
            main_pointer = a_reg[arg_1]
        else:
            print("Warunek nie spełniony!")
    elif opcode == "RND":#18
        a_reg[arg_3] = random.randint(1,65535)
        b_reg[arg_3] = random.randint(1,65535)
    elif opcode == "CLR":#19
        a_reg[arg_3] = 0
        b_reg[arg_3] = 0
    elif opcode == "RIO":
        io_output[arg_3] = a_reg[arg_1]
    elif opcode == "IOR":
        a_reg[arg_3] = io_input[arg_1]
        b_reg[arg_3] = io_input[arg_1]


