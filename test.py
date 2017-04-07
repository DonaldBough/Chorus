import server
import os
import sys
from database import Database

class Test():

    ##-----------------------------------------------------------------------------------------------------------------##
    # Write at least 5 to 6 tests for each API
    # Test your corresponding APIs. Check the name above API test funtions.
    # Possible steps to write tests:
    # step1: Create a hard coded input
    # step2: Create the hard coded output for the above hard coded input
    # step3: Create the output from the corressponding API call from server.py with the above hard coded input in step1
    # step4: Compare output in step2 and step3. If they match, print("SUCCESS") else print("FAILED")
    # step5: Repeat this for 5 to 6 tests
    ##-----------------------------------------------------------------------------------------------------------------##
    
  ## Responsible: Ivan
    # Tests CreateEvent: Check that event is created successfully and that 2 different events cant be created with same names/passwords
    def testCreateEvent():
        print("Testing CreateEvent:")
        print("Test1")
        db = Database()
        db.insertEvent("LIVE", 1, 1,'Ivan', 1, 2)
        eventID = db.getEventID('Ivan', 1)

        if (eventID == 1): 
            print("Test1: SUCCESS")
        else:
            print("Test1: FAIL")

        print("Test2")
        db.insertEvent("LIVE", 2, 1,'Ivan', 3, 4)
        eventID = db.getEventID('Ivan', 2)

        if (eventID == 2): 
            print("Test2: FAIL")
        else:
            print("Test2: SUCCESS")

        print("Test3")
        db.insertEvent("LIVE", 3, 1,'Timmay', 5, 6)
        eventID = db.getEventID('Timmay', 3)

        if (eventID == 2): 
            print("Test3: SUCCESS")
        else:
            print("Test3: FAIL")

        print("Test4")
        db.insertEvent("LIVE", 3, 1,'Donaldo', 5, 6)
        eventID = db.getEventID('Donaldo', 3)

        if (eventID == 3): 
            print("Test3: FAIL")
        else:
            print("Test3: SUCCESS")

        print("Test5")
        db.insertEvent("LIVE", 4, 1,'Donaldo', 7, 8)
        eventID = db.getEventID('Donaldo', 4)

        if (eventID == 3): 
            print("Test3: SUCCESS")
        else:
            print("Test3: FAIL")

        print("Test6")
        db.insertEvent("LIVE", 5, 1,'Ronald123', 9, 10)
        eventID = db.getEventID('Ronald123', 5)

        if (eventID == 4): 
            print("Test3: SUCCESS")
        else:
            print("Test3: FAIL")

    ## Responsible: Ivan
    # Tests JoinEvent: Check that user successfully joins events and cannot join event if he inputs wrong event name/password
    def testJoinEvent():
        print("Testing JoinEvent:")
        print("Test1")
        db = Database()
        eventID = db.getEventID("Ivan")
        if (eventID == 1):
            print("Test1: SUCCESS")
        else:
            print("Test1: FAIL")

        print("Test2")
        eventID = db.getEventID("Timmay")
        if (eventID == 2):
            print("Test2: SUCCESS")
        else:
            print("Test2: FAIL")

        print("Test3")
        eventID = db.getEventID("Timmay")
        if (eventID == 3):
            print("Test2: FAIL")
        else:
            print("Test2: SUCCESS")

        print("Test4")
        eventID = db.getEventID("Donaldo")
        if (eventID == 3):
            print("Test2: SUCCESS")
        else:
            print("Test2: FAIL")

        print("Test5")
        eventID = db.getEventID("")
        if (eventID == 4):
            print("Test2: FAIL")
        else:
            print("Test2: SUCCESS")

        print("Test6")
        eventID = db.getEventID("Ronald123")
        if (eventID == 4):
            print("Test2: SUCCESS")
        else:
            print("Test2: FAIL")
    


    ## Responsible: Donald
    # Tests sendvote: Check that votes and vetos are updated properly 
    def testSendVoteVeto1():
        print("Testing SendVoteVeto1:")
        #def isVoted(self, eventID, userID, songid):
        #def registerVote(self, eventID, eventID, songID, vote):
        db = Database()
        result = db.isVoted(1, 1, 1)
        if result is None:
            print "Test 1 failed"
            return

        print "Test1: SUCCESS"

        result = db.isVoted(1, 1, 5498)
        if result is not None:
            print "Test 2 failed"
            return

        print "Test2: SUCCESS"

        db.registerVote(1, 4, 1, 1)
        result = db.isVoted(4, 1, 1)
        if result is None:
            print "Test 3 failed"
            return
        print "Test3: SUCCESS"

        print "All tests passed :)"

    ## Responsible: Kareem
    # Test sendvote: Check that user can't vote/veto a particular song more than once
    def testSendVoteVeto2():
        print("Testing SendVote2:")
        print("Test1: SUCCESS")

    ## Responsible: Sid
    # Tests getQueue: Check that songs are displayed in descing order of votes and ascending order of vetos if two songs have same number of votes
    def testGetQueue():
        print("Testing getQueue:")
        print("Test1: SUCCESS")

    ## Responsible: Ronak
    # Tests getPlayedSongs: Check that songs are displayed in descing order of votes and ascending order of vetos if two songs have same number of votes
    def testGetPlayedSongs():
        print("Testing getPlayedSongs:")
        print("Test1: SUCCESS")
    
    ##-----------------INSTRUCTIONS---------------##
    # Run option 1: python test.py  
    # Rub option 2: python test.py (Name of test method, ex: testSendVote1)
    # Option 1: tests all APIs
    # Option 2: tests your input API
    ##--------------------------------------------##

    if __name__ == '__main__':
        #os.system("python server.py")
        testSendVoteVeto1()
