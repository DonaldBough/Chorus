import mysql.connector


#All functions that interact with the database go here


class Database:
    #Template for what insert statements look like, table name/columns aren't right
    def insertEvent(self, eventID, eventStatus, hostID, explicit):
        print("Inserting a new event")
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO EVENT (eventStatus, hostID, explicit, eventID) "
            "VALUES(%s, %s, %s, %s)")
        data = (eventStatus, hostID, explicit, eventID)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def insertHost(self, hostID, playlistID, spotifyToken, spotifyUsername):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO HOST (hostID, playlistID, spotifyToken, spotifyUsername) "
           "VALUES(%s, %s, %s, %s)")
        data = (hostID, playlistID, spotifyToken, spotifyUsername)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def getHostSpotifyToken(self, hostID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT spotifyToken FROM HOST WHERE hostID = %s") % (hostID)
        cursor.execute(query)
        token = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()

        return token[0]

    def getArtistOfSong(self, songID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT artist FROM NEXTSONGS WHERE songID = %s") % (songID)
        cursor.execute(query)
        artist = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()
        if artist is not None:
            return artist[0]

    def joinEvent(self, currentEvent, inEvent, host):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO user (currentEvent, inEvent, host) "
           "VALUES(%s, %s, %s)")
        data = (currentEvent, inEvent, host)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()
