import cv2

try:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
except cv2.error as e:
    print(f"Hata: Haar Cascade dosyası yüklenemedi. 'haarcascade_frontalface_default.xml' dosyasının doğru yolda olduğundan emin olun.\nOpenCV Hatası: {e}")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera başlatılamadı.")
    exit()

print("Kamera başlatıldı. Çıkmak için 'q' tuşuna basın.")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Hata: Görüntü alınamadı.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  
        minNeighbors=5,   
        minSize=(30, 30)  
    )

    
    for (x, y, w, h) in faces:
        
        face_roi = frame[y:y+h, x:x+w]

        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)

        frame[y:y+h, x:x+w] = blurred_face

    cv2.imshow('Gercek Zamanli Yuz Bulaniklastirma', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Uygulama sonlandırıldı.")