#!/usr/bin/python2.7
#-*-coding:utf-8-*-

import os



def getAllPath(workpath):
	allPath=[]
	docList=os.walk(workpath)
	for path,doc,file in docList:
		for afile in file:
			allPath.append(path+"/"+afile)
	return allPath
def getFixedPath(pathList,fixed):
	fixedPath=[]
	for path in pathList:
		if path.endswith(fixed):
			fixedPath.append(path)
	return fixedPath
def getAFileLines(path):
	data=open(path)
	num=len(data.readlines())
	return num
if __name__ == '__main__':
	rootdir=u'/Users/FanXingGuo/home'
	pt=raw_input("Path:")
	li=getAllPath(pt)
	fixedPath=getFixedPath(li,".java")
	i=0
	for filePath in fixedPath:
		print filePath
		i+=getAFileLines(filePath)
	print "files:"
	print len(fixedPath)
	print "lines:"
	print i


