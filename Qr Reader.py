import cv2

# Open the camera (0 = default webcam)
cap = cv2.VideoCapture(0)

# Create a QR detector
detector = cv2.QRCodeDetector()

print("Scanning... Press q to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect and decode the QR
    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        print("QR Code detected:", data)

    # Show camera feed
    cv2.imshow("QR Scanner", frame)

    # Quit by pressing Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()