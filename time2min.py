# -*- coding: utf-8 -*-

import numpy as np
import list2csv
import csvWR
list=[['NO', '부서명', '사번', '성명', '직위', '근무일', '입실', '근무시작', '근무종료', '퇴실', '근무시간', '근태구분', '근태변경', '근무연장', '비고'],
['44', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.03', '08:45', '', '', '21:02', '', '정상', '', '', ''],
['43', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.04', '09:28', '', '', '21:06', '', '지각Ⅰ', '신청', '', ''],
['42', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.05', '09:41', '', '', '20:17', '', '지각Ⅱ', '신청', '', ''],
['41', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.06', '09:06', '', '', '20:19', '', '지각Ⅰ', '신청', '', ''],
['40', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.07', '09:29', '', '', '20:23', '', '지각Ⅰ', '신청', '', ''],
['39', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.08', '12:27', '', '', '14:15', '', '휴일근무', '', '', ''],
['38', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.10', '09:59', '', '', '20:23', '', '지각Ⅱ', '신청', '', ''],
['37', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.11', '07:34', '', '', '19:14', '', '정상', '', '', ''],
['36', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.12', '09:21', '', '', '21:01', '', '지각Ⅰ', '신청', '', ''],
['35', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.13', '09:14', '', '', '21:13', '', '지각Ⅰ', '신청', '', ''],
['34', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.14', '10:12', '', '', '18:29', '', '지각Ⅱ', '신청', '', ''],
['33', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.17', '09:11', '', '', '19:59', '', '지각Ⅰ', '신청', '', ''],
['32', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.18', '09:41', '', '', '20:17', '', '지각Ⅱ', '신청', '', ''],
['31', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.19', '10:32', '', '', '22:29', '', '지각Ⅱ', '신청', '', ''],
['30', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.20', '10:19', '', '', '20:45', '', '지각Ⅱ', '신청', '', ''],
['29', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.21', '08:50', '', '', '18:07', '', '정상', '', '', ''],
['28', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.27', '07:25', '', '', '19:44', '', '정상', '', '', ''],
['27', 'B3팀', '2018321', '엄기훈', '연구원', '2018.09.28', '09:43', '', '', '18:34', '', '지각Ⅱ', '신청', '', ''],
['26', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.01', '09:07', '', '', '19:42', '', '지각Ⅰ', '신청', '', ''],
['25', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.02', '08:53', '', '', '18:54', '', '정상', '', '', ''],
['24', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.03', '18:03', '', '', '19:28', '', '휴일근무', '', '', ''],
['23', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.04', '08:55', '', '', '22:03', '', '정상', '', '', ''],
['22', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.05', '09:01', '', '', '19:11', '', '지각Ⅰ', '신청', '', ''],
['21', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.08', '09:05', '', '', '21:39', '', '지각Ⅰ', '신청', '', ''],
['20', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.10', '09:12', '', '', '21:50', '', '지각Ⅰ', '신청', '', ''],
['19', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.11', '09:17', '', '', '21:28', '', '지각Ⅰ', '신청', '', ''],
['18', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.12', '09:19', '', '', '18:53', '', '지각Ⅰ', '신청', '', ''],
['17', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.15', '08:44', '', '', '2018.10.16 00:47', '', '정상', '', '', ''],
['16', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.16', '10:24', '', '', '22:22', '', '지각Ⅱ', '신청', '', ''],
['15', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.17', '09:42', '', '', '21:00', '', '지각Ⅱ', '신청', '', ''],
['14', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.18', '09:02', '', '', '21:14', '', '지각Ⅰ', '신청', '', ''],
['13', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.19', '09:07', '', '', '20:24', '', '지각Ⅰ', '신청', '', ''],
['12', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.21', '15:16', '', '', '23:22', '', '휴일근무', '', '', ''],
['11', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.22', '08:56', '', '', '21:47', '', '정상', '', '', ''],
['10', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.23', '09:53', '', '', '21:46', '', '지각Ⅱ', '신청', '', ''],
['9', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.24', '09:26', '', '', '20:37', '', '지각Ⅰ', '신청', '', ''],
['8', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.25', '09:29', '', '', '22:45', '', '지각Ⅰ', '신청', '', ''],
['7', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.26', '09:56', '', '', '20:55', '', '지각Ⅱ', '신청', '', ''],
['6', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.29', '08:58', '', '', '22:35', '', '정상', '', '', ''],
['5', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.30', '09:11', '', '', '2018.10.31 01:41', '', '지각Ⅰ', '신청', '', ''],
['4', 'B3팀', '2018321', '엄기훈', '연구원', '2018.10.31', '09:19', '', '', '21:03', '', '지각Ⅰ', '신청', '', ''],
['3', 'B3팀', '2018321', '엄기훈', '연구원', '2018.11.01', '14:42', '', '', '20:32', '', '반차(오전)', '', '', ''],
['2', 'B3팀', '2018321', '엄기훈', '연구원', '2018.11.02', '09:46', '', '', '18:12', '', '지각Ⅱ', '신청', '', ''],
['1', 'B3팀', '2018321', '엄기훈', '연구원', '2018.11.05', '09:20', '', '', '2018.11.06 00:19', '', '지각Ⅰ', '신청', '', '']]
#print(list)
csvWR.csvWR(list)
#list2csv.list2csv(list)

workTime = []

del(list[0])
for row in list:
    date=row[5]
    inTime=row[6]
    outTime=row[9]

    inList=inTime.split(":")
    outList=inList


    if(outTime[0:4]=='2018'):
        outList=outTime[11:].split(":")
        outList[0]=str(int(outList[0])+24)
    else:
        outList = outTime.split(":")



    inMin = int(inList[0]  )*60+int(inList[1])
    outMin = int(outList[0])*60+int(outList[1])
    workHour = (outMin-inMin)/60

    print(date,"\t", inList, "\t", outList, "\t",workHour)

    workTime.append(workHour)
print(workTime)
print(np.mean(workTime)-2)




