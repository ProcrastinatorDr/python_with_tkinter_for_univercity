import math
class DataClass:
    # points_counted_using_for: dict = {}
    # points_counted_using_while: dict = {}
    def __init__(self):
        self.points_counted_using_for = {}
        self.points_counted_using_while = {}
        self.image_path = "" 
        self.a: float
        self.b: float
        self.h: float
    def count_points_using_for(self):
        raise NotImplementedError("Метод должен быть определен в дочернем классе!")
    def count_points_using_while(self):
        raise NotImplementedError("Метод должен быть определен в дочернем классе!")
    def get_x_values(self, points):
        return points.keys()
    def get_y_values(self, points):
        return points.values()

class FirstTaskData(DataClass):
    def __init__(self):
        super().__init__()
        self.image_path = "images/first_task.PNG"
        self.a = -2
        self.b = 2
        self.h = 0.1
        self.count_points_using_for()
        self.count_points_using_while()
    def count_points_using_for(self):
        self.points_counted_using_for = {}
        left_border = self.a
        right_border = self.b
        step = self.h
        def _count_y(x):
            y = 0
            # 1 + sin^3(x + 0.5), if    x < -0.5
            if x < -0.5:
                y = 1 + (math.sin(x + 0.5)) ** 3

            # 1,                  if x >= -0.5, and x <= 0.5
            elif x >= -0.5 and x <= 0.5:
                y = 1
        
            # 1 + sin^3(x - 0.5), if    x > 0.5
            else:
                y = 1 + (math.sin(x - 0.5)) ** 3
            return y
        steps_number = math.ceil((right_border - left_border) / step)
        for i in range(steps_number):
            x = left_border
            y = _count_y(x)

            self.points_counted_using_for[x] = y
            left_border += step

    
    # По заданию, не требуется.
    def count_points_using_while(self):
        self.points_counted_using_while = {}

class SecondTaskData(DataClass):
    def __init__(self):
        super().__init__()
        self.image_path = "images/second_task.PNG"
        self.a = -1
        self.b = 2
        self.h = 0.1
        self.count_points_using_for()
        self.count_points_using_while()
    # for
    def count_points_using_for(self):
        self.points_counted_using_for = {}
        
    # while
    def count_points_using_while(self):
        self.points_counted_using_while = {}
        left_border = self.a
        right_border = self.b
        step = self.h
        def _count_y(x):
            y = 0
            # x + e^(-x),       if    x <= 0
            if x <= 0:
                y = x + (math.e ** (-x))

            # 1,                  if x > 0, and x < 1
            elif x > 0 and x < 1:
                y = 1
        
            # 1 + (x - 1)^2, if    x >= 1
            else:
                y = 1 + ((x - 1) ** 2)
            return y
        while left_border < right_border:
            x = left_border
            y = _count_y(x)

            self.points_counted_using_while[x] = y
            left_border += step


class ThirdTaskData(DataClass):
    def __init__(self):
        super().__init__()
        self.image_path = "images/third_task.PNG"
        self.a = -2
        self.b = 2
        self.h = 0.1
        self.count_points_using_for()
        self.count_points_using_while()
    def count_points_using_for(self):
        self.points_counted_using_for = {}
        left_border = self.a
        right_border = self.b
        step = self.h
        steps_number = math.ceil((right_border - left_border) / step)
        for i in range(steps_number):
            x = left_border
            y = self._count_y(x)

            self.points_counted_using_for[x] = y
            left_border += step
    def count_points_using_while(self):
        self.points_counted_using_while = {}
        x = 0
        y = 0
        left_border = self.a
        right_border = self.b
        step =self.h
        while left_border < right_border:
            x = left_border
            y = self._count_y(x)

            self.points_counted_using_while[x] = y
            left_border += step
    def _count_y(self, x):
        y = 0
        # -cos((x + 1) / 2),       if    x <= -1
        if x <= -1:
            y = -math.cos((x + 1) / 2)

        # sin((pi * x) / 2),                  if x > -1, and x < 1
        elif x > -1 and x < 1:
            y = math.sin((math.pi * x) / 2)
        
        # cos((x - 1) / 2), if    x >= 1
        else:
            y = math.cos((x - 1) / 2)
        return y

