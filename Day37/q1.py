def numberToWords(num):
  
  to19='One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thiirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'. split()
  tens='Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
  thousands=['','Thousand','Million','Billion'] 
  def words(n):
    if n==0:return[]
    if n<20:return[to19[n-1]]
    if n<100:return [tens[n//10-2]]+words(n%10)
    return [to19[n//100-1]]+['Hundred']+words(n%100)
  if num==0: return 'Zero'
  res,i=[],0
  while num:
    if num%1000:
      res=words(num%1000) + ([thousands[i]] if thousands[i] else []) + res
    num //=1000
    i+=1
  return ' '.join(res)
num=int(input("Ente a number :"))
print(numberToWords(num))









