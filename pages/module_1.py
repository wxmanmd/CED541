# Firebase to store vids & comments

import streamlit as st
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

st.title("Module 1 Videos and Comments")

# Initialize Firebase with your Firebase project's credentials
firebase_credentials = credentials.Certificate("~/Documents/GitHub/CED541/credentials.js")
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
