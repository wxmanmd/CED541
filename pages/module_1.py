import streamlit as st
import os
import pcloud

st.title("Module 1")

st.title("Module 1 Videos")
st.header("Upload your video")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.spinner("Uploading...")
    st.write("File uploaded.")
    #st.video(uploaded_file)

st.header("Use the dropdown list to choose a file to watch")

#keep video script

def get_video_files_in_dir(directory):
    out = []
    for item in os.listdir(directory):
        try:
            name, ext = item.split(".")
        except:
            continue
        if name and ext:
            if ext in VIDEO_EXTENSIONS:
                out.append(item)
    return out

avdir = os.path.expanduser("~")
files = get_video_files_in_dir(avdir)

if len(files) == 0:
    st.write(
        "No videos have yet been uploaded. Videos are needed to activate this player."
        % avdir
    )

else:
    filename = st.selectbox(
        "Select a video file to play" % avdir,
        files,
        0,
    )

st.video(os.path.join(avdir, filename))

def shorten_vid_option(opt):
    return opt.split("/")[-1]

#drop down list

vid = st.selectbox(
    "Pick a video to play",
    (
        "https://youtu.be/_T8LGqJtuGc",
        "https://www.youtube.com/watch?v=kmfC-i9WgH0",
        "https://www.youtube.com/embed/sSn4e1lLVpA",
        "http://www.rochikahn.com/video/videos/zapatillas.mp4",
        "http://www.marmosetcare.com/video/in-the-wild/intro.webm",
        "https://www.orthopedicone.com/u/home-vid-4.mp4",
    ),
    0,
    shorten_vid_option,
)

st.video(vid)

# NEW code

import streamlit as st
import os
import pcloud

st.title("Video Upload and Playback with pCloud")

# Initialize pCloud API client
pcloud_client = pcloud.Client(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')

# Create a folder in pCloud to store uploaded videos
folder_name = 'uploaded_videos'
folder_info = pcloud_client.create_folder(folder_name)

# Upload videos
uploaded_files = st.file_uploader("Upload video(s)", type=["mp4", "avi"], accept_multiple_files=True)

# Save the uploaded videos to pCloud and display success
if uploaded_files:
    for video in uploaded_files:
        video_name = os.path.join(folder_name, video.name)
        pcloud_client.uploadfile(video, video_name)
        st.success(f"Video '{video.name}' uploaded to pCloud.")

# List and select videos in the pCloud folder
video_list = pcloud_client.listfolder(folder_info['metadata']['folderid'])['metadata']['contents']

# Create a dropdown menu to select a video to play
videos = [video['name'] for video in video_list]
selected_video = st.selectbox("Select a video to play", videos)

# Display the selected video
if selected_video:
    video_path = os.path.join(folder_name, selected_video)
    st.video(f"https://usercontent.pcloud.com/{video_path}")
