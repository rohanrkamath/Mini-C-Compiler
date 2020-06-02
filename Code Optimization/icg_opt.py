import re
import sys
import operator

istemp = lambda s : bool(re.match(r"^t[0-9]*$", s)) #if regex used, returns 1		


def eval_binary_expr(op1, oper, op2): #converts op1,op2 to int
    op1,op2 = int(op1), int(op2)
    if(oper=='+'):
        return op1+op2
    elif(oper=='-'):
        return op1-op2
    elif(oper=='*'):
        return op1*op2
    elif(oper=="/"):
        return op1/op2
    elif(oper=="<"):
        return op1<op2
    elif(oper==">"):
        return op1>op2
    elif(oper=="||"):
        return op1 or op2
    elif(oper=="&&"):
        return op1 and op2
	


def printICG(list_of_lines): #print removing white spaces
    for i in list_of_lines:
        print(i.strip())

def add_to_dict(x,y): 
    temp_vars[x]=y

def constant_folding(list_of_lines):
    for i in range(len(list_of_lines)):
        if(len(list_of_lines[i].split())==5): #splitting line sndf check if length is 5
            x=list_of_lines[i].split()
            if x[2].isdigit() and x[4].isdigit(): #is 2 and 4 are digits, join
                s=" "
                t=s.join([x[0],x[1],str(eval_binary_expr(x[2],x[3],x[4])),"\n"]) #operation
                list_of_lines[i]=t #list of lines

def func1(x,i):
    if x[2].isdigit() or x[4].isdigit(): 
        if x[2].isdigit():
            if(x[4] in temp_vars): #if temp var
                s=" "
                val=temp_vars[x[4]] #takes value of 4
                s=s.join([x[0],x[1],x[2],x[3],val,"\n"])
                list_of_lines[i]=s
                return list_of_lines
        elif x[4].isdigit():
            if(x[2] in temp_vars):
                s=" "
                val=temp_vars[x[2]]
                s=s.join([x[0],x[1],val,x[3],x[4],"\n"])
                list_of_lines[i]=s
                return list_of_lines
    else:
        if(x[2] in temp_vars):
            if(x[4] in temp_vars):
                s=" "
                val1=temp_vars[x[2]]
                val2=temp_vars[x[4]]
                s=s.join([x[0],x[1],val1,x[3],val2,"\n"])
                list_of_lines[i]=s
                return list_of_lines
            else:
                val=temp_vars[x[2]]
                s=" "
                s=s.join([x[0],x[1],val,x[3],x[4],"\n"])
                list_of_lines[i]=s
                return list_of_lines
        if(x[4] in temp_vars):
            val=temp_vars[x[4]]
            s=" "
            s=s.join([x[0],x[1],x[2],x[3],val,"\n"])
            list_of_lines[i]=s
            return list_of_lines


def constant_propagation():
    #print(list_of_lines)
    for i in range(len(list_of_lines)):
        temp_list=list_of_lines[i].split()
        l=len(temp_list)
        if(l==3):
            add_to_dict(temp_list[0],temp_list[2])
        elif(l==5):
            func1(temp_list,i)

def remove_dead_code(list_of_lines) :
	#print (list_of_lines)
	num_lines = len(list_of_lines)
	temps_on_lhs = set()
	for line in list_of_lines :
		tokens = line.split()
		if istemp(tokens[0]) :
			temps_on_lhs.add(tokens[0])

	useful_temps = set()
	#calculating all the token
	for line in list_of_lines :
		tokens = line.split()
		if len(tokens) >= 3 :
			if istemp(tokens[2]) :	
				useful_temps.add(tokens[2])
		if len(tokens) >= 2 :
			if istemp(tokens[1]) :
				useful_temps.add(tokens[1])

	#to find all the useless tokens in a set	
	temps_to_remove = temps_on_lhs - useful_temps
	new_list_of_lines = []
	for line in list_of_lines :
		tokens = line.split()
		if tokens[0] not in temps_to_remove :
			new_list_of_lines.append(line)
	if num_lines == len(new_list_of_lines) :
		return new_list_of_lines
	return remove_dead_code(new_list_of_lines)

if __name__ == "__main__" :
        list_of_lines = []
        f = open("INPUT.txt", "r")
        for line in f :
            list_of_lines.append(line)
        f.close()
        temp_list=list()
        temp_vars=dict()

        print('ICG: ')
        printICG(list_of_lines)
        print("\n\n")

        print('After Constant Propagation')
        constant_propagation()
        printICG(list_of_lines)
        print("\n\n")

        print('After Constant Folding: ')
        constant_folding(list_of_lines)
        printICG(list_of_lines)
        print("\n\n")

        print('After Dead Code Elimination: ')
        list_of_lines=remove_dead_code(list_of_lines)
        list_of_lines=remove_dead_code(list_of_lines)
        printICG(list_of_lines)

