def merge_the_tools(string, k):
    new_string=""
    a=len(string)
    b=len(string)//k
    for i in range(0,b):
        mediator=string[i*k:(i+1)*k]
        new_string=""
        for c in mediator:
            if c not in new_string:
                new_string+= c
        print(new_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)