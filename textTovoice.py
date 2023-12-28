from gtts import gTTS
from pydub import AudioSegment

def text_to_speech(input_text, output_mp3):
    # Create a gTTS object
    tts = gTTS(text=input_text, lang='en')
    tts.lang = 'bn'
    # Save the speech as an MP3 file
    tts.save(output_mp3)

def main():
    # Specify the file paths
    input_file_path = 'story.txt'
    output_mp3_path = 'speech2.mp3'

    # Open the text file and read its content
    with open(input_file_path, 'r') as file:
        text_content = file.read()

    # Convert the text to speech and save it as an MP3 file
    text_to_speech(text_content, output_mp3_path)

if __name__ == "__main__":
    main()
