#music List
liked_songs = {
     'Amoranth': 'Archangle',
     'Sabbaton': 'Red Barron',
     'Glory Hammer': 'Fly Away',
}

def write_liked_songs_to_file(songs, filename):
  with open(filename, 'w') as file:
    file.write('Liked Songs:\n')
    for artist, song in songs.items():
      file.write(f' {artist} by {song}\n')

write_liked_songs_to_file(liked_songs, 'music.txt')