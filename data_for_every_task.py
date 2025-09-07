import math
class DataClass:
    points_by_parameter_loop_operator: dict
    points_by_precondition_loop_operator: dict
    image_path: str = ""
    def count_points_with_parameter_loop_operator(self, a, b, h):
        raise NotImplementedError("Метод должен быть определен в дочернем классе!")
    def count_points_with_precondition_loop_operator(self, a, b, h):
        raise NotImplementedError("Метод должен быть определен в дочернем классе!")
    # Даны по условию задачи.
    from enum import Enum
    class TaskOptions(Enum):
        parameter_loop_operator = 0,
        precondition_loop_operator = 1,
        parameter_and_precondition = 2

class FirstTaskData(DataClass):
    task_image = 1
    def __init__(self, picture_path):
        pass
    def count_points_with_parameter_loop_operator(self, a, b, h):
        left_border = a
        right_border = b
        step = h
        steps_number = math.ceil((right_border - left_border) / step)
        for i in steps_number:
            x = left_border
            y = _count_y(x)

            self.points_by_parameter_loop_operator.points[x] = y
            left_border += step
        def _count_y(self, x):
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
    
    # По заданию, не требуется.
    def count_with_precondition_loop_operator(self, a, b, h):
        points_by_precondition_loop_operator = {}
class SecondTaskData(DataClass):
    # for
    def loop_operator_with_parameter_method(self, a, b, h):
        points_by_parameter_loop_operator = {}
        
    # while
    def loop_operator_with_precondition_method(self, a, b, h):
        left_border = a
        right_border = b
        step = h
        while left_border < right_border:
            x = left_border
            y = _count_y(x)

            DataClass.points_by_precondition_loop_operator.points[x] = y
            left_border += step
        def _count_y(self, x):
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

class ThirdTaskData(DataClass):
    def count_points_with_parameter_loop_operator(self, a, b, h):
        left_border = a
        right_border = b
        step = h
        steps_number = math.ceil((right_border - left_border) / step)
        for i in steps_number:
            x = left_border
            y = self._count_y(x)

            self.points_by_parameter_loop_operator.points[x] = y
            left_border += step
    def count_points_with_precondition_loop_operator(self, a, b, h):
        x = 0
        y = 0
        left_border = a
        right_border = b
        step = h
        while left_border < right_border:
            x = left_border
            y = self._count_y(x)

            DataClass.points_by_precondition_loop_operator.points[x] = y
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