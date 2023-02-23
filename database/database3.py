import sqlite3

def joinOperation():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select albums.Title,
                        artists.Name from artists
                        inner join albums
                        on artists.ArtistId = albums.ArtistId""")
    
    for row in cursor:
        print("Title: " + row[0] + "Name: " + row[1])

    connection.close()

joinOperation()
