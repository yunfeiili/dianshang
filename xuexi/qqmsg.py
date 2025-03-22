

# 使用psutil来判断QQ是否登录
import psutil,time,os
import pyperclip
import pyautogui as gui

people = '游戏G'	# 好友全称
message = '初次测试数据：注意：这里我基本上都是用的pyautogui操作鼠标和键盘执行自动化操作，其中的鼠标移动、点击坐标是根据我自身情况编写的，所以可能其他人不太适用，如果需要使用则需根据具体情况修改。'	# 发送的消息

QQ_dir = r'‪D:\QQ\Bin\QQ.exe'	# QQ路径

# 判断QQ是否登录
def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:  # 通过PID判断
        if psutil.Process(pid).name() == process_name:
            return isinstance(pid,int)

# 发送消息
def send_msg(people, msg):
    if proc_exist('QQ.exe'):
        # 打开QQ主界面
        gui.moveTo(1580, 1080, duration=0.2)
        gui.moveTo(1580, 1050, duration=0.2)
        gui.click()
        time.sleep(0.5)
    else:
        # 登录QQ
        QQ_login()

    # 搜索好友并打开聊天窗口
    gui.moveTo(1532, 155, duration=0.2) #搜索好友输入框的鼠标位置
    gui.click()
    time.sleep(0.5)
    pyperclip.copy(people)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    gui.hotkey('Enter')
    time.sleep(1)

    for i in range(1,3):
    # 输入需要发送的信息
        gui.moveTo(285, 524, duration=0.2)  #发送消息输入框的鼠标位置游戏G

        gui.click()
        pyperclip.copy(msg)
        gui.hotkey('ctrl', 'v')
        gui.hotkey('Enter')

    # 隐藏主界面并退出聊天界面
    gui.moveTo(980, 35, duration=0.5) #关闭窗口的鼠标位置
    gui.click()
    time.sleep(0.5)
    gui.hotkey('ctrl', 'w')

# 登录QQ
def QQ_login():
    os.startfile(QQ_dir)
    print('正在打开QQ')
    time.sleep(3)
    gui.moveTo(960, 695, duration=0.5)
    gui.click()
    time.sleep(10)

if __name__ == "__main__":

    send_msg(people,message)

# 获取鼠标位置
# while True:
#     last_position=gui.position()
#     if last_position!=gui.position():
#         print(gui.position())
