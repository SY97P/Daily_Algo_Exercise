def get_lower_value(cnt, stack):
    result = ""
    for i in reversed(range(len(stack))):
        if stack[i] == '0':
            result = ''.join(stack[:i+1]) + '110'*cnt + ''.join(stack[i+1:])
            break
    else:
        result = '110'*cnt + ''.join(stack)
    return result


def parse_token(st):
    stack = []
    cnt = 0
    for i, s in enumerate(st):
        if len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and s == '0':
            cnt += 1
            stack.pop()
            stack.pop()
            continue
        stack.append(s)
    return cnt, stack


def solution(strs):
    answer = []
    for st in strs:
        cnt, stack = parse_token(st)
        result = get_lower_value(cnt, stack)
        answer.append(result)
    return answer


def main():
    answer = solution(["1110", "100111100", "0111111010"])
    print(answer)


if __name__ == '__main__':
    main()
