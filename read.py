import cv2 as cv
from rescale_resize import rescale_frame, change_resolution

# Reading Images
def read_image(path: str) -> None:
    """
    Read an image from a file and display it
    
    Args:
        path: str: The path to the image file
        
    Returns:
        None
    """
    try:
        # Load an image using 'imread' specifying the path to image
        img = cv.imread(path)

        # show the image
        cv.imshow('Barcelona', img)

        # Wait for a key press to close the image
        cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
        
def read_image_with_rescale(path: str, scale: float = 0.75) -> None:
    """
    Read an image from a file, rescale it and display it
    
    Args:
        path: str: The path to the image file
        scale: float: The scale factor of the image
        
    Returns:
        None
    """
    try:
         # Load an image using 'imread' specifying the path to image
        img = cv.imread(path)
        
        # Rescale the image
        img_rescaled = rescale_frame(img, scale)

        # show the image
        cv.imshow('Barcelona', img_rescaled)

        # Wait for a key press to close the image
        cv.waitKey(0)
    except Exception as e:
        print(f'Error: {e}')
    
def read_video_from_path(path: str) -> None:
    """
    Read a video from a file and display it
    
    Args:
        path: str: The path to the video file
        
    Returns:
        None
    """
    try:
        # Load a video using 'VideoCapture' specifying the path to video
        capture = cv.VideoCapture(path)

        # Loop through the video frames
        while True:
            isTrue, frame = capture.read()

            # Display each frame
            cv.imshow('Video', frame)

            # If the 'd' key is pressed, break out of the loop
            if cv.waitKey(20) & 0xFF==ord('d'):
                break

        # Release the capture object
        capture.release()

        # Destroy all windows
        cv.destroyAllWindows()
    except Exception as e:
        print(f'Error: {e}')
        
def read_video_from_path_with_rescale(path: str, scale: float = 0.75) -> None:
    """
    Read a video from a file, rescale it and display it
    
    Args:
        path: str: The path to the video file
        scale: float: The scale factor of the video
        
    Returns:
        None
    """
    try:
        # Load a video using 'VideoCapture' specifying the path to video
        capture = cv.VideoCapture(path)

        # Loop through the video frames
        while True:
            isTrue, frame = capture.read()

            # Rescale the frame
            frame_rescaled = rescale_frame(frame, scale)

            # Display each frame
            cv.imshow('Video', frame_rescaled)

            # If the 'd' key is pressed, break out of the loop
            if cv.waitKey(20) & 0xFF==ord('d'):
                break

        # Release the capture object
        capture.release()

        # Destroy all windows
        cv.destroyAllWindows()
    except Exception as e:
        print(f'Error: {e}')
    
def read_video_from_camera(camera: int) -> None:
    """
    Read a video from the camera and display it
    
    Args:
        None
        
    Returns:
        None
    """
    try:
        # Load a video using 'VideoCapture' specifying the path to video
        capture = cv.VideoCapture(camera)

        # Loop through the video frames
        while True:
            isTrue, frame = capture.read()

            # Display each frame
            cv.imshow('Video', frame)

            # If the 'd' key is pressed, break out of the loop
            if cv.waitKey(20) & 0xFF==ord('d'):
                break

        # Release the capture object
        capture.release()

        # Destroy all windows
        cv.destroyAllWindows()
    except Exception as e:
        print(f'Error: {e}')
        
def read_video_from_camera_with_rescale(camera: int, scale: float = 0.75) -> None:
    """
    Read a video from the camera, rescale it and display it
    
    Args:
        None
        
    Returns:
        None
    """
    try:
        # Load a video using 'VideoCapture' specifying the path to video
        capture = cv.VideoCapture(camera)

        # Loop through the video frames
        while True:
            isTrue, frame = capture.read()

            # Rescale the frame
            frame_rescaled = rescale_frame(frame, scale)

            # Display each frame
            cv.imshow('Video', frame_rescaled)

            # If the 'd' key is pressed, break out of the loop
            if cv.waitKey(20) & 0xFF==ord('d'):
                break

        # Release the capture object
        capture.release()

        # Destroy all windows
        cv.destroyAllWindows()
    except Exception as e:
        print(f'Error: {e}')
        
def read_video_from_camera_with_resolution(camera: int, width: int, height: int) -> None:
    """
    Read a video from the camera, rescale it and display it
    
    Args:
        None
        
    Returns:
        None
    """
    try:
        # Load a video using 'VideoCapture' specifying the path to video
        capture = cv.VideoCapture(camera)

        # Set the resolution
        change_resolution(capture, width, height)

        # Loop through the video frames
        while True:
            isTrue, frame = capture.read()

            # Display each frame
            cv.imshow('Video', frame)

            # If the 'd' key is pressed, break out of the loop
            if cv.waitKey(20) & 0xFF==ord('d'):
                break

        # Release the capture object
        capture.release()

        # Destroy all windows
        cv.destroyAllWindows()
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    # read_image('photos/image (1).jpg')
    # read_video_from_path('videos/video.mp4')
    # read_video_from_camera(0)
    # read_image_with_rescale('photos/barcelona.png', 0.2)
    # read_video_from_path_with_rescale('videos/video.mp4', 0.5)
    # read_video_from_camera_with_rescale(0)
    read_video_from_camera_with_resolution(0, 1024, 1024)
