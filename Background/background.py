from PIL import Image
import glob

images = glob.glob('./raw/*/*.jpg')


def get_background(dirname, pix_size):
    for index, image in enumerate(images):
        img = Image.open(image)
        size = img.size
        width = size[0]
        height = size[1]
        min_size = min(width, height)

        if (min_size < pix_size):
            rate = pix_size // min_size + 1
            img = img.resize((width * rate, height * rate), Image.ANTIALIAS)
        size = img.size
        width = size[0]
        height = size[1]

        cropped = img.crop(((width - pix_size) / 2, (height - pix_size) / 2, pix_size + (width - pix_size) / 2,
                            pix_size + (height - pix_size) / 2))
        cropped.save('./{}/{}.jpg'.format(dirname, str(index)))


if __name__ == '__main__':
    # 生成344*344背景
    # get_background('back_pic',344)
    # 生成60*60单字图
    get_background('single_pic', 60)
