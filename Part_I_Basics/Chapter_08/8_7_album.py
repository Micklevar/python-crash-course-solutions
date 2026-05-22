# 8-7. Album:

def make_album(artist_name, album_title, n_songs=None):
    """build a dictionary describing a music album"""

    # The number of songs is stored if the user is entered as an argument
    if n_songs:
        album = {"artist" : artist_name,"album": album_title, "songs" : n_songs}
    else:
        album = {"artist" : artist_name,"album": album_title}
    return album

# call the function
mcr = make_album(album_title="I brought you my bullets, you brought me your love", artist_name="My Chemical Romance")
jj = make_album("Julio Jaramillo", "El Ruiseñor de América", 14)
canser = make_album("Canserbero", "Muerte")

print(f"\n{mcr}\n{jj}\n{canser}")