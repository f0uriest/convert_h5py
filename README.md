# Convert H5py

This package performs the simple function of updating the string formatting in saved hdf5 files to be compatible with h5py version 3.

Usage is ``convert_h5py(file_in)``. This will modify the original file in place. Passing in another path as ``file_out`` will first copy the original file before modifying it.

No guarantees, it might corrupt your data / break your computer / destroy the world etc etc. Use at your own risk.
