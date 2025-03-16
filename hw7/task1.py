def tribonacci(n, answer = [0, 0, 1]) :
    if n < 3: yield answer
    else:
        for i in range(n-2):
            next_num = sum(answer[-3:])
            answer.append(next_num)
        yield answer
       

