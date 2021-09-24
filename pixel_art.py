from random import choice

from PIL import Image, ImageDraw


def get_prob_colors(start, end, i):
    colors = COLORS[start:end]
    colors.append(COLORS[i])
    for _ in range(2):
        if start > 0 and _ == 0:
            start -= 1
        if end < len(COLORS) - 1:
            end += 1
        colors.extend(COLORS[start:end])
    return colors

CANVAS_SIZE = (4500, 5400)
PIXEL_SIZE = 60
WIDTH = 60
HEIGHT = 20
GAP = 9
TOP_BUFFER = 500

#gray_generator = [(x*25, x*25, x*25) for x in range(11)]


COLORS = [
            (73,89,70),
            (166,191,75),
            (102,140,74),
            (242,230,65),
            (242,183,5),
            (242,159,5),
            (242,135,5),
            (191,106,57),
            (140,59,13),
            (115,68,41),
        ]

image = Image.new("RGBA", CANVAS_SIZE, (255,255,255,0))
draw = ImageDraw.Draw(image)

image_width = PIXEL_SIZE * WIDTH + (WIDTH - 1) * GAP
offset = (CANVAS_SIZE[0] - image_width)/2

start_corner = (offset, TOP_BUFFER)

for row in range(HEIGHT):
    for col in range(WIDTH):
        x = start_corner[0] + (col * (PIXEL_SIZE + GAP))
        y = start_corner[1] + (row * (PIXEL_SIZE + GAP))

        rough_index = int((col / WIDTH) * len(COLORS))
        color_start_range = rough_index - 2
        color_end_range = rough_index + 2
        if color_start_range < 0:
            color_start_range = 0
        if color_end_range > len(COLORS) - 1:
            color_end_range = len(COLORS) - 1

        colors = COLORS[color_start_range:color_end_range]
        prob_colors = get_prob_colors(color_start_range, color_end_range, rough_index)
        color = choice(prob_colors)


        draw.rectangle([(x,y), (x+PIXEL_SIZE, y+PIXEL_SIZE)], fill=color)



image.save('pixels.png')

