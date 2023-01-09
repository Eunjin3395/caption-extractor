fileName="{}주차{}".format(13,1)
vttFile=open(fileName+".txt","rt")
outFile=open(fileName+"_수정.hwp","w",encoding="cp949")
outLine=""
while True:
      line=vttFile.readline()
      if not line: break
      if("-->" not in line):
        tempLine=line.replace("\n"," ")

        outLine+=tempLine


outFile.write(outLine)

vttFile.close()
outFile.close()
print("{} success".format(fileName))