def find_rectangular_overlap(rect1, rect2):
    # Calculate the overlap between the two rectangles
    d = {}
    x = max(rect1['left_x'], rect2['left_x'])
    y = max(rect1['bottom_y'], rect2['bottom_y'])

    x1 = min((rect1['left_x'] + rect1['width']), (rect2['left_x'] + rect2['width']))
    y1 = min((rect1['bottom_y'] + rect1['height']), (rect2['bottom_y'] + rect2['height']))

    if (x1 > x and y1 > y):
        d['left_x'] = x
        d['bottom_y'] = y
        d['width'] = x1 - x
        d['height'] = y1 - y

    else:
        d['left_x'] = None
        d['bottom_y'] = None
        d['width'] = None
        d['height'] = None

    return d

rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
print(find_rectangular_overlap(rect1,rect2))