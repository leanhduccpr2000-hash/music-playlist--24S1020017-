
def add_song():
    title = input("Nhập tên bài hát: ")
    artist = input("Nhập tên ca sĩ: ")
    duration = int(input("Nhập thời lượng (giây): "))

    songs.append({
        'title': title,
        'artist': artist,
        'duration': duration
    })

    print("Đã thêm bài hát vào playlist.")


    