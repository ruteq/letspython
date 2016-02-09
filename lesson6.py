import datetime

a=[2,0,8,7,4,5,9,6,1,3]

print (a)
n=len(a)
m=n-1
while m>0:
 for i in range(m):
   if a[i]>a[i+1]:
    x=a[i]
    a[i]=a[i+1]
    a[i+1]=x
 m=m-1
print(a)

def avg_time(a):
    avg_list = a[:]
    avg_list.remove(min(avg_list))
    avg_list.remove(max(avg_list))
    avg_out = sum(avg_list) / len(avg_list)
    return(avg_out)




