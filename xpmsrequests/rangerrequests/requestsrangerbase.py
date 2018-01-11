import time
import requests
import json
import os
import logging

from xpmsrequests.data import DataVariables

class RangerBase(object):

    def __init__(self):
        # Create the Logger
        self.logger = logging.getLogger(__name__)

    def getJsonFileData(self,jsonFile):
        self.logger.info('Into getJsonFileData method')
        filePath = os.path.abspath(__file__ + "/../../data/jsonfiles") + '/'
        self.logger.info('File path Is :',filePath)
        tempJson = open(filePath + jsonFile)

        self.logger.info('template Json is :' + str(tempJson))
        jsonFileData = json.load(tempJson)
        return jsonFileData

    def getResponse(self,url,jsonData):
        self.logger.info('Into getResponse method')
        headers = {'Content-Type': 'application/json'}
        self.logger.info('!!!!!!!!!!!!!The Request is :!!!!!!!!!!!!!!!')
        response = requests.post(url, headers=headers, json=jsonData)
        self.logger.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        self.logger.info(response.json())
        self.logger.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        self.logger.info('Response Json is ' + str(response))
        # print(response.json()['job_id'])
        if (response.status_code == 200):
            self.logger.info(' JobId is :' + response.json()['job_id'])
            return response.json()['job_id']
        else:
            self.logger.error('failed to get the JobId ')
            return None
