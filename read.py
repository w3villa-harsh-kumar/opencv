import cv2 as cv

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

if __name__ == '__main__':
    read_image('photos/image (1).jpg')
    # read_video_from_path('videos/video.mp4')
    # read_video_from_camera(0)
