import cv2

from rect import Rectangle
from SSD import get_SSD_model, process_frame_bgr_with_SSD, voc_classes

import numpy as np
import cv2

# Thickness of bounding boxes
THICKNESS=3

SSD_net, bbox_helper, _ = get_SSD_model()

slope = 1000

# initialize the known distance from the camera to the object, which
# in this case is 24 inches
KNOWN_DISTANCE = 200

# initialize the known object width, which in this case, the piece of
# paper is 12 inches wide
KNOWN_WIDTH = 80

# load the first image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread('test_images/test1.jpg')
bboxes = process_frame_bgr_with_SSD(
    image, SSD_net, bbox_helper, min_confidence=0.2,
    allow_classes=[2, 7, 14, 15])
_, _, x_min, _, x_max, _ = bboxes[0]

# focallength = width * known_distance / known_width
focalLength = ((x_max-x_min) * KNOWN_DISTANCE) / KNOWN_WIDTH
print(f"focallength: {focalLength}")

color_palette = (
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
)

def distance_to_camera(knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    return (slope * knownWidth * focalLength) / perWidth

def main():
    image = cv2.imread('test_images/test1.jpg')
    bboxes = process_frame_bgr_with_SSD(
        image, SSD_net, bbox_helper, min_confidence=0.2,
        allow_classes=[2, 7, 14, 15])

    h, w = image.shape[:2]

    for i, row in enumerate(bboxes):
        # parse row
        label, confidence, x_min, y_min, x_max, y_max = row

        # convert coordinates that belong to range (0, 1) back to image space (h, w)
        x_min = int(round(x_min * w))
        y_min = int(round(y_min * h))
        x_max = int(round(x_max * w))
        y_max = int(round(y_max * h))

        label_text = voc_classes[int(label)-1]
        bbox = Rectangle(x_min, y_min, x_max, y_max, label=label_text)
        bbox.draw(
            image, draw_label=True, color=color_palette[i],
            thickness=THICKNESS)
        perWidth = x_max-x_min
        inches = distance_to_camera(KNOWN_WIDTH, focalLength, perWidth)
        print(f"perWidth = {perWidth}")

        cv2.putText(
            image, "%.2fft" % (inches / 12),
            (image.shape[1] - 250, image.shape[0] - 20 - i*50),
            cv2.FONT_HERSHEY_SIMPLEX,
            2.0, color_palette[i], 3)

        # Save image for reference later
        cv2.imwrite('output_images/distance_estimation.jpg', image)

        cv2.imshow('Result', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

if __name__ == '__main__':
    main()
