# Import the OpenCV library
import cv2

# Create a VideoCapture object to capture video from the default camera (index 0)
cap = cv2.VideoCapture(0)  # 0 stands for the default camera

# Start an infinite loop to continuously capture frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()  # 'ret' is a boolean indicating whether the frame was captured successfully

    # Display the resulting frame in a window titled 'Laptop Camera'
    cv2.imshow('Laptop Camera', frame)

    # Exit the loop and stop capturing if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()
