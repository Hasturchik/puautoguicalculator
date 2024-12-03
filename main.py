import pyautogui
import os
import time

buttons = {'1':'1.png', '2':'2.png', '7':'7.png','+':'plus.png', '=':'equals.png' }
def open_calculator():
    if os.name == "nt":
        os.system("start calc")
    elif os.uname().sysname == "Darwin":
        os.system("open -a Calculator")
    elif os.uname().sysname == "Linux":
        os.system("gnome-calculator")
    else:
        raise OSError("Операционная система не поддерживается.")
    time.sleep(2)

def locate_and_click(image_path):
    button = pyautogui.locateOnScreen(image_path, confidence=0.9)
    if button is None:
        raise ValueError(f"Кнопка '{image_path}' не найдена на экране.")
    pyautogui.click(pyautogui.center(button))

def main():
    open_calculator()

    try:
        locate_and_click(buttons['1'])
        locate_and_click(buttons['2'])
        locate_and_click(buttons['+'])
        locate_and_click(buttons['7'])
        locate_and_click(buttons['='])
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
