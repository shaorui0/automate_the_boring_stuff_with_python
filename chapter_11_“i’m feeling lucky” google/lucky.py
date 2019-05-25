#<div class="r">
#    <a href="https://www.linkedin.com/in/%E7%91%9E-%E9%82%B5-956386a1" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.linkedin.com/in/%25E7%2591%259E-%25E9%2582%25B5-956386a1&amp;ved=2ahUKEwjh6_TetrbiAhVP-qwKHZFJA3EQFjAHegQIABAB"><h3 class="LC20lb">邵瑞- EMC - 北京汽车研究总院有限公司 | LinkedIn</h3><br><div class="TbwUpd"><cite class="iUh30">https://www.linkedin.com/in/瑞-邵-956386a1</cite></div></a></div>
# 通过分析，每一个div class='r'里面都有一个arg = href（url也行），
# 获取到arg的data，即为链接，通过webbrowser打开超链接即可

#! python3
# lucky.py - Open serval Google search results

import sys, requests, webbrowser, bs4

#webbrowser.open('www.google.com')
res = requests.get('https://www.google.com.hk/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
#此时获取到了keyword搜索的html page

# TODO:parse page...
soup = bs4.BeautifulSoup(res.text)
linkElem = soup.select('.r a') # <div class="r"> <a href="..."> .r-->class r
# TODO:open href
numOpen = min(5, len(linkElem)) #top 5
for i in range(numOpen):
    webbrowser.open('https:\\google.com' + linkElem[i].get('href'))

