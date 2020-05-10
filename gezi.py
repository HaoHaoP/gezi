from PIL import ImageFilter
from PIL import Image
import os


def main():
    print("皓皓格子生成器","展开")
    for root, dirs, files in os.walk('src'):
        for f in files:
            try:
                print("读取",os.path.join(root, f))
                new = Image.new('RGB', (2000,2000))
                img = Image.open(os.path.join(root, f))
                img = img.resize((100,100),Image.ANTIALIAS)
                sizeX = 0
                while sizeX <= 2000:
                    sizeY = 0
                    while sizeY <= 2000:
                        new.paste(img,(sizeX,sizeY,sizeX+100,sizeY+100))
                        sizeY += 100
                    sizeX += 100
                new.save(os.path.join(root, f)+'(生成).jpg')
                print("生成",os.path.join(root, f))
            except IOError:
                print("失败",(os.path.join(root, f)))    
    print("皓皓格子生成器","生成完成")    



if __name__ == '__main__':
    main()