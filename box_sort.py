class Box:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        return self._length * self._width * self._height

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


def box_sort(box_list):
    for i in range(1, len(box_list)):
        current_box = box_list[i]
        j = i - 1
        while j >= 0 and box_list[j].volume() < current_box.volume():
            box_list[j + 1] = box_list[j]
            j -= 1
        box_list[j + 1] = current_box


# Example usage
b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
box_list = [b1, b2, b3]

box_sort(box_list)


for box in box_list:
    print(f"Box Dimensions (LxWxH): {box.get_length()} x {box.get_width()} x {box.get_height()}, Volume: {box.volume()}")
