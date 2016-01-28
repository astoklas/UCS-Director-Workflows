import json
import urllib
import requests
import re

class sparkAPI:

#
# Get your own token - mine is: 'YTdiZDFiNTYtZDA5Yi00NDJmLWJhNDctZmU3MzUxYWQ5OGM2Njc4MjRjNTUtOTU5'
#

    __DEBUG = False

    __authenticationToken = ''
    __listRoomsUrl = 'https://api.ciscospark.com/v1/rooms'
    __headers = {}

    def debugPrint(self,msg):
        if self.__DEBUG:
            print msg

    def __init__(self, token):
        self.__authenticationToken = token
        self.__headers = {'Authorization':'Bearer '+self.__authenticationToken}
        self.debugPrint(self.__authenticationToken)
        self.debugPrint(self.__headers)

    def listRooms(self):
        self.debugPrint(self.__authenticationToken)
        self.debugPrint(self.__headers)

        self.r = requests.get(self.__listRoomsUrl,headers=self.__headers)
        if self.r.status_code != 200:
            self.debugPrint(self.r.status_code)
            return None
        else:
            self.debugPrint(json.dumps(self.r.json(),indent=2))
            return self.r.json()

    def searchRoom(self,roomList,roomName=''):
        result = []
        for item in roomList['items']:
            if re.search(roomName,item['title']):
                result.append(item['id'])
                print item['title'], ' <--> ', roomName,' ...hit'
        return result

s = sparkAPI(token='YTdiZDFiNTYtZDA5Yi00NDJmLWJhNDctZmU3MzUxYWQ5OGM2Njc4MjRjNTUtOTU5')
rooms = s.listRooms()
for item in rooms['items']:
    print 'Title:', item['title']
    print '  ID:', item['id']
print
print
print s.searchRoom(rooms,'Swiss')


