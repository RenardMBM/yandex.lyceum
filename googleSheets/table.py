import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'Attendance log-665425bc6351.json'
SPREADSHEET_ID = '1sUhBeXNpSJfIYaei_4e5A03AjDKUoT18MZOMKQ3x8xE'

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID, ranges=[],
                                         includeGridData=True).execute()

# print(spreadsheet, sep='\n')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('')
print('')
print(spreadsheet)
print(spreadsheet['sheets'][0]['properties']['gridProperties'])
columnCount = spreadsheet['sheets'][0]['properties']['gridProperties']['columnCount']
print(columnCount)

requests = [{
    'updateSpreadsProperties': {
        'properties': {
            'gridProperties': {
                'columnCount': columnCount + 1
            }
        },
        'fields': 'columnCount'
    }
}]

results = service.spreadsheets().values().batchUpdate(spreadsheetId=SPREADSHEET_ID,
                                                      body={"requests": [
                                                          {
                                                              "updateSheetProperties": {
                                                                  "properties": {
                                                                      "gridProperties": {
                                                                          "columnCount": columnCount + 1
                                                                      }
                                                                  }
                                                              }
                                                          }
                                                      ]})

numSecondLetter = columnCount % 26
numFirstLetter = columnCount // 26
if numFirstLetter:
    letters = alphabet[numFirstLetter] + alphabet[numSecondLetter]
else:
    letters = alphabet[numSecondLetter]
print(letters)

students = [
    'Бадерик Михаил', 'Бадерик Павел', 'Бандур Вероника', 'Бандур Максим', 'Кузоро Сергей',
    'Лосев Петр', 'Момот Максим', 'Моргунов Николай', 'Софья', 'Шибаев Василий'
]
answers = []
for name in students:
    answers.append(["\'+" if input(name) == '+'else 'N'])

print(results.execute())
