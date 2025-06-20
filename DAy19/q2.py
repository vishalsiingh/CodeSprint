from collections import defaultdict

def process_ops(ops):
    stack = []
    freq = defaultdict(int)
    res = []

    for op in ops:
        if op.startswith("PUSH"):
            x = op.split()[1]
            stack.append(x)
            freq[x] += 1

        elif op == "POP":
            if stack:
                top = stack.pop()
                freq[top] -= 1

        elif op == "COUNT":
            if stack:
                res.append(str(freq[stack[-1]]))
            else:
                res.append("EMPTY")

    return res


n = int(input())
ops = [input().strip() for _ in range(n)]


print("\n".join(process_ops(ops)))
