def arithmetic_arranger(*input):
    result=""
    num1=[]
    symb=[]
    num2=[]
    res=[]
    num=[]
    error = None
    numbers=input[0]
    if len(numbers) > 5:
        result = "Error: Too many problems."
    else:
        for n in range(len(numbers)):
            spl_num = numbers[n].split()
            if len(spl_num[0]) > 4 or len(spl_num[2]) > 4:
                error = "Error: Numbers cannot be more than four digits."
                break
            elif spl_num[1] != '+' and spl_num[1] != '-':
                error = "Error: Operator must be '+' or '-'."
                break
            else:
              num.append(spl_num[0])
              num.append(spl_num[2])
    for n in range(len(num)):
        try:
            int(num[n])
        except:
            error="Error: Numbers must only contain digits."
    if error is None:
        for n in range(len(numbers)):
            spl_num = numbers[n].split()
            num1.append(spl_num[0])
            symb.append(spl_num[1])
            num2.append(spl_num[2])
            if symb[n] == "+":
                res.append(str(int(num1[n])+int(num2[n])))
            else:
                res.append(str(int(num1[n])-int(num2[n])))
        num1=[]
        num2=[]
        line=[]
        for n in range(len(numbers)):
            space=""
            line_str="--"
            spl_num = numbers[n].split()
            if len(spl_num[0])-len(spl_num[2]) > 0:
                num1.append(str("  "+spl_num[0]))
                for n in range(len(spl_num[0])-len(spl_num[2])):
                    space=space+" "
                num2.append(str(spl_num[1]+" "+space+spl_num[2]))
                for n in range(len(spl_num[0])):
                    line_str=line_str+"-"
                line.append(line_str)
            elif len(spl_num[0])-len(spl_num[2]) < 0:
                for n in range(len(spl_num[2])-len(spl_num[0])):
                    space=space+" "
                num1.append(str("  "+space+spl_num[0]))
                num2.append(str(spl_num[1]+" "+spl_num[2]))
                for n in range(len(spl_num[2])):
                    line_str=line_str+"-"
                line.append(line_str)
            else:
                num1.append(str("  "+spl_num[0]))
                num2.append(str(spl_num[1]+" "+spl_num[2]))
                for n in range(len(spl_num[0])):
                    line_str=line_str+"-"
                line.append(line_str)
        resl=[]
        for n in range(len(numbers)):
            space=""
            for s in range(len(line[n])-len(res[n])):
                space=space+" "
            resl.append(space+res[n])
        num1_res=str(num1[0])
        num2_res=str(num2[0])
        resl_res=str(resl[0])
        line_res=str(line[0])
        for n in range(1, len(num1)):
            num1_res=num1_res+"    "+num1[n]
            num2_res=num2_res+"    "+num2[n]
            resl_res=resl_res+"    "+resl[n]
            line_res=line_res+"    "+line[n]
        try:
            if input[1] is True:
                result=num1_res+"\n"+num2_res+"\n"+line_res+"\n"+resl_res
        except:
            result=num1_res+"\n"+num2_res+"\n"+line_res
    else:
        result=error
    return result

print(arithmetic_arranger(["3999 - 12", "100 - 3801", "9999 + 9999", "2 - 49"],True))