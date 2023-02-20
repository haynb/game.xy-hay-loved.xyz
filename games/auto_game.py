# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
import os
import time



connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '8848',
    db = 'game',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()


i = 1

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
service = Service(r"/www/games/chromedriver")
browser = webdriver.Chrome(service=service,options=options)
# cookies = {'name':"wordpress_1698359ba8f1d2acd5e6022f04256358",'value':"mail_19388864%7C1675219183%7C0qtNxG135vgswZg2d1U2h4LfMQzGTWYBHP6UkUgRxdT%7Cc71cad0a0e653b9e3d09ffad8712259d8afb583a230cf9dcf8d817f8d9541479","Domain":"www.wrmdjyx.cn","Path":"/wp-content/plugins","IsHttpOnly":False,"IsSecure":True,"IsSession":False,"Expires":"2023-02-01T22:39:40.618+08:00"},{'name':"wordpress_sec_1698359ba8f1d2acd5e6022f04256358",'value':"mail_19388864%7C1675219183%7CPpXA6uHJiOCTlAQk8xYdyJL1aQArNIVqHEHy60VBwgw%7Cfb0256bce5aa356c9b136322b14a29e882c5977d0c78dd4952b3ae75dcced978","Domain":"www.wrmdjyx.cn","Path":"/wp-content/plugins","IsHttpOnly":True,"IsSecure":True,"IsSession":False,"Expires":"2023-02-01T22:39:40.618+08:00"},{'name':"wordpress_1698359ba8f1d2acd5e6022f04256358",'value':"mail_19388864%7C1675219183%7C0qtNxG135vgswZg2d1U2h4LfMQzGTWYBHP6UkUgRxdT%7Cc71cad0a0e653b9e3d09ffad8712259d8afb583a230cf9dcf8d817f8d9541479","Domain":"www.wrmdjyx.cn","Path":"/wp-admin","IsHttpOnly":False,"IsSecure":True,"IsSession":False,"Expires":"2023-02-01T22:39:40.618+08:00"},{'name':"wordpress_sec_1698359ba8f1d2acd5e6022f04256358",'value':"mail_19388864%7C1675219183%7CPpXA6uHJiOCTlAQk8xYdyJL1aQArNIVqHEHy60VBwgw%7Cfb0256bce5aa356c9b136322b14a29e882c5977d0c78dd4952b3ae75dcced978","Domain":"www.wrmdjyx.cn","Path":"/wp-admin","IsHttpOnly":True,"IsSecure":True,"IsSession":False,"Expires":"2023-02-01T22:39:40.618+08:00"},{'name':"_EDGE_V",'value':"1","Domain":".bing.com","Path":"/","IsHttpOnly":False,"IsSecure":True,"IsSession":False,"Expires":"2024-02-11T10:45:47.741+08:00"},{'name':"MUID",'value':"17A07D41BBE3689825E86FDDBAA06918","Domain":".bing.com","Path":"/","IsHttpOnly":True,"IsSecure":False,"IsSession":False,"Expires":"2024-02-11T10:45:47.741+08:00"},{'name':"MUIDB",'value':"17A07D41BBE3689825E86FDDBAA06918","Domain":"www.bing.com","Path":"/","IsHttpOnly":False,"IsSecure":True,"IsSession":False,"Expires":"2024-02-11T10:45:47.741+08:00"},{'name':"MUIDB",'value':"17A07D41BBE3689825E86FDDBAA06918","Domain":"cn.bing.com","Path":"/","IsHttpOnly":False,"IsSecure":True,"IsSession":False,"Expires":"2024-02-11T10:45:57.338+08:00"},{'name':"USRLOC",'value':"HS=1","Domain":".bing.com","Path":"/","IsHttpOnly":True,"IsSecure":True,"IsSession":False,"Expires":"2024-02-21T10:45:46.957+08:00"},{'name':"SRCHD",'value':"AF=WCVSID","Domain":".bing.com","Path":"/","IsHttpOnly":True,"IsSecure":False,"IsSession":False,"Expires":"2024-02-21T10:45:46.957+08:00"},{'name':"SRCHUID",'value':"V=2&GUID=396BBB51F68A4876A5944D6499CDE1FB&dmnchg=1","Domain":".bing.com","Path":"/","IsHttpOnly":True,"IsSecure":False,"IsSession":False,"Expires":"2024-02-21T10:45:46.957+08:00"},{'name':"SRCHUSR",'value':"DOB=20230117","Domain":".bing.com","Path":"/","IsHttpOnly":True,"IsSecure":False,"IsSession":False,"Expires":"2024-02-21T10:45:46.957+08:00"},{'name':"MMCASM",'value':"ID=B3FFAEB354F24D49BFBE8FF9ECE14C16","Domain":".bing.com","Path":"/","IsHttpOnly":True,"IsSecure":False,"IsSession":False,"Expires":"2024-02-21T10:45:47.055+08:00"},{'name':"MUIDB",'value':"17A07D41BBE3689825E86FDDBAA06918","Domain":"www2.bing.com","Path":"/","IsHttpOnly":False,"IsSecure":True,"IsSession":False,"Expires":"2024-02-11T10:45:50.353+08:00"},{'name':"SRCHHPGUSR",'value':"SRCHLANG=zh-Hans&CW=360&CH=636&SCW=360&SCH=636&BRW=MM&BRH=MM&DPR=1.0&UTC=480&WTS=63809520349","Domain":".bing.com","Path":"/","IsHttpOnly":True,"IsSecure":False,"IsSession":False,"Expires":"2024-02-21T10:45:50.157+08:00"},{'name':"HMACCOUNT_BFESS",'value':"4A17FD1CE38BCB74","Domain":".hm.baidu.com","Path":"/","IsHttpOnly":True,"IsSecure":False,"IsSession":False,"Expires":"2024-02-21T11:35:09.083+08:00"},{'name':"Hm_lvt_54434aa6770b6d9fef104d146430b53b",'value':"1673926509,1673926823,1673927028,1673927163","Domain":".flk.npc.gov.cn","Path":"/","IsHttpOnly":False,"IsSecure":False,"IsSession":False,"Expires":"2024-01-17T11:46:02+08:00"},{'name':"PHPSESSID",'value':"o38p66nkjk2kfuadkrbs3t2304","Domain":"www.wrmdjyx.cn","Path":"/","IsHttpOnly":False,"IsSecure":False,"IsSession":False,"Expires":"0001-01-01T00:00:00"},{'name':"wordpress_logged_in_1698359ba8f1d2acd5e6022f04256358",'value':"mail_19388864%7C1675219183%7CPpXA6uHJiOCTlAQk8xYdyJL1aQArNIVqHEHy60VBwgw%7Cbc64e983d2ab291e2f68ae2342be5da899eaf01ab6c256f42801845728041f9b","Domain":"www.wrmdjyx.cn","Path":"/","IsHttpOnly":False,"IsSecure":True,"IsSession":False,"Expires":"2023-02-01T22:39:40.618+08:00"}
cookies = {'name':"PHPSESSID",'value':"t3l5sghp6pt3o5k721g4e391vo",'name':"wordpress_logged_in_1698359ba8f1d2acd5e6022f04256358",'value':"mail_19388864%7C1676531361%7CPJNBjOFU3eY0xvUyPLa4xMtI3AmjkTkyzwTYg3PawWu%7C07a6c296c9b5e1f6388804ffe10f66d6b41e018a6f1eb903cc74ddb7181c2111"}
browser.get('https://www.wrmdjyx.cn/qbyx')
# for cookie in cookies:
#     browser.add_cookie(cookie_dict=cookie)
browser.add_cookie(cookie_dict=cookies)
    

