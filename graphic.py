import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import data_for_every_task as counting_data
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from PIL import Image, ImageTk

class GUIApp:
    root: Tk
    width = "720"
    height= "480"
    a = 1
    b = 2
    h = 3
    from enum import Enum
    class TaskOptions(Enum):
        parameter_loop_operator = 0,
        precondition_loop_operator = 1,
        parameter_and_precondition = 2
    current_option = TaskOptions.parameter_loop_operator

    _first_task_data = counting_data.FirstTaskData()
    _second_task_data = counting_data.SecondTaskData()
    _third_task_data = counting_data.ThirdTaskData()
    
    _current_counting_class = _first_task_data
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
    def build_graphic(self):
        self._current_counting_class.count_points_using_for(self.a, self.b, self.h)
        self._current_counting_class.count_points_using_while(self.a, self.b, self.h)
    def make_build_graphic_button(self):
        button = ttk.Button(text="Построить график", command=self.build_graphic) # создаем кнопку из пакета ttk
        button.pack()
# Запуск приложения
if __name__ == "__main__":
    app = GUIApp()
    app.make_window()
    app.make_sections()
    app.make_build_graphic_button()

    app.run()