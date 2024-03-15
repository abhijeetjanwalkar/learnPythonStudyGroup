'''
8-8. User Albums: 
Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
'''
def make_album(artist_name, title, number_of_songs=None):
    """Return a dictionary of information about Music Album"""
    if number_of_songs:
        music_album_details = {'artist': artist_name, 'album': title, 'numberOfSongs': number_of_songs}
    else:
        music_album_details = {'artist': artist_name, 'album': title}
    return music_album_details

while True:
    artist_name = input("Artist Name: ")
    if artist_name == 'q':
        break
    title_name = input("Album Title: ")
    if title_name == "q":
        break
    songs = input("Enter number of Songs: ")
    if songs == 'q':
        break
    album_details = make_album(artist_name, title_name, songs)
    print(f"\n The album details are {album_details}")