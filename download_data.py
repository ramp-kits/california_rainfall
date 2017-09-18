"""Download data after cloning.
Run this once. It will create `data/imgs` and download the images there
using the names `<id>`, where `<id>`s are coming from `data/train.csv` and
`data/test.csv`. If images are properly unzipped in `data/imgs`, you can
delete the zip file `data/imgs.zip` to save space.
"""

import os
import shutil
from subprocess import call
from os.path import exists, join
import ssl 
import requests

if os.path.exists('data'):
    data_files = os.listdir('data')
    for data_file in data_files:
        if ".nc" in data_file:
            os.remove(join('data', data_file))
if not exists("data"):
    os.mkdir('data')

url = 'https://storage.ramp.studio/california_rainfall'
variables = ["PSL", "TMQ", "TS", "U_500", "V_500"]
modes = ["train", "test"]
f_names = []
for mode in modes:
    for var in variables:
        f_names.append("{0}_{1}.nc".format(mode, var))
for f_name in f_names:
    print(f_name)
    url_in = '{}/{}'.format(url, f_name)
    f_name_out = os.path.join('data', f_name)
    #cmd = 'wget {} --output-document={} --no-check-certificate'.format(
    #    url_in, f_name_out)
    #call(cmd, shell=True)
    f_data = requests.get(url_in, verify=False)
    with open(join("data", f_name), "wb") as f_file:
        f_file.write(f_data.content)
