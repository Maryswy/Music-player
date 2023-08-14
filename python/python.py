import os
import csv
import re
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

# Function to process a single .m3u file
def process_file(file_path):
    filename = os.path.basename(file_path)
    content_keywords, metadata = extract_keywords_from_content(file_path)
    filename_keywords = extract_keywords_from_filename(filename)
    combined_keywords = list(set(content_keywords + filename_keywords))
    
    generic = categorize_genre(combined_keywords)
    
    return {
        "Filename": filename,
        "Path": file_path,
        "Generic": generic,
        "Title": metadata.get("title", ""),
        "URL": metadata.get("url", "")
    }

# Function to extract keywords from file content
def extract_keywords_from_content(file_path):
    metadata = {}
    keywords = []
    
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("#EXTINF"):
                title = re.findall(r',(.+)', line)
                metadata["title"] = title[0] if title else ""
            elif line.startswith("http"):
                metadata["url"] = line.strip()
            else:
                keywords.extend(re.findall(r'\b\w{3,}\b', line))
                
    return keywords, metadata

# Function to extract keywords from filename
def extract_keywords_from_filename(filename):
    # Remove file extension and split into words
    filename = os.path.splitext(filename)[0]
    keywords = filename.lower().split('_')
    
    return keywords

# Function to categorize genre based on keywords
def categorize_genre(keywords):
    genre_keywords = {
"rock": ["rock"],
        "pop": ["pop", "top 40" , "top40"],
        "jazz": ["jazz", "swing", "big band", "bebop", "dixieland"],
        "classical": ["classical", "orchestra", "symphony", "piano", "violin", "cello", "opera", "choir", "choral"],
        "electronic": ["electronic", "techno", "house", "trance", "dubstep", "drum and bass", "dub", "ambient", "idm", "edm", "electronica"],
        "hip-hop": ["hip-hop", "rap", "hip hop", "rap and hip-hop" , "hiphop"],
        "country": ["country", "bluegrass" , "blue grass", "folk"],
        "world": ["world", "ethnic", "world music", "world-music", "worldmusic"],
        "reggae": ["reggae", "ska", "dub"],
        "metal": ["metal", "heavy metal", "death metal", "black metal", "thrash metal", "doom metal", "power metal", "progressive metal", "metalcore", "nu metal", "grindcore", "hardcore"],
        "blues": ["blues", "delta blues", "electric blues", "blues-rock", "blues rock"],
        "folk": ["folk", "folk music", "folk-music", "folkmusic"],
        "new-age": ["new-age", "new age", "newage"],
        "r&b": ["r&b", "rhythm and blues", "rhythm & blues", "rhythm n blues", "rhythm 'n' blues"],
        "latin": ["latin", "salsa", "samba", "tango", "mambo", "merengue", "bachata", "reggaeton", "cumbia", "flamenco", "rumba", "bolero", "mariachi", "brazilian", "bossa nova"],
        "dance": ["dance", "dance music", "dance-music", "dancemusic", "club", "club music", "club-music", "clubmusic"],
        "disco": ["disco", "discofox", "disco-fox", "disco fox"],
        "funk": ["funk", "funky", "funk music", "funk-music", "funkmusic"],
        "soul": ["soul", "soul music", "soul-music", "soulmusic"],
        "ambient": ["ambient", "ambient music", "ambient-music", "ambientmusic"],
        "gospel": ["gospel", "gospel music", "gospel-music", "gospelmusic"],
        "christian": ["christian", "christian music", "christian-music", "christianmusic"],
        "soundtrack": ["soundtrack", "soundtracks", "soundtrack music", "soundtrack-music", "soundtrackmusic"],
        "spoken-word": ["spoken-word", "spoken word", "spokenword"],
        "comedy": ["comedy", "comedy music", "comedy-music", "comedymusic"],
        "children": ["children", "children's music", "children's-music", "childrensmusic"],
        "holiday": ["holiday", "holiday music", "holiday-music", "holidaymusic"],
        "reggaeton": ["reggaeton", "reggaeton music", "reggaeton-music", "reggaetonmusic"],
        "ska": ["ska", "ska music", "ska-music", "skamusic"],
        "acoustic": ["acoustic", "acoustic music", "acoustic-music", "acousticmusic"],
        "easy-listening": ["easy-listening", "easy listening", "easylistening"],
        "instrumental": ["instrumental", "instrumental music", "instrumental-music", "instrumentalmusic"],
        "oldies": ["oldies", "oldies music", "oldies-music", "oldiesmusic"],
        "punk": ["punk", "punk music", "punk-music", "punkmusic"],
        "alternative": ["alternative", "alternative music", "alternative-music", "alternativemusic"],
        "indie": ["indie", "indie music", "indie-music", "indiemusic"],
        "experimental": ["experimental", "experimental music", "experimental-music", "experimentalmusic"],
        "gothic": ["gothic", "gothic music", "gothic-music", "gothicmusic"],
        "grunge": ["grunge", "grunge music", "grunge-music", "grungemusic"],
        "hardcore": ["hardcore", "hardcore music", "hardcore-music", "hardcoremusic", "hard core"],
        "industrial": ["industrial"],
        "lo-fi": ["lo-fi"],
        "noise": ["noise"],
        "progressive": ["progressive"],
        "psychedelic": ["psychedelic"],
        "rockabilly": ["rockabilly"],
        "shoegaze": ["shoegaze"],
        "ska-punk": ["ska-punk"],
        "space-rock": ["space-rock"],
        "surf": ["surf"],
        "emo": ["emo"],
        "darkwave": ["darkwave"],
        "Arabic": ["Arabic"],
        "Chinese": ["Chinese"],
        "Hindi": ["Hindi"],
        "Japanese": ["Japanese"],
        "Korean": ["Korean"],
        "Thai": ["Thai"],
        "Turkish": ["Turkish"],
        "Vietnamese": ["Vietnamese"],
        "African": ["African"],
        "Celtic": ["Celtic"],
        "European": ["European"],
        "Indian": ["Indian", "India"],
        "Middle-Eastern": ["Middle-Eastern", "Middle Eastern"],
        "North-African": ["North-African"],
        "South-American": ["South-American"],
        "South-East-Asian": ["South-East-Asian"],
        "Balkan": ["Balkan"],
        "Bollywood": ["Bollywood"],
        "Bossa-Nova": ["Bossa-Nova"],
        "Cajun": ["Cajun"],
        "Caribbean": ["Caribbean"],
        "Celtic": ["Celtic"],
        "Cumbia": ["Cumbia"],
        "Flamenco": ["Flamenco"],
        "Fado": ["Fado"],
        "Gypsy": ["Gypsy"],
        "Hawaiian": ["Hawaiian"],
        "Klezmer": ["Klezmer"],
        "Mambo": ["Mambo"],
        "Mariachi": ["Mariachi"],
        "Merengue": ["Merengue"],
        "Polka": ["Polka"],
        "Rai": ["Rai"],
        "Salsa": ["Salsa"],
        "Samba": ["Samba"],
        "Tango": ["Tango"],
        "Zydeco": ["Zydeco"],
        "Bhangra": ["Bhangra"],
        # Add more genres and their associated keywords as needed
    }

    for genre, keys in genre_keywords.items():
        if any(key in keywords for key in keys):
            return genre
    return "unknown"

# Define the directory path
root_dir = "/home/mostafa/Desktop/projects/Music-player/m3u-radio-music-playlists"

# Get a list of all .m3u files
m3u_files = [os.path.join(dirpath, filename) for dirpath, _, filenames in os.walk(root_dir) for filename in filenames if filename.endswith(".m3u")]

# Create a Pool of worker processes
num_processes = cpu_count()  # Number of available CPU cores
with Pool(num_processes) as pool:
    data = list(tqdm(pool.imap(process_file, m3u_files), total=len(m3u_files), desc="Processing"))

# Write extracted information to a CSV file
csv_file = "radio_info_categorized.csv"
csv_columns = ["Filename", "Path", "Generic", "Title", "URL"]

with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print("CSV file created successfully!")

