import cv2
import numpy as np
image = None  # Placeholder for the image variable
while True:
    print("\n===== NumPy Image Editor =====")
    print("1. Load Image")
    print("2. Show Image")
    print("3. Grayscale")
    print("4. Negative")
    print("5. Increase Brightness")
    print("6. Rotate 90°")
    print("7. Flip Horizontal")
    print("8. Blur")
    print("9. Edge Detection")
    print("10. Save Image")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        path = input("Enter image path: ")
        image = cv2.imread(path)

        if image is None:
            print("Image not found!")
        else:
            print("Image Loaded Successfully!")

    elif choice == "2":
        if image is not None:
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Load an image first.")

    elif choice == "3":
        if image is not None:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            print("Converted to Grayscale.")
        else:
            print("Load an image first.")

    elif choice == "4":
        if image is not None:
            image = 255 - image
            print("Negative Applied.")
        else:
            print("Load an image first.")

    elif choice == "5":
        if image is not None:
            image = cv2.convertScaleAbs(image, alpha=1, beta=50)
            print("Brightness Increased.")
        else:
            print("Load an image first.")

    elif choice == "6":
        if image is not None:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            print("Image Rotated.")
        else:
            print("Load an image first.")

    elif choice == "7":
        if image is not None:
            image = cv2.flip(image, 1)
            print("Image Flipped.")
        else:
            print("Load an image first.")

    elif choice == "8":
        if image is not None:
            image = cv2.GaussianBlur(image, (9, 9), 0)
            print("Blur Applied.")
        else:
            print("Load an image first.")

    elif choice == "9":
        if image is not None:
            if len(image.shape) == 3:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                gray = image

            image = cv2.Canny(gray, 100, 200)
            print("Edge Detection Applied.")
        else:
            print("Load an image first.")

    elif choice == "10":
        if image is not None:
            name = input("Enter output filename (example: output.jpg): ")
            cv2.imwrite(name, image)
            print("Image Saved Successfully!")
        else:
            print("Load an image first.")

    elif choice == "11":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")