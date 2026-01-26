import cv2



# Get the name of the person before starting the camera
person_name = input("Enter the name of the person to detect: ")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_c = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 

# capture frames from a camera
cap = cv2.VideoCapture(0)

while True: 
    # reads frames from a camera
    ret, img = cap.read() 
    if not ret:
        break

    # convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2) 
        
        # --- NEW FEATURE: ADD NAME TEXT ---
        # Parameters: (image, text, position, font, scale, color, thickness)
        cv2.putText(img, person_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detects eyes inside the face ROI
        eyes = eye_c.detectMultiScale(roi_gray) 

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 127, 255), 2)

    # Display the image
    cv2.imshow('Face and Eye Detection', img)

    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
