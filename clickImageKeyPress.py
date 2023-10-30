# Import the OpenCV library
import cv2

# Create a VideoCapture object to capture video from the default camera (index 0)
cap = cv2.VideoCapture(0)  # 0 stands for the default camera

# Start an infinite loop to continuously capture frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()  # 'ret' is a boolean indicating whether the frame was captured successfully

    # Display the resulting frame in a window titled 'Press c to capture'
    cv2.imshow('Press c to capture', frame)

    # Check if the 'c' key has been pressed
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # If the 'c' key is pressed, save the captured frame as an image file named 'captured_image.jpg'
        cv2.imwrite('captured_image.jpg', frame)
        # Print a message to indicate that the image has been successfully captured and saved
        print("Image captured and saved as captured_image.jpg")
        # Break out of the loop to stop capturing frames
        break

# Release the VideoCapture object to free the camera
cap.release()

# Close the display window
cv2.destroyAllWindows()
