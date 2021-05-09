from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data.strip():
            print (">>> Data\n"+ data)
    def handle_comment(self, data):
        if len(data.split("\n"))>1:
            print(">>> Multi-line Comment\n"+data)
        else:
            print (">>> Single-line Comment\n"+data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()