import re
import sys

reg_available = ['R0','R1','R2','R3','R4','R5','R6','R7','R8','R9','R10']
arth_op = {'+':'ADD','*':'MUL','-':'SUB','/':'DIV'}
cond_op = {'==':'BE','!=':'BNE','<':'BGT','>':'BLT','<=':'BLE','>=':'BGE'}

reg_values = {}
reg_occupied  = []

def check_function(operand): #checks if value is stored in a register 
    for key in reg_values.keys(): #key -> register, value->register value
        if(operand == reg_values[key]):
            reg = key
            reg_occupied.remove(reg)
            reg_occupied.append(reg)
            return reg

    if(len(reg_available) != 0): #case were the value doesnt exist in register
        reg = reg_available.pop(0)
        reg_occupied.append(reg)
    else:
        reg = reg_occupied[0]
        reg = reg_occupied.pop(0)
        reg_values.pop(reg)
        reg_occupied.append(reg)

    print("\t MOV",reg,operand) #storing in memory
    reg_values[reg]=operand
    return reg


def arth_function(line,operation):
    reg1 = check_function(line[2]) #check on 2
    if(line[4].isnumeric()):
        reg2 = line[4] #reg2 stores line 4 is numeric, else checks.
    else:
        reg2 = check_function(line[4])

    if(len(reg_available) != 0): 
        reg3 = reg_available.pop(0)
        reg_occupied.append(reg3)
    else:
        reg3 = reg_occupied[0]
        reg3 = reg_occupied.pop(0)
        reg_values.pop(reg3)
        reg_occupied.append(reg3)

    print("\t",operation,reg3,reg1,reg2) #add r3 r2 r1
    regex_match= re.findall("^t[0-9]*$",line[0]) #checks for loop, join
    if(len(regex_match)):
        pass
    else:
        print("\t STR",reg3,line[0]) #if not store

    reg_values[reg3] = line[0] #storing the value in reg3 


def conditional_operation(line):
    reg1 = check_function(line[2])
    if(line[4].isnumeric()):
        reg2 = line[4]
    else:
        reg2 = check_function(line[4])

    print("\t CMP",reg1,reg2)

condition_used = " "


def function_eval(line):
    global condition_used
    line = line.split()

    for operator in arth_op:
        if operator in line and len(line) == 5 :
            arth_function(line,arth_op[operator]) #parameter line, arth_op[operator] --> value from arith_dict(ex ADD)
            return
    
    for operator in cond_op:
        if operator in line and len(line) == 5 :
            condition_used = cond_op[operator] #storing the condition
            conditional_operation(line)
            return
    if(len(line) == 1):
        regex_match = re.findall("^[A-Za-z0-9]*:$",line[0]) #jump, loop
        if(len(regex_match)): 
            print(line[0])
            return
    
    if 'ifFalse' in line and len(line) == 4: #34
        print("\t",condition_used,line[3])  
        return  

    if 'goto' in line and len(line) == 2: #44
        print("\t B",line[1])
        return
    
    if '=' in line and len(line) == 3:
        reg1 = check_function(line[2])
        print("\t STR",reg1,line[0]) #1
        regex_match= re.findall("^t[0-9]*$",line[2]) #if line[2] is strings, is string retirns 1
        if(line[2].isnumeric() or len(regex_match)):
            pass
        else:
            if(len(reg_available) != 0):
                reg2 = reg_available.pop(0)
                reg_occupied.append(reg2)
            else:
                reg2 = reg_occupied[0]
                reg2 = reg_occupied.pop(0)
                reg_values.pop(reg2)
                reg_occupied.append(reg2)
        
        for reg in reg_values.keys():
            if(reg_values[reg] == line[0]):
                reg_values.pop(reg)
                reg_occupied.remove(reg)
                reg_available.append(reg)
                break
        
        if(not line[2].isnumeric() and not len(regex_match)):
            reg_values[reg2] = line[0]
        if(reg_values[reg1].isnumeric() or len(regex_match)):
            reg_occupied.remove(reg1)
            reg_occupied.append(reg1)
            reg_values[reg1] = line[0]
        return 
print("ICG:")
print("\n")
f = open('example.txt','r')
message = f.read()
print(message)
f.close()
print("\n\n")
print("TARGET CODE:")
print("\n")
read = open("example.txt", "r")
for i in read:
    function_eval(i) #iterate through input file

