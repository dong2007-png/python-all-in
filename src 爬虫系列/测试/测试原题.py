# 思路：1.使用requests库发送请求，获取网页数据。
#     2.使用lxml库解析网页数据，获取手机列表，用xpath定位解析
#     3.遍历手机列表，获取手机名称、参考价格、目前评分、点评数、京东价格、天猫价格、京东链接、天猫链接、手机图片。
#     4.将获取到的数据保存到列表中。
#     5.将列表转换为DataFrame，并保存为excel文件。
#     6.将图片保存到指定目录。

import requests
from lxml import etree
import pandas as pd

all_data = []
page = [1,2,3,4]
for i in page:
    url = f"https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_{i}.html"
    fake_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0",
        "cookie":"z_pro_city=s_provice%3Dhunan%26s_city%3Dchangsha; userProvinceId=20; userCityId=326; userCountyId=1591; userLocationId=153320; realLocationId=153320; userFidLocationId=153320; m_area_city_new=changsha; m_area_cityId_new=326; m_area_provinceId_new=20; ip_ck=5cCH5vPxj7QuMjc2MTk2LjE3NzcyODY5NjU%3D; listSubcateId=57; zol_check=1234414281; zol_cipher=55e94226a9a8ade810406179bce5349f; Adshow=1; lv=1777294551; vn=2; questionnaire_pv=1777248027"
    }

    response = requests.get(url, headers=fake_headers)
    if response.status_code == 200:
        html = etree.HTML(response.text)
        phone_list = html.xpath('//li[@data-follow-id]')
        print(f"在第{i}页找到 {len(phone_list)} 款手机")
        for phone in phone_list:
            #手机名称
            phone_title = phone.xpath('.//h3/a/@title')[0]
            print(phone_title)
            #参考价格
            phone_price = phone.xpath('.//b[@class="price-type"]')[0].text
            print(phone_price)
            #目前评分
            score_list = phone.xpath('.//span[@class="score"]/text()')
            phone_score = score_list[0] if score_list else ''
            print("目前评分：",phone_score)
            #点评数
            comment_list = phone.xpath('.//a[@class="comment-num"]/text()')
            phone_comment=comment_list[0] if comment_list else ''
            print("点评数：",phone_comment)
            #京东价格
            jingdong_price = phone.xpath('.//div[@class="item-b2cprice"]/a[1]/text()')
            phone_jd=jingdong_price[0] if jingdong_price else '无'
            print("京东价格：",phone_jd)
            #天猫价格
            tianmao_price = phone.xpath('.//div[@class="item-b2cprice"]/a[2]/text()')
            phone_tm=tianmao_price[0] if tianmao_price else '无'
            print("天猫价格：",phone_tm)
            #京东链接
            jingdong_link = phone.xpath('.//div[@class="item-b2cprice"]/a[1]/@href')
            phone_jd_link=jingdong_link[0] if jingdong_link else '无'
            print("京东链接：",phone_jd_link)
            #天猫链接
            tianmao_link = phone.xpath('.//div[@class="item-b2cprice"]/a[2]/@href')
            phone_tm_link=tianmao_link[0] if tianmao_link else '无'
            print("天猫链接：",phone_tm_link)
            #手机图片
            img_tag = phone.xpath('.//a[@class="pic"]/img')
            phone_img = img_tag[0].get('.src') if img_tag else ''
            img_data = requests.get(phone_img, headers=fake_headers).content
            with open(f"phone-images/{len(all_data) + 1}.jpg", "wb") as f:
                        f.write(img_data)
            all_data.append({
                "手机图片":len(all_data)+1,
                "手机名称": phone_title,
                "参考价格": phone_price,
                "目前评分": phone_score,
                "点评数": phone_comment,
                "京东价格": phone_jd,
                "京东购买链接": phone_jd_link,
                "天猫价格": phone_tm,
                "天猫购买链接": phone_tm_link,
            })
df = pd.DataFrame(all_data)
df.to_excel("zol_phone.xlsx", index=False)
print("所有手机信息已保存")

