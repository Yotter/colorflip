import cv2

# Loads in the original image and makes a grayscale copy
img = cv2.imread('image.jpg', -1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
height = len(img)
width = len(img[0])
center = (int(width / 2), int(height / 2))


# Inverts the colors on the image.
print('Loading image... Estimated wait time: {} seconds'.format(int(height * width * 0.0000115)))
for y, py in enumerate(img):
	for x, px in enumerate(py):
		for pos, i in enumerate(px):
			img[y][x][pos] = 255-i

# Intro
intro = cv2.imread('intro.png', -1)
cv2.imshow('image', intro)
print('Image loaded.')
cv2.waitKey(0)

# Main animation
cv2.circle(img, (center), 3, (0,0,255), -1)
cv2.imshow('image', img)
cv2.waitKey(20000)

# Gray
cv2.circle(gray, (center), 3, (0,0,255), -1)
cv2.imshow('image', gray)
cv2.waitKey(20000)
cv2.destroyAllWindows()