import cv2 as cv

#  Note the below function is works with Images, Videos and Live Videos
def rescale_frame(frame, scale=0.75):
    """
    Rescale the frame of the video/image to a certain scale
    
    Args:
        frame: np.ndarray
            The frame of the video/image
        scale: float
            The scale factor of the frame
            
    Returns:
        frame_rescaled: np.ndarray
            The rescaled frame of the video/image
    """
    print("Frame Shape:", frame.shape)
    # Get the dimensions of the frame
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    # Create a tuple of the dimensions
    dimensions = (width, height)
    
    # Return the rescaled frame
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
  
# Note the below function only works with Live Videos
def change_resolution(cap, width, height):
    """
    Change the resolution of the video capture
    
    Args:
        cap: cv.VideoCapture
            The video capture object
        width: int
            The width of the video capture
        height: int
            The height of the video capture
            
    Returns:
        None
    """
    cap.set(3, width)
    cap.set(4, height)
    


