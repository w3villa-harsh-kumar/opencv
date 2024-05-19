import cv2 as cv
import numpy as np

def translate(img, x, y):
  """
  Translate an image by x and y pixels
  
  Args:
    img: np.ndarray
      The image to translate
    x: int
      The number of pixels to translate the image in the x-direction
    y: int
      The number of pixels to translate the image in the y-direction
      
  Returns:
    img_translated: np.ndarray
      The translated image
  """
  # -x = left
  # -y = up
  # +x = right
  # +y = down
  
  # Create a translation matrix
  translated_matrix = np.float32([[1,0,x], [0,1,y]])
  
  # Get the dimensions of the image
  dimensions = (img.shape[1], img.shape[0])
  
  # Translate the image
  return cv.warpAffine(img, translated_matrix, dimensions)

def rotate(img, angle, rotatedPoint=None):
  """
  Rotate an image by an angle
  
  Args:
    img: np.ndarray
      The image to rotate
    angle: float
      The angle to rotate the image
    rotatedPoint: tuple
      The point to rotate the image around
      
  Returns:
    img_rotated: np.ndarray
      The rotated image
  """
  # Get the dimensions of the image
  dimensions = (img.shape[1], img.shape[0]) # Here img.shape[1] is width and img.shape[0] is height
  
  # If the rotated point is not provided, rotate the image around the center
  if rotatedPoint is None:
    rotatedPoint = (dimensions[0]//2, dimensions[1]//2) 
    
  # Create a rotation matrix
  rotationMatrix = cv.getRotationMatrix2D(rotatedPoint, angle, 1.0)
  
  # Rotate the image
  return cv.warpAffine(img, rotationMatrix, dimensions)

def flip(img, flipCode):
  """
  Flip an image
  
  Args:
    img: np.ndarray
      The image to flip
    flipCode: int
      The flip code to flip the image
      
  Returns:
    img_flipped: np.ndarray
      The flipped image
  """
  # 0 => flip vertically
  # 1 => flip horizontally
  # -1 => flip both vertically and horizontally
  # Flip the image
  return cv.flip(img, flipCode)

if __name__ == "__main__":
  img = cv.imread('photos/promises.jpg')
  cv.imshow("Original Image", img)
  translated_img = translate(img, 100, -100)
  cv.imshow("Translated Image", translated_img)
  rotated_img = rotate(img, -45)
  cv.imshow("Rotated Image", rotated_img)
  rotated_image_around_point = rotate(img, 45, (img.shape[1]//3, img.shape[0]//3))
  horizontal_flip = flip(img, 1)
  cv.imshow("Horizontal Flip", horizontal_flip)
  vertical_flip = flip(img, 0)
  cv.imshow("Vertical Flip", vertical_flip)
  both_flip = flip(img, -1)
  cv.imshow("Both Flip", both_flip)
  cv.waitKey(0)