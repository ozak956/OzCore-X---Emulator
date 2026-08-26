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

a_reg = [0,0,0,0,0,0,0,0]  # Rejestr główny A
b_reg = [0,0,0,0,0,0,0,0]  # Rejestr główny B

a = 0 #Rejestr pomocnicyz
b = 0 #Rejestr pomocnicyz
cout = 0

#Flagi
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
    a_reg[arg_3] = cout
    b_reg[arg_3] = cout   

while running:
    if main_pointer >= len(instrukcje):
        running = False
        break
    InstructionToArguments()
    main_pointer += 1
    print(opcode)

    # Sprawdzanie instrukcji
    if opcode == "NOP":
        print("NOP")
