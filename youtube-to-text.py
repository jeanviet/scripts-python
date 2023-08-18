import re

def extract_youtube_video_id(url):
    # Pattern pour extraire l'ID de la vidéo YouTube depuis l'URL
    pattern = r"(?<=v=)[a-zA-Z0-9_-]+"

    # Recherche du pattern dans l'URL
    match = re.search(pattern, url)

    if match:
        return match.group()
    else:
        return None

# Demande à l'utilisateur de saisir l'URL YouTube
url = input("Veuillez saisir l'URL de la vidéo YouTube : ")

# Extraction de l'ID de la vidéo
videoID = extract_youtube_video_id(url)

if videoID:
    print("L'ID de la vidéo YouTube est :", videoID)
else:
    print("Impossible de trouver l'ID de la vidéo YouTube dans l'URL fournie.")

# Choix de la langue 

langue = input("Langue de vos sous-titres : en ou fr ?")
  
# Récupération de la transcription texte

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

transcript = YouTubeTranscriptApi.get_transcript(videoID, languages=[langue])
# transcript = YouTubeTranscriptApi.get_transcript(videoID, languages=['fr'])


formatter = TextFormatter()

# .format_transcript(transcript) turns the transcript into a TXT string.
txt_formatted = formatter.format_transcript(transcript)

# Now we can write it out to a file.
with open('transcript.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(txt_formatted)
