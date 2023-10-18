import streamlit as st
import os

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