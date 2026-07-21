#%%
import os
import numpy as np
import matplotlib.pyplot as plt
import pydicom

#%%
# For the get vol data function would be
def get_vol_data_pydicom(directory):
    """
    Extract a volume from a dictory with a dicom for each 
    individual slice of the 3D scan
    """    
    # Init the dicoms variable 
    dicoms = [] 

    # Set up the paths to search 
    dicom_names = os.listdir(directory)
    
    # Extract only dicoms of the right type 
    for dicom_name in dicom_names:
        dicom_path = os.path.join(directory, dicom_name)
        ds = pydicom.dcmread(dicom_path)
        
        ds_type = ds.file_meta.MediaStorageSOPClassUID.name
        if ds_type == 'MR Image Storage':
            dicoms.append(ds)
        else:
            print(f"Skipping file: {dicom_name}")
            print(f"DS Type: {ds_type}")
    
    dicoms = sorted(dicoms,key=lambda ds: float(ds.SliceLocation))
    slices = [ds.pixel_array for ds in dicoms]
    volume = np.stack(slices)

    print(f"Found {len(slices)} slices")
    return (volume)

#%%
root_directory = "HippocampalMRISlices"
patient_folders = sorted(os.listdir(root_directory))
patient_num = 1

directory = os.path.join(root_directory, patient_folders[patient_num])

volume = get_vol_data_pydicom(directory)
#%%
from matplotlib.widgets import Slider, Button

plt.close('all') # close previous plots
fig, ax = plt.subplots() 
plt.subplots_adjust(bottom=0.35) 
ax_order = plt.axes([0.25, 0.1, 0.65, 0.03]) # to create space for the slider
ax.imshow(volume[0,:,:])

num_slices = volume.shape[0]
order_slider = Slider(ax_order, 'Order', 0, num_slices -1, valinit=0, valstep=1, color='lightblue') # the slider

def update(val):
    '''update function'''
    ord = order_slider.val
    ax.imshow(volume[ord, :,:])
    fig.canvas.draw_idle()

order_slider.on_changed(update)

ax_reset = fig.add_axes((0.8, 0.025, 0.1, 0.04)) # to create space for the reset button
button = Button(ax_reset, 'Reset', hovercolor='0.975')


def reset(event):
    '''for reset button'''
    order_slider.reset()
  
button.on_clicked(reset)

plt.show()
