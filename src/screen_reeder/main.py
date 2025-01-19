import os, tkinter, keyboard, threading
from gtts import gTTS
from playsound import playsound


def clear_console():
    osname = os.name
    if osname == 'nt':
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For macOS & Linux


def __init__():
    clear_console()
    print('-------------\nScreen-Reeder\n-------------')

    global language, tempfile
    language = input('Input language (ex. nl, en, fr): ')
    print(f"Reading in '{language}' now...")
    print('Press CTRL+ALT+L to change language')

    userpath = os.path.expanduser('~')
    temppath = os.path.join(userpath, '.screen-reeder\\temp')
    tempfile = os.path.join(temppath, 'gTTS_output_temp.mp3')

    if os.path.exists(temppath):
        pass
    else:
        os.makedirs(temppath)


def get_selected_text():
    try:
        data = tkinter.Tk().clipboard_get().strip().replace('\n', '')
        return data
    except:
        return


def remove_old_file():
    try:
        os.remove(tempfile)
    except:
        pass


def get_keypress():
    while True:
        if keyboard.is_pressed('ctrl+alt+l'):
            __init__()
        else:
            continue
thread_get_keypress = threading.Thread(target=get_keypress, name='Get keypresses')


def play_selected_text():
    text_previous = None

    while True:
        text_selected = get_selected_text()

        if text_selected == text_previous:
            continue
        else:
            remove_old_file()
            gTTS(text=text_selected, lang=language).save(tempfile)
            playsound(tempfile)
            text_previous = text_selected


def main():
    __init__()
    thread_get_keypress.start()
    play_selected_text()