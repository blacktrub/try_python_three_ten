from typing import Union

code = 100
def match_code(code: int | float) -> None:
    match code:
        case 100 | 110:
            print("hundred")
        case 200:
            print("two hundred")
        case _:
            print("none")

point = (1, 1)
match point:
    case (0, x):
        print('one')
    case (x, 1):
        print('two')

        
class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

match Point(1, 1):
    case Point(x=1, y=y):
        print(y)
    

error = (3, 'message', 3)
match error:
    # case (x, *other):
    #     print(x, other)
    case (x, m, y) if x == y:
        print('with if')
    case (x, m, y):
        print('without if')