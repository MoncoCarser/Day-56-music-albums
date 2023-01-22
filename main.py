import csv, os

with open("100MostStreamedSongs.csv") as file:
    data = csv.DictReader(file)

    for row in data:

        files = os.listdir()
        if row["Artist(s)"] not in files:
            os.mkdir(row["Artist(s)"])
            
        folder_name = row["Artist(s)"]
        song_name = f"{row['Song']}.song"
        
# Creating a file at specified folder
# join directory and file path
        with open(os.path.join(folder_name, song_name), "w") as fp:
            fp.write(" ")
            
#As seen in solution code, I could check if file already in dir.
        
