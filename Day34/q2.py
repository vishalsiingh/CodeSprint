import bisect
houses=list(map(int,input().split()))
heaters=sorted(map(int,input().split()))
print(max(min(abs(h-heaters[bisect.bisect_left(heaters,h)-1]) if bisect.bisect_left(heaters,h)>0 else float('inf'),
               abs(h-heaters[bisect.bisect_left(heaters,h)]) if bisect.bisect_left(heaters,h)<len(heaters) else float('inf'))
          for h in houses))














