import numpy as np
import matplotlib.pyplot as plt
import pydicom
#%matplotlib qt
%matplotlib ipympl

#new

import imageio
def get_vol_data(file_directory):  
    '''a function to get the 3D pixel data from a DICOM file
    '''
    vol_data = imageio.volread(file_directory) 
    return vol_data

def slices(number_of_slice, slice_type, file_directory):
    '''returns the information of the specified slice, to be plotted
    slice_type are defined as 'axial', 'coronal', and 'sagittal' 
    number_of_slice defines the specific slice to be returned
    '''
    vol = get_vol_data(file_directory)
    if slice_type == 'axial':
        return vol[number_of_slice,:,:]
    elif slice_type == 'coronal':
        return vol[:,number_of_slice,:]
    elif slice_type == 'sagittal':
        return vol[:,:,number_of_slice]
    else:
        raise ValueError("Please choose from 'axial', 'coronal', or 'sagittal', and a slice number must be between 0 and 255")

file_directory = # needs to be a r'' string

axial_slice = slices(90, 'axial', file_directory)
saggital_slice = slices(90, 'sagittal', file_directory)
coronal_slice = slices(90, 'coronal', file_directory)


# plotting the MRI images in the plane
plt.close('all') # just to close all the other graphs before this run
plt.figure(figsize=(2,2)) # small because of preference, I used %matplotlib ipympl to expand the graphs
plt.imshow(axial_slice, cmap='gray')
plt.title('Axial slice')
plt.axis('off')
plt.show()

plt.figure(figsize=(2,2))
plt.imshow(coronal_slice, cmap='gray')
plt.title('Coronal Slice')
plt.axis('off')
plt.show()

plt.figure(figsize=(2,2))
plt.imshow(sagittal_slice, cmap='gray') 
plt.title('Sagittal Slice')
plt.axis('off')
plt.show()
