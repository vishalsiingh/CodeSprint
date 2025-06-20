def count_jewels_in_stones(jewels:str,stones:str)-> int:
  jewel_set=set(jewels)
  count=sum(stone in jewel_set for stone in stones)
  return count
jewels=input("Enter jewels string:")
stones=input("Enter stones string")
print(count_jewels_in_stones(jewels,stones))