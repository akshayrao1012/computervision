# Import the OpenCV library
import cv2

# Create a VideoCapture object to capture video from the default camera (index 0)
cap = cv2.VideoCapture(0)  # 0 stands for the default camera

# Capture a frame from the camera
ret, frame = cap.read()  # 'ret' is a boolean indicating whether the frame was captured successfully

# Release the VideoCapture object to free the camera
cap.release()

# Save the captured frame as an image file named 'captured_image.jpg'
cv2.imwrite('captured_image.jpg', frame)

# Display a message to indicate that the image has been successfully captured and saved
print("Image captured and saved as captured_image.jpg")
