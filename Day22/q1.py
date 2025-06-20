def trap_rainwater(n, height):
    left, right = 0, n - 1
    left_max = right_max = water = 0
    while left <= right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water
n = int(input())
height = list(map(int, input().split()))
print(trap_rainwater(n, height))
