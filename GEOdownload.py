#!/usr/bin/env python3
"""
Author: Jungsoo Lee <jslfree080@gmail.com>
"""
import os
import wget

from abc import *
from GEOparse import get_GEO


class WEBFILEdownloader(metaclass=ABCMeta):
    def __init__(self, dest_dir):
        self.dest_dir = dest_dir
        assert self.dest_dir.endswith('/') or self.dest_dir.endswith('\\'), "The directory path should end with / or \\\ "

    @abstractmethod
    def run_download(self):
        pass

    def set_dest_dir(self, dest_dir):
        self.dest_dir = dest_dir


class ProcessDir:
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self):
        pass


class NewDir(ProcessDir):
    def process(self, pre_path, new_dir):
        self.get_dir = pre_path + new_dir
        os.makedirs(self.get_dir, exist_ok=True)


class GEOdownloader(WEBFILEdownloader):
    def run_download(self, gse_name):
        new_dir = NewDir()
        new_dir.process(self.dest_dir, gse_name)
        gse = get_GEO(geo=gse_name, destdir=self.dest_dir)
        for supp_files in gse.metadata['supplementary_file']:
            try:
                wget.download(supp_files, out=new_dir.get_dir)
            except wget.exceptions.ContentTooShortError:
                print(supp_files)


if __name__ == "__main__":
    gse = GEOdownloader("/Users/jslit/Documents/")
    gse.run_download("GSE185553")
    gse.run_download("GSE185277")
    gse.set_dest_dir("/Users/jslit/Desktop/")
    gse.run_download("GSE198323")