import pytest
import os
import json
import  logging
import allure

from xpmsrequests.rangerrequests import  requestsranger
from xpmsrequests.data import DataVariables
from xpmsrequests.configuration import ExcelReading

logger = logging.getLogger(__name__)

#*************************************************
def upload(filename):
    logger.info('**********************************************************' )
    result = False
    try:
        logger.info('Testing upload of Image')
        reqTest = requestsranger.RangerReq()
        filePath = os.path.abspath(__file__ + "/../../data/images") + '/'
        logger.info('FilePath is : '+filePath+filename)
        uploadResponseJson = reqTest.upLoadReq(filePath + filename)

        if (uploadResponseJson['status']['success'] == True):
            result = True
            logger.info('Status of returned json of upload image result is ' + str(uploadResponseJson['status']))

        assert True, result
        logger.info('test_uploadreq method passed')
        return uploadResponseJson
    except:
        logger.error('Status of returned json of upload image result is ' + str(uploadResponseJson['status']))
        logger.error('Upload of Image failed')
        logger.info('**********************************************************')
        assert True==result

    logger.info('**********************************************************')

#*************************************************
def insightIngest(uploadJson):
    logger.info('**********************************************************')
    result = False
    try:
        logger.info('Testing InsightIngest')
        reqTest = requestsranger.RangerReq()

        logger.info('Upload Response Json is :'+str(uploadJson))
        JobId = reqTest.insightIngest(uploadJson)
        #logger.info('The test_MimeTypeClassifier Job Id Is :'+str(JobId))

        if (JobId != None):
            result = True

        assert True, result
        logger.info('Testing insightIngest method passed')
        logger.info('**********************************************************')
        return JobId
    except:
        logger.error('result =' + str(result))
        logger.error('Testing insightIngest method failed')
        logger.info('**********************************************************')
        assert True == result

# *************************************************
def extractDocumentMetadata(injestInsightJobIdentifier):
    logger.info('**********************************************************')
    result = False
    try:
        logger.info('Testing extractDocumentMetadata')
        reqTest = requestsranger.RangerReq()

        logger.info('insightIngest Response is :' + str(injestInsightJobIdentifier))

        JobId = reqTest.insightExtractDocumentMetadata(reqTest.getDataByJobId(injestInsightJobIdentifier))
        # logger.info('The test_MimeTypeClassifier Job Id Is :'+str(JobId))

        if (JobId != None):
            result = True

        assert True, result
        logger.info('Testing extractDocumentMetadata method passed')
        logger.info('**********************************************************')
        return JobId
    except:
        logger.error('result =' + str(result))
        logger.error('Testing extractDocumentMetadata method failed')
        logger.info('**********************************************************')
        assert True == result

# *************************************************
def convertDocument(extractDocumentMetadataJobIdentifier):
    logger.info('**********************************************************')
    result = False
    try:
        logger.info('Testing ConvertDocument')
        reqTest = requestsranger.RangerReq()

        logger.info('ExtractDocumentMetadata Response is :' + str(extractDocumentMetadataJobIdentifier))

        JobId = reqTest.insightConvertDocument(reqTest.getDataByJobId(extractDocumentMetadataJobIdentifier))
        # logger.info('The test_MimeTypeClassifier Job Id Is :'+str(JobId))

        if (JobId != None):
            result = True

        assert True, result
        logger.info('Testing convertDocument method passed')
        logger.info('**********************************************************')
        return JobId
    except:
        logger.error('result =' + str(result))
        logger.error('Testing convertDocument method failed')
        logger.info('**********************************************************')
        assert True == result

# *************************************************
def classifyDocument(convertDocumentJobIdentifier):
    logger.info('**********************************************************')
    result = False
    try:
        logger.info('Testing classifyDocument')
        reqTest = requestsranger.RangerReq()

        logger.info('ConvertDocument Response is :' + str(convertDocumentJobIdentifier))

        JobId = reqTest.insightClassifyDocument(reqTest.getDataByJobId(convertDocumentJobIdentifier))
        # logger.info('The test_MimeTypeClassifier Job Id Is :'+str(JobId))

        if (JobId != None):
            result = True

        assert True, result
        logger.info('Testing classifyDocument method passed')
        logger.info('**********************************************************')
        return JobId
    except:
        logger.error('result =' + str(result))
        logger.error('Testing classifyDocument method failed')
        logger.info('**********************************************************')
        assert True == result

