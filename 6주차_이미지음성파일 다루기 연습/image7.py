from PIL import Image
 
img_01 = Image.open("C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\h.jpeg")
img_02 = Image.open("C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\(1).jpeg")

img_01_size = img_01.size
img_02_size = img_02.size

 
print('img 1 size: ', img_01_size)
print('img 2 size: ', img_02_size)

 
new_im = Image.new('RGB', (2*img_01_size[0],img_01_size[1]), (250,250,250))
 
new_im.paste(img_01, (0,0))
new_im.paste(img_02, (img_01_size[0],0))

 
new_im.save("merged_images.png", "PNG")
new_im.show()