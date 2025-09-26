import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import data_for_every_task as counting_data
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from PIL import Image, ImageTk

class GUIApp:
    width = "1600"
    height= "900"
    

    _first_task_data = counting_data.FirstTaskData()
    _second_task_data = counting_data.SecondTaskData()
    _third_task_data = counting_data.ThirdTaskData()
    first_task = 1
    second_task = 2
    third_task = 3
    task_class_by_chosen_option: dict[int, counting_data.DataClass] = {
        first_task : _first_task_data,
        second_task : _second_task_data,
        third_task : _third_task_data,
    }
    
    def __init__(self) -> None:
        self.make_window()
        self.current_radio_button_chosen = IntVar(value=self.first_task)
        self.current_counting_option  = self.task_class_by_chosen_option[self.current_radio_button_chosen.get()]
        self.a = DoubleVar(value=self.current_counting_option.a)
        self.b = DoubleVar(value=self.current_counting_option.b)
        self.h = DoubleVar(value=self.current_counting_option.h)

    def make_window(self):
        self.root = tk.Tk()
        self.root.title("Контрольная работа №1")
        self.root.geometry(self.width + "x" + self.height)
        self.root.resizable(False, False)
        self.root.attributes("-toolwindow", True)
    

    #_current_counting_class = task_class_by_user_choice[str(user_choice)]

    def make_sections(self):
        self.make_choosing_option_frame()
        self.make_graphic_settings_frame()
        self.make_graphic_data_frame()
        #label = Label(text="Таблицы с расчетами по данным") # создаем текстовую метку
        #label.pack()
    def make_choosing_option_frame(self):
        self.choosing_option_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=5)
        self.make_task_options(self.choosing_option_frame)
        self.choosing_option_frame.pack(anchor=W)
        
    def make_graphic_settings_frame(self):
        self.graphic_settings_frame = ttk.Frame(borderwidth=1, relief=SOLID)
        self.graphic_settings_frame.pack(anchor=N)
        self.task_image = PhotoImage(file=self.current_counting_option.image_path) 
        self.task_image_label = ttk.Label(master=self.graphic_settings_frame, image=self.task_image)
        self.task_image_label.pack()
        self.make_parameters_section()
        self.make_build_graphic_button(self.graphic_settings_frame)
    def update_a_if_is_valid(self):
        self.current_counting_option.a = self.check_if_number(self.current_counting_option.a, self.a_entry.get())  
        return True
    def update_b_if_is_valid(self):
        self.current_counting_option.b = self.check_if_number(self.current_counting_option.b, self.b_entry.get()) 
        return True
    def update_h_if_is_valid(self):
        self.current_counting_option.h = self.check_if_number(self.current_counting_option.h, self.h_entry.get()) 
        return True
    def check_if_number(self, current_value, user_input):
        try:  
            new_value = float(user_input)  
            print("Converted float:", new_value)  
            return new_value
        except ValueError:  
            print("Invalid input. Please enter a valid number.") 
            return current_value
    def make_parameters_section(self):
        self.parameters_frame = ttk.Frame(master=self.graphic_settings_frame,borderwidth=1, relief=SOLID)
        self.a_label = ttk.Label(master=self.parameters_frame, text="a = ")
        self.b_label = ttk.Label(master=self.parameters_frame, text="b = ")
        self.h_label = ttk.Label(master=self.parameters_frame, text="h = ")
        self.a_label.grid(row=0, column=0)
        self.b_label.grid(row=1, column=0)
        self.h_label.grid(row=2, column=0)
        self.a_entry = ttk.Entry(master=self.parameters_frame, validate="focusout", textvariable=self.a, validatecommand=self.update_a_if_is_valid)
        self.b_entry = ttk.Entry(master=self.parameters_frame, validate="focusout", textvariable=self.b, validatecommand=self.update_b_if_is_valid)
        self.h_entry = ttk.Entry(master=self.parameters_frame, validate="focusout", textvariable=self.h, validatecommand=self.update_h_if_is_valid)
        self.a_entry.grid(row=0, column=1)
        self.b_entry.grid(row=1, column=1)
        self.h_entry.grid(row=2, column=1)
        self.parameters_frame.pack()
    
    def make_build_graphic_button(self, frame):
        button = ttk.Button(master=frame, text="Построить график", command=self.build_graphic) # создаем кнопку из пакета ttk
        
        button.pack()

    def make_graphic_data_frame(self):
        self.graphic_data_frame = ttk.Frame(master=self.graphic_settings_frame,borderwidth=1, relief=SOLID)
        #x = self.current_counting_option.points_counted_using_for.keys()
        #y = self.current_counting_option.points_counted_using_for.values()

        self.graphic_figure = Figure()
        # graphic = self.graphic_figure.add_subplot()
        #graphic.plot(x, y)
        self.graphic_canvas = FigureCanvasTkAgg(self.graphic_figure, master=self.graphic_data_frame)  
        #self.graphic_canvas.draw()  
        self.graphic_canvas.get_tk_widget().pack()
        self.build_graphic()
        self.graphic_data_frame.pack()

        self.make_tables(self.graphic_data_frame)
        
        #plt.grid(True)

    def make_tables(self, frame):
        def make_table(points: dict, title):
            table_frame = ttk.Frame(master=frame, borderwidth=1, relief=SOLID, width=500, height=60)
            
            table_frame.pack(expand=False, fill='none')
            table_frame.pack_propagate(False)
            scrollbar = ttk.Scrollbar(master=table_frame, orient=HORIZONTAL)
            scrollbar.pack(side="bottom",fill="x", expand=False)

            tree = ttk.Treeview(master=table_frame, columns=tuple(range(points.__len__())), show="", selectmode="none", xscrollcommand=scrollbar.set)
            scrollbar.config(command=tree.xview)

            column_width = 40
            for column in tree["columns"]:
                tree.column(column, width=column_width, anchor="center")

            ndigits = 3
            rounded_keys = []
            rounded_values = []
            for key, value in points.items():
                rounded_keys.append(round(key, ndigits))
                rounded_values.append(round(value, ndigits))
            tree.insert("", END, values = tuple(rounded_keys))
            tree.insert("", END, values = tuple(rounded_values))

            tree.pack(expand=False, fill='none', side='top')
        make_table(self.current_counting_option.points_counted_using_for, "for")
        make_table(self.current_counting_option.points_counted_using_while, "while")
        

    
        #plt.show()
    def run(self):
        self.root.mainloop()
    #def build_graphic(self):
      #  self._current_counting_class = self.task_class_by_chosen_option[self.current_radio_button_chosen.get()] 
      #  self._current_counting_class.count_points_using_for()
      #  self._current_counting_class.count_points_using_while()

    def change_task(self):
        self.current_counting_option = self.task_class_by_chosen_option[self.current_radio_button_chosen.get()]
        self.task_image = PhotoImage(file=self.current_counting_option.image_path)
        self.task_image_label.configure(image=self.task_image)
        self.update_parameters()
        self.a_entry.configure(textvariable=self.a)
        self.b_entry.configure(textvariable=self.b)
        self.h_entry.configure(textvariable=self.h)
        self.build_graphic()

    def update_parameters(self):
        self.a.set(self.current_counting_option.a)
        self.b.set(self.current_counting_option.b)
        self.h.set(self.current_counting_option.h)
    def build_graphic(self):
        """Обновляет график с текущими данными"""
        
        self.count_points()
        # Получаем актуальные данные
        x = list(self.current_counting_option.points_counted_using_for.keys())
        y = list(self.current_counting_option.points_counted_using_for.values())

        # Очищаем предыдущий график
        self.graphic_figure.clear()
    
        # Создаем новый график
        graphic = self.graphic_figure.add_subplot()
        graphic.plot(x, y)
        graphic.set_xlabel('X')
        graphic.set_ylabel('Y')
        graphic.set_title('График функции')
        self.graphic_figure.tight_layout()
        print(self.current_counting_option.a)
        # Обновляем canvas
        self.graphic_canvas.draw()
        for a in x:
            print(round(a,2), end=" ")
        print()
    def count_points(self):
        self.current_counting_option.count_points_using_for()
        self.current_counting_option.count_points_using_while()
    def make_task_options(self, frame):
        self.radiobuttons = []
        self.radiobuttons.append(ttk.Radiobutton(master=frame, text="1-е задание", value=self.first_task, variable=self.current_radio_button_chosen, command=self.change_task))
        self.radiobuttons.append(ttk.Radiobutton(master=frame, text="2-е задание", value=self.second_task, variable=self.current_radio_button_chosen, command=self.change_task))
        self.radiobuttons.append(ttk.Radiobutton(master=frame, text="3-е задание", value=self.third_task, variable=self.current_radio_button_chosen, command=self.change_task))
        for radiobutton in self.radiobuttons:
            radiobutton.pack()
        #self.first_task_button = 
        #self.second_task_button = 
        #self.second_task_button = 


# Запуск приложения
if __name__ == "__main__":
    app = GUIApp()
    #app.make_window()
    app.make_sections()
    #app.make_choosing_option_frame()

    app.run()