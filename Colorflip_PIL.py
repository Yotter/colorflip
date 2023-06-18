from PIL import Image

# Loads in the original image and makes a grayscale copy
img = Image.open('river.jpg')
img.show()
# gray = Image.cvtColor(img, Image.COLOR_BGR2GRAY)
# gray = Image.cvtColor(gray, Image.COLOR_GRAY2BGR)
# height = len(img)
# width = len(img[0])
# center = (int(width / 2), int(height / 2))


# # Inverts the colors on the image.
# print('Loading image... Estimated wait time: {} seconds'.format(int(height * width * 0.0000115)))
# for y, py in enumerate(img):
# 	for x, px in enumerate(py):
# 		for pos, i in enumerate(px):
# 			img[y][x][pos] = 255-i

# # Intro
# intro = Image.imread('intro.png', -1)
# Image.imshow('image', intro)
# print('Image loaded.')
# Image.waitKey(0)

# # Main animation
# Image.circle(img, (center), 2, (0,0,255), -1)
# Image.imshow('image', img)
# Image.waitKey(20000)

# # Gray
# Image.circle(gray, (center), 2, (0,0,255), -1)
# Image.imshow('image', gray)
# Image.waitKey(20000)
# Image.destroyAllWindows()