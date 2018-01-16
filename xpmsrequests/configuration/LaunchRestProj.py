import os
from xpmsrequests.configuration import ExcelReading


def main():

    executionList = []
    testsToExecute = ''

    excelObj = ExcelReading.ExcelOperations()
    executionList = excelObj.getExecutionList()

    for i in range(0,executionList.__len__(),1):
        testsToExecute = testsToExecute + executionList[i] + ","

    testsToExecute = testsToExecute.rstrip(',')
    print("Tests to execute are :",testsToExecute)

    #os.chdir("../../")
    print(os.path.abspath(__file__))

    print("The current working dir is :",os.getcwd())

    os.system("pytest xpmsrequests/testscriptsranger/ --alluredir TempAllure  --allure_stories="+testsToExecute)

    #os.system("allure serve TempAllure")

if __name__ == "__main__":
    main()
