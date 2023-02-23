How Does Splittify Work?

The beauty of Splitify is that it is extremely easy to use. All you need to do is follow these simple steps:
Download the project https://github.com/rodolflying/splittify or clone the repository

Install the Required Libraries and programs

Before you can start using Splitify, you will need to install some libraries and programs These include:
Python: you can download from the official page. don't forget to check the "Add to path" checkbox then next, next, next as usual program.

Demucs: main library to split the audio files using an IA trained on +800 songs
pytube: Downloading from youtube youtube
searchpython: Youtube search engine for searching user queries
moviepy : to transform format from audio .mp4 to .mp3
FFMPEG installed and added to path (for any OS here the instructions : https://www.hostinger.com/tutorials/how-to-install-ffmpeg)

here all the requirements if you want to do instead:

pip install -r requirements.txt
https://github.com/rodolflying/splittify/blob/master/requirements.txt

Once you have installed these libraries, you will be ready to use Splittify.

2.  Choose Your Mode
There are two main folders in the project, one its the folder with mp3 downloads (outputs folder, you can also pass songs in mp3 that you already have!) and the other its the one with the separated tracks by demucs, where every song has its own folder with 4 tracks each.

Splitify offers two modes for you to choose from. The first mode is to input all the songs and download them, and then split them immediately. The second mode is to compare the folders "outputs" and "separated" and download the songs that are not in the "separated" folder.

simply run the main() function in the Python script. The script will prompt you to select a mode of operation and will guide you through the rest of the process.
Mode One: you will be prompted to enter a search query for each song you want to download and split. The script will use the YouTube API to find the best match for your search query and will download the audio from the resulting video. Once all of the songs have been downloaded, the script will use the Demucs library to split the audio into its component tracks.

Mode Two: the script will compare the "outputs" and "separated" folders and will download any songs that are in the "outputs" folder but not in the "separated" folder. Once all of the songs have been downloaded, the script will use the Demucs library to split the audio into its component tracks.



Example of use:

Mode One

Here's an straightforward example of how you could use Splittify. Suppose you want to separate the tracks of the songs "Distraido-Rafa Berrios" and "Os Tincoas- Deja a girar girar" (pretty known artists and songs jeje i know, i know) , here are the steps to do so in a couple of minutes:

I) Start by running the python main.py on your terminal of preference (should be on terminal cmd or bash, doesn't work on jupyter notebook) this will prompt you to select a mode.

II) Select a mode: 

1. Input all the songs names and download them and then split them immediately
2. Compare the folders 'outputs' and 'separated' and download the songs that are not in separated
Enter a number:


Mode 1

1. If you choose mode 1, the program will prompt you to input the name of the song you want to download and split.Note that it's going to choose the most likely result of a google search, so it's pretty accuarate. You can input as many paths as you like, just press enter when you are done.

2. The program will split the songs you that are in the outputs folder. You can find the individual track files of each one in the "separated/htdemucs" folder with respective name of the file. 

Mode 2 

If you choose mode 2, the program will compare the "outputs" and "separated" folders and will split the songs that arent splitted yet. If you have some problem with some of the songs, it will be downloaded anyways so the mode 2 would help you to split the songs that couldn't be splitted before and also the songs that you can put manually on the outputs folder.
