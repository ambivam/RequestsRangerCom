#Docker image to test ranger api's
#********************************
FROM ubuntu:latest 
MAINTAINER rajanikanthb@xpms.io 
#********************************
RUN apt-get update
#RUN apt-get -y upgrade
RUN apt-get install -y python-pip
RUN apt-get install -y python3-pip
RUN apt-get -y install software-properties-common

RUN apt-add-repository ppa:qameta/allure
RUN apt-get update 
RUN apt-get install -y allure

RUN pip install Flask
RUN pip3 install requests
RUN pip install requests
RUN pip install pytest
#RUN pip install allure-pytest
RUN pip install allure-python-commons
RUN pip install pytest-allure-adaptor
RUN pip install pytest-xdist

#********************************
#ADD RequestsRangerCom /home/RequestsRangerCom/
COPY RequestsRangerCom/ /home/RequestsRangerCom/
WORKDIR /home/RequestsRangerCom/

#RUN ["pytest","xpmsrequests/testscriptsranger/", "--alluredir", "TempAllure","--allure_stories=ExtractDocumentText"]
#RUN pytest xpmsrequests/testscriptsranger/ --alluredir TempAllure --allure_stories=Smoke && return 0
RUN ["python", "/home/RequestsRangerCom/xpmsrequests/configuration/RunPytest.py"]
CMD ["allure","serve","TempAllure","--port","3232"]

#********************************
#ENTRYPOINT [pytest /home/RequestsCOG/xpmsrequests/testscripts/ --alluredir TempAllure  --allure_stories=upload,mimeclassifier && allure serve TempAllure --port 3232]
#ENTRYPOINT ["pytest xpmsrequests/testscripts/ --alluredir TempAllure  --allure_stories=upload,mimeclassifier"]
#ENTRYPOINT ["pytest" && "/xpmsrequests/testscripts/" && "--alluredir TempAllure" && "--allure_stories=upload,mimeclassifier"]
#ENTRYPOINT ["chmod", "+x","./home/RequestsCOG/xpmsrequests/cmds.sh"]
#ENTRYPOINT ["pytest", "xpmsrequests/testscripts/","--alluredir","TempAllure","--allure_stories=upload,mimeclassifier" && "allure","serve","TempAllure","--port","3232"]
#********************************
#CMD ["pytest", "/home/RequestsCOG/xpmsrequests/testscripts/", "--alluredir", "TempAllure",  "--allure_stories=upload,mimeclassifier"]
#RUN ["pytest", "xpmsrequests/testscripts/", "--alluredir", "TempAllure",  "--allure_stories=upload,mimeclassifier"]
#RUN ["allure","serve","TempAllure","--port","3232"]
#CMD ["allure","serve","TempAllure","--port","3232"]
#RUN ["chmod", "+x","/home/RequestsCOG/xpmsrequests/cmds.sh"]
#CMD ["chmod +x","/home/RequestsCOG/xpmsrequests/cmds.sh"]
#WORKDIR /home/RequestsCOG/xpmsrequests/
#RUN ["chmod", "+x","/home/RequestsCOG/xpmsrequests/cmds.sh"]
#CMD ["cmds.sh"]
#CMD ["python", "/home/RequestsCOG/RunPytest.py"]
#CMD ["pytest", "/home/RequestsCOG/xpmsrequests/testscripts/";"allure","serve","TempAllure","--port","3232"]
#CMD ["pytest /home/RequestsCOG/xpmsrequests/testscripts/";"allure serve TempAllure --port 3232"]
#CMD ["/home/RequestsCOG/xpmsrequests/cmds.sh"]
#********************************




