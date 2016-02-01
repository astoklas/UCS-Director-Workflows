import json
import requests
import re
import urllib

SparkAPItoken = 'YTdiZDFiNTYtZDA5Yi00NDJmLWJhNDctZmU3MzUxYWQ5OGM2Njc4MjRjNTUtOTU5'

#class sparkRoom:
#
#    __APIhandler = None
#
#    def __init__(self, sparkAPI, roomName):
#
#
#    def createRoom(self):
#        return None
#
#    def deleteRoom(self):
#        return None
#
#    def exists(self):
#        return True
#
#    def sendMessage(self,msg):
#        return None
#
#    def sendMessageTo(self,msg,person):
#        return None


#class sparkMessage:
#
#    def __init__(self):
#nothing to do


class sparkPerson:
# Sample Response
# {
#	"items": [
#		{
#			"id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83Mzk3MjY5YS05ZmM5LTQzZDUtOThlNC1lNDU0MmE3ZDQ3Zjg",
#			"emails": [
#				"astoklas@cisco.com"
#			],
#			"displayName": "Alexander Stoklasa (astoklas)",
#			"avatar": "https://1efa7a94ed216783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~8245a515cae296b67c0481b403d47a6c~rKMELD4BSUWxIRg6WirfZw==~1600",
#			"created": "2012-06-15T20:29:55.558Z"
#		}
#	]
#}
#
#
#    _id = None
#    _emails = None
#    _displayName = None
#    _avatar = None
#    _created = None
#    _json = None

    def __init__(self,sAPI=None,displayName=None,eMail=None):
        self._id = None
        self._emails = None
        self._displayName = None
        self._avatar = None
        self._created = None
        self._json = None
        self._alternateEmails = None

        if eMail is not None:
            self._json = sAPI.queryUserByMail(eMail)
        elif displayName is not None:
            self._json = sAPI.queryUserByName(displayName)
        else:
            self._json = sAPI.queryMe()
            self._id = self._json['id']
            self._avatar = self._json['avatar']
            self._created = self._json['created']
            self._emails = self._json['emails'][0]           # We only read the first eMail address.... even if there are more
            self._alternateEmails = self._json['emails']
            self._displayName = self._json['displayName']
            return None

        if self._json is not None:
            item = self._json['items'][0]
            self._id = item['id']
            self._avatar = item['avatar']
            self._created = item['created']
            self._emails = item['emails'][0]           # We only read the first eMail address.... even if there are more
            self._displayName = item['displayName']
            self._alternateEmails = item['emails']

    @property
    def id(self):
        return self._id
    @property
    def emails(self):
        return self._emails
    @property
    def displayName(self):
        return self._displayName
    @property
    def avatar(self):
        return self._avatar
    @property
    def created(self):
        return self._created
    @property
    def json(self):
        return self._json
    @property
    def alternateEmails(self):
        return self._alternateEmails


class sparkAPI:

#
# Get your own token - mine is: 'YTdiZDFiNTYtZDA5Yi00NDJmLWJhNDctZmU3MzUxYWQ5OGM2Njc4MjRjNTUtOTU5'
#

    __DEBUG = False

    __RoomsUrl = 'https://api.ciscospark.com/v1/rooms'
    __MessageUrl = 'https://api.ciscospark.com/v1/messages'
    __PeopleUrl = 'https://api.ciscospark.com/v1/people'
    __PeopleUrlMe = 'https://api.ciscospark.com/v1/people/me'
    __headers = {}

    def debugPrint(self,msg):
        if self.__DEBUG:
            print msg

    def __init__(self):
        self.__headers = {'Authorization':'Bearer '+SparkAPItoken, 'Content-Type':'application/json' }
        self.debugPrint('Headers:')
        self.debugPrint(self.__headers)

    def queryUserByMail(self, eMail=None):
        if eMail is not None:
            query = {'email':eMail}
            url = self.__PeopleUrl + '?' + urllib.urlencode(query=query)
            self.debugPrint(url)
        r = requests.get(url,headers=self.__headers)
        self.debugPrint(r.status_code)
        self.debugPrint(json.dumps(r.json(),indent=2))
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def queryUserByName(self, displayName=None):
        if displayName is not None:
            query = {'displayName':displayName}
            url = self.__PeopleUrl + '?' + urllib.urlencode(query=query)
            self.debugPrint(url)
        r = requests.get(url,headers=self.__headers)
        self.debugPrint(r.status_code)
        self.debugPrint(json.dumps(r.json(),indent=2))
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def queryMe(self):
        r = requests.get(self.__PeopleUrlMe,headers=self.__headers)
        self.debugPrint(r.status_code)
        self.debugPrint(json.dumps(r.json(),indent=2))
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def listRooms(self):
        self.debugPrint(self.__headers)

        self.r = requests.get(self.__RoomsUrl,headers=self.__headers)
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
                self.debugPrint(item['title']+' <--> '+roomName+' ...hit')
        return result

    def createRoom(self,roomName):
        rBody = '''
        {
            "title" : "%s"
        } ''' % (roomName)
        print rBody
        r = requests.post(self.__RoomsUrl,headers=self.__headers,data=rBody)
        if r.status_code == 200:
            return r.json()['id']

    def deleteRoom(self,roomId):
        headers = self.__headers
        r = requests.delete(self.__RoomsUrl+'/'+roomId,headers=headers)
        if r.status_code == 204:
            print "Successful Deleted"
            return True
        else:
            return False


    def sendMessage(self,roomId,msg='',file=''):
        rBody = '''
        {
            "roomId": "%s",
            "text": "%s"
        } ''' % (roomId,msg)
        print rBody
        r = requests.post(self.__MessageUrl,headers=self.__headers,data=rBody)
        print r.status_code
        print r.json()
        if r.status_code == 200:
            return r.json()['id']


s = sparkAPI()

myPerson = sparkPerson(sAPI=s, eMail='astoklas@cisco.com')
print myPerson.id
print myPerson.emails

me = sparkPerson(sAPI=s)
print me.id
print me.emails


#rooms = s.listRooms()
#for item in rooms['items']:
#    print 'Title:', item['title']
#    print '  ID:', item['id']

#rooms = s.searchRoom(s.listRooms(),roomName="astoklas_Test_")
#print rooms

#for id in rooms:
#    print id
#    s.deleteRoom(id)


#roomId = s.createRoom('astoklas_Test_1')
#s.sendMessage(roomId,msg="Hello World!")
#s.sendMessage(roomId,msg="Hello World!")
#s.sendMessage(roomId,msg="Hello World!")
#s.deleteRoom(roomId)

