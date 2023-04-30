import pyautogui
import time

times_searched = 0
times_worked = 0
daily_work_switch = 0  # When it reaches 24, a day has passed and can be reset to 0 after typing .daily in chat
times_daily_work_completed = 0


def find_and_click_search_field():
    confidence = 0.90
    attempts = 45
    for attempt in range(attempts):
        try:
            # Find the search field and click on it
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('images/discord_searchbar_plus.png', confidence=confidence)
            pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInCirc)
            time.sleep(1)
            pyautogui.moveRel(100, 0)
            time.sleep(1)
            pyautogui.click()
            break
        except TypeError:
            print(f"Search Field Not Found, Missed at confidence lvl {confidence}")
            confidence -= 0.01


def searcher():
    global times_searched

    pyautogui.typewrite('/trainall')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    times_searched += 1
    print(f'Trained {times_searched} times.')


def server_work():
    global daily_work_switch
    global times_worked
    global times_daily_work_completed
    print('working...')
    
    pyautogui.typewrite('.work')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    
    times_worked += 1
    print(f'Times worked: {times_worked}')
    
    # sleeping for 1 hour + 100 seconds
    time.sleep(3700)
    daily_work_switch += 1
    
    # once every 24 hours you can do daily work - below part of this function completes this. 
    print(f'daily work switch: {daily_work_switch}')
    if daily_work_switch == 24:
        time.sleep(10)
        pyautogui.typewrite('.d')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        times_daily_work_completed += 1
        print(f'Times daily work completed: {times_daily_work_completed}')
        daily_work_switch = 0

time.sleep(5)
find_and_click_search_field()
while True:
    searcher()
    server_work()
    server_work()


