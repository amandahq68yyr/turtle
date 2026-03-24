import turtle
import random

# 画布和圆圈参数设置
window = 500      # 窗口大小（像素）
radius = 180      # 圆的半径
dash = 12         # 虚线中每段的长度
center_x = 0      # 圆心的 x 坐标
center_y = 0      # 圆心的 y 坐标
spead = 50        # 速度参数（暂未使用）

# 初始化画布
screen = turtle.Screen()
screen.setup(window, window)      # 设置窗口大小
screen.bgcolor("white")           # 背景色设为白色
turtle.colormode(255)             # 颜色模式设为 RGB (0-255)

# 画边界圆圈
turtle.penup()                    # 抬笔，移动时不画线
turtle.goto(0, -radius)           # 移动到圆的底部起点
turtle.pendown()                  # 落笔，准备画线
turtle.pensize(1)                 # 设置线条粗细
turtle.circle(radius)             # 画一个圆作为边界

# 创建小海龟（用于随机行走）
bob = turtle.Turtle()
bob.shape("circle")               # 设置海龟形状为圆形
bob.penup()                       # 抬笔
bob.goto(0, 0)                    # 移动到圆心
bob.pendown()                     # 落笔

# 主循环：随机行走
while True:
    # 随机选择一个方向和步数
    angle = random.randint(0, 360)       # 随机角度（0-360度）
    steps = random.randint(5, 20)        # 随机步数（5-20步）
    bob.setheading(angle)                # 设置海龟朝向

    # 随机生成一个 RGB 颜色
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    bob.pencolor(r, g, b)                # 设置画笔颜色

    # 画虚线：循环多步，每步画一段、空一段
    for i in range(steps):
        # 检测是否即将越界
        if bob.distance(center_x, center_y) >= radius - 5:
            bob.penup()                  # 抬笔，避免回中心时画线
            bob.goto(center_x, center_y) # 瞬移回圆心，重新开始
            break                        # 跳出循环，开始新的随机行走
        
        bob.pendown()                    # 落笔画线
        bob.forward(dash)                # 前进一段（画实线部分）
        bob.penup()                      # 抬笔
        bob.forward(dash)                # 前进一段（留空白部分）

turtle.done()                             # 保持窗口打开
