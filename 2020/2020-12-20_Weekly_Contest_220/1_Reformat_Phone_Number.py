def reformatNumber(number):
    number = number.replace(" ", "").replace("-", "")
    if len(number) < 4:
        return number
    elif len(number) == 4:
        return number[0:2] + "-" + number[2:4]
    else:
        answer = []
        i = 3
        while i < len(number) - 1:
            answer.append(number[i - 3:i])
            i += 3
        if len(number) - i > 0:
            answer.append(number[i - 3: i - 1])
            answer.append(number[i - 1:])
        else:
            answer.append(number[i - 3:])
        # print(answer)
        answer = "-".join(answer)
        return answer


inp1 = "1-23-45 6"
inp2 = "123 4-567"
inp3 = "123 4-5678"
inp4 = "12"
inp5 = "--17-5 229 35-39475 "
print(reformatNumber(inp1))
print(reformatNumber(inp2))
print(reformatNumber(inp3))
print(reformatNumber(inp4))
print(reformatNumber(inp5))
