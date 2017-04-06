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

    def insertUser(self, userID, currentEvent, inEvent, hostID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO USER (userID, currentEvent, inEvent, hostID) "
           "VALUES(%s, %s, %s, %s)")
        data = (userID, currentEvent, inEvent, hostID)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def insertSong(self, songID, eventID, voteCount, songName, artist, explicit, vetoCount, vetoBoolean):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO NEXTSONGS (songID, eventID, voteCount, songName, artist, explicit, vetoCount, vetoBoolean) "
           "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
        data = (songID, eventID, voteCount, songName, artist, explicit, vetoCount, vetoBoolean)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def getPlaylist(self, hostID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT playlistID FROM HOST WHERE hostID = %s") % (hostID)
        cursor.execute(query)
        playlistID = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()

        return playlistID[0]

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

    def getSongArtist(self, songName):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT artist FROM NEXTSONGS WHERE songName = '%s'") % (songName)
        cursor.execute(query)
        artist = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()
        if artist is not None:
            return artist[0]

    def getSongID(self, songName):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT songID FROM NEXTSONGS WHERE songName = '%s'") % (songName)
        cursor.execute(query)
        songID = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()
        if songID is not None:
            return songID[0]

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

    def getEventID(self, eventName):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT eventID FROM EVENT WHERE eventName = '" + eventName + "'")
        print(query)
        cursor.execute(query)
        result = cursor.fetchone()[0];
        cursor.close()
        cnx.commit()
        cnx.close()
        return result

    def registerVote(self, userID, eventID, songID, vote):
        print("Inserting a new event")
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1',
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("UPDATE NEXTSONGS SET voteCount = voteCount + 1 WHERE songID = %s")
        data = (songID)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def registerVeto(self, userID, eventID, songID, veto):
        print("Inserting a new event")
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1',
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("UPDATE NEXTSONGS SET vetoCount = vetoCount + 1 WHERE songID = %s")
        data = (songID)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def getQueue(self, eventID, userID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT songid, votecount, artist, vetocount, songname FROM NEXTSONGS WHERE eventid = '%s' order by voteCount desc, vetocount asc") % (eventid) 
        cursor.execute(query)
        cursor.close()
        cnx.commit()
        cnx.close()

    def getPlayedSongs(self, eventID, userID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT songsid, eventID, playOrder, songname, artist FROM PLAYEDSONGS WHERE eventid = '%s' order by playOrder") % (eventid) 
        cursor.execute(query)
        cursor.close()
        cnx.commit()
        cnx.close()

    def isVoted(self, eventID, userID, songid):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT songid, votecount, artist, vetocount, songname FROM NEXTSONGS WHERE eventid = '%s' order by voteCount desc, vetocount asc") % (eventid) 
        cursor.execute(query)
        cursor.close()
        cnx.commit()
        cnx.close()