page = 1
if os.path.exists("/www/games/page.txt"):
    with open("/www/games/page.txt", "r") as file:
        content = file.read()
        if len(content) != 0:
            page = int(content)
            print("page:  ",page)
        
        
while page < 342 and i <= 10 :
    print("正在爬取第 ",page," 页")
    page_url = 'https://www.wrmdjyx.cn/qbyx/page/' + str(page)
    browser.get(page_url)
    # browser.implicitly_wait(5) # seconds
    time.sleep(5)
    html = browser.page_source
    soup=etree.HTML(html)
    kuais = soup.xpath('//*[@id="main"]/div[2]/div/div/div/div[1]/div')
    for kuai in kuais:
        biaoti = str(kuai.xpath('.//header/h2/a/text()')[0])
        
        cursor.execute("SELECT * FROM game WHERE game_name LIKE %s", ('%'+biaoti+'%',))
        # cursor.execute("SELECT * FROM game WHERE game_name LIKE '无敌'")
        result = cursor.fetchall()
        if len(result) != 0:
            continue
        # print(result)
        # print('            ' + str(len(result)))
        biaoqians = kuai.xpath('.//span/a/text()')
        bq = ''
        for biaoqian in biaoqians:
            bq = bq + str(biaoqian) + ';'
        # print (biaoqians)                                标签   ['全部游戏', '动作冒险']
        # print(biaoti)                                    标题
        img_url = str(kuai.xpath('.//img/@src')[0])               #标题大图
        # print(img_url)
        url = kuai.xpath('.//header/h2/a/@href')[0]
        browser.get(url)
        try:
            wait = WebDriverWait(browser, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ripro_v2_shop_down-2"]/div[2]/div')))
        except:
            continue
        html = browser.page_source
        soup=etree.HTML(html)
        ljs = soup.xpath('//*[@id="ripro_v2_shop_down-2"]/div[2]/div')
        jhm = soup.xpath('//*[@id="ripro_v2_shop_down-2"]/div[3]/ul/li[1]/p[2]/text()')[0]      #激活码
        video = soup.xpath('//video/@src')               #视频
        wenbens = soup.xpath('//article/div/div[2]/div/p')
        game_disc = ''
        game_img_link = ''
        for wenben in wenbens:
            if len(wenben.xpath('./img')) != 0:
                zps = wenben.xpath('./img/@src')
                for zp in zps:
                    # print(type(zp))
                    game_img_link = game_img_link + str(zp) + ';'                #文本内的图片
            for wb in wenben.xpath('./text()'):
                # print(wb)
                game_disc = game_disc + str(wb)
        
        # print(jhm)
        # i = 0
        game_link =''
        for lj in ljs :
            # if i <3:
            wz = lj.xpath('./a/@href')[0]
            browser.get(wz)
            lianjie = browser.current_url                                  #链接
            if 'www.wrmdjyx' in lianjie or 'cloud.189' in lianjie:
                lianjie = ''
            if lianjie != '':
                game_link = game_link + lianjie + ';'
        # print('标题： ' + str(biaoti[0]))
        # print('激活码： ' + str(jhm))
        # if len(video) != 0 :
        #     print('视频： ' + str(video[0]))
        # else:
        #     print('视频： ' + str(video))
        # print('文本： ' + game_disc)
        # print('图片： ' + game_img_link)
        # print('链接： ' + game_link)
        game_video = ''
        if len(video) != 0:
            game_video = str(video[0]) 
        cursor.execute(
            '''
            INSERT INTO game (game_name,game_title,game_t_img,game_video,game_dis,game_jhm,game_imgs,game_url,date)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,CURDATE())
            ''',(biaoti,bq,img_url,game_video,game_disc,str(jhm),game_img_link,game_link,)
        )
        connection.commit()
    page += 1
    i += 1
    with open("/www/games/page.txt", "w") as file:
        file.write(str(page))

        
cursor.close()
connection.close()
    
        
        
        