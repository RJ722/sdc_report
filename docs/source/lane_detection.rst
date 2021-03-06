Lane Finding
============

The goals / steps of this project are the following:

-  Compute the camera calibration matrix and distortion coefficients
   given a set of chessboard images.
-  Apply a distortion correction to raw images.
-  Use color transforms, gradients, etc., to create a thresholded binary
   image.
-  Apply a perspective transform to rectify binary image (“birds-eye
   view”).
-  Detect lane pixels and fit to find the lane boundary.
-  Determine the curvature of the lane and vehicle position with respect
   to center.
-  Warp the detected lane boundaries back onto the original image.
-  Output visual display of the lane boundaries and numerical estimation
   of lane curvature and vehicle position.

Camera Calibration
~~~~~~~~~~~~~~~~~~

OpenCV provide some really helpful built-in functions for the task on
camera calibration. First of all, to detect the calibration pattern in
the calibration images, we can use the function
``cv2.findChessboardCorners(image, pattern_size)``.

Once we have stored the correspondences between 3D world and 2D image
points for a bunch of images, we can proceed to actually calibrate the
camera through ``cv2.calibrateCamera()``. Among other things, this
function returns both the *camera matrix* and the *distortion
coefficients*, which we can use to undistort the frames.

We applied this distortion correction to the test image using the
``cv2.undistort()`` function and obtained the following result
(appreciating the effect of calibration is easier on the borders of the
image):

.. figure:: img/chessboard-comparison.png

Pipeline
~~~~~~~~

Once the camera is calibrated, we can use the camera matrix and
distortion coefficients we found to undistort also the test images.
Indeed, if we want to study the *geometry* of the road, we have to be
sure that the images we’re processing do not present distortions. Here’s
the result of distortion-correction on one of the test images:

.. figure:: img/lane_comparison.png

In this case appreciating the result is slightly harder, but we can
notice, nonetheless, some difference on both, the extreme left and extreme
right sides of the image.

Binarization
^^^^^^^^^^^^

Since correctly creating the binary image from the input frame is the very first
step of the whole pipeline that will lead us to detect the lane. For this
reason, we found that is also one of the most important. If the binary image is
bad, it’s very difficult to recover and to obtain good results in the successive
steps of the pipeline.

We used a combination of color and gradient thresholds to generate a binary
image. In order to detect the white lines, we found that equalizing the
histogram of the input frame before thresholding works really well to highlight
the actual lane lines. For the yellow lines, we employed a threshold on V
channel in HSV color space. Furthermore, we also convolve the input frame with
Sobel kernel to get an estimate of the gradients of the lines. Finally, we make
use of morphological closure to *fill the gaps* in the binary image. Here is a
step-by-step process:

.. figure:: img/binarization.png

Perspective Transform
^^^^^^^^^^^^^^^^^^^^^

Code relating to warping between the two perspective can be found
``perspective_utils.py``. The function ``calibration_utils.birdeye()`` takes as
input the frame (either color or binary) and returns the bird’s-eye view of the
scene. In order to perform the perspective warping, we need to map 4 points in
the original space and 4 points in the warped space.

For this purpose, both source and destination points were mapped as follows:

::

       h, w = img.shape[:2]

       src = np.float32([[w, h-10],    # br
                         [0, h-10],    # bl
                         [546, 460],   # tl
                         [732, 460]])  # tr
       dst = np.float32([[w, h],       # br
                         [0, h],       # bl
                         [0, 0],       # tl
                         [w, 0]])      # tr

We verified that the perspective transform was working as expected by
drawing the ``src`` and ``dst`` points onto a test image and its warped
counterpart to verify that the lines appear parallel in the warped
image.

.. figure:: img/perspective_output.png

Fitting lane line with a polynomial
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to identify which pixels of a given binary image belong to
lane-lines, we have (at least) two possibilities. If we have a brand new
frame, and we never identified where the lane-lines are, we must perform
an exhaustive search on the frame. This search is implemented in
``line_utils.get_fits_by_sliding_windows()``: starting from the bottom
of the image, precisely from the peaks location of the histogram of the
binary image, we slide two windows towards the upper side of the image,
deciding which pixels belong to which lane-line.

