# -*- encoding:utf-8 -*-

# Image downloader script script from its URL
#
# Proposed by:
#   https://coderwall.com/p/lngdkg/saving-images-with-just-requests-http-for-humans
#
# Source in:
#   https://gist.github.com/hanleybrand/4221658

import os
from io import open as iopen

import requests


class RequestException(Exception):
    # raises if requests http code is not 200 OK
    pass


class ImageDownloader:
    """
    Use:
        URL_SOURCE = 'http://www.example.com/source.png'
        image_downloader = ImageDownloader(URL_SOURCE)
        image_downloader.go()

        ... and it is done. But a TODO list is still to be done
        
    TODOs:
        - connection errors management
        - content type validation: only imagee
        - destination folder validation: create if does not exist?
        - overrides files?
        - async download 
        - events logger
            - verbosity level
    """

    # current directory path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, url_source=None, file_name='downloaded_image', dest_folder=None):
        self.url_source = url_source
        self.file_name = file_name
        self.dest_folder = dest_folder or self.BASE_DIR

    def _request_resource(self):
        print u'Requesting URL %s' % self.url_source
        req = requests.get(self.url_source)

        if req.status_code != 200:
            err_msg = u'Error requesting resource: HTTP %s %s' % (req.status_code, req.reason)
            raise RequestException(err_msg)

        return req

    def __write_resource_from_request(self, req):
        file_name = '%s.jpg' % self.file_name

        file_path = os.path.join(self.dest_folder, file_name)

        print u'Writing %s' % file_name
        with iopen(file_path, 'wb') as file:
            file.write(req.content)

    def go(self):
        print 'Downloading to %s' % self.dest_folder
        req = self._request_resource()
        self.__write_resource_from_request(req)


if __name__ == '__main__':
    # Google logo
    URL_SOURCE = 'https://www.google.com.py/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
    image_downloader = ImageDownloader(URL_SOURCE, file_name='google_logo')
    image_downloader.go()
