import win32api
import win32con
import win32clipboard
import time

'''
這支程式是有關於各種模擬鍵盤操作
，只適用於windows
'''
# 按鍵對應表
VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    ' ': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0
}


# 讀取剪貼板
def read_clipboard():
    print("執行:read_clipboard() , 讀取剪貼板")
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    win32clipboard.CloseClipboard()
    return str(text)[2:-1]
    # 傳回剪貼板的內容(string)


# 寫入剪貼板
def write_clipboard(a_string):
    print("執行:write_clipboard(a_string) , 寫入剪貼板")
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()  # 這一行特別重要，經過實驗如果不加這一行的話會做動不正常
    win32clipboard.SetClipboardText(a_string)
    win32clipboard.CloseClipboard()


# 選擇游標前端全部
def select_front():
    print("執行:select_front() , 選擇游標前端全部")
    win32api.keybd_event(VK_CODE['ctrl'], 0, 0, 0)  # 按下
    win32api.keybd_event(VK_CODE['shift'], 0, 0, 0)  # 按下
    win32api.keybd_event(VK_CODE['home'], 0, 0, 0)  # 按下

    win32api.keybd_event(VK_CODE['ctrl'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起
    win32api.keybd_event(VK_CODE['shift'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起
    win32api.keybd_event(VK_CODE['home'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起


def right_arrow():
    print("執行:right_arrow()")
    win32api.keybd_event(VK_CODE['right_arrow'], 0, 0, 0)  # 按下
    win32api.keybd_event(VK_CODE['right_arrow'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起


# 檢查各種按鍵狀態
def check_all_key_state():
    """檢查各種按鍵狀態
    輸出:回傳on的按鍵，格式是pd.Series"""
    print("執行:check_all_key_state() ，檢查各按鍵狀態")
    sr = pd.Series()
    for i in VK_CODE:
        sr.at[i] = win32api.GetKeyState(VK_CODE[i])
    mask = sr.values == 1
    return sr[mask]


# 複製
def copy():
    """複製"""
    print("執行:copy()")
    win32api.keybd_event(VK_CODE['left_control'], 0, 0, 0)  # 按下
    win32api.keybd_event(VK_CODE['c'], 0, 0, 0)  # 按下
    win32api.keybd_event(VK_CODE['c'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起
    win32api.keybd_event(VK_CODE['left_control'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起


# 貼上
def paste():
    """貼上"""
    print("執行:paste()")
    win32api.keybd_event(VK_CODE['left_control'], 0, 0, 0)  # 按下
    win32api.keybd_event(VK_CODE['v'], 0, 0, 0)  # 按下
    win32api.keybd_event(VK_CODE['v'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起
    win32api.keybd_event(VK_CODE['left_control'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起


# 偵測是否按下啟動熱鍵
def start_condition():
    """偵測是否按下啟動熱鍵
    輸出:假如按下 回傳True"""
    check1 = win32api.GetAsyncKeyState(VK_CODE['ctrl']) != 0
    check2 = win32api.GetAsyncKeyState(VK_CODE['alt']) != 0
    return check1 & check2


# 偵測啟動熱鍵是否全部放開
def start_key_all_up():
    """這支程式偵測是否全部按鍵彈起來
    輸出:假如熱鍵全部放開回傳True"""
    check1 = win32api.GetAsyncKeyState(VK_CODE['ctrl']) == 0
    check2 = win32api.GetAsyncKeyState(VK_CODE['alt']) == 0
    return check1 & check2


# 關閉Num_Lock
def close_num_lock():
    """回傳原本num_lock狀態
    輸出: return 1 if num_lock is ON"""
    print("執行:close_num_lock() ，關閉Num_Lock")
    num_lock_state = win32api.GetKeyState(VK_CODE['num_lock'])
    if num_lock_state:  # return 1 if num_lock is ON
        # 關閉num_lock
        win32api.keybd_event(VK_CODE['num_lock'], 0, 0, 0)  # 按下
        win32api.keybd_event(VK_CODE['num_lock'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起
    return num_lock_state


# 復原Num_Lock
# 輸入: 之前的num lock狀態(0或1)
def return_num_lock(previous_num_lock_state):
    """復原num lock
    輸入: 之前的numlock狀態(0或1)"""
    print("執行:return_num_lock(previous_num_lock_state) ，復原Num_Lock")
    if not previous_num_lock_state == win32api.GetKeyState(VK_CODE['num_lock']):
        win32api.keybd_event(VK_CODE['num_lock'], 0, 0, 0)  # 按下
        win32api.keybd_event(VK_CODE['num_lock'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起


# 向前刪
def backspace():
    """向前刪"""
    print("執行:backspace() ，向前刪")
    win32api.keybd_event(VK_CODE['backspace'], 0, 0, 0)  # 按下
    win32api.keybd_event(VK_CODE['backspace'], 0, win32con.KEYEVENTF_KEYUP, 0)  # 彈起


# 複製程式碼
def copy_code():
    """將I beam之前的文字全部複製起來"""
    print("CopyCode---------------------------------------------------------------------------------")
    num_lock_ex_state = close_num_lock()
    cb_temp = read_clipboard()
    select_front()
    copy()
    right_arrow()
    print("開始等待剪貼簿改變")
    a = 0
    while True:
        code = read_clipboard()
        if cb_temp != code:
            print("ReadClipboard延遲了", a * 0.05, "秒")
            break
        elif a == 20:
            print("ReadClipboard延遲了", a * 0.05, "秒太久, 可能沒有複製到東西")
            break
        else:
            a = a + 1
            time.sleep(0.05)
    print("將剪貼簿恢復原狀")
    write_clipboard(cb_temp)
    return_num_lock(num_lock_ex_state)
    print("CopyCode結束----------------------------------------------------------------------------------")
    return code


# 貼上程式碼
def paste_code(choice):
    # print("output收到:", choice)
    cb_temp = read_clipboard()
    # print("之前的cb_tmp:", cb_temp)

    write_clipboard(choice)
    # 等待剪貼簿改變
    a = 0
    while True:
        code = read_clipboard()
        if cb_temp != code:
            break
        else:
            a = a + 1
            time.sleep(0.05)
    print("剪貼簿上面的資料:", code)

    print("ReadClipboard延遲了", a * 0.05, "秒")

    paste()
    time.sleep(0.5)  # 太快會導致貼上成下面ㄉ
    write_clipboard(cb_temp)  # 將剪貼簿恢復原狀
