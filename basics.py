import cv2 as cv
from read import read_image
from rescale_resize import rescale_frame

def convert_into_grayscale(path: str, title: str) -> None:
    """
    Convert an image into grayscale and display it
    
    Args:
        path: str: The path to the image file
        
    Returns:
        None
    """
    try:
      # Load an image using 'imread' specifying the path to image
      img = cv.imread(path)
      
      # Convert the image into grayscale
      grayscale = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
      
      # show the image
      cv.imshow(title, grayscale)
      
      # Wait for a key press to close the image
      cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
        
def convert_into_blur(path: str, title: str) -> None:
    """
    Convert an image into blur and display it
    
    Args:
        path: str: The path to the image file
        
    Returns:
        None
    """
    try:
      # Load an image using 'imread' specifying the path to image
      img = cv.imread(path)
      
      # Convert the image into blur
      blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
      
      # show the image
      cv.imshow(title, blur)
      
      # Wait for a key press to close the image
      cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
      
def find_edge_cascade(path: str, title: str) -> None:
    """
    Find the edges of an image using the Canny Edge Detection algorithm and display it
    
    Args:
        path: str: The path to the image file
        
    Returns:
        None
    """
    #  Edge Cascade => It is a technique to find the edges of an image using the Canny Edge Detection algorithm. It is used in computer vision to detect a wide range of edges in images. 
    # UseCase => It is used in computer vision to detect a wide range of edges in images.
    try:
      # Load an image using 'imread' specifying the path to image
      img = cv.imread(path)
      
      # Find the edges of the image
      canny = cv.Canny(img, threshold1=125, threshold2=175)
      
      # show the image
      cv.imshow(title, canny)
      
      # Wait for a key press to close the image
      cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
        
def dilating_image(path: str, title: str) -> None:
    """
    Dilate the edges of an image using the Dilation algorithm and display it
    
    Args:
        path: str: The path to the image file
        
    Returns:
        None
    """
    #  Dilation => It is a technique to increase the size of the object in an image. It is used in computer vision to increase the size of the object in an image.
    # UseCase => It is used in computer vision to increase the size of the object in an image.
    try:
      # Load an image using 'imread' specifying the path to image
      img = cv.imread(path)
      
      # Find the edges of the image
      canny = cv.Canny(img, threshold1=125, threshold2=175)
      
      # Dilate the edges of the image
      dilated = cv.dilate(canny, kernel=(7, 7), iterations=3)
      
      # show the image
      cv.imshow(title, dilated)
      
      # Wait for a key press to close the image
      cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
        
def eroding_image(path: str, title: str) -> None:
    """
    Erode the edges of an image using the Erosion algorithm and display it
    
    Args:
        path: str: The path to the image file
        
    Returns:
        None
    """
    #  Erosion => It is a technique to decrease the size of the object in an image. It is used in computer vision to decrease the size of the object in an image.
    # UseCase => It is used in computer vision to decrease the size of the object in an image.
    try:
      # Load an image using 'imread' specifying the path to image
      img = cv.imread(path)
      
      # Find the edges of the image
      canny = cv.Canny(img, threshold1=125, threshold2=175)
      
      # Dilate the edges of the image
      dilated = cv.dilate(canny, kernel=(7, 7), iterations=3)
      
      # Erode the edges of the image
      eroded = cv.erode(dilated, kernel=(7, 7), iterations=3)
      
      # show the image
      cv.imshow(title, eroded)
      
      # Wait for a key press to close the image
      cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
        
def resize_image(path: str, title: str, size: tuple = (500, 500)) -> None:
    """
    Resize an image using the resize algorithm and display it
    
    Args:
        path: str: The path to the image file
        
    Returns:
        None
    """
    #  Resize => It is a technique to resize an image. It is used in computer vision to resize an image.
    # UseCase => It is used in computer vision to resize an image.
    try:
      # Load an image using 'imread' specifying the path to image
      img = cv.imread(path)
      
      # Resize the image
      resized = cv.resize(img, size, interpolation=cv.INTER_CUBIC)
      
      # show the image
      cv.imshow(title, resized)
      
      # Wait for a key press to close the image
      cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
        
def crop_image(path: str, title: str, x: int = 0, y: int = 0, width: int = 100, height: int = 100) -> None:
    """
    Crop an image using the slicing technique and display it
    
    Args:
        path: str: The path to the image file
        
    Returns:
        None
    """
    #  Crop => It is a technique to crop an image. It is used in computer vision to crop an image.
    # UseCase => It is used in computer vision to crop an image.
    try:
      # Load an image using 'imread' specifying the path to image
      img = cv.imread(path)
      
      # Crop the image
      cropped = img[y:height, x:width]
      
      # show the image
      cv.imshow(title, cropped)
      
      # Wait for a key press to close the image
      cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
        
if __name__ == "__main__":
  read_image('photos/promises.jpg')
  # convert_into_grayscale('photos/promises.jpg', "Gray Scale Image")
  # convert_into_blur('photos/promises.jpg', "Blur Image")
  # find_edge_cascade('photos/promises.jpg', "Edge Cascade Image")
  # dilating_image('photos/promises.jpg', "Dilated Image")
  # eroding_image('photos/promises.jpg', "Eroded Image")
  resize_image('photos/promises.jpg', "Resized Image")
  crop_image('photos/promises.jpg', "Cropped Image", width=400, height=400, x=100, y=100)
  