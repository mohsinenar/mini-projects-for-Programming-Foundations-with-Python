
import urllib.request
import urllib.parse
def read_text():
    quotes = open(r"E:\python\check_profanity_text\text.txt")
    content = quotes.read()
    print(content)
    quotes.close();
    check_profanity(content)


def check_profanity(text_to_check):
    the_text = {'q':text_to_check}
    data = urllib.parse.urlencode(the_text)
    url = "http://www.wdylike.appspot.com/?"
    #print(url + data)
    result = urllib.request.urlopen(url + data).read()
    print(result)
    
read_text();
