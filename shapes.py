import cv2 as cv 
import numpy as np
from draw import Colors

class Shape:
    """
    A class to represent a shape
    
    Attributes:
        shape: str
            The shape of the object
    """
    def __init__(self, shape: str) -> None:
        """
        Construct all the necessary attributes for the shape object
        
        Args:
            shape: str
                The shape of the object
        """
        self.shape = shape
        
    def draw_shape(self, img: np.ndarray = np.zeros((500, 500, 3), dtype='uint8'), color: tuple = (0, 255, 0), x: int = 0, y: int = 0, width: int = 100, height: int = 100, thickness: int = 2) -> None:
        """
        Draw a shape on an image
        
        Args:
            img: np.ndarray
                The image to draw the shape on
            color: tuple
                The color of the shape
            x: int
                The x-coordinate of the shape
            y: int
                The y-coordinate of the shape
            width: int
                The width of the shape
            height: int
                The height of the shape
            thickness: int
                The thickness of the shape  
                
        Returns:
            None
        """
        if self.shape == 'rectangle':
            cv.rectangle(img, (x, y), (x + width, y + height), color, thickness=thickness)
        elif self.shape == 'circle':
            cv.circle(img, (x, y), radius=width, color=color, thickness=thickness)
        elif self.shape == 'line':
            cv.line(img, (x, y), (x + width, y + height), color, thickness=thickness)
        elif self.shape == 'ellipse':
            cv.ellipse(img, (x, y), (width, height), 0, 0, 360, color, thickness=thickness)
        elif self.shape == 'text':
            cv.putText(img, 'Hello World!', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, color, thickness=thickness)
        else:
            raise ValueError('Invalid shape')
        
        cv.imshow('Shapes', img)
        cv.waitKey(0)
        
        
if __name__ == "__main__":
    # Create a blank image
    blank_image = np.zeros((500, 500, 3), dtype='uint8')
    
    # Create a shape object
    shape = Shape('rectangle')
    
    # Draw the shape
    shape.draw_shape(img=blank_image, color=Colors.AQUA, x=0, y=0, width=100, height=100, thickness=-1)
    
    # Create a shape object
    shape = Shape('circle')
    
    # Draw the shape
    shape.draw_shape(img=blank_image, color=Colors.BROWN, x=200, y=200, width=100)
    
    # Create a shape object
    shape = Shape('line')
    
    # Draw the shape
    shape.draw_shape(img=blank_image, color=Colors.INDIGO, x=300, y=300, width=100, height=100)
    
    # Create a shape object
    shape = Shape('ellipse')
    
    # Draw the shape
    shape.draw_shape(img=blank_image, color=Colors.CORAL, x=250, y=300, width=100, height=200)
    
    # Create a shape object
    shape = Shape('text')
    
    # Draw the shape
    shape.draw_shape(img=blank_image,color=Colors.MAGENTA, x=300, y=300, width=0, height=0)
    
    cv.destroyAllWindows()