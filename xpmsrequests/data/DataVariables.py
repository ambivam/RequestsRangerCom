
#*************************Variables*********************
TimeOut = 12
PollTime = 5
#*************************CogX URLs*********************

CmsImage = 'CMS1500_1.png'

JpgImage = 'cms_1.jpg'

#CogXBaseUrl = 'http://apigw-dev.ranger.xpms.ai/apidocs'
CogXBaseUrl = 'http://devintkapi.apps.xpms.io/'

TestSuiteExcel = 'TestSuiteRestServices.xlsx'

TestDataExcel = 'TestSuiteData.xlsx'

Image = 'image'

JobIdUrl = 'http://devintkapi.apps.xpms.io/job/'


UploadUrl = CogXBaseUrl+'upload'+'/'

MimeTypeClassifierUrl = CogXBaseUrl + Image + '/' + 'mimeTypeClassifier'

ClassifyUrl = CogXBaseUrl + Image + '/' +'classify'

PreProcessUrl = CogXBaseUrl + Image + '/'+'preProcess'

SliceURL = CogXBaseUrl + Image + '/'+'slice'

OcrURL = CogXBaseUrl + Image + '/'+'ocr'

#************************jsonfiles cogx************************

TempJson = 'temp.json'

SliceJson = 'slicejson.json'

OcrJson = 'ocrjson.json'

PreProcessJson = 'preprocess.json'

#********************DataVariables CogX******************
tempData = 'Family Plan 6'

tempDataJpg = 'DIAGNOSIS POINTER_4'

classifier = 'csf'
#*******************Data Variables Ranger****************
entityId = '66db655d-c6fa-4d97-b1dd-c3f75e4eb54f'

solutionId = 'test_2de78758-b3b8-4c7c-b08c-cde339dea7e8'
#*********************jsonfiles ranger*******************

Insightingestjson = 'insightingestjson.json'

GetInsightJson = 'getinsight.json'

#*********************Ranger URLs************************

RangerJobIdUrl = 'http://apigw-dev.ranger.xpms.ai/job/'

RangerURL = 'http://apigw-dev.ranger.xpms.ai/'

RangerUploadURL = RangerURL + 'upload'+'/'

GetInsightURL = RangerURL + 'insight/getInsight'

#********************************************************