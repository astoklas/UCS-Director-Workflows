import json
input = '''
{
  "items": [
    {
      "lastActivity": "2016-01-27T18:19:58.004Z",
      "created": "2016-01-26T10:49:38.220Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vN2VlYjFlYzAtYzQxYS0xMWU1LTkyN2EtYTNlZTNjNWRjOWM3",
      "title": "Metapod Ambassadors Bootcamp ( Tech) "
    },
    {
      "lastActivity": "2016-01-25T15:53:03.533Z",
      "created": "2016-01-25T15:53:01.233Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vMDc1MGYyMTUtODAzYy0zMDdiLTg1YjEtMDc5YTg2MDVhNGFj",
      "title": "Sebastian Straube (sestraub)"
    },
    {
      "lastActivity": "2016-01-08T15:00:55.981Z",
      "created": "2016-01-08T15:00:18.856Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vNDUyN2Q0ZjktOWQwNC0zZGZiLWExNzMtNWE3ZDQxNGEzMjIy",
      "title": "Roman Gischig (rgischig)"
    },
    {
      "lastActivity": "2016-01-27T16:16:52.486Z",
      "created": "2016-01-05T17:18:19.165Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vNTA5YzJjZDAtYjNkMC0xMWU1LWJlZTktMDMzM2M0MDc1MGEy",
      "title": "Swiss FAST-IT Team"
    },
    {
      "lastActivity": "2016-01-05T10:58:10.866Z",
      "created": "2016-01-05T10:58:10.866Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vZTM1NzE4YTUtZjk5NS0zODdhLThlNmYtNjYwOWJiZDMxYjZj",
      "title": "Collaboration TMEs"
    },
    {
      "lastActivity": "2015-12-10T13:28:36.419Z",
      "created": "2015-12-10T13:02:05.194Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vMzY0NGRlYTAtOWYzZS0xMWU1LTk2OTItZWIwMjZmZTliY2Mw",
      "title": "chester 4 alex"
    },
    {
      "lastActivity": "2015-12-01T20:37:05.604Z",
      "created": "2015-12-01T20:36:13.192Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vMjk5ZmE4ODAtOTg2Yi0xMWU1LTkzYzgtMzkwOTYzMmFmNGIw",
      "title": "Architecture@rhugento - Project: Sparing"
    },
    {
      "lastActivity": "2015-12-01T20:35:11.178Z",
      "created": "2015-12-01T20:28:08.277Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vZjI3OGJhNTMtNzIyYi0zNTZjLWJiYTUtYWRkZDgxYmFjYzA0",
      "title": "Rene Hugentobler (rhugento)"
    },
    {
      "lastActivity": "2015-12-10T10:32:02.430Z",
      "created": "2015-11-13T16:01:00.076Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYmI5YTllYzAtOGExZi0xMWU1LTkwMzYtODk5NTdmNjE4NDQ3",
      "title": "Swiss - All In For Good"
    },
    {
      "lastActivity": "2015-11-13T15:59:28.299Z",
      "created": "2015-11-13T15:59:28.299Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vODRlNjhmYjAtOGExZi0xMWU1LWExMzQtNDkzZmUyMjlmYzRj",
      "title": "swiss all in for good"
    },
    {
      "lastActivity": "2015-09-22T13:50:51.160Z",
      "created": "2015-09-18T22:34:26.861Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vNmIzNjI1ZDAtNWU1NS0xMWU1LTk0ZjMtMWRhNThmNGY2MDRm",
      "title": "Atrete Show"
    },
    {
      "lastActivity": "2015-11-03T08:22:24.902Z",
      "created": "2015-09-18T08:27:05.501Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vMGI2NjQ0ZDAtNWRkZi0xMWU1LWI0ODUtY2Q3ZDYyZmExOTE5",
      "title": "Greifenseelauf 2015"
    },
    {
      "lastActivity": "2015-10-08T08:03:06.618Z",
      "created": "2015-09-02T20:45:26.104Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vOGEwMWQ1ODAtNTFiMy0xMWU1LWEzM2UtODlmMjQ3MDQ4MGRj",
      "title": "Fast IT Team Switzerland"
    },
    {
      "lastActivity": "2015-08-24T16:46:22.827Z",
      "created": "2015-08-13T21:16:12.624Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vODY1YjZkMDAtNDIwMC0xMWU1LWFjYTctNDdiMGM1NTkwNDZh",
      "title": "MH & VSG Enclave"
    },
    {
      "lastActivity": "2016-01-28T09:23:28.875Z",
      "created": "2015-08-10T18:21:11.473Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vOTNmMWIyMTAtM2Y4Yy0xMWU1LTk5NjktMjM1MTJhZDE1MTk2",
      "title": "Swiss - All"
    },
    {
      "lastActivity": "2015-11-27T08:39:39.545Z",
      "created": "2015-07-19T20:29:16.857Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vZDNiM2JhOTAtMmU1NC0xMWU1LWE0YzEtM2JiOTBkM2Q1M2Qz",
      "title": "TOUCH - EXCITE - PROOF"
    },
    {
      "lastActivity": "2015-09-01T09:40:35.117Z",
      "created": "2015-07-07T02:48:40.804Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYWNiM2EyNDAtMjQ1Mi0xMWU1LWFiM2YtOWIwMDNjNGI4ZWI1",
      "title": "EMEAR Technical Power Training"
    },
    {
      "lastActivity": "2016-01-19T19:00:27.657Z",
      "created": "2015-06-24T14:09:05.353Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vOTJhOGIzOTAtMWE3YS0xMWU1LTk0N2UtODEzNGRhMzIxNmE3",
      "title": "FSI Virtual Team Workshop"
    },
    {
      "lastActivity": "2015-10-29T10:12:26.829Z",
      "created": "2015-06-17T00:12:16.440Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vODJlYzUzODAtMTQ4NS0xMWU1LWFjMmUtY2Q4MWJmNTMyMGM0",
      "title": "2015 June Architect VT Event - Interaction Community"
    },
    {
      "lastActivity": "2015-04-28T20:34:51.806Z",
      "created": "2015-04-14T12:29:57.477Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vZjYxZTk5NTAtZTJhMS0xMWU0LWJkZWEtOWQ1MGQ3NzI4YTBk",
      "title": "OpenEnegyMonitoring"
    },
    {
      "lastActivity": "2015-12-14T10:47:09.873Z",
      "created": "2015-04-11T06:09:08.885Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vNDQwZWU0NTAtZTAxMS0xMWU0LTlhODEtNDUxNmI4OGI3MDc0",
      "title": "Put to Bin List"
    },
    {
      "lastActivity": "2015-05-08T07:31:52.183Z",
      "created": "2015-03-18T08:15:19.587Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vMjZiNWY4YzgtNTdmYi0zOWIxLTgzMTktMTVlNGVkNmZhNTdi",
      "title": "Anna Gillitzer (annagill)"
    },
    {
      "lastActivity": "2015-11-16T11:54:18.695Z",
      "created": "2015-03-06T10:17:57.345Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vMGYzZTFkMTAtYzNlYS0xMWU0LWExMTMtODNmOTlkNDI2M2Nk",
      "title": "Wireless-Issue in ZH-Office"
    },
    {
      "lastActivity": "2016-01-05T10:57:25.885Z",
      "created": "2015-02-26T09:45:02.219Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYTRlNmI4YWMtMzFkMi0zNWZiLWJjMjAtN2U2ZjJkYTM0YTNh",
      "title": "Markus Bina (mbina)"
    },
    {
      "lastActivity": "2015-11-05T21:55:26.373Z",
      "created": "2015-02-11T20:00:37.450Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYTU5NjhhYTAtYjIyOC0xMWU0LThlYTItMjFjNGI1MmU3NmUy",
      "title": "Swiss Gamechangers Usergroup"
    },
    {
      "lastActivity": "2014-11-30T22:55:11.527Z",
      "created": "2014-11-25T20:08:07.631Z",
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYzViMjM1ZjAtNzRkZS0xMWU0LTgzM2ItNzUxNTIzOGZiNWJj",
      "title": "Hi-Touch Team Switzerland"
    }
  ]
}'''

info = json.loads(input)

for item in info['items']:
    print 'Title:', item['title']
    print '  ID:', item['id']