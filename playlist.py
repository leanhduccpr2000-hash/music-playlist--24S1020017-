
 
def view_playlist():
    if not songs:
        print("Playlist đang trống.")
        return
    
    print("\n--- DANH SÁCH PHÁT ---")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['title']} - {song['artist']} ({song['duration']}s)")


    