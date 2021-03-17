import urllib.request
import re

def readURL(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def readLocation(html_page):
    #html_page='abacda window ajdfia\nasdjfida'
    matchObj = re.match( r'.*name="location" content="(.*?)" .*"', html_page, re.S)
    if matchObj:
        return matchObj.group(1)
    return None

def readPrice(html_page):
    matchObj = re.match( r'.*<span class="total">(.*?)</span.*', html_page, re.S)
    if matchObj:
        return matchObj.group(1)
    return None

def readArea(html_page):
    matchObj = re.match( r'.*<li><span class="label">建筑面积</span>(.*?)</li>.*', html_page, re.S)
    if matchObj:
        return matchObj.group(1)
    return None

def readPosition(html_page):
    matchObj = re.match( r".*resblockPosition:'(.*?)'.*", html_page, re.S)
    if matchObj:
        return matchObj.group(1)
    return None

def processHTML(html_page):
    result=[]
    result.append(readLocation(html_page))
    result.append(readPrice(html_page))
    result.append(readArea(html_page))
    result.append(readPosition(html_page))
    print(result)
    return result

def getCrawlerResult(url):
    return processHTML(readURL(url))

if __name__=='__main__':
    content=readURL('https://bj.lianjia.com/xiaoqu/1111027378316/')
    processHTML(content)

    content=readURL('https://bj.lianjia.com/ershoufang/101104047080.html#around')
    processHTML(content)

    content=readURL('https://bj.lianjia.com/ershoufang/101108885741.html')
    processHTML(content)