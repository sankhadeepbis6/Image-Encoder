import encoder
import os


if __name__ == "__main__":

    key = input("Enter the key: ")

    app = encoder.KeyMatrix(key)

    choice = 1

    while choice:
        print("0. To Exit")
        print("1. Encode Image")
        print("2. Decode Image")
        print("3. Show Histogram")
        print("4. Show Image")
        print("5. Image Comparison")
        print("6. Change Key")
        print("7. Show PSNR")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            app.star_mul("Thank You", "*")

        elif choice == 1:
            app.star_mul("Encoder", "-")
            input_path = input("Enter path and name of the image: ")
            output_path = input("Enter output path and name of image: ")

            if not os.path.exists(input_path):
                app.star_mul("Path doe's not exists","*", 10)
                continue

            app.encode_image(input_path, output_path)
            app.star_mul("Encoded")

        elif choice == 2:
            app.star_mul("Decoder", "-")
            input_path = input("Enter path and name of the image: ")
            output_path = input("Enter output path and name of image: ")

            if not os.path.exists(input_path):
                app.star_mul("Path doe's not exists", "*", 10)
                continue

            app.decode_image(input_path, output_path)
            app.star_mul("Decoded")

        elif choice == 3:
            app.star_mul("Histogram", "-")
            path = input("Enter path and name of image: ")

            if not os.path.exists(path):
                app.star_mul("Path doe's not exists", "*", 10)
                continue

            app.histogram(path)
            app.star_mul("Histogram", "*")

        elif choice == 4:
            app.star_mul("Show Image", "-")
            path = input("Enter path and name of image: ")

            if not os.path.exists(path):
                app.star_mul("Path doe's not exists", "*", 10)
                continue

            app.show_image(path)
            app.star_mul("Image Shower", "-")

        elif choice == 5:
            app.star_mul("Image Comparison", "-")
            path_1 = input("Enter path of 1st image: ")
            path_2 = input("Enter path of 2nd image: ")

            if not os.path.exists(path_1) or not os.path.exists(path_2):
                app.star_mul("Path doe's not exists", "*", 10)
                continue

            mistake, accuracy = app.image_compare(path_1, path_2)
            print("Number of mistakes:", mistake)
            print("Accuracy:", accuracy)
            app.star_mul("Compared")

        elif choice == 6:
            app.star_mul("Change Key", "-")
            input_key = input("Enter new key: ")
            app.key_builder(input_key)
            app.star_mul("Key Changed", "*")

        elif choice == 7:
            app.star_mul("Image PSNR", "-")
            path_1 = input("Enter path of 1st image: ")
            path_2 = input("Enter path of 2nd image: ")

            if not os.path.exists(path_1) or not os.path.exists(path_2):
                app.star_mul("Path doe's not exists", "*", 10)
                continue

            psnr, mse = app.show_psnr(path_1, path_2)
            print("The PSNR is:", psnr)
            print("The value of MSE:", mse)
            app.star_mul("PSNR shown")

        else:
            app.star_mul("Wrong Input", "-")
            app.star_mul("Try Again", "*")



