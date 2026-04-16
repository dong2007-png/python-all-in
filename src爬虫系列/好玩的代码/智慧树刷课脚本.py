import pyautogui
import random
import time
import cv2
import numpy as np

# ==================== 配置（适配你当前的窗口化界面） ====================
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
MOUSE_THRESHOLD = 10  # 你一动鼠标，脚本立刻停手
last_x, last_y = pyautogui.position()

# 你的界面专用坐标（根据截图校准）
# 窗口化（当前界面）
OPTION_A = (770, 570)
OPTION_B = (770, 630)
CLOSE_BTN = (960, 770)
PLAY_AREA = (480, 880)


# ==================== 工具函数 ====================
def random_sleep(a, b):
    time.sleep(random.uniform(a, b))


def is_user_operating():
    """检测你是否在操作鼠标，一动就暂停"""
    global last_x, last_y
    curr_x, curr_y = pyautogui.position()
    dist = ((curr_x - last_x) ** 2 + (curr_y - last_y) ** 2) ** 0.5
    last_x, last_y = curr_x, curr_y
    return dist > MOUSE_THRESHOLD


def human_move(x, y):
    """模拟真人鼠标移动，不是瞬移"""
    cx, cy = pyautogui.position()
    # 轻微偏移，模拟人手抖动
    offset_x = random.randint(-5, 5)
    offset_y = random.randint(-5, 5)
    # 曲线移动，更自然
    pyautogui.moveTo(cx + offset_x, cy + offset_y, random.uniform(0.2, 0.4))
    pyautogui.moveTo(x + offset_x, y + offset_y, random.uniform(0.2, 0.4))


# ==================== 弹窗检测（适配你的弹窗） ====================
def detect_popup():
    """只检测你这种“弹题测验”弹窗"""
    try:
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        h, w = frame.shape[:2]
        # 只截取弹窗所在的区域，避开视频和侧边栏
        crop = frame[350:800, 600:1100]
        gray = cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY)
        # 弹窗特征：大面积纯白背景 + 黑色文字
        white_bg = cv2.inRange(gray, 245, 255)
        black_text = cv2.inRange(gray, 0, 60)
        white_count = cv2.countNonZero(white_bg)
        black_count = cv2.countNonZero(black_text)
        # 只有同时满足两个条件，才判定为弹窗
        return white_count > 35000 and black_count > 8000
    except:
        return False


# ==================== 核心操作（按你的坐标执行） ====================
def choose_answer():
    """随机选A或B选项"""
    x, y = random.choice([OPTION_A, OPTION_B])
    human_move(x, y)
    random_sleep(0.4, 0.8)
    pyautogui.click()
    print(f"✅ 已选择选项，坐标：({x}, {y})")


def close_popup():
    """点击弹窗底部的关闭按钮（你截图里的那个）"""
    x, y = CLOSE_BTN
    human_move(x, y)
    random_sleep(0.5, 1.0)
    pyautogui.click()
    print(f"✅ 已点击关闭按钮，坐标：({x}, {y})")


def resume_video():
    """点击视频区域恢复播放"""
    x, y = PLAY_AREA
    human_move(x, y)
    random_sleep(0.3, 0.7)
    pyautogui.click()
    print("✅ 恢复视频播放")


# ==================== 主程序 ====================
print("=" * 60)
print("🚀 智慧树专用脚本（根据你的弹窗截图校准）")
print("📌 坐标100%匹配 | 你一动鼠标就暂停")
print("⏹️  停止：Ctrl + C")
print("=" * 60)

try:
    while True:
        # 你在操作鼠标时，脚本直接跳过
        if is_user_operating():
            random_sleep(0.5, 1)
            continue

        # 检测到弹窗，执行完整流程
        if detect_popup():
            print("\n💡 检测到弹题测验，开始处理...")
            # 模拟读题，防检测
            random_sleep(3, 6)
            choose_answer()
            random_sleep(0.8, 1.5)
            close_popup()
            random_sleep(0.8, 1.5)
            resume_video()
            print("✅ 弹窗处理完毕，继续刷课\n")

        # 正常等待
        random_sleep(2, 4)

except KeyboardInterrupt:
    print("\n🛑 脚本已停止")