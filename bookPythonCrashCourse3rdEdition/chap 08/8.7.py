'''
8-7. Album: 
Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of 
information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least 
one new function call that includes the number of songs on an album.
'''

def make_album(artist_name, title, number_of_songs=None):
    """Return a dictionary of information about Music Album"""
    if number_of_songs:
        music_album_details = {'artist': artist_name, 'album': title, 'numberOfSongs': number_of_songs}
    else:
        music_album_details = {'artist': artist_name, 'album': title}
    return music_album_details
music_album1 = make_album ('Lucky Ali', 'Sunoh')
print(music_album1)
music_album2 = make_album ('Lucky Ali', 'Sifar')
print(music_album2)
music_album3 = make_album ('Lucky Ali', 'Aks', '10')
print(music_album3)