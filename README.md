# DICOM-project1
This repository contains the first DICOM coding exercises assigned to me by my SEPNet supervisor.  
The coding exercise goes as follows:

1. Can you view one of the 3D datasets in the axial, sagittal and coronal planes?
2. **BONUS** Can create a slider to view all the image slices for a patient?

The file **test.py** contains the code for my initial answer to the first question. 
The file **test.ipynb** contains answers to the first and bonus questions with a lot of unnecessary cells.

**task1.ipynb** contains my inital answer to the first question and feedback from my supervisor.
**bonus.py** and **bonus.ipynb** are the answers to the bonus question.

Each coding file contains a section where the code combs through the folder containing the DICOM files. Simply change the directory or filepath value when running the code on another device.

The libraries that need to be imported for all the code to work is as follows:
1. \verb|os|
2. \verb|numpy| as \verb|np|
3. \verb|pydicom|
4. \verb|json|
5. \verb|matplotlib.pyplot| as \verb|plt|
6. \verb|imageio|

