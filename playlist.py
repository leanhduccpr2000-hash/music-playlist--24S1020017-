def search_by_artist():
    artist_name = input("Nhập tên ca sĩ cần tìm: ")

    found = False
    for song in songs:
        if artist_name.lower() in song['artist'].lower():
            print(f"- {song['title']} ({song['duration']}s)")
            found = True

    if not found:
        print("Không tìm thấy bài hát nào của ca sĩ này.")

 
