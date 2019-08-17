# GeeTest
模拟极验3.0点击文字图片的生成方式，但做不到完全模拟。可以利用该模拟的数据做模型的预训练，然后迁移，效果应该可以。

![验证码](https://github.com/gaoming95/GeeTest/blob/master/result/0.jpg)![验证码](https://github.com/gaoming95/GeeTest/blob/master/result/1.jpg)

![单字](https://github.com/gaoming95/GeeTest/blob/master/Single/%E5%95%8A/0.jpg)![单字](https://github.com/gaoming95/GeeTest/blob/master/Single/%E5%95%8A/1.jpg)


## 1 资源下载
如果只需要训练数据集，不需要clone代码。

已经准备了生成的数据，包括3559*1000个单字图片和20000张验证码图片

- [验证码下载](https://pan.baidu.com/s/142SgYSAuIbWDUrlTyiSfiA) 提取码：2sg1
- [单字下载1](https://pan.baidu.com/s/1xWYrSf1EhG8YAaHmDQvfbA) 提取码：xnlz
- [单字下载2](https://pan.baidu.com/s/1JOZHQ0ACcK8CldiLoiUhlQ) 提取码：hyoq

## 2 自己模拟生成
### 2.1 准备背景图片
可以自己下载，如果没有，可以参考

[背景图片](https://pan.baidu.com/s/1OSmOaD7mWeBYbH_5XldEbA) 提取码：f9mp

### 2.1 运行`Background\background.py`
```
if __name__ == '__main__':
    # 生成344*344背景
    # get_background('back_pic',344)
    # 生成60*60单字图
    get_background('single_pic', 60)
```
344*344是
