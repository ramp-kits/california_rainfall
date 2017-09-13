"""Download data after cloning.
Run this once. It will create `data/imgs` and download the images there
using the names `<id>`, where `<id>`s are coming from `data/train.csv` and
`data/test.csv`. If images are properly unzipped in `data/imgs`, you can
delete the zip file `data/imgs.zip` to save space.
"""

import os
import shutil
from subprocess import call

if os.path.exists('data'):
    shutil.rmtree('data')
os.mkdir('data')

url = 'https://storage.ramp.studio/california_rainfall'
variables = ["PSL", "TMQ", "TS", "U_500", "V_500"]
csv_variables = ["precip", "precip_90"]
modes = ["train", "test"]
f_names = []
for mode in modes:
    for var in variables:
        f_names.append("{0}_{1}.nc".format(mode, var))
    for var in csv_variables:
        f_names.append("{0}_{1}.csv".format(mode, var))
for f_name in f_names:
    url_in = '{}/{}'.format(url, f_name)
    f_name_out = os.path.join('data', f_name)
    cmd = 'wget {} --output-document={} --no-check-certificate'.format(
        url_in, f_name_out)
    call(cmd, shell=True)
