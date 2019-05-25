# 将keyword直接输在command line上面，浏览器自动打开（n个tags？）
# 可输入k个keyword，同时打开 k*n个new tag

# 读取command line ， 获取len(sys.argv)
# 打开google搜索框，输入keywords[i](loop,有没有可能使用generator(没必要)
# 打开新的tag？

# 意味着
# 获取sys.argv, 传给requests, requests获取搜索结果(html)，分析html page找到每一个链接(result相关)，打开相应的链接（通过new tags）