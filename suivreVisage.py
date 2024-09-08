import cv2

# Chargement du modèle de détection de visage
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialisation de la caméra
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Envoyer les commandes au robot pour suivre le visage
        # (à implémenter)

    # Affichage de l'image
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:  # Appuyer sur 'Esc' pour quitter
        break

cap.release()
cv2.destroyAllWindows()
