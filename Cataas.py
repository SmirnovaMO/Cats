from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO



def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


def exit():
    window.destroy()


window = Tk()
window.title('Cats!')
window.geometry('600x520')

label = Label()
label.pack()

mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Загрузить нового котика', command=set_image)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=exit)
mainmenu.add_cascade(label='Click here', menu=filemenu)

url = 'https://cataas.com/cat'

set_image()

window.mainloop()
