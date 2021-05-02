def average(array):
    sum=0
    for i in set(array):
        sum=sum+i
    avg=sum/len(set(array))
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)