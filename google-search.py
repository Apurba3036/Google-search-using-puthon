from googlesearch import search
search_query=input("Hey! Ask me anything: ")
for i in search( search_query,tld='co.in', lang='en', tbs='0',  num=10, start=0, stop=10, pause=2.0):
    print(i)
