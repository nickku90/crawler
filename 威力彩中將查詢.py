import requests
from bs4 import BeautifulSoup

url="https://www.taiwanlottery.com.tw/index_new.aspx"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"}

html=requests.get(url,headers=headers)

sp=BeautifulSoup(html.text,"lxml")

data=sp.find_all("div",{"class":"contents_box02"})
datas=data[0].find("div",{"class":"contents_mine_tx02"}).span.text
print("期數:",datas)

order=sp.find_all("div",{"class":"ball_tx ball_green"})
order_new=[]
for i in range(6):
    order_new.append(order[i].text)
print("開出順序:",order_new)

for i in range(len(order_new)):
    order_new[i]=int(order_new[i])
order_new.sort()
for i in range(len(order_new)):
    order_new[i]=str(order_new[i])
print("大小順序:",order_new)

second=data[0].find_all("div",{"class":"ball_red"})
print("第二區:",second[0].text)
