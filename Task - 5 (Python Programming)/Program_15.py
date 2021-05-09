import re
N=int(input())
for _ in range(N):
    card_no=input().strip()
    r=re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',card_no)
    if r:
        process= "".join(r.group(0).split('-'))
        final_card_no= re.search(r'(\d)\1{3,}',process)
        if final_card_no:
            print("Invalid")
        else:
            print("Valid")
    else:           
        print("Invalid")
