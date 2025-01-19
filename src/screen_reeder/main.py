import os, tkinter
from gtts import gTTS
from playsound import playsound


def __init__():
    print('-------------\nScreen-Reeder\n-------------')

    global language, tempfile
    language = input('Input language (ex. nl, en, fr): ')
    print(f"Talking in '{language}' now...")

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
    play_selected_text()