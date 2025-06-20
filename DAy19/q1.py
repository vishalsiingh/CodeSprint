def process_ops(ops):
    main, mins, res = [], [], []
    for op in ops:
        if op.startswith("PUSH"):
            x = int(op.split()[1])
            main.append(x)
            if not mins or x <= mins[-1]:
                mins.append(x)
        elif op == "POP":
            if main:
                if main.pop() == mins[-1]:
                    mins.pop()
        elif op == "MIN":
            res.append(str(mins[-1]) if mins else "EMPTY")
    return res

n = int(input())
ops = [input().strip() for _ in range(n)]
print("\n".join(process_ops(ops)))
