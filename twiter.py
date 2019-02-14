import requests
import codecs
from lxml import etree

path = r'C:\Users\luopan\Desktop\twitter网页\Columbia University (@Columbia) _ Twitter.html'

content = codecs.open(path,'r','utf-8').read()

html = etree.HTML(content)
infos = html.xpath('//*[@id="stream-items-id"]/li')
for info in infos:
    p = info.xpath('div[1]/div[2]/div[2]/p')[0]  #这里先取到p标签
    content = p.xpath('string(.)')  #然后使用这个方法可以得到p标签下的所有文本，这样就不会漏掉了
    pic = info.xpath('div[1]/div[2]/div[3]/div/div/div/div/img/@src')  你前面的info没有定位到循环点，要写到li，这样没图片就返回为空列表
    print(content,pic)