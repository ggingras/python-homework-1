
### Import 4 properties from main file
from main import Released, Producers, Song, HasBeenNumberOne

### Define my functions
def released():
    return Released

def producers():
    return Producers

def song():
    return Song

def hasBeenNumberOne():
    return HasBeenNumberOne

### Print four song properties using defined functions
print('Favourite Song: ' + song())
print('Released: ' + released().strftime('%m/%d/%Y'))
print('Song Producers: ' + ", ".join(str(x) for x in producers()))
print('Has been number one on Billboard: ' + str(hasBeenNumberOne()))
