Splittify

Splittify is a Python script that can download any song from the internet (as long as its on youtube) 
and split in 4 wav audio files (drums, bass, vocals and others) using the Demucs library. demucs its commonly
used in the terminal but with this aproach its done using subprocess library.

There are two main folders in the project, one its the folder with mp3 downloads (outputs folder) and the other
its the one with the separated tracks by demucs.

It provides two modes of operation: one in which the user inputs a list of songs to download and split, one after one,
and inmediatly split the track and another in which the script compares the "outputs" and "separated" folders and downloads any songs
that are not in the "separated" folder (this is in case of some error while doing the splitting)

Requirements
Splittify requires the following libraries to be installed:

demucs -> main library to split the audio files (for further info https://github.com/facebookresearch/demucs)
pytube -> Downloading from youtube
youtubesearchpython -> Youtube search engine for searching user queries
moviepy -> to transform format from audio .mp4 to .mp3

you can run also the requeriments.txt in terminal with pip install -r requirements.txt

IMPORTANT: ffmpeg needs to be in path of the system (or environ) for demucs to work

with this tutorial you should be able to install it correctly and add it to the path in any OS :

https://www.hostinger.com/tutorials/how-to-install-ffmpeg

To use Splittify, simply run the main() function in the Python script. The script will prompt you to select a mode of operation and will guide you through the rest of the process.

Mode One
In Mode One, you will be prompted to enter a search query for each song you want to download and split. The script will use the YouTube API to find the best match for your search query and will download the audio from the resulting video. Once all of the songs have been downloaded, the script will use the Demucs library to split the audio into its component tracks.

Mode Two
In Mode Two, the script will compare the "outputs" and "separated" folders and will download any songs that are in the "outputs" folder but not in the "separated" folder. Once all of the songs have been downloaded, the script will use the Demucs library to split the audio into its component tracks.

Acknowledgments
Splittify was created by rodolflying ( for further contact reply to rodolflying@gmail.com). It is based on the Demucs library by Facebook AI Research.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
