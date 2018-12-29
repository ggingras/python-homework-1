
"""
Pirple homework 1. Understanding variables in python.

Information about my favorite song Learning to Fly
"""

### Import date function to initialized song released date
from datetime import date

### All song properties being initialized
Song, Artist, Album = "Learning to Fly", "Pink Floyd", "A Momentary Lapse of Reason"
Genre = "Rock"
DurationInSeconds = 293
Released = date(1987, 9, 14)
Label = "Columbia (US)"
SongWriters = ["David Gilmour", "Anthony Moore", "Bob Ezrin", "Jon Carin"]
Producers = ["Bob Ezrin", "David Gilmour"]
Nominations = ["MTV Video Music Award for Best Cinematography", "MTV Video Music Award for Best Direction"]
YoutubeViews = 63282953 

### Print all properties to console
print('Favourite Song: ' + Song)
print('Album: ' + Album)
print('Artist: ' + Artist)
print('Genre: ' + Genre)
print('Duration (in secconds): ' + str(DurationInSeconds))
print('Released: ' + Released.strftime('%m/%d/%Y'))
print('Label:' + Label)
print('Song writers: ' + ", ".join(str(x) for x in SongWriters))
print('Song producers: ' + ", ".join(str(x) for x in Producers))
print('Nominations: ' + ", ".join(str(x) for x in Nominations))
print('Youtube views: ' + str(YoutubeViews))