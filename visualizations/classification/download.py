#!/usr/bin/env python3

# Copyright (c) 2017 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""Download big files from Google Drive."""

import shutil
import sys
import requests
import os
import time
import urllib.request
import zipfile



def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)

    if percent % 5 == 0:
        sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
            (percent, progress_size / (1024 * 1024), speed, duration))
        sys.stdout.flush()

def sizeof_fmt(num, suffix='B'):
    # https://stackoverflow.com/a/1094933/5308925
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1000.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1000.0
    return "%.2f%s%s" % (num, 'Yi', suffix)


def print_status(destination, progress):
    message = "Downloading %s...    %s" % (destination, sizeof_fmt(progress))
    empty_space = shutil.get_terminal_size((80, 20)).columns - len(message)
    sys.stdout.write('\r' + message + empty_space * ' ')
    sys.stdout.flush()


def download_file_from_google_drive(id, destination):
    # https://stackoverflow.com/a/39225039/5308925

    def save_response_content(response, destination):
        chunk_size = 32768
        written_size = 0

        with open(destination, "wb") as f:
            for chunk in response.iter_content(chunk_size):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    written_size += chunk_size
                    print_status(destination, written_size)
        print('Done.')

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    url = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(url, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(url, params=params, stream=True)

    save_response_content(response, destination)


def download_contents():

    import os, ssl
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    # download model
    model_path = './cls_model.pth'
    if os.path.isfile(model_path):
        print('Model file already downloaded in', model_path)
    else:
        download_file_from_google_drive('1WWf5B5fmik5_P1dwxltJ-atRkYeCcCC5', './cls_model.pth')

    # download dataset
    dataset_path = './shapenetcore_partanno_segmentation_benchmark_v0.zip'
    if os.path.isfile(dataset_path):
        print('Dataset file already downloaded in', dataset_path)
    else:
        dataset_url = 'https://shapenet.cs.stanford.edu/ericyi/shapenetcore_partanno_segmentation_benchmark_v0.zip'
        urllib.request.urlretrieve(dataset_url, os.path.basename(dataset_url), reporthook)

        # unzip dataset
        zip_ref = zipfile.ZipFile(os.path.basename(dataset_url), 'r')
        zip_ref.extractall('.')
        zip_ref.close()

        print('Now unzipping...Wait for 2 minutes ish...!')
    return 0

if __name__ == '__main__':
    download_contents()
