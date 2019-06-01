# <ul class="comicNav">
#    <li> prev可以一直向前遍历，遍历按钮
# <div id="bottom" class="box">
#    <img src="图片.imag">,图片所在地

# 打开漫画页，找到第一页（<）,从前往后遍历，每一页的imag解析出来，保存到folder，点击“下一页<li>里面” ，循环，直到无法向后（‘#’）
# 组织成文件后，zip压缩，通过rss发送给kindle？
import downloadXkcd

if __name__ == '__main__':
    url = 'https://xkcd.com/'
    downloadXkcd.downloadPageContent(url)
