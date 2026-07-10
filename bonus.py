### very slow slider
import os
import numpy as np
import matplotlib.pyplot as plt
import pydicom
%matplotlib qt


def dictionary(directory):
    '''returns a dictionary
    key = order of the dicom file (integer starting from 0)
    value = pixel data of the dicom file
    '''
    dicom_dict = {}
    dicom_order = []
    counter = 0
    for entry in os.scandir(directory): # looping through all the files in the directory
        if 'MR.1.2.246' in str(entry):
            # order = int(str(entry)[30:37]) # was used previously as a 
            ds = pydicom.dcmread(entry.path) # reading the dicom files
            dicom_dict[counter] = ds.pixel_array # appending the empty dictionary
            dicom_order.append(counter)
        counter += 1
    return dicom_order, dicom_dict

directory = # the folder directory, i.e.: r'C:\Users\slaar\Desktop\project\HippocampalMRISlices\01'
dicom_dict = dictionary(directory)[1]
dicom_order = dictionary(directory)[0]

from matplotlib.widgets import Slider, Button
import IPython.display as display 

plt.close('all') # close previous plots
fig, ax = plt.subplots() 
plt.subplots_adjust(bottom=0.35) 
ax_order = plt.axes([0.25, 0.1, 0.65, 0.03]) # to create space for the slider
ax.imshow(dicom_dict[min(dicom_order)])

order_slider = Slider(ax_order, 'Order', min(dicom_order), max(dicom_order), valinit=0, valstep=1, color='lightblue') # the slider


def update(val):
    '''update function'''
    ord = order_slider.val
    ax.imshow(dicom_dict[ord])
    fig.canvas.draw_idle()

order_slider.on_changed(update)

ax_reset = fig.add_axes((0.8, 0.025, 0.1, 0.04)) # to create space for the reset button
button = Button(ax_reset, 'Reset', hovercolor='0.975')


def reset(event):
  '''for reset button'''
    order_slider.reset()
button.on_clicked(reset)

plt.show()

