import cv2
import numpy as np
from sklearn.cluster import KMeans

def summarize_video(video_path, num_frames):
    # Load the video and retrieve the frame rate
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    
    # Initialize a list to store the frames
    frames = []
    
    # Read the frames from the video and store them in the list
    success, frame = video.read()
    while success:
        frames.append(frame)
        success, frame = video.read()
        
    # If the number of frames is less than or equal to the desired number of frames, return the original video
    if len(frames) <= num_frames:
        return frames
    
    # Convert the frames to a 4D array
    frames_array = np.asarray(frames)
    frames_array = np.expand_dims(frames_array, axis=3)
    
    # Use K-Means clustering to group the frames into num_frames clusters
    kmeans = KMeans(n_clusters=num_frames).fit(frames_array)
    
    # Select the centroid of each cluster as the representative frame
    summarized_frames = kmeans.cluster_centers_
    
    # Convert the summarized frames back to 8-bit unsigned integers
    summarized_frames = np.uint8(summarized_frames)
    
    # Return the summarized frames
    return summarized_frames

# Test the summarize_video function
video_path = "sample_video.mp4"
num_frames = 5
summarized_frames = summarize_video(video_path, num_frames)

print('summarized_frames -> ', summarized_frames)