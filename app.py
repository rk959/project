import pandas as pd
import random

# Create a music dataset
data = {
    "Mood": [
        "happy","happy","happy",
        "sad","sad","sad",
        "relax","relax","relax",
        "energetic","energetic","energetic"
    ],
    
    "Song": [
        "Happy",
        "Uptown Funk",
        "Can't Stop The Feeling",
        
        "Someone Like You",
        "Let Her Go",
        "Fix You",
        
        "Let It Be",
        "Perfect",
        "Weightless",
        
        "Believer",
        "Stronger",
        "Eye of the Tiger"
    ],
    
    "Artist":[
        "Pharrell Williams",
        "Bruno Mars",
        "Justin Timberlake",
        
        "Adele",
        "Passenger",
        "Coldplay",
        
        "The Beatles",
        "Ed Sheeran",
        "Marconi Union",
        
        "Imagine Dragons",
        "Kanye West",
        "Survivor"
    ]
}

# Convert to DataFrame
music_df = pd.DataFrame(data)

print("🎵 Music Mood Suggester 🎵")
print("---------------------------")

# Show available moods
print("\nAvailable moods:")
print(music_df["Mood"].unique())

# User input
user_mood = input("\nEnter your mood: ").lower()

# Filter songs based on mood
filtered_songs = music_df[music_df["Mood"] == user_mood]

# Check if mood exists
if len(filtered_songs) > 0:
    
    print("\nSongs for your mood:\n")
    
    for index, row in filtered_songs.iterrows():
        print(row["Song"], "-", row["Artist"])
    
    # Random suggestion
    suggestion = filtered_songs.sample(1)
    
    print("\n⭐ Recommended Song:")
    print(
        suggestion["Song"].values[0],
        "-",
        suggestion["Artist"].values[0]
    )

else:
    print("\n❌ Mood not found. Try: happy, sad, relax, energetic")

print("\nEnjoy your music! 🎧")