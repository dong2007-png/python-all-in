import requests
import json

# ===================== 【固定配置：全大写】=====================
# 5个城市 = 5页数据（永远不改）
CITIES = [
    {"name": "北京", "lat": 39.90, "lon": 116.41},
    {"name": "上海", "lat": 31.23, "lon": 121.47},
    {"name": "广州", "lat": 23.13, "lon": 113.27},
    {"name": "深圳", "lat": 22.55, "lon": 114.05},
    {"name": "成都", "lat": 30.67, "lon": 104.07}
]
# 请求头（固定不改）
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
# 保存文件名（固定不改）
JSON_FILE = "天气数据.json"
# ==============================================================

# ------------------- 【普通变量：小写】-------------------
# 存储所有爬取数据（会变化）
all_data = []

# 循环爬取5页（page/city 都是临时变量，小写）
for page, city in enumerate(CITIES, 1):
    print(f"📥 正在爬取 第{page}页 | {city['name']}")

    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&daily=temperature_2m_max,temperature_2m_min,weathercode&forecast_days=3"

    res = requests.get(url, headers=HEADERS)
    data = res.json()

    data["页码"] = page
    data["城市"] = city["name"]
    all_data.append(data)

# 保存JSON文件
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

# 读取并解析JSON
with open(JSON_FILE, "r", encoding="utf-8") as f:
    parse_data = json.load(f)

# 天气翻译
weather_map = {0: "晴天", 1: "多云", 2: "少云", 3: "阴天", 45: "雾", 51: "小雨"}

# 输出清晰数据
print("\n📊 解析后数据：")
for item in parse_data:
    for i in range(3):
        print(
            f"第{item['页码']}页 | {item['城市']} | {item['daily']['time'][i]} | {weather_map.get(item['daily']['weathercode'][i], '未知')} | {item['daily']['temperature_2m_max'][i]}℃~{item['daily']['temperature_2m_min'][i]}℃")