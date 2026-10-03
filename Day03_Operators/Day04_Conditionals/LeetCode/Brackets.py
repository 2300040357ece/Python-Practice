t = int(input())

for _ in range(t):
    A = input().strip()
    balance = 0
    max_balance = 0

    for ch in A:
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        max_balance = max(max_balance, balance)

    print('(' * max_balance + ')' * max_balance)