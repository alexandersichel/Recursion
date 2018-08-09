def prime_number(n):
  x = 2
  while x <= (n/2):
    if n % x == 0:
      return False
    else:
      x += 1
  return True

def prime_output(n, prime_list = []):
  if n == 2:
    return (prime_list)
  else:
    if prime_number (n) == True:
      prime_output(n= n-1, prime_list = prime_list+[n])
    else:
      prime_output(n= n-1, prime_list = prime_list)

print (prime_output(10))