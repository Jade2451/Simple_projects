from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark():
    """
    Adds a text watermark to a specified image.
    """
    print("🖼️  Image Watermarker 🖼️")

    try:
        # --- Get User Input ---
        image_path = input("Enter the path to the image: ")
        watermark_text = input("Enter the watermark text: ")
        
        # --- Open the image ---
        original_image = Image.open(image_path).convert("RGBA")
        width, height = original_image.size

        # --- Prepare to draw on the image ---
        txt_image = Image.new("RGBA", original_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_image)

        # --- Set up font and text properties ---
        try:
            # Try to use a common system font
            font = ImageFont.truetype("arial.ttf", size=int(height / 20))
        except IOError:
            # If not found, use a default font
            font = ImageFont.load_default()
            print("Arial font not found, using default font.")

        # Calculate text size and position
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Position at the bottom-right corner with some padding
        margin = 10
        x = width - text_width - margin
        y = height - text_height - margin
        position = (x, y)

        # --- Add the watermark text ---
        # The fourth value in the color tuple is transparency (0-255)
        draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)

        # --- Combine the original image with the text layer ---
        watermarked_image = Image.alpha_composite(original_image, txt_image)

        # --- Save the new image ---
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_watermarked.png"
        watermarked_image.convert("RGB").save(output_path)
        
        print(f"\n✅ Success! Watermarked image saved as '{output_path}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    add_watermark()
