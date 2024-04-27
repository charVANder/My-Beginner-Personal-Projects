''' 
Evangeline Kim
December 13th, 2023
Youtube URL to mp3/mp4 downloads
'''

# Import necessary libraries
from os import remove
from urllib.parse import urlsplit
from pytube import YouTube # class YouTube only receives strings as a URL attribute
from moviepy.editor import VideoFileClip # Also has filename and bitrate optional arguments


def download_and_convert(url_link, filename: str = "ytmp3_file", bitrate: str = "128k"): 
    '''Function download_and_convert() takes a youtube link, downloads the mp4 video, and extracts/downloads
    the mp3 file (files go into the same directory as this program). The leftover mp4 file will be deleted.

    Parameters: url_link, optional name of your file (filename), and optional audio quality (bitrate)
    Returns: Downloaded mp3 file will appear in the same directory as this program.
    '''  
    try:
        # Create Youtube object using the URL
        yt_link = YouTube(url_link)
        
        # Download the mp4
        print(f"\n{'-'*30}LOADING VIDEO...{'-'*30}")
        yt_video = yt_link.streams.get_highest_resolution() # Ensures the best resolution video. Good if you wanted to keep mp4.
        yt_video.download(filename=filename+".mp4") # Download file as mp4. Concatenate to add .mp4
        print(f"\n{'-'*14}MP4 DOWNLOAD COMPLETE. NOW CONVERTING TO MP3...{'-'*14}")

        # Convert mp4 to mp3
        yt_video = VideoFileClip(filename+".mp4") # Loads video from the downloaded mp4 file
        yt_video.audio.write_audiofile((filename+".mp3"), bitrate=bitrate) # Converting...
        
        # Delete the original mp4 and give closing print statement.
        print(f"\n{'-'*14}MP3 CONVERSION COMPLETE. NOW DELETING THE MP4...{'-'*14}")
        remove(filename+".mp4")
        print(f"\n{'-'*24}MP3 DOWNLOAD COMPLETE! ENJOY!{'-'*24}")    
    
    # Account for more unexpected errors
    except Exception as e:
        print(f'''Unexpected Error: {e}\n{"-"*10}Have you tried{"-"*10}\nChecking all your URLs?\nUsing the correct file path?
Checking your software installations?\nFor more information, try reading the README file\n{"-"*34}''') 


def download_mp4(url_link, filename: str = "ytmp4_file"):
    '''Function download_mp4() takes a youtube link and downloads the mp4 video at the highest resolution.

    Parameters: url_link, optional name of your file (filename).
    Returns: Downloaded mp4 file will appear in the same directory as this program.
    ''' 
    try:
        # Create Youtube object using the URL
        yt_link = YouTube(url_link)
        
        # Download the mp4
        print(f"\n{'-'*30}LOADING VIDEO...{'-'*30}")
        yt_video = yt_link.streams.get_highest_resolution() # Ensures the best resolution video. Good if you wanted to keep mp4.
        yt_video.download(filename=filename+".mp4") # Download file as mp4. Concatenate to add .mp4
        print(f"\n{'-'*24}MP4 DOWNLOAD COMPLETE. ENJOY!{'-'*24}")
        
    # Account for more unexpected errors
    except Exception as e:
        print(f'''Unexpected Error: {e}\n{"-"*10}Have you tried{"-"*10}\nChecking all your URLs?\nUsing the correct file path?
Checking your software installations?\nFor more information, try reading the README file\n{"-"*34}''')


def validate_url(url):
    '''Function validate_url takes a url and makes sure that it is valid.

    Parameters: The URL that needs to be validated (url)
    Returns: Validates that the URL has a scheme and a network location. False otherwise.
    '''
    try:
        tester = urlsplit(url)
        return all([tester.scheme, tester.netloc]) # Checks network location.
    except ValueError: # Accounting for value errors
        return False


def get_file_urls(file_path):
    '''Function get_file_URLs takes a file, extracts all of the youtube URLs, and puts them into a list.

    Parameters: The file that holds the URLs (file)
    Returns: A list of all the youtube URLs in the file (url_list)
    '''
    url_list = []
    with open(file_path, "r") as file:
        for line in file:
            if line.strip() != '': # Accounting for return lines
                url = line.strip()
                if validate_url(url):
                    url_list.append(url)
                elif validate_url(url) == False: # Will account for invalid URLs
                    print(f"\nInvalid URL found: {url}\nPlease try fixing your URL file and try again.")
    return url_list


def main():
    # Choosing whether to paste the URL, read through a file, or run the test URL
    option = input(f'''\n{"~"*25}WELCOME TO VANS YOUTUBE-2-MP3/MP4 CONVERTER/DOWNLOADER!{"~"*25}
WOULD YOU LIKE TO...
OPTION 1: Paste in your URL? --> press 1
OPTION 2: Run a file of URLs? --> press 2
OPTION 3: Use the test URL? --> press 3
OPTION 4: Exit the program? --> press 4
(Option 1 is the default for any other key)\n>>> ''')
    
    # File handling option
    if option == "2":
        mp4_option = input("\nWOULD YOU LIKE MP4(s) OR MP3(s)?\nPress 4 for mp4\nPress any other key for mp3\n>>> ")
        file_path = input("Please paste the file path to your file:\n>>> ")
        try:
            if mp4_option == "4":                
                url_list = get_file_urls(file_path)
                count = 0 # Keeping track if there are multiple URLs
                for url in url_list:
                    download_mp4(url, "ytmp4_file"+("#"*count)) # Give each mp4 a different filename by adding "#"
                    count +=1
                    print("\nLoading the next URL...") # Message so that user knows the program is still going.
                print("No more URLs!")
            else:
                url_list = get_file_urls(file_path)
                count = 0 # Keeping track if there are multiple URLs
                for url in url_list:
                    download_and_convert(url, "ytmp3_file"+("#"*count)) # Give each mp3 a different filename by adding "#"
                    count +=1
                    print("\nLoading the next URL...") # Message so that user knows the program is still going.
                print("No more URLs!")
        except FileNotFoundError: # Account for incorrect file path input.
            print(f"Error: File not found.\nPlease try checking your file path!")
    
    # Using the Test URL
    elif option == "3":
        url_link = "https://www.youtube.com/watch?v=oHg5SJYRHA0"
        mp4_option = input("\nWOULD YOU LIKE AN MP4 OR AN MP3?\nPress 4 for mp4\nPress any other key for mp3\n>>> ")
        if mp4_option == "4":
            download_mp4(url_link, "test_url")
        else:
            download_and_convert(url_link, "test_url") # Bitrate and filename can be changed using optional parameters!

    # Option to exit program
    elif option == "4":
        print("\nRUN COMPLETE.")
        return

    # URL pasting option
    else: # Option 1 is the default 
        mp4_option = input("\nWOULD YOU LIKE AN MP4 OR AN MP3?\nPress 4 for mp4\nPress any other key for mp3\n>>> ")
        url_link = input(f"Please paste your URL here:\n>>> ")
        if validate_url(url_link) == False:
            print(f"\nInvalid URL: Please check your URL and try again.")
        elif mp4_option == "4" and validate_url(url_link):
            download_mp4(url_link)
        else:
            download_and_convert(url_link)
    
    print("\nRUN COMPLETE.")
if __name__ == "__main__":
    main()
