import pyautogui
import time


times_searched = 0


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
    times_searched += 1
    print(f'Trained {times_searched} times.')
    print('Waiting 2 hours...')
    # sleeping for 2 hours + 100 seconds
    time.sleep(7300)



time.sleep(5)
while True:
    find_and_click_search_field()
    searcher()
    
    
    
