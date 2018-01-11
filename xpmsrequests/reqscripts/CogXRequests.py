import time
import requests
import json
import os
import logging

from xpmsrequests.data import DataVariables
from xpmsrequests.reqscripts import cogx_framework

class CogXReq(cogx_framework.CogxBaseTest):

    def __init__(self):
        # Create the Logger
        super(CogXReq,self).__init__()
        self.logger = logging.getLogger(__name__)
    # *****************************************************************************************************
    # *****************************************************************************************************

    def getDataByJobId(self,JobId):
        self.logger.info('Into getDataByJobId method')
        jobIdUrl = DataVariables.JobIdUrl+JobId
        self.logger.info('JobIdUrl is :'+jobIdUrl)
        status = 'in-progress'
        processStatus = 'process_status'

        try:
            count = 1
            while (count <= DataVariables.TimeOut):
                tempJson = requests.get(jobIdUrl).json()
                if(count > DataVariables.TimeOut):
                    self.logger.error('Time Count Exceeded')
                    return None
                if (tempJson[processStatus] != status):
                    print('Exited while')
                    self.logger.info('Returning Json :'+str(tempJson))
                    return tempJson
                if (tempJson[processStatus] == status):
                    self.logger.info('Into Sleep')
                    self.logger.info('Sleep Time is : '+str(DataVariables.PollTime))
                    time.sleep(DataVariables.PollTime)
                    count += 1
                    self.logger.info('count is :'+str(count))
        except:
            print('Unable to generate response')
            self.logger.error('Unable to generate response')


    # *****************************************************************************************************
    # *****************************************************************************************************

    def upLoadReq(self,imgUrl):

        self.logger.info('Into upLoadReq method')
        files = {'file': open(imgUrl, 'rb')}
        #self.logger.info('file is:'+str(files))
        response = requests.post(DataVariables.UploadUrl, files=files)
        self.logger.info('Response Json after uploading image is'+str(response.json()))
        if(response.status_code == 200):
            self.logger.info('Status of Response returned after uploading the image is ' + str(response.status_code))
            return response.json()
        else:
            self.logger.error('Status of Response returned after uploading the image is' + str(response.status_code))
            return None

    # *****************************************************************************************************
    # *****************************************************************************************************

    def mimeTypeClassifier(self,mimeClassifierJson):
        self.logger.info('Into mimeTypeClassifier method')
        jsonFileData = self.getJsonFileData(DataVariables.TempJson)
        self.logger.info('The parameters body Of Mime Type Classifier is :'+str(jsonFileData))
        #self.logger.info(jsonFileData['data']['resources'][0])
        jsonFileData['data']['resources'][0] = mimeClassifierJson['metadata']
        self.logger.info('Parameters filepath of mimeTypeClassifier after assigning metadata of Upload json is :'+str(jsonFileData['data']['resources'][0]))

        mimetypeClassifierJobId = self.getResponse(DataVariables.MimeTypeClassifierUrl, jsonFileData)
        self.logger.info('Job Id returned by MimetypeClassifier is :'+str(mimetypeClassifierJobId))
        return mimetypeClassifierJobId

    # *****************************************************************************************************
    # *****************************************************************************************************
    def classify(self,classifyJson):
        self.logger.info('Into classify method')
        jsonFileData = self.getJsonFileData(DataVariables.TempJson)
        self.logger.info('The parameters body Of Classify method is :' + str(jsonFileData))
        self.logger.info(jsonFileData['data']['resources'][0])
        jsonFileData['data']['resources'][0]['file_path'] = classifyJson['result']['metadata']['file_path']
        self.logger.info('Parameters filepath of Classify after assigning metadata of MimeTypeClassifier json is :' + str(jsonFileData['data']['resources'][0]))

        classifyJobID = self.getResponse(DataVariables.ClassifyUrl, jsonFileData)
        self.logger.info('Job Id returned by Classify is :' + str(classifyJobID))
        return classifyJobID

    # *****************************************************************************************************
    # *****************************************************************************************************

    def preProcess(self,classifyJson):
        self.logger.info('Into preProcess method')
        jsonFileData = self.getJsonFileData(DataVariables.PreProcessJson)
        self.logger.info('The parameters body Of preProcess method is :' + str(jsonFileData))
        self.logger.info(jsonFileData['data']['resources'][0])
        jsonFileData['data']['resources'][0]['classifier'] = classifyJson['result']['metadata']['classifier']
        jsonFileData['data']['resources'][0]['file_path'] = classifyJson['result']['metadata']['file_path']
        self.logger.info('Parameters filepath of Preprocess after assigning metadata of Classify json is :' + str(jsonFileData))
        preProcessJobId = self.getResponse(DataVariables.PreProcessUrl, jsonFileData)
        self.logger.info('Job Id returned by PreProcess is :' + str(preProcessJobId))
        return preProcessJobId
    # *****************************************************************************************************
    # *****************************************************************************************************

    def slice(self,preprocessJson,dataKey):
        self.logger.info('Into slice method')
        jsonFileData = self.getJsonFileData(DataVariables.SliceJson)
        self.logger.info('The parameters body Of Slice method is :' + str(jsonFileData))
        self.logger.info(jsonFileData['data']['resources'][0]['fields'][0])
        jsonFileData['data']['resources'][0]['fields'][0] = preprocessJson['result']['metadata']['fields'][dataKey]
        jsonFileData['data']['resources'][0]['file_path'] = preprocessJson['result']['metadata']['file_path']
        self.logger.info('Parameters filepath and fields of slice after assigning metadata of preprocess json is :' + str(jsonFileData))
        sliceJobId = self.getResponse(DataVariables.SliceURL, jsonFileData)
        self.logger.info('Job Id returned by Slice is :' + str(sliceJobId))
        return sliceJobId

    # ******************************************************************sliceJson***********************************
    # *****************************************************************************************************
    def ocr(self,sliceJson):
        self.logger.info('Into ocr method')
        jsonFileData = self.getJsonFileData(DataVariables.OcrJson)
        self.logger.info('The parameters body Of Ocr method is :' + str(jsonFileData))
        self.logger.info(jsonFileData['data']['resources'][0]['fields'][0])
        jsonFileData['data']['resources'][0]['fields'][0]['field_type'] = sliceJson['result']['metadata']['fields'][0]['field_type']
        jsonFileData['data']['resources'][0]['fields'][0]['name'] = sliceJson['result']['metadata']['fields'][0]['name']
        jsonFileData['data']['resources'][0]['fields'][0]['file_path'] = sliceJson['result']['metadata']['fields'][0]['file_path']
        self.logger.info('Parameters filepath,fields and name of ocr after assigning metadata of slice json is :' + str(jsonFileData))
        ocrJobId = self.getResponse(DataVariables.OcrURL, jsonFileData)
        self.logger.info('Job Id returned by Ocr is :' + str(ocrJobId))
        return ocrJobId

    #*****************************************************************************************************
    #*****************************************************************************************************