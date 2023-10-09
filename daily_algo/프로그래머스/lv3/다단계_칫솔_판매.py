parent = dict()
profit = dict()


def get_dept(value):
    return int(value * 0.1)


def repay(person, proceed):
    if proceed < 1 or person == '-':
        return
    dept = get_dept(proceed)
    profit[person] += proceed - dept
    repay(parent[person], dept)


def solution(enroll, referral, seller, amount):
    global parent, profit
    parent = {enroll[i]: referral[i] for i in range(len(enroll))}
    profit = {enroll[i]: 0 for i in range(len(enroll))}

    for i, a in enumerate(amount):
        repay(seller[i], a * 100)

    return [profit[e] for e in enroll]


def main():
    answer = solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                      ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                      ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])
    print(answer)


if __name__ == '__main__':
    main()
