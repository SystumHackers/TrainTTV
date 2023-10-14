import openai
import moviepy.editor as mp
from moviepy.editor import TextClip

# Set your OpenAI API key
openai.api_key = "sk-...xzgd"

def generate_speech(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Convert the following text to speech: '{text}'",
        max_tokens=100,
    )
    return response.choices[0].text
def text_to_video(text):
    # Generate speech using GPT-3
    speech = generate_speech(text)

    # Create a TextClip with the generated speech
    video_clip = TextClip(speech, color='white', bg_color='black', fontsize=20)
    
    # Set the video duration (adjust as needed)
    video_clip = video_clip.set_duration(10)
    
    # Write the video to a file
    video_clip.write_videofile("output.mp4", codec="libx264")
def main():   
 user_text = input("Enter the text you want to convert to a video: ")
text_to_video(user_text)
print("Video successfully created as 'output.mp4'.")

if __name__ == "__main__":
    main()