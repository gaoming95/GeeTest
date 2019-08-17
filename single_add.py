import threading

from PIL import Image, ImageFont, ImageDraw, ImageOps
import numpy as np
import os
import glob

font_dict = {
    # 0: 'Fonts/simkai.ttf',
    0: 'Fonts/simsun.ttc',
    # 2: 'Fonts/STHUPO.TTF',
    # 3: 'Fonts/STXIHEI.TTF',
    1: 'Fonts/STXINGKA.TTF',
    # 5: 'Fonts/msyh.ttc',
    # 6: 'Fonts/msyhbd.ttc',
    # 7: 'Fonts/msyhl.ttc'
}


def get_char(c):
    font_type = np.random.randint(0, len(font_dict))
    font_size = np.random.randint(40, 60)
    image_size = font_size
    rotate = np.random.randint(-180, 180)

    font = ImageFont.truetype(font_dict[font_type], font_size)
    txt = Image.new('L', (image_size, image_size))
    d = ImageDraw.Draw(txt)
    d.text((0, 0), c, font=font, fill=255)
    w = txt.rotate(rotate, expand=1)
    return w


def gen_pic(strs, num):
    for index, input_str in enumerate(strs):
        path = os.path.join('Single', input_str)
        if not os.path.exists(path):
            os.mkdir(path)
        for n in range(num):
            pic_num = np.random.randint(0, 1444)
            back_img = 'Background/single_pic/{}.jpg'.format(pic_num)
            im = Image.open(back_img)

            w = get_char(input_str)

            R = np.random.randint(0, 256)
            G = np.random.randint(0, 256)
            B = np.random.randint(0, 256)
            im.paste(ImageOps.colorize(w, (0, 0, 0), (R, G, B)), (0, 0), w)

            # im.show()
            pic_path = os.path.join(path, '{}.jpg'.format(n))
            im.save(pic_path)
        print('{} 字符:{}'.format(index, input_str))


if __name__ == '__main__':

    has = glob.glob('Single/*')

    hs = [h.split('\\')[-1] for h in has]

    with open('Words/one', 'r', encoding='utf-8') as g:
        strs = [i.strip() for i in g.readlines()]

    new_h = []

    for i in strs:
        if i not in hs:
            new_h.append(i)
    nums_thread = 4

    per_step = len(new_h) // nums_thread

    threads = []
    for i in range(nums_thread):
        threads.append(threading.Thread(target=gen_pic, args=(new_h[per_step * i:per_step * (i + 1)], 1000)))

    for i in range(nums_thread):
        threads[i].start()

    for i in range(nums_thread):
        threads[i].join()

        # gen_pic(strs, 10000)
