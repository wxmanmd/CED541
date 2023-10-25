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
# Firebase to store vids & comments

import streamlit as st
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

st.title("Video Upload and Comments with Firebase")

# Initialize Firebase with your Firebase project's credentials
firebase_credentials = credentials.Certificate("path/to/your/firebase-credentials.json")
firebase_app = firebase_admin.initialize_app(firebase_credentials)

# Create a reference to your Firebase Realtime Database or Firestore
firebase_db = db.reference('/videos_and_comments')

# Upload videos
uploaded_files = st.file_uploader("Upload video(s)", type=["mp4", "avi"], accept_multiple_files=True)

if uploaded_files:
    for video in uploaded_files:
        video_name = video.name
        video_url = None  # You'll store the video URL in Firebase
        # Store the video in Firebase Storage or as a download URL in the database
        # You can use Firebase Storage to store the actual video files

        # Save video information to Firebase
        video_data = {
            "name": video_name,
            "url": video_url
        }
        video_ref = firebase_db.child("videos").push(video_data)

        st.success(f"Video '{video_name}' uploaded.")

# Create a dropdown menu to select a video to play
videos = firebase_db.child("videos").get()
video_names = [video.val()["name"] for video in videos]
selected_video_name = st.selectbox("Select a video to play", video_names)

if selected_video_name:
    selected_video = None  # Retrieve the selected video data from Firebase
    video_url = selected_video.val()["url"]
    st.video(video_url)

    st.subheader("Comments")
    comment = st.text_area("Add your comment:")
    if st.button("Submit"):
        # Save the comment in Firebase under the selected video
        comment_data = {
            "text": comment,
            "video_id": selected_video.key
        }
        firebase_db.child("comments").push(comment_data)

    comments = firebase_db.child("comments").order_by_child("video_id").equal_to(selected_video.key).get()
    for comment in comments:
        st.write(comment.val()["text"])
