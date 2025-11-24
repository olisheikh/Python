img_file = open('img1.png', 'rb')
img = img_file.read()

img_copy_file = open('img2.jpg', 'wb')

img_copy_file.write(img)

img_file.close()
img_copy_file.close()