import pytesseract as pt

from PIL import Image

image = Image.open('c:/Users/fukan/Desktop/1.png')

# 调用pytesseract，把图片转化成文字
# 返回结果就是转换后的结果

text = pt.image_to_string(image)
print(text)
