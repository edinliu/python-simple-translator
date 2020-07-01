from googletrans import Translator
import googletrans as goo
import gui 
import keyboard.keyboard_windows as kbd
import time


def translate():
    translator = goo.Translator()
    kbd.copy()
    time.sleep(0.5)
    res = translator.translate(kbd.read_clipboard(), dest='zh-tw').text
    gui.show(res)

def main():
    print("翻譯軟體，作者:新莊丹鳳區劉家豪")
    # 檢查按鍵狀態
    while True:
        if (kbd.start_condition() == False) & (kbd.start_key_all_up() == True):
            print("按鍵初始狀態正常")
            break
        else:
            print("按鍵初始狀態異常，1秒後即將重新檢查")
            time.sleep(1)
            continue

    print("開始迴圈偵測熱鍵ctrl+alt")
    while True:  # making a loop
        if kbd.start_condition():
            while True:
                if kbd.start_key_all_up():
                    print('熱鍵被按下，開始執行')
                    translate()
                    break
                # time.sleep(0.1)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
