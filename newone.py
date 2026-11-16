# from PIL import Image
# import os
# import tkinter as tk
# from tkinter import filedialog

# def upload_image():
#     """Function to upload an image file"""
#     file_path = filedialog.askopenfilename(title="Select Image File",
#                                             filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")))
#     return file_path

# def split_image(image_path, threshold, num_shares, output_folder):
#     """Function to split the image using Shamir's Secret Sharing"""
#     try:
#         # Open the image file
#         with open(image_path, 'rb') as f:
#             image_data = f.read()

#         # Create the output folder if it does not exist
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         # Split the image data using Shamir's Secret Sharing
#         share_data = _split_secret(image_data, threshold, num_shares)

#         # Save each share as a separate file
#         for i, share in enumerate(share_data):
#             share_path = os.path.join(output_folder, f'share_{i + 1}.bin')
#             with open(share_path, 'wb') as f:
#                 f.write(share)
#             print(f"Share {i + 1} saved as: {share_path}")

#         print("Image shared successfully.")
#     except Exception as e:
#         print(f"Error: {e}")

# def _split_secret(secret, threshold, num_shares):
#     """Function to split the secret using Shamir's Secret Sharing"""
#     share_data = []
#     # Implement Shamir's Secret Sharing algorithm here
#     # This is just a placeholder implementation
#     for _ in range(num_shares):
#         share_data.append(secret)

#     return share_data

# def main():
#     # Create the main window
#     root = tk.Tk()
#     root.title("Shamir Secret Image Sharing")
#     root.geometry("400x200")

#     # Function to handle sharing when the button is clicked
#     def share_image():
#         # Ask the user to upload an image file
#         image_path = upload_image()

#         # Check if the user canceled the upload
#         if not image_path:
#             status_label.config(text="No image selected.")
#             return

#         # Split the image using Shamir's Secret Sharing
#         # Set your custom output folder path here
#         output_folder = "F:\Steganographyx-main"
#         split_image(image_path, threshold=3, num_shares=5, output_folder=output_folder)
#         status_label.config(text="Image shared successfully.")

#     # Create a button to trigger the image sharing process
#     share_button = tk.Button(root, text="Share Image", command=share_image)
#     share_button.pack(pady=10)

#     # Create a label to display status messages
#     status_label = tk.Label(root, text="")
#     status_label.pack(pady=10)

#     # Run the Tkinter event loop
#     root.mainloop()

# if __name__ == "__main__":
#     main()
import os
import tkinter as tk
from tkinter import filedialog

def upload_image():
    """Function to upload an image file"""
    file_path = filedialog.askopenfilename(title="Select Image File",
                                            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")))
    return file_path

def split_image(image_path, threshold, num_shares, output_folder):
    """Function to split the image using Shamir's Secret Sharing"""
    try:
        # Open the image file
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # Create the output folder if it does not exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Split the image data using Shamir's Secret Sharing
        share_data = _split_secret(image_data, threshold, num_shares)

        # Save each share as a separate file
        for i, share in enumerate(share_data):
            share_path = os.path.join(output_folder, f'share_{i + 1}.bin')
            with open(share_path, 'wb') as f:
                f.write(share)
            print(f"Share {i + 1} saved as: {share_path}")

        print("Image shared successfully.")
    except Exception as e:
        print(f"Error: {e}")

def _split_secret(secret, threshold, num_shares):
    """Function to split the secret using Shamir's Secret Sharing"""
    share_data = []
    # Implement Shamir's Secret Sharing algorithm here
    # This is just a placeholder implementation
    for _ in range(num_shares):
        share_data.append(secret)

    return share_data

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Shamir Secret Image Sharing")
    root.geometry("400x200")
    root.configure(bg="#f0f0f0")  # Set background color

    # Function to handle sharing when the button is clicked
    def share_image():
        # Ask the user to upload an image file
        image_path = upload_image()

        # Check if the user canceled the upload
        if not image_path:
            status_label.config(text="No image selected.")
            return

        # Split the image using Shamir's Secret Sharing
        # Set your custom output folder path here
        output_folder = "F:/Steganographyx-main"  # Change to your desired folder path
        split_image(image_path, threshold=3, num_shares=5, output_folder=output_folder)
        status_label.config(text="Image shared successfully.")

    # Create a button to trigger the image sharing process
    share_button = tk.Button(root, text="Share Image", command=share_image, bg="#008CBA", fg="white", font=("Arial", 12))
    share_button.pack(pady=10)

    # Create a label to display status messages
    status_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 10))
    status_label.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
