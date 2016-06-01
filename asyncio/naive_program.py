import urllib.request

urls = [ "https://www.google.com","httpr://www.python.org" ]
for link in urls:
    request = urllib.request.Request( link)
    response = urllib.request.urlopen( request)
    '''
    action here
    '''
    
    
'''\
NORMAL:  sloooow
[][][]  [][]    [][]{}{}   {}{}{}    {}{}{} {}

THREADING:  still sloow
google:  [] [] []      [][]     [][][][]    []
python:   {}{}{}    {}          {}{}    {}      {}{}

ASYNCIO: Event Loop:  fastest
[] {} [] {} [] {} {}{}{} [][][] {}{} [][]
'''