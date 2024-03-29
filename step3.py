import matplotlib.pylab as plt
import cv2
import numpy as np

image = cv2.imread("road.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width/2, height/1.45),
    (1100, height)
]

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    chanel_count = img.shape[2]
    match_mask_color = (255,) * chanel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

cropped_image = region_of_interest(image,
                np.array([region_of_interest_vertices], np.int32),)

plt.imshow(cropped_image)
plt.show()
