from PIL import Image


if __name__=="__main__":
    im = Image.open("lena.jpg")
    im  = im.convert('RGB')
    # im.show()
    source = im.split()
    mask = Image.open("mask.bmp")
    mask  = mask.convert('RGB')
    mask = mask.resize(im.size)
    print(mask.format, mask.size, mask.mode)
    print(im.format, im.size, im.mode)
    # mask.show()
    out = Image.blend(im,mask,0.1)
    out.show()
    exit()
    print(im.format, im.size, im.mode)
    for j in range(0,im.size[0]):
        for i in range(0,im.size[1]):
            pix = im.getpixel((i,j))
            im.putpixel((i,j), (pix[0],0,0))
    im.show()
