import streamlit as st
import os

st.title("Audio Player")

# Get list of audio files
audio_dir = "AudioFiles"
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

if not audio_files:
    st.warning("No audio files found in the AudioFiles directory!")
else:
    # Create a selectbox to choose the audio file
    selected_file = st.selectbox(
        "Select an audio file to play:",
        audio_files
    )
    
    # Display the audio player
    audio_path = os.path.join(audio_dir, selected_file)
    st.audio(audio_path)
    
    # Display file information
    file_size = os.path.getsize(audio_path) / 1024  # Size in KB
    st.info(f"File: {selected_file}\nSize: {file_size:.1f} KB")
