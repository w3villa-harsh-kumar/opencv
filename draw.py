import cv2 as cv
import numpy as np

class Colors:
    """
    A class to represent a color
    
    Attributes:
        RED: tuple
            The RGB value for red
        GREEN: tuple
            The RGB value for green
        BLUE: tuple
            The RGB value for blue
        WHITE: tuple
            The RGB value for white
        BLACK: tuple
            The RGB value for black
    """
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (0, 255, 255)
    CYAN = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    SKY_BLUE = (135, 206, 235)
    ORANGE = (255, 165, 0)
    PINK = (255, 192, 203)
    PURPLE = (128, 0, 128)
    BROWN = (165, 42, 42)
    GREY = (128, 128, 128)
    DARK_GREY = (169, 169, 169)
    LIGHT_GREY = (211, 211, 211)
    BEIGE = (245, 245, 220)
    IVORY = (255, 255, 240)
    LAVENDER = (230, 230, 250)
    OLIVE = (128, 128, 0)
    MAROON = (128, 0, 0)
    TEAL = (0, 128, 128)
    NAVY = (0, 0, 128)
    SILVER = (192, 192, 192)
    GOLD = (255, 215, 0)
    VIOLET = (238, 130, 238)
    INDIGO = (75, 0, 130)
    TURQUOISE = (64, 224, 208)
    AQUA = (0, 255, 255)
    MINT = (189, 252, 201)
    LIME = (0, 255, 0)
    SALMON = (250, 128, 114)
    CORAL = (255, 127, 80)
    KHAKI = (240, 230, 140)
    TAN = (210, 180, 140)
    BEIGE = (245, 245, 220)
    IVORY = (255, 255, 240)

# Draw a blank image
def draw_blank_image(width: int = 600, height: int = 500) -> None:
    """
    Draw a blank image
    
    Args:
        width: int
            The width of the image
        height: int
            The height of the image
            
    Returns:
        None
    """
    blank_image= np.zeros((height, width, 3), dtype='uint8')
    cv.imshow('Blank Image', blank_image)
    cv.waitKey(0)
    
def draw_single_color_image(width: int = 600, height: int = 500, color: tuple = (0, 255, 0), title: str = 'Single Color Image', d1: int = 0, d2: int = 500, d3: int = 0, d4: int = 600) -> None:
    """
    Draw a single color image
    
    Args:
        width: int
            The width of the image
        height: int
            The height of the image
        color: tuple
            The color of the image
        title: str
            The title of the image
    
    Returns:
        None
    """
    blank_image= np.zeros((height, width, 3), dtype='uint8')
    blank_image[d1:d2, d3:d4] = color
    cv.imshow(title, blank_image)
    cv.waitKey(0)
    
if __name__ == '__main__':
    # draw_blank_image()
    draw_single_color_image(color=Colors.PINK, title='Red Image', d1=0, d2=250, d3=0, d4=300)