# *************************************************
def extractDocumentElements(classifyDocumentJobIdentifier):
    logger.info('**********************************************************')
    result = False
    try:
        logger.info('Testing extractDocumentElements')
        reqTest = requestsranger.RangerReq()

        logger.info('ClassifyDocument Response is :' + str(classifyDocumentJobIdentifier))

        JobId = reqTest.insightExtractDocumentElements(reqTest.getDataByJobId(classifyDocumentJobIdentifier))
        # logger.info('The test_MimeTypeClassifier Job Id Is :'+str(JobId))

        if (JobId != None):
            result = True

        assert True, result
        logger.info('Testing ExtractDocumentElements method passed')
        logger.info('**********************************************************')
        return JobId
    except:
        logger.error('result =' + str(result))
        logger.error('Testing ExtractDocumentElements method failed')
        logger.info('**********************************************************')
        assert True == result

# *************************************************
def extractDocumentText(extractDocumentElementsJobIdentifier):
    logger.info('**********************************************************')
    result = False
    try:
        logger.info('Testing extractDocumentText')
        reqTest = requestsranger.RangerReq()

        logger.info('ExtractDocumentElements Response is :' + str(extractDocumentElementsJobIdentifier))

        JobId = reqTest.insightExtractDocumentText(reqTest.getDataByJobId(extractDocumentElementsJobIdentifier))
        # logger.info('The test_MimeTypeClassifier Job Id Is :'+str(JobId))

        if (JobId != None):
            result = True

        assert True, result
        logger.info('Testing ExtractDocumentText method passed')
        logger.info('**********************************************************')
        return JobId
    except:
        logger.error('result =' + str(result))
        logger.error('Testing ExtractDocumentText method failed')
        logger.info('**********************************************************')
        assert True == result


#***********************************************
#To Validate The Json Returned By Upload Request
#***********************************************
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@pytest.allure.step('To Test The Request Uploading test_uploadreq')
@allure.feature('Feature1')
@allure.story('Smoke','Regression','upload')
def test_uploadreq():
    upload(DataVariables.CmsImage)

#****************************************************
#To Validate The JobId returned by InsightIngest
#****************************************************
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.step('To Test The JobId returned by InsightIngest')
@allure.feature('Feature1')
@allure.story('Smoke','InsightIngest')
def test_InsightIngest():
    insightIngest(upload(DataVariables.CmsImage))
#****************************************************

#To Validate The JobId returned by ExtractDocumentMetadata
#****************************************************
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.step('To Test The JobId returned by ExtractDocumentMetadata')
@allure.feature('Feature1')
@allure.story('Smoke','ExtractDocumentMetadata')
def test_ExtractDocumentMetadata():
    extractDocumentMetadata(insightIngest(upload(DataVariables.CmsImage)))
#****************************************************
#To Validate The JobId returned by ConvertDocument
#****************************************************
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.step('To Test The JobId returned by ConvertDocument')
@allure.feature('Feature1')
@allure.story('Smoke','ConvertDocument')
def test_ConvertDocument():
    convertDocument(extractDocumentMetadata(insightIngest(upload(DataVariables.CmsImage))))
#****************************************************
#To Validate The JobId returned by ClassifyDocument
#****************************************************
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.step('To Test The JobId returned by ClassifyDocument')
@allure.feature('Feature1')
@allure.story('Smoke','ClassifyDocument')
def test_ClassifyDocument():
    classifyDocument(convertDocument(extractDocumentMetadata(insightIngest(upload(DataVariables.CmsImage)))))
#****************************************************
#To Validate The JobId returned by ExtractDocumentElements
#****************************************************
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.step('To Test The JobId returned by ExtractDocumentElements')
@allure.feature('Feature1')
@allure.story('Smoke','ExtractDocumentElements')
def test_ExtractDocumentElements():
    extractDocumentElements(classifyDocument(convertDocument(extractDocumentMetadata(insightIngest(upload(DataVariables.CmsImage))))))
#****************************************************
#To Validate The JobId returned by ExtractDocumentText
#****************************************************
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.step('To Test The JobId returned by ExtractDocumentText')
@allure.feature('Feature1')
@allure.story('Smoke','ExtractDocumentText')
def test_ExtractDocumentText():
    extractDocumentText(extractDocumentElements(classifyDocument(convertDocument(extractDocumentMetadata(insightIngest(upload(DataVariables.CmsImage)))))))
#****************************************************
