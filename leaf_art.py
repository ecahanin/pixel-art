import numpy as np
from random import choice, randint

from PIL import Image

LEAF_COLORS = [
                (242,159,5),
                (242,135,5),
                (191,106,57),
                (140,59,13),
                (115,68,41),
            ]
CANVAS_SIZE = (300, 300)


def get_leaf():
    leaf = Image.open('leaf.png')
    leaf.convert('RGBA')
    return color_leaf(leaf)
    
    

def color_leaf(img):
    color = choice(LEAF_COLORS)
    data = np.array(img)
    red, green, blue, alpha = data.T
    replace_area = (red==0) & (green==0) & (blue==255)
    data[..., :-1][replace_area.T] = color
    colored_img = Image.fromarray(data, mode='RGBA')
    return colored_img

def make_canvas(size=CANVAS_SIZE):
    canvas = Image.new('RGBA', size, (255,255,255,0))
    random_points = []
    jitter = [-3,-2,-1,0,1,2,3]
    for x in range(-10, size[0] + 10):
        for y in range(-10, size[1] + 10):
            xi = x + choice(jitter)
            yi = y + choice(jitter)
            if 0 <= xi < size[0]:
                if 0 <= yi < size[1]:
                    random_points.append((xi, yi))
    while random_points:
        coords = random_points.pop(randint(0,len(random_points)-1))
        leaf = get_leaf()
        canvas.paste(leaf, coords, leaf)
    canvas.save('testc.png')

        





if __name__ == '__main__':
    make_canvas()