from moviepy.editor import VideoFileClip, ImageSequenceClip, vfx, CompositeVideoClip, AudioFileClip
import cv2
import pyttsx3
import threading
import time

# Load the translated text from the file with the 'utf-8' encoding
with open('translated_text.txt', 'r', encoding='utf-8') as f:
    translated_text = f.read()

# Split the text by the line break to separate English and translated text
english_text, _ = translated_text.split('\n', 1)

# Convert English text to lowercase
english_text = english_text.lower()

def text_to_speech(text, audio_filename, speed_factor, volume=1.0):
    engine = pyttsx3.init()
    engine.save_to_file(text, audio_filename)
    engine.runAndWait()

    # Load the generated audio clip and adjust the volume
    audio_clip = AudioFileClip(audio_filename)
    audio_clip = audio_clip.volumex(volume)

    # Slow down the audio
    slowed_audio = audio_clip.fx(vfx.speedx, speed_factor)

    # Create a loop of the slowed audio
    looped_audio = slowed_audio.fx(vfx.loop, duration=audio_clip.duration * 3)

    return looped_audio

# Function to display the GIF at a specific speed
def display_gif(gif_clip, speed_factor):
    for frame in gif_clip.iter_frames(fps=gif_clip.fps * speed_factor):
        cv2.imshow("Slowed GIF", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

# Load the original GIF
gif_clip = VideoFileClip(r"C:\Users\Akarshan\Python App\aigif.gif")

# Define how many times you want to repeat the GIF
repeat_count = 3  # Repeat three times

# Duplicate the GIF frames
repeated_frames = [frame for frame in gif_clip.iter_frames()]

# Create an ImageSequenceClip from the list of frames
repeated_gif = ImageSequenceClip(repeated_frames, fps=gif_clip.fps)

# Save the repeated GIF to a file
repeated_gif.write_gif("repeated.gif")

# Load the repeated GIF
repeated_gif_clip = VideoFileClip("repeated.gif")

# Slow down the GIF by a factor (e.g., 2x slower)
slowed_gif_clip = repeated_gif_clip.fx(vfx.speedx, factor=0.5)  # Factor less than 1 to slow down

# Create a thread for text-to-speech with increased volume
tts_thread = threading.Thread(target=text_to_speech, args=(english_text, "output_audio.mp3", 0.5, 2.0))  # Adjust the speed factor and volume as needed
tts_thread.start()

# Get the duration of the spoken message
message_duration = gif_clip.duration * 3  # Adjust this based on your repeat_count

# Calculate the speed factor to match the GIF duration with the message duration
speed_factor = message_duration / gif_clip.duration

# Display the GIF at the adjusted speed
display_gif(slowed_gif_clip, speed_factor)
# Close the OpenCV window when the text-to-speech is complete
tts_thread.join()
cv2.destroyAllWindows()

# Load the video
video_clip = VideoFileClip(r"C:\Users\Akarshan\Python App\Video.mp4")

# Calculate the center for circular motion
center_x = video_clip.size[0] / 2 - slowed_gif_clip.size[0] / 2
center_y = video_clip.size[1] / 2

# Apply circular motion to the GIF
rotated_gif_clip = slowed_gif_clip.set_position((center_x, center_y)).set_duration(video_clip.duration)

# Load the text-to-speech audio
tts_audio = text_to_speech(english_text, "output_audio.mp3", 1, 2.0)  # Adjust the speed factor and volume as needed

# Combine the video and the rotated GIF with looped text-to-speech audio
final_video_clip = CompositeVideoClip([video_clip.set_duration(video_clip.duration), rotated_gif_clip])

# Set the audio of the final video to the looped text-to-speech audio
final_video_clip = final_video_clip.set_audio(tts_audio)

# Write the final video with looped, slowed-down text-to-speech audio
final_video_clip.write_videofile("output_sample.mp4", fps=video_clip.fps, codec='libx264', audio_codec='aac')
