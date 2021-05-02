f __name__ == '__main__':
    n,m = map(int, input().split())
    array=list(map(int, input().split()))
    like=set(map(int, input().split()))
    dislike=set(map(int, input().split()))
    sum1=0
    sum2=0
    for k in array:
        if k in like:
            sum1=sum1+1
        if k in dislike:
            sum2=sum2+1
    print(sum1-sum2)