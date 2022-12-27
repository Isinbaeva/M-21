from PIL import Image, ImageDraw


def gradient(c):
    ni = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(ni)
    if c.upper() == 'R':
        for i in range(0, 512, 2):
            draw.line((i, 0, i, 200), fill=(i // 2, 0, 0), width=2)
    elif c.upper() == 'G':
        for i in range(0, 512, 2):
            draw.line((i, 0, i, 200), fill=(0, i // 2, 0), width=2)
    else:
        for i in range(0, 512, 2):
            draw.line((i, 0, i, 200), fill=(0, 0, i // 2), width=2)
    ni.save('res4.png', 'PNG')


gradient("R")
