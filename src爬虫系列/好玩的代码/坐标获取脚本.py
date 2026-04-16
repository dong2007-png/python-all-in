import pyautogui
import time

print("=" * 50)
print("智慧树弹窗坐标获取工具（稳定版）")
print("=" * 50)

def get_pos(name):
    print(f"\n请把鼠标移动到【{name}】正中心，放稳后按回车键...")
    input()  # 按回车继续
    x, y = pyautogui.position()
    print(f"✅ {name} 坐标：X={x}, Y={y}")
    return (x, y)

# 依次获取三个点
a = get_pos("A选项（对）圆圈")
b = get_pos("B选项（错）圆圈")
close = get_pos("底部关闭按钮")

print("\n" + "="*40)

print("📋 最终精确坐标：")
print(f"A选项：X={a[0]}, Y={a[1]}")
print(f"B选项：X={b[0]}, Y={b[1]}")
print(f"关闭按钮：X={close[0]}, Y={close[1]}")
print("="*40)