# 8-8. User Albums:

albums = []

def make_album(artist_name, album_title, n_songs=None):
    """build a dictionary describing a music album"""

    # The number of songs is stored if the user is entered as an argument
    if n_songs:
        album = {"artist" : artist_name,"album": album_title, "songs" : n_songs}
    else:
        album = {"artist" : artist_name,"album": album_title}
    return album

def make_set_albums(album):
    """build a set of albumns"""
    return albums.append(album)


while True:

    add = input("Do you want to add a album?? (yes/no): ")
    if add == "yes":
        a_name = input("\nEnter the artist name (enter '0' at any time to quit): ")

        a_title = input("\nEnter the album name (enter '0' at any time to quit):")

        songs = int(input("\nEnter the number of songs (enter '0' at any time to quit): "))

        album = make_album(a_name, a_title, songs) # call the function for create a album
        make_set_albums(album) # call the function to store a album in set of albumns

    else:
        size = len(albums)
        print(f"the total number of albums is: {size}")
        for album in albums:
            print(album)
        break



    



