import mysql.connector


#All functions that interact with the database go here


class Database:
    ##################################
    #           INSERT STATEMENTS    #
    ##################################

    #Template for what insert statements look like, table name/columns aren't right
    def insertEvent(self, eventStatus, hostID, explicitAllowed, eventName, accessToken, refreshToken):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO EVENT (eventStatus, hostID, explicitAllowed, eventName, accessToken, refreshToken) "
            "VALUES(%s, %s, %s, %s, %s, %s)")
        data = (eventStatus, hostID, explicitAllowed, eventName, accessToken, refreshToken)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def insertHost(self, playlistID, spotifyToken, spotifyUsername):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO HOST (playlistID, spotifyToken, spotifyUsername) "
           "VALUES(%s, %s, %s)")
        data = (playlistID, spotifyToken, spotifyUsername)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def insertUser(self, currentEvent, inEvent, hostID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO USER (currentEvent, inEvent, hostID) "
           "VALUES(%s, %s, %s)")
        data = (currentEvent, inEvent, hostID)
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

    ##################################
    #           GET STATEMENTS       #
    ##################################

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

    def getEventID(self, eventName, hostID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT eventID FROM EVENT WHERE eventName = %s and hostID = %s")
        data = (eventName, hostID)
        cursor.execute(query, data)

        result = cursor.fetchone()[0];
        cursor.close()
        cnx.commit()
        cnx.close()
        return result

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

    ##################################
    #        OTHER STATEMENTS        #
    ##################################

    def registerVote(self, userID, eventID, songID, vote):
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
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1',
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("UPDATE NEXTSONGS SET vetoCount = vetoCount + 1 WHERE songID = %s")
        data = (songID)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

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

    def isVoted(self, eventID, userID, songid):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT songid, votecount, artist, vetocount, songname FROM NEXTSONGS WHERE eventid = '%s' order by voteCount desc, vetocount asc") % (eventid) 
        cursor.execute(query)
        cursor.close()
        cnx.commit()
        cnx.close()

