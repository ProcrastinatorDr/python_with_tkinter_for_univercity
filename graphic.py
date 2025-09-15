import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from PIL import Image, ImageTk

class GUIApp:
    root: Tk
    width = "720"
    height= "480"
    def make_window(self):
        root = tk.Tk()
        root.title("Контрольная работа №1")
        root.geometry(self.width + "x" + self.height)
        root.resizable(False, False)
        root.attributes("-toolwindow", True)
        self.root = root
    def make_sections(self):
        label = Label(text="Таблицы с расчетами по данным") # создаем текстовую метку
        label.pack()
    def run(self):
        self.root.mainloop()
    def make_build_graphic_button(self):
        button = ttk.Button(text="Построить график") # создаем кнопку из пакета ttk
        button.pack()  
# Запуск приложения
if __name__ == "__main__":
    app = GUIApp()
    app.make_window()
    app.make_sections()
    app.make_build_graphic_button()

    app.run()