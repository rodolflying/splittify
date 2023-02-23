from pytube import YouTube
from youtubesearchpython import VideosSearch
import os
import re
from moviepy.editor import AudioFileClip

def on_complete(stream,file_path):
    print(stream)
    print(file_path)
def on_progress(stream,chunk,bytes_remaining):
    print(100-bytes_remaining/stream.filesize *100)
#convert base to readeble text (remove emojis)
def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                                "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
def download_audio_only_mp4(url):
    video_object=  YouTube(url,
                    on_complete_callback=on_complete,
                    on_progress_callback = on_progress)
    #download
    video = video_object.streams.filter(only_audio=True).first()
    downloaded_file =video.download()
    base, ext = os.path.splitext(downloaded_file)
    # clean emojis from the base name
    clean_base = deEmojify(base).split("\\")[-1]
    print(clean_base, downloaded_file)
    file_path = os.getcwd() + "\\outputs\\" +  clean_base + '.mp4'
    # move to outputs folder
    os.rename(downloaded_file, file_path)

    return file_path

def search_url(query):
    # set up the search query and the number of search results you want to get
    num_results = 2
    # search for YouTube videos for the search query
    search_results = VideosSearch(query, limit=num_results).result()["result"]
    most_views = 0
    # loop through the search results and print the video title and URL
    for result in search_results:
        # decide if this is the video with more views using search_results[0]["viewCount"]["text"]
        # and converting a string like this '1,677,027 views' into an integer like this 1677027
        views_count = int(result["viewCount"]["text"].replace(",", "").replace(" views", ""))
        print(f'{result["title"]} - {views_count} views - {result["link"]}')
        # to find the video url of the result with more views, choose that link to use it later
        if "live" not in result["title"].lower():
            if views_count > most_views :
                most_views = views_count
                video_url = result["link"]
    return video_url

def convert_mp4_to_mp3(file_path):
    # set up the file paths for the input MP4 file and output MP3 file
    input_file = file_path 
    output_file = file_path.replace(".mp4","") + ".mp3"
    # create an AudioFileClip object from the input MP4 file
    clip = AudioFileClip(input_file)
    # write the audio from the clip to an MP3 file
    clip.write_audiofile(output_file)
    # close the clip to release any resources it was using
    clip.close()
    # drop the mp4 file
    os.remove(input_file)
    return output_file

def download_mp3(query):
    # Mejora: agregar fuzzy wuzzy para determinar que es lo mas parecido
    video_url = search_url(query)
    print(video_url)
    file_path = download_audio_only_mp4(video_url)
    mp3_path = convert_mp4_to_mp3(file_path)
    return mp3_path

# def main(query_paths):

#     query = input("Enter a search query (if you want to exit don't type or delete input and press enter): ")

#     query_path = download_mp3(query)
#     query_paths.append(query_path)
#     while query != "":
#         print()
#         query = input("Enter a search query (if you want to exit don't type or delete input and press enter): ")
#         if query == "":
#             break
#         query_path = download_mp3(query)
#         query_paths.append(query_path)
#     return query_paths

def main(query_paths):
    queries = []
    while True:
        query = input("Enter a search [ song and artist] )(press enter to start downloading): ")
        if query == "":
            break
        queries.append(query)

    for query in queries:
        query_path = download_mp3(query)
        query_paths.append(query_path)

    return query_paths

if __name__ == "__main__":
    query_paths = []
    query_paths = main()
    