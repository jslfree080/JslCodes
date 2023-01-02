#!/usr/bin/env python3
"""
Author: Jungsoo Lee <jungsoo080@korea.ac.kr>
"""
from abc import *
from GEOparse import *
from os import *
from wget import *

class WEBFILEdownloader(metaclass = ABCMeta):
    def __init__(self, destDirP):
        self.destDir = destDirP
        assert self.destDir.endswith('/') or self.destDir.endswith('\\'), "The directory path should end with / or \\\ "
    @abstractmethod
    def runDownload(self):
        pass
    def setDestDir(self, destDirP):
        self.destDir = destDirP

class ProcessDir:
    __metaclass__ = ABCMeta
    @abstractmethod
    def process(self):
        pass
        
class NewDir(ProcessDir):
    def process(self, prePathP, newDirP):
        self.getDir = prePathP + newDirP
        mkdir(self.getDir)
        
class GEOdownloader(WEBFILEdownloader):
    def runDownload(self, gseNameP):
        newdir = NewDir()
        newdir.process(self.destDir, gseNameP)
        gse = get_GEO(geo = gseNameP, destdir = self.destDir)
        for suppFiles in gse.metadata['supplementary_file']:
            try:
                download(suppFiles, newdir.getDir)
            except ContentTooShortError:
                print(suppFiles)

if __name__ == "__main__":
    gse = GEOdownloader("/Users/jungsoo080/Documents/Python3/")
    gse.runDownload("GSE185553")
    gse.runDownload("GSE185277")
    gse.setDestDir("/Users/jungsoo080/Desktop/")
    gse.runDownload("GSE198323")
