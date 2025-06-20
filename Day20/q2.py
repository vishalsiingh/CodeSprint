def solve(arr):
    n = len(arr)
    nge = [-1] * n
    nse = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            nge[i] = stack[-1]
        stack.append(i)

    
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            nse[i] = stack[-1]
        stack.append(i)
    res = []
    for i in range(n):
        g = nge[i]
        res.append(arr[nse[g]] if g != -1 and nse[g] != -1 else -1)

    return res
n = int(input())
arr = list(map(int, input().split()))
print(*solve(arr))
