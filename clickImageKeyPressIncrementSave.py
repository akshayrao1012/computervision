# Import the required libraries
import cv2
import os

# Create a VideoCapture object to capture video from the default camera (index 0)
cap = cv2.VideoCapture(0)  # 0 stands for the default camera

# Set the initial value of the counter
counter = 1

# Start an infinite loop to continuously capture frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()  # 'ret' is a boolean indicating whether the frame was captured successfully

    # Display the resulting frame in a window titled 'Press c to capture, q to quit'
    cv2.imshow('Press c to capture, q to quit', frame)

    # Check if the 'c' key has been pressed
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Define the file name with the counter value
        file_name = f"captured_image_{counter}.jpg"

        # Check if the file already exists
        while os.path.exists(file_name):
            # Increment the counter if the file already exists
            counter += 1
            file_name = f"captured_image_{counter}.jpg"

        # Save the captured frame with the unique file name
        cv2.imwrite(file_name, frame)
        # Print a message to indicate that the image has been successfully captured and saved with the unique file name
        print(f"Image captured and saved as {file_name}")

        # Increment the counter for the next image
        counter += 1

    # Check if the 'q' key has been pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # If the 'q' key is pressed, break out of the loop to stop capturing frames
        break

# Release the VideoCapture object to free the camera
cap.release()

# Close the display window
cv2.destroyAllWindows()
