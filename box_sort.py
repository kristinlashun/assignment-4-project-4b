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
        current = box_list[i]
        j = i - 1
        # Compare volumes and shift boxes
        while j >= 0 and box_list[j].volume() < current.volume():
            box_list[j + 1] = box_list[j]
            j -= 1
        box_list[j + 1] = current