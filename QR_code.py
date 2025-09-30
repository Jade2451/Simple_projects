import qrcode
import os

def create_qr_code():
    """
    Generates a QR code from user input and saves it as a PNG image.
    """
    print("📲 QR Code Generator 📲")
    
    # --- Get User Input ---
    data_to_encode = input("Enter the text or URL to encode in the QR code: ")
    output_filename = input("Enter the desired output filename (e.g., website.png): ")

    # --- Validate Input ---
    if not data_to_encode:
        print("Error: You must enter some data to encode.")
        return
        
    if not output_filename:
        print("Error: You must provide an output filename.")
        return
        
    # Add .png extension if the user forgot it
    if not output_filename.lower().endswith('.png'):
        output_filename += '.png'

    # --- Generate the QR Code ---
    try:
        # Create qr code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add data to the instance
        qr.add_data(data_to_encode)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save(output_filename)
        
        print(f"\n✅ Success! QR code saved as '{output_filename}' in the current directory.")
        print(f"Full path: {os.path.abspath(output_filename)}")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


# --- Main execution block ---
if __name__ == "__main__":
    create_qr_code()
