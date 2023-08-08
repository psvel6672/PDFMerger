from PyPDF2 import PdfReader, PdfFileWriter
import os, datetime

output = PdfFileWriter()
addPageCnt = 0

tempFiles = os.listdir("Template Files")

for i in tempFiles:
    filePath = os.getcwd()+'/Template Files/'+str(i)
    if filePath.endswith(".pdf"):
        reader = PdfReader(filePath)
        for page in reader.pages:
            output.addPage(page)
            addPageCnt += 1

if addPageCnt > 0:

    now = datetime.datetime.now().strftime("%I_%M_%S_%p")
    
    with open("./OutputPDF/mergedfile_"+str(now)+".pdf", "wb") as outputStream:
        output.write(outputStream)
else:
    print("No Files")
