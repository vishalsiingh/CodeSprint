from collections import Counter

def findAnagrams(logStream, pattern):
    pat_len = len(pattern)
    pat_count = Counter(pattern)
    win_count = Counter(logStream[:pat_len])
    result = []

    if win_count == pat_count:
        result.append(0)

    for i in range(pat_len, len(logStream)):
        win_count[logStream[i]] += 1
        win_count[logStream[i - pat_len]] -= 1
        if win_count[logStream[i - pat_len]] == 0:
            del win_count[logStream[i - pat_len]]
        if win_count == pat_count:
            result.append(i - pat_len + 1)

    return result


logStream = input("Enter log stream: ")
pattern = input("Enter suspicious pattern: ")

result = findAnagrams(logStream, pattern)
print("Anagram starting indices:", result)
