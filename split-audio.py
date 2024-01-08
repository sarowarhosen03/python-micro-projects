import os
from pydub import AudioSegment

def split_audio(input_file, output_folder, segment_length_ms=119000):
    audio = AudioSegment.from_file(input_file)
    total_duration_in_ms = audio.duration_seconds * 1000


    current_start_time = 0
    segment_number = 1

    while current_start_time < total_duration_in_ms:
        current_end_time = min(current_start_time + segment_length_ms, total_duration_in_ms)
        segment = audio[current_start_time:current_end_time]
        segment.export(f"{output_folder}/segment_{segment_number}.mp3", format="mp3")

        current_start_time += segment_length_ms
        segment_number += 1

# Replace 'input_audio.mp3' with your audio file and specify the output folder
filename = 'speech2.mp3'
folder_name = filename.split('.')[0]

# if not exist folder with this name, create one
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

split_audio(filename, folder_name)
