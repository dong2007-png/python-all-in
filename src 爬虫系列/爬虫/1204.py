import requests
import json
import pandas as pd  # 将pandas重命名为pd
# pandas是第三方库 需要安装 pip install pandas
# pandas操作excel需要依赖openpyxl  所以也需要安装    pip install openpyxl
# 可以一起安装 pip install pandas openpyxl
# 1. 准备好所有地区的id
chan_ids = [727, 728, 729, 730, 731, 936, 1219]

# 2. 构建请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}
# 构建存储所有数据的列表
all_data = []
# 3. 定义爬虫函数
def spider():
    for chan_id in chan_ids:
        # 函数内部构建完整的url
        url = f'https://act-api-takumi-static.mihoyo.com/content_v2_user/app/16471662a82d418a/getContentList?iAppId=43&iChanId={chan_id}&iPageSize=50&iPage=1&sLangKey=zh-cn&iOrder=6'
        # print(url)  # 拼接完成的url
        # 4. 发起请求
        res = requests.get(url, headers=headers)
        # print(res.text)
        # 4.1 把获取到的json数据转换为python字典
        res_data = res.json()['data']['list']   # 这是requests的函数
        """
        732_0 头像图片
        732_1 全身图
        732_5 中文配音员,
        732_6 日文配音员
        iInfoId 角色id
        """
        for item in res_data:
            sTitle = item['sTitle']  # 角色名
            sExt = json.loads(item['sExt']) # 转换存放角色信息的字典 json模块中的函数
            img_url = sExt['732_0'][0]['url']  # 头像url
            iInfoId = item['iInfoId']    # 角色id
            scv_cn = sExt['732_5']  # 中文配音员
            scv_jp = sExt['732_6']  # 日文配音员
            # print(sTitle, img_url, iInfoId, scv_cn, scv_jp)
            # 5 把解析到的数据做成一个本地的持久化存储的文件  --> excel文件
            all_data.append([sTitle, img_url, iInfoId, scv_cn, scv_jp])
            # [[sTitle, img_url, iInfoId, scv_cn, scv_jp],
            # [sTitle, img_url, iInfoId, scv_cn, scv_jp]]
# 运行爬虫函数
spider()
# 查看获取的所有角色数据
# print(all_data)
# 通过python去构建表格并且写入数据 (借助pandas这个库)
df = pd.DataFrame(all_data, columns=['角色名', '图片url', 'id', '中配', '日配'])
# 把数据存储excel中
df.to_excel('原神启动.xlsx', index=False)
print('数据保存成功')