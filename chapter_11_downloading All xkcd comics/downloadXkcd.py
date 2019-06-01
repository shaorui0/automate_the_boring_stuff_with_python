#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests,bs4,os

def downloadPageContent(url):
    os.makedirs('xkcd', exist_ok = True)
    print("download start!")
    while not url.endswith('#'):
        # TODO:download page
        print("Download the page %s" % url)
        res = requests.get(url)
        res.raise_for_status()

        noStarchSoup = bs4.BeautifulSoup(res.text)
        # TODO:find url of the comic image
            # <div id='comic'>
            #    <img src='//img_url'>
        comicElem = noStarchSoup.select('#comic img')
        if comicElem == []:
            print("couldn't find comic imag")
        else:
            comicUrl = 'http:'+ comicElem[0].get('src')
            # TODO:download image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # TODO:store img in 'xkcd'
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
            # TODO:get the prev buttom
            prevLink = noStarchSoup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')

    print("download done!")

