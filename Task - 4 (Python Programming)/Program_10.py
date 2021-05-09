def print_formatted(number):
    length = len(bin(number)[2:])
    for i in range(1,number+1):
        o = str(oct(i))[2:]
        h = str(hex(i))[2:]
        h = h.upper()
        b = str(bin(i))[2:]
        d = str(i)
        print(d.rjust(length,' ')+" "+o.rjust(length,' ')+" "+h.rjust(length,' ')+" "            +b.rjust(length,' ')+" ")
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)