On the other hand, if we’re processing a video and we confidently
identified lane-lines on the previous frame, we can limit our search in
the neighborhood of the lane-lines we detected before: after all we’re
going at 30fps, so the lines won’t be so far, right? This second
approach is implemented in ``line_utils.get_fits_by_previous_fits()``.
In order to keep track of detected lines across successive frames, we
employ a class defined in ``line_utils.Line``, which helps in keeping
the code cleaner.

::

   class Line:

       def __init__(self, buffer_len=10):

           # flag to mark if the line was detected the last iteration
           self.detected = False

           # polynomial coefficients fitted on the last iteration
           self.last_fit_pixel = None
           self.last_fit_meter = None

           # list of polynomial coefficients of the last N iterations
           self.recent_fits_pixel = collections.deque(maxlen=buffer_len)
           self.recent_fits_meter = collections.deque(maxlen=2 * buffer_len)

           self.radius_of_curvature = None

           # store all pixels coords (x, y) of line detected
           self.all_x = None
           self.all_y = None
       
       # ...

As it can be seen, when a detection of lane-lines is available for a previous
frame, new lane-lines are searched through
``line_utils.get_fits_by_previous_fits()`` otherwise, the more expensive sliding
windows search is performed.

.. figure:: img/sliding_windows_before.png

   Bird’s-eye view (binary)

.. figure:: img/sliding_windows_after.png

   Bird’s-eye view (lane detected)

Radius of Curvature
^^^^^^^^^^^^^^^^^^^

Offset from center of the lane is computed in ``compute_offset_from_center()``
as one of the step of the processing pipeline. The offset from the lane center
can be computed under the hypothesis that the camera is fixed and mounted in the
midpoint of the car roof. In this case, we can approximate the car’s deviation
from the lane center as the distance between the center of the image and the
midpoint at the bottom of the image of the two lane-lines detected.

During the previous lane-line detection phase, a 2nd order polynomial is fitted
to each lane-line using ``np.polyfit()``. This function returns the 3
coefficients that describe the curve, namely the coefficients of both the 2nd
and 1st order terms plus the bias. From these coefficients, we can compute the
radius of curvature of the curve. From an implementation standpoint, we decided
to move these methods as properties of ``Line`` class.

::

   class Line:
     # ...
       @property
       # average of polynomial coefficients of the last N iterations
       def average_fit(self):
           return np.mean(self.recent_fits_pixel, axis=0)

       @property
       # radius of curvature of the line (averaged)
       def curvature(self):
           y_eval = 0
           coeffs = self.average_fit
           return (
    (1 + (2 * coeffs[0] * y_eval + coeffs[1]) ** 2) ** 1.5) / np.absolute(2 * coeffs[0])

       @property
       # radius of curvature of the line (averaged)
       def curvature_meter(self):
           y_eval = 0
           coeffs = np.mean(self.recent_fits_meter, axis=0)
           return (
    (1 + (2 * coeffs[0] * y_eval + coeffs[1]) ** 2) ** 1.5) / np.absolute(2 * coeffs[0])

Example Output
^^^^^^^^^^^^^^

The qualitative result for one of the given test images follows:

.. figure:: img/lane_find.jpg

   Example result from ``project_video.mp4``


Discussion
~~~~~~~~~~

We found that the more delicate aspect of the pipeline is the first step, namely
the binarization of the input frame. Indeed, if that step fails, most of
successive steps will lead to poor results. Also, we observed that this part is
implemented by thresholding the input frame, so we let the correct value of a
threshold be our single-point of failure. We think that a CNN could be employed
to successfully make this step more robust. Some datasets like Synthia
<http://synthia-dataset.net/> should hopefully provide enough lane marking
annotation to train a deep network. 
