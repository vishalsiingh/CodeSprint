from collections import Counter
import heapq
def reorganizeString(s):
    freq=Counter(s)
    heap=[(-cnt,ch) for ch,cnt in freq.items()]
    heapq.heapify(heap)
    res,prev=[],(0,'')
    while heap:
      cnt,ch=heapq.heappop(heap)
      res.append(ch)
      if prev[0]<0:
        heapq.heappush(heap,prev)
      prev=(cnt+1,ch)
    result=''.join(res)
    return result if all(result[i] !=result[i+1] for i in range(len(result)-1)) else ""
s=input("Enter the String: ")
print("Rearranged string: ",reorganizeString(s))



















