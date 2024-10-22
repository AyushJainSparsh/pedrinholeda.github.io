int n = int(input("Enter your number : "))
flag = False
for i in range(2,n):
  if n%i == 0:
    flag = True

if flag:
  print('Number is not prime')
else:
  print('Number is prime')
