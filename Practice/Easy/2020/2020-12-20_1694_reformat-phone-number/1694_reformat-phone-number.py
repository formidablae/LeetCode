class Solution:
    def reformatNumber(self, number: str) -> str:
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
