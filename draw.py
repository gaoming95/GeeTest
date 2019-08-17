from PIL import Image, ImageFont, ImageDraw, ImageOps
import numpy as np
import math

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
    w_s = w.size
    w_w = w_s[0]
    w_h = w_s[1]
    # w = w.crop(((w_w - image_size) / 2, (w_h - image_size) / 2, image_size + (w_w - image_size) / 2,
    #             image_size + (w_h - image_size) / 2))
    return w, (w_w, w_h)


def is_margin(res, x_1, y_1):
    if not len(res):
        return True
    for loc in res:
        distance2 = math.pow(loc[0] - x_1, 2) + math.pow(loc[1] - y_1, 2)
        if (distance2 < 3600):
            return False
    return True


def get_loc(count):
    res = []
    while True:
        if len(res) == count:
            return res

        x_1 = np.random.randint(0, 344 - 60)
        y_1 = np.random.randint(0, 344 - 60)

        if (is_margin(res, x_1, y_1)):
            res.append((x_1, y_1))


def gen_pic(strs, num):
    g = open('result/result', 'w', encoding='utf-8')
    for i in range(num):
        pic_num = np.random.randint(0, 1444)
        back_img = 'Background/back_pic/{}.jpg'.format(pic_num)
        im = Image.open(back_img)

        word_num = np.random.randint(0, len(strs))
        input_str = strs[word_num]
        loc = get_loc(len(input_str))
        font_size_list = []

        for j in range(len(input_str)):
            w, (w_w, w_h) = get_char(input_str[j])
            font_size_list.append((w_w, w_h))
            l = loc[j]

            R = np.random.randint(0, 256)
            G = np.random.randint(0, 256)
            B = np.random.randint(0, 256)
            im.paste(ImageOps.colorize(w, (0, 0, 0), (R, G, B)), (l[0], l[1]), w)

        loc_res = [(loc[l][0], loc[l][1], loc[l][0] + font_size_list[l][0], loc[l][1] + font_size_list[l][1]) for l in
                   range(len(input_str))]

        print('{} 文本:{} 位置{}'.format(i, input_str, loc_res))
        g.write('{}\t文本:{}\t位置{}\n'.format(i, input_str, loc_res))
        # im.show()
        im.save('result/{}.jpg'.format(i))


if __name__ == '__main__':
    with open('Words/four', 'r', encoding='utf-8') as g:
        strs = [i.strip() for i in g.readlines()]
    gen_pic(strs, 20000)
