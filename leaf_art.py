import numpy as np
from random import choice

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
    leaf = color_leaf(leaf)
    leaf.save('testleaf.png')
    

def color_leaf(img):
    color = choice(LEAF_COLORS)
    data = np.array(img)
    red, green, blue, alpha = data.T
    replace_area = (red==0) & (green==0) & (blue==255)
    data[..., :-1][replace_area.T] = color
    colored_img = Image.fromarray(data, mode='RGBA')
    return colored_img






if __name__ == '__main__':
    get_leaf()