import pandas as pd

df_metallica_songs = pd.DataFrame()

df_album_1 = pd.read_csv("01-kill-em-all.txt", header=None)
df_album_2 = pd.read_csv("02-Ride The Lightning.txt", header=None, sep="|")
df_album_3 = pd.read_csv("03-Master Of Puppets.txt", header=None)
df_album_4 = pd.read_csv("04-...And Justice For All.txt", header=None)
df_album_5 = pd.read_csv("05-Black Album.txt", header=None)
df_album_6 = pd.read_csv("06-Load.txt", header=None)
df_album_7 = pd.read_csv("07-Re-load.txt", header=None)
df_album_8 = pd.read_csv("08-extras.txt", header=None)
df_album_9 = pd.read_csv("09-St-Anger.txt", header=None)
df_album_10 = pd.read_csv("10-Death-Magnetic.txt", header=None)
df_album_11 = pd.read_csv("11-Hardwired.txt", header=None)

df_metallica_songs = df_metallica_songs.append(df_album_1)
df_metallica_songs = df_metallica_songs.append(df_album_2)
df_metallica_songs = df_metallica_songs.append(df_album_3)
df_metallica_songs = df_metallica_songs.append(df_album_4)
df_metallica_songs = df_metallica_songs.append(df_album_5)
df_metallica_songs = df_metallica_songs.append(df_album_6)
df_metallica_songs = df_metallica_songs.append(df_album_7)
df_metallica_songs = df_metallica_songs.append(df_album_8)
df_metallica_songs = df_metallica_songs.append(df_album_9)
df_metallica_songs = df_metallica_songs.append(df_album_10)
df_metallica_songs = df_metallica_songs.append(df_album_11)

df_metallica_songs.columns = ["album", "track_number", "song_name", "song_lyric"]

df_metallica_songs["song_lyric"] = df_metallica_songs["song_lyric"].str.replace('"', "")

df_metallica_songs.to_csv("df_metallica_songs.txt", sep="|", header=True, index=False)
