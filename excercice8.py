def FirstFactorial(num):
  n=1
  x=1
  for n in range(int(num)):
      n+=1
      x*=n
  return x

# keep this function call here 
print(FirstFactorial(input()))
