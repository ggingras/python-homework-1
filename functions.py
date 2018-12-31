
### Import 4 properties from main file
from main import Released, Producers, Song, HasBeenNumberOne

### Define my functions
def GetReleasedDate():
    return Released

def GetProducers():
    return Producers

def GetSongName():
    return Song

def IsSongHasBeenNumberOne():
    return HasBeenNumberOne

### Print four song properties using defined functions
print('Favourite Song: ' + GetSongName())
print('Released: ' + GetReleasedDate().strftime('%m/%d/%Y'))
print('Song Producers: ' + ", ".join(str(x) for x in GetProducers()))
print('Has been number one on Billboard: ' + str(IsSongHasBeenNumberOne()))