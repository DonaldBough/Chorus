import mysql.connector


#All functions that interact with the database go here


class Database:
  ##################################
  #           INSERT STATEMENTS    #
  ##################################

  #Template for what insert statements look like, table name/columns aren't right
  def insertEvent(self, eventStatus, hostID, explicitAllowed, eventName):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("INSERT INTO EVENT (eventStatus, hostID, explicitAllowed, eventName) "
      "VALUES(%s, %s, %s, %s)")
    data = (eventStatus, hostID, explicitAllowed, eventName)
    cursor.execute(query, data)
    cursor.close()
    cnx.commit()
    cnx.close()

  def insertUser(self, currentEvent, inEvent, host):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("INSERT INTO USER (currentEvent, inEvent, host) "
       "VALUES(%s, %s, %s)")
    data = (currentEvent, inEvent, host)
    cursor.execute(query, data)

    #Get the userID from the insert
    cursor.execute("SELECT LAST_INSERT_ID()")
    userID = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if userID is None:
      return -1
    return userID[0]

  def insertHost(self, currentEvent, inEvent, host, spotifyUsername, playlistID, spotifyToken, refreshToken):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("INSERT INTO USER (currentEvent, inEvent, host, spotifyUsername, playlistID, spotifyToken, refreshToken) "
       "VALUES(%s, %s, %s, %s, %s, %s, %s)")
    data = (currentEvent, inEvent, host, spotifyUsername, playlistID, spotifyToken, refreshToken)
    cursor.execute(query, data)

    #Get the userID from the insert
    cursor.execute("SELECT LAST_INSERT_ID()")
    userID = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if userID is None:
      return -1
    return userID[0]
  
  def insertSong(self, songID, eventID, voteCount, songName, artist, isExplicit, vetoCount, vetoBoolean):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("INSERT INTO NEXTSONGS (songID, eventID, voteCount, songName, artist, isExplicit, vetoCount, vetoBoolean) "
       "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
    data = (songID, eventID, voteCount, songName, artist, isExplicit, vetoCount, vetoBoolean)
    cursor.execute(query, data)
    cursor.close()
    cnx.commit()
    cnx.close()

  def insertPlaylistID(self, userID, playlistID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("UPDATE USER set playlistID = '%s' where userid = '%s'") % (playlistID, userID)
    cursor.execute(query)
    cursor.close()
    cnx.commit()
    cnx.close()

  def insertUserData(self, userID, spotifyUsername, spotifyToken):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("UPDATE USER set spotifyUsername = '%s' and spotifyToken = '%s' where userID = '%s'") % (spotifyUsername, spotifyToken, userID)
    cursor.execute(query)
    cursor.close()
    cnx.commit()
    cnx.close()



  ##################################
  #           GET STATEMENTS       #
  ##################################

  def getPlaylist(self, userID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT playlistID FROM USER WHERE userID = %s") % (userID)
    cursor.execute(query)
    playlistID = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if playlistID is None:
      return -1
    return playlistID[0]

  def getPlaylistID(self, eventID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT playlistID from USER where currentEvent = '%s' and host = 1") % (eventID)
    cursor.execute(query)
    playlistID = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if playlistID is None:
      return -1
    return playlistID[0]

  def getHostSpotifyToken(self, eventid):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT spotifyToken from USER where currentEvent = '%s' and host = 1") % (eventid)
    cursor.execute(query)
    token = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if token is None:
      return -1
    return token[0]

  def getHostSpotifyUserName(self, eventid):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT spotifyUsername from USER where currentEvent = '%s' and host = 1") % (eventid)
    cursor.execute(query)
    token = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if token is None:
      return -1
    return token[0]

  def getUserToken(self, userID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT spotifyToken from USER where userID = '%s'") % (userID)
    cursor.execute(query)
    token = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if token is None:
      return -1
    return token[0]

  def getGuestUsername(self, userID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT spotifyUsername from USER where userID = '%s'") % (userID)
    cursor.execute(query)
    token = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if token is None:
      return -1
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

    if artist is None:
      return "NO ARTIST FOUND"
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
    if songID is None:
      return -1
    return songID[0]


  def getEventid(self, eventname):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT eventid FROM EVENT WHERE eventname = '%s' ") % (eventname)
    cursor.execute(query)
    token = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if token is None:
      return -1
    return token[0]

  def getQueue(self, eventID, userID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT songid, votecount, artist, vetocount, songname FROM NEXTSONGS WHERE eventid = '%s' order by voteCount desc, vetocount asc") % (eventID) 
    row = cursor.execute(query)

    songs = []
    for row in cursor:
      songs.append({'songname': row[4], 'artist': row[2], 'songid': row[0], 'votecount': row[1], 'vetocount': row[3]})

    cursor.close()
    cnx.commit()
    cnx.close()

    return songs

  def getPlayedSongs(self, eventID, userID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT songsid, eventID, playOrder, songname, artist FROM PLAYEDSONGS WHERE eventid = '%s' order by playOrder") % (eventID) 
    row = cursor.execute(query)

    songs = []
    for row in cursor:
      songs.append({'songname': row[3], 'artist': row[4], 'songid': row[0]})

    cursor.close()
    cnx.commit()
    cnx.close()

    return songs

  def getTopSong(self, eventID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT MAX(songID) FROM NEXTSONGS WHERE eventid = %s") % (eventID) 
    cursor.execute(query)
    songID = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if songID is None:
      return -1
    return songID[0]


  def getUserID(self, eventID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT userID from USER where currentEvent = '%s'") % (eventID) 
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if result is None:
      return -1
    return token[0]

  def getHostID(self, eventID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT userID from USER where currentEvent = '%s' and host = 1") % (eventID) 
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if result is None:
      return -1
    return token[0]
  
  #get accessToken based off of the eventID
  def getEventSpotifyToken(self, eventID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT spotifyToken FROM USER WHERE currentEvent = '%s' ") % (eventID)
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if result is None:
      return -1
    return result[0]

  def getGuestSpotifyToken(self, userID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT spotifyToken FROM USER WHERE userID = '%s'") % (userID)
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if result is None:
      return -1
    return result[0]

  def getCurrentPlayingSong(self, eventID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT currentSongID FROM EVENT WHERE eventID = '%s' ") % (eventID)
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if result is None:
      return -1
    return result[0]

  def eventNameCheck(self, eventname):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT eventName FROM EVENT WHERE eventName = '%s' ") % (eventname)
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if result is None:
      return -1
    return result[0]

  def getAllEventID(self):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT eventID FROM EVENT")
    cursor.execute(query)
    resultList = []
    for (eventID) in cursor:
      resultList.append(eventID)

    cursor.close()
    cnx.commit()
    cnx.close()
    return resultList


  ##################################
  #        OTHER STATEMENTS        #
  ##################################

  def registerVote(self, songID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1',
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("UPDATE NEXTSONGS SET voteCount = voteCount + 1 WHERE songID = '%s'") % (songID)
    cursor.execute(query)
    cursor.close()
    cnx.commit()
    cnx.close()

  def updateVote(self, userID, eventID, songID, vote):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1',
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("INSERT into VOTEDSONGS (userid, eventid, songid, vote) VALUES (%s, %s, %s, 1)") % (userID, eventID, songID)
    cursor.execute(query)
    cursor.close()
    cnx.commit()
    cnx.close()

  def registerVeto(self, songID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1',
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("UPDATE NEXTSONGS SET vetoCount = vetoCount + 1 WHERE songID = '%s'") % (songID)
    cursor.execute(query)
    cursor.close()
    cnx.commit()
    cnx.close()

  def updateVeto(self, userID, eventID, songID, vote):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1',
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("INSERT into VOTEDSONGS (userid, eventid, songid, veto) VALUES (%s, %s, %s, 1)") % (userID, eventID, songID)
    cursor.execute(query)
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

  def isVoted(self, eventID, userID, songID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query = ("""select eventid, userid, songid from VOTEDSONGS where eventid = '%s' 
    and userid = '%s' and songid = '%s' """) % (eventID, userID, songID); 
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.commit()
    cnx.close()

    if result is None:
      return -1
    return result[0]

  #transfer songs from nextsongs to playedsongs table
  def transfer(self, songID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query1 = ("""INSERT into PLAYEDSONGS (songsid, eventid, songname)
    select songid, eventid, songname from NEXTSONGS where songID = '%s' """) % (songID);
    cursor.execute(query1)

    query2 = ("DELETE from NEXTSONGS where songID = '%s'") % (songID)
    cursor.execute(query2)
    cursor.close()
    cnx.commit()
    cnx.close()

  def isEvent(self, eventName):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query1 = ("SELECT from event where eventname = '%s'") % (eventName); 
    cursor.execute(query1)
    cursor.close()
    cnx.commit()
    cnx.close()

  def updateCurrentSong(self, songID, eventID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor(buffered=True)
    query1 = ("UPDATE EVENT SET currentSongID = '%s' WHERE eventID = '%s'") % (songID, eventID); 
    cursor.execute(query1)
    cursor.close()
    cnx.commit()
    cnx.close()

  def updateHostEventID(self, hostID, eventID):
    cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1',
      host='174.138.64.25', database ='mydb')
    cursor = cnx.cursor()
    query = ("UPDATE USER SET currentEvent = '%s' WHERE userID = '%s'") % (eventID, hostID)
    cursor.execute(query)
    cursor.close()
    cnx.commit()
    cnx.close()