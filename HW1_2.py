from PIL import Image
 
 
def ResizeImage(k,hightsize,filein):
    """
    改变图片大小
    :param filein: 输入图片
    :param fileout: 输出图片
    :param width: 输出图片宽度
    :param height: 输出图片宽度
    :param type: 输出图片类型（png, gif, jpeg...）
    :return:
    """
    img = Image.open(filein)
    scale=hightsize/img.size[1] 
    width = int(img.size[0] * scale)
    height = int(img.size[1] * scale)
    ttype = img.format
    out = img.resize((width, height), Image.ANTIALIAS)
    # 第二个参数：
    # Image.NEAREST ：低质量
    # Image.BILINEAR：双线性
    # Image.BICUBIC ：三次样条插值
    # Image.ANTIALIAS：高质量
    fileout=filein
    out.save(fileout, ttype)