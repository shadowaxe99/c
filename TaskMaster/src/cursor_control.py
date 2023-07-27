```python
import pyautogui

class CursorControl:
    def __init__(self):
        self.cursor_position = pyautogui.position()

    def get_cursor_position(self):
        self.cursor_position = pyautogui.position()
        return self.cursor_position

    def set_cursor_position(self, x, y):
        pyautogui.moveTo(x, y)
        self.cursor_position = (x, y)

    def move_cursor(self, x, y):
        pyautogui.move(x, y)
        self.cursor_position = pyautogui.position()

    def click(self, button='left'):
        pyautogui.click(button=button)

    def double_click(self, button='left'):
        pyautogui.doubleClick(button=button)

    def right_click(self):
        pyautogui.rightClick()

    def middle_click(self):
        pyautogui.middleClick()

    def scroll(self, clicks):
        pyautogui.scroll(clicks)

if __name__ == "__main__":
    cursor = CursorControl()
    cursor.set_cursor_position(100, 200)
    cursor.move_cursor(50, -50)
    cursor.click()
    cursor.scroll(10)
```