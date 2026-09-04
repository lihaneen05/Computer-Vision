import cv2

# Path pointing from Files/ folder to Images/ folder
image_path = "../Images/fall.png"

# Load the image
image = cv2.imread(image_path)

# Check if the image loaded successfully
if image is not None:
    # Display the image in a window
    cv2.imshow("Loaded Image", image)
    
    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load image. Check the file path.")
