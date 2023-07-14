number=int(input())
hour=number//3600
minute=(number % 3600)//60
second=(number % 3600)%60
print(hour, minute ,second)