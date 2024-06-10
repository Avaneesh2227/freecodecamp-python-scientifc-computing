def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    problem=[i.split() for i in problems]
    line1=[]
    line2=[]
    line3=[]
    line4=[]
    for j in problem:
        if not j[0].isdigit() or not j[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if j[1]!= "+" and j[1]!="-":
            return "Error: Operator must be '+' or '-'."
        big = len(max(j, key = len))
        if big>4:
            return 'Error: Numbers cannot be more than four digits.'
        line1.append(" "*(abs(len(j[0])-big)+2)+j[0]+(" "*4))
        line2.append(j[1]+" "*(abs(len(j[2])-big)+1)+j[2]+(" "*4))
        line3.append("-"*(big+2)+(" "*4))
        if show_answers:
            result=str(solver(int(j[0]),int(j[1]+j[2]),lambda x,y:x+y))
            line4.append(" "*abs(len(result)-len(line3[-1].rstrip()))+result+" "*4)
            #line4.append(" "*((len(result)-len(line3[-1]))-1)+result)
    stringf=""
    stringf+=("".join(line1)).rstrip()+"\n"
    stringf+=("".join(line2)).rstrip()+"\n"
    if not show_answers:
        stringf+=("".join(line3)).rstrip()
    else:
        stringf+=("".join(line3)).rstrip()+"\n"
        stringf+=("".join(line4)).rstrip()
    
    #stringf+=("".join(line4))

    #lines = stringf.split('\n')
    #single_line_string = '\\n'.join(lines)
    #print(single_line_string)


    return(stringf)


def solver(num1,num2,func):
    return func(num1,num2) 

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
