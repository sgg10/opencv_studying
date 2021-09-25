import cv2

# Lectura
image = cv2.imread("../images/logo_platzi.png")

# Escritura
cv2.imwrite("logo_platzi2.png", image)

# Visualización
cv2.imshow("Logo de la razon de media vida nuestra", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
