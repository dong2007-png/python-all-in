import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd


# --- 档次二练习8：豆瓣电影Top250爬虫 (保存Excel版) ---
def get_douban_top250():
    base_url = "https://movie.douban.com/top250"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://movie.douban.com/"
    }

    all_movies = []

    for page in range(10):
        url = f"{base_url}?start={page * 25}"
        print(f"正在爬取第 {page + 1} 页...")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                print(f"请求失败，状态码: {response.status_code}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            movie_items = soup.find_all('div', class_='item')

            if not movie_items:
                print("未找到电影列表，停止爬取")
                break

            for item in movie_items:
                # --- 精准提取逻辑 ---
                info_div = item.find('div', class_='info')
                if not info_div: continue

                # 1. 电影名
                hd_div = info_div.find('div', class_='hd')
                title_tag = hd_div.find('span', class_='title') if hd_div else None
                title = title_tag.get_text(strip=True) if title_tag else "未知电影"

                # 2. 评分
                bd_div = info_div.find('div', class_='bd')
                rating_tag = bd_div.find('span', class_='rating_num') if bd_div else None
                rating = rating_tag.get_text(strip=True) if rating_tag else "无评分"

                # 3. 评价人数
                rating_people = "0"
                if rating_tag:
                    rating_parent = rating_tag.parent
                    if rating_parent:
                        span_list = rating_parent.find_all('span')
                        if span_list:
                            rating_people = span_list[-1].get_text(strip=True).replace('人评价', '')

                # 4. 导演
                director = "未知导演"
                info_p_tag = bd_div.find('p') if bd_div else None
                if info_p_tag:
                    info_text = info_p_tag.get_text(strip=True)
                    if '导演:' in info_text:
                        director_part = info_text.split('主演:')[0] if '主演:' in info_text else info_text
                        director = director_part.replace('导演:', '').strip()

                all_movies.append({
                    "排名": len(all_movies) + 1,
                    "电影名称": title,
                    "评分": rating,
                    "评价人数": rating_people,
                    "导演": director
                })
                print(f"已获取: {title}")

            time.sleep(random.uniform(1, 3))

        except Exception as e:
            print(f"爬取出错: {e}")
            break

    return all_movies


def save_data_to_excel(data_list, filename="douban_top250.xlsx"):
    """
    使用 Pandas 将数据保存为 Excel (.xlsx) 文件
    """
    if not data_list:
        print("没有数据可保存！")
        return

    # 1. 转换为 DataFrame
    df = pd.DataFrame(data_list)

    # 2. 调整列顺序
    df = df[["排名", "电影名称", "评分", "评价人数", "导演"]]

    # 3. 保存为 Excel
    # index=False: 不保存行索引
    df.to_excel(filename, index=False)

    print(f"\n✅ 数据已成功保存至: {filename}")
    print(f"共保存 {len(df)} 条数据。")


if __name__ == "__main__":
    # 1. 爬取数据
    movies = get_douban_top250()

    # 2. 打印预览
    if movies:
        print("\n--- Top 5 电影预览 ---")
        for i, m in enumerate(movies[:5]):
            print(f"{i + 1}. {m['电影名称']} | {m['评分']}")

    # 3. 保存到 Excel
    save_data_to_excel(movies)