from moviepy.editor import ImageClip, TextClip, concatenate_videoclips


# Create a list of image file paths
image_files = ["image1.png", "image2.png", "image3.png"]

# Create a list of text strings
text_strings = ["Beatiful scenary", "Keyboard SUI", "Hellooo"]

# Create an empty list to store the clips
clips = []

# Iterate through the images and text
for i in range(len(image_files)):
    # Open the image using the ImageClip class
    image = ImageClip(image_files[i])
    
    # Create a text clip using the TextClip class
    text = TextClip(text_strings[i], fontsize=24, color='white')
    
    # Set the duration of the image and text clips
    image_duration = 5
    text_duration = 2
    
    # Position the text on the image
    text = text.set_pos('center').set_duration(text_duration)
    final_clip = CompositeVideoClip([image, text])
    final_clip = final_clip.set_duration(image_duration)
    clips.append(final_clip)

# Concatenate the clips together
final_video = concatenate_videoclips(clips)

# Write the video to a file
final_video.write_videofile("final_video.mp4")
