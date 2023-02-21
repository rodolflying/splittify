import subprocess
import download_songs
import os
# set up the input and output file paths
# input_files = download_songs.main(query_paths = [])
# print(input_files)
def user_input():
    ''' There are 2 modes
        Mode One:  is input all the songs and download them and  then split them inmediately
    and the other is input
        Mode Two:  is compare the folders "outputs" and "separated" and download the songs that are not in separated
    '''
    print("Select a mode: ")
    print("1. Input all the songs and download them and  then split them inmediately")
    print("2. Compare the folders 'outputs' and 'separated' and download the songs that are not in separated")
    mode = input("Enter a number: ")
    if mode == "1":
        print("Mode 1 Activated")
        input_files = download_songs.main(query_paths = [])
        # print songs to be processed formatting properly
        print("Songs to be processed: ")
        for song in input_files:
            print(song)
    elif mode == "2":
        print("Mode 2 Activated")
        # Compare the folders "outputs" and "separated" and download the songs that are not in separated
        input_files = compare_folders()
        # print songs to be processed formatting properly
        print("Songs to be processed: ")

        ## improvement idea: make print a function and use it in both modes
        ## improvement idea: print also the time stimation based on the other songs
        ## times, in order to do this must capture the starting time and the ending time an then calculate the time differences and then with some meta data from the songs determine a estimation of the time it will take to process the songs
        for song in input_files:
            print(song)

    return input_files

def compare_folders():
    # Compare the folders "outputs" and "separated" and download the songs that are not in separated
    # get the list of files in the outputs folder
    outputs = os.listdir("outputs")
    # get the list of files in the separated folder
    separated = os.listdir("separated\\htdemucs")

    songs_to_proccess = []
    # using the files of outputs folder , wich are songs in .mp3 format, search for their respective folder inside the separated folders name. consider that the folder name is the same as the song name but without the .mp3 extension
    for song in outputs:
        # get the song name without the .mp3 extension
        song_name = song.replace(".mp3", "")
        # if the song name is not in the separated folder, download the song
        if song_name not in separated:
            # add the song name to the separated list
            songs_to_proccess.append(os.getcwd()+"\\outputs\\"+ song)
    # return the list of songs to be processed

    return songs_to_proccess



    return input_files
def split_songs(input_files):
    # loop through the input files and process each file with Demucs
    for input_file in input_files:
        # set up the demucs command with the input and output file paths
        command = f'python -m demucs -d cpu --mp3 --mp3-bitrate 320 "{input_file}"'
        # use subprocess to run the demucs command as a subprocess
        p = subprocess.Popen(command, stdout=subprocess.PIPE,shell = True)
        # wait for the subprocess to finish
        out = p.stdout.read()
        print(f"\nEl proceso esta corriendo en la memoria: {p} \nProceso {input_file} terminado. Output:  {out}")
        # print a message to confirm the file has been processed
        print(f"Processed")

def main():
    # get the list of files to be processed and download if necessary
    input_files = user_input()
    # process the files with Demucs
    split_songs(input_files)

if __name__ == "__main__":
    main()
