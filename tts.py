from gtts import gTTS
import os

def convert_text_to_speech():
    """
    Converts user-provided text into an MP3 audio file.
    """
    print("🔊 Text-to-Speech Converter 🔊")

    try:
        # --- Get User Input ---
        text_to_speak = input("Enter the text you want to convert to speech: ")
        
        if not text_to_speak:
            print("No text entered. Exiting.")
            return

        output_filename = input("Enter the desired output filename (e.g., audio.mp3): ")
        if not output_filename.lower().endswith('.mp3'):
            output_filename += '.mp3'

        # --- Create the gTTS object ---
        print("\nConverting text to speech... This may take a moment.")
        tts = gTTS(text=text_to_speak, lang='en', slow=False)
        
        # --- Save the audio file ---
        tts.save(output_filename)
        
        print(f"\n✅ Success! Audio saved as '{output_filename}'")
        print(f"Full path: {os.path.abspath(output_filename)}")

    except Exception as e:
        print(f"\n❌ An error occurred. Please check your internet connection. Details: {e}")


# --- Main execution block ---
if __name__ == "__main__":
    convert_text_to_speech()
