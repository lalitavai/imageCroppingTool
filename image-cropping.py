import cv2


source = cv2.imread("sample.jpg")

window_name = "Crops Image And Save Automatically"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

# Initialize variables
bounding_box = []

def draw_rectangle(event, x, y, flags, param):
    """Mouse callback function to draw a bounding box."""
    global bounding_box

    if event == cv2.EVENT_LBUTTONDOWN:
        bounding_box = [(x, y)]  # Start point

    elif event == cv2.EVENT_LBUTTONUP:
        # Finalize the bounding box
        bounding_box.append((x, y))  # End point
        cv2.rectangle(source, bounding_box[0], bounding_box[1], (255, 255, 0), 2)
        cv2.imshow(window_name, source)
        # Automatically save the cropped face
        x1, y1 = bounding_box[0]
        x2, y2 = bounding_box[1]

        # Ensure the coordinates are valid
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        cropped_face = source[y1:y2, x1:x2]
        if cropped_face.size == 0:
            print("Error: Invalid bounding box.")
            return
        filename = "face.jpg"
        cv2.imwrite(filename, cropped_face)
        print(f"Cropped face saved as: {filename}")

# Set the mouse callback
cv2.setMouseCallback(window_name, draw_rectangle)

k = 0
# loop until escape character is pressed
while k!=27 :
        # Display the image
        cv2.imshow(window_name, source)
        cv2.putText(source, '''Choose corner and drag,Press ESC to exit ''',
                    (10, 470), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 255), 2)

        # Wait for a key press
        c = cv2.waitKey(20)& 0xFF
        if c == 27:
            break

# Clean up
cv2.destroyAllWindows()
