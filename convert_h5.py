import h5py
import shutil
import numpy as np
import sys

def convert_attrs(f):
    for key in f:
        s = f[key]
        if isinstance(s, str):
            f[key] = np.string_(s)
    
def convert_groups(f):
    convert_attrs(f.attrs)
    for key in f:
        s = f[key]
        if isinstance(s,str):
            f[key] = np.string_(s)
        elif isinstance(s, h5py.Group):
            convert_groups(f[key])
            
def convert_h5py(file_in, file_out=None):
    if file_out:
        shutil.copy(file_in, file_out)
    else:
        file_out = file_in
    f = h5py.File(file_out, 'a')
    convert_groups(f)
    f.close()

if __name__ == "__main__":
    if len(sys.argv) in [2, 3]:
        convert_h5py(sys.argv[1], sys.argv[2:])
    else:
        print("Usage: convert_h5py file_in [file_out]")
