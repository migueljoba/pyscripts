# -*-encoding: utf-8 -*-
import os
import requests


class OutputPathException(Exception):
    pass


class ZipDownloader:
    """
    Use:
        URL_SOURCE = 'http://www.example.com/source.zip'
        zipi = ZipDownloader(URL_SOURCE)
        zipi.go()

        ... and it is done.
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, url_source, dest_path=None, uncompress=False):
        self.url_source = url_source
        self.dest_path = dest_path
        self.uncompress = uncompress

    def _request_resource(self):
        req = requests.get(self.url_source)
        return req

    def __write_resource_from_request(self, req):

        if self.dest_path is None:
            self.dest_path = os.path.join('.', "zipi_default_dest.zip")

        with open(self.dest_path, 'wb') as dest:
            for chunk in req.iter_content(chunk_size=1):
                dest.write(chunk)

    def __uncompress(self):

        # TODO impllement this!!
        # file_path = os.path.join(BASE_DIR, folder, file_name)
        # tmp_folder = os.path.join('.', "test_test")
        # zip_ref = zipfile.ZipFile(self.dest_path, 'r')
        # zip_ref.extractall(tmp_folder)
        # zip_ref.close()
        raise NotImplementedError(u'uncompress boolean is not implemented yet :( ')

    def go(self):
        print 'Downloading to %s' % self.dest_path
        req = self._request_resource()
        self.__write_resource_from_request(req)

        if self.uncompress:
            self.__uncompress()
