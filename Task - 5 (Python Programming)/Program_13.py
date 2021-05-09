from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
N=int(input())
parser = MyHTMLParser()
for _ in range(N):
    S=input()
    parser.feed(''.join(S))