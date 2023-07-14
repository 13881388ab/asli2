num = int(input("write number fo students : "))
max=0
min  = 1000
min_num=0
sum=0
a=0
for i in range(num):
    k=i+1
    print("write numaer", k ," student score ")
    score = float(input("score :"))
    sum += score
    if max < score :
        max = score
        max_num = k
    if min > score :
        min = score
        min_num = k
avarage=sum / num
print("the avarage of all class is", avarage,".")
print("maximum grade was thegrade of student numaer",max_num,"with the grade",max)
print("maximum grade was thegrade of student numaer",max_num,"with the grade",min)
