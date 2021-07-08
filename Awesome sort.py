T=int(input())
for _ in range(T):
    N=int(input())
    arr=list(map(int,input().strip().split()))[:N]
    ev1=sorted([e for e in arr if (e%5==0) and (e%2==0)])
    ev1.sort(reverse=True)
    ev2=sorted([e for e in arr if (e%5!=0) and (e%2==0)])
    ev2.sort(reverse=True)
    od=([e for e in arr if e%2!=0])
    print(ev1+ev2+od)
