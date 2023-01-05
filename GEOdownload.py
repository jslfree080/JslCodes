"""
Author: Jungsoo Lee
Date: January 5, 2023,

This script automates downloading supplementary files from GEO.
"""
import os
import wget

from abc import ABC, abstractmethod
from GEOparse import get_GEO


class ProcessDir(ABC):
    @abstractmethod
    def process(self):
        pass


class NewDir(ProcessDir):
    def __init__(self, pre_path, new_dir):
        self.get_dir = pre_path + new_dir

    def process(self):
        """Create a new directory."""
        try:
            os.makedirs(self.get_dir, exist_ok=True)
        except OSError as e:
            print(f"An error occurred while creating the directory {self.get_dir}: {e}")

    def __repr__(self):
        return f'{self.__class__.__name__}({self.get_dir})'


class DownloadWebfile(ABC):
    def __init__(self, destination_dir):
        self.destination_dir = destination_dir
        assert self.destination_dir.endswith('/') or self.destination_dir.endswith('\\'),\
            "The directory path should end with '/' or '\\\\' "

    @abstractmethod
    def run_download(self, data_name):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}({self.destination_dir})'


class DownloadGEO(DownloadWebfile):
    def run_download(self, data_name):
        """Download supplementary files from GEO."""
        # Create a new directory for the supplementary files
        new_dir = NewDir(self.destination_dir, data_name)
        new_dir.process()

        # Retrieve metadata for the given GEO accession number
        try:
            gse = get_GEO(geo=data_name, destdir=self.destination_dir)
        except Exception as e:
            print(f'An error occurred while retrieving metadata for {data_name}: {e}')
            return

        # Download the supplementary files
        if 'supplementary_file' in gse.metadata:
            for supp_files in gse.metadata['supplementary_file']:
                try:
                    # Save the file to the new directory created above
                    wget.download(supp_files, out=new_dir.get_dir)
                except (IOError, ValueError, OSError) as e:
                    print(f'An error occurred while downloading the file from {supp_files} to {new_dir.get_dir}: {e}')
        else:
            print(f'There are no supplementary files listed in the metadata for {data_name}')


if __name__ == "__main__":
    """Download supplementary files from GEO."""
    supp_downloader = DownloadGEO("/Users/jslit/Documents/")
    supp_downloader.run_download("GSE185553")
    supp_downloader.run_download("GSE185277")
    supp_downloader.destination_dir("/Users/jslit/Desktop/")
    supp_downloader.run_download("GSE198323")
