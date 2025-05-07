.. _quick start to quick start:

Quick Start
===========

If you've installed Docker you can
download the latest docker of MIAAIM directly from docker hub by running::

  docker pull mghvicmiaaim/miaaim  # pull MIAAIM docker

TMA013
^^^^^^^^^^^^^

TMA013 is a coupled MALDI-TOF mass spectrometry imaging (MSI) and Imaging Mass Cytometry (IMC) data
set from a prostate tumor biopsy. In this example, the MSI dataset is
considered the "moving" image, and the IMC data set is the "fixed" image.
Run through this example workflow by following the following steps.

.. warning::
    Executing all steps for TMA013 will require you to have ~10GB of free
    space on your computer.

Download Data
-------------

1. Go to the link below to download the data and place the contents to your current working
directory in a :code:`input` subdirectory. You will need to reference your current working directory as opt in the docker.
::

    https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YU6V7E

Image Preprocessing
-------------------

2. The first step of the pipeline is processing each image so that they can
be aligned later in the pipeline. To process the images for TMA013,
reference and run the following jupyter notebooks. .ipynb versions of these notebooks can be downloaded `here <https://github.com/MGH-VIC/MGH-VIC.github.io/tree/main/source>`_:


`01_HDI_Preprocessing.ipynb <https://mgh-vic.github.io/01_HDI_IMC_Preprocessing.html>`_

`02_1_MSI_ExportHDF5.ipynb <https://mgh-vic.github.io/02_1_MSI_ExportHDF5.html>`_

`02_2_HDI_MSI_Preprocess.ipynb <https://mgh-vic.github.io/02_2_HDI_MSI_Preprocess.html>`_

`03_HE_preprocess_TIFF.ipynb <https://mgh-vic.github.io/03_HE_preprocess_TIFF.html>`_

Manual Image Registration
-------------------------
3. If manual image registration is necessary, follow the following steps using ImageJ
to create a csv file containing landmark points

- Load images to register into ImageJ
- Use the Multi-Point Tool (7th icon from the left in a standard install of ImageJ that contains 5 crosshairs) to select landmarks between images
- One image at a time, create a summary of the point selections with *ctrl + m* and export these points as a .csv file


Image Registration
------------------
4. After processing each of the images, use the following jupyter notebooks/python scripts to register
the moving image to the fixed image. In the notebooks for 04_ilastik, either of these can be run, depending on if you want to run ilastik headless or not:

`04_ilastikTraining.ipynb <https://mgh-vic.github.io/04_ilastikTraining.html>`_

`05_ilastikHeadless.ipynb <https://mgh-vic.github.io/05_ilastikHeadless.html>`_

`06_HDI_Registration.ipynb <https://mgh-vic.github.io/06_HDI_Registration.html>`_

Image Segmentation
------------------
5. After registering the images, perform nuclei and membrane-based segmentation and quantile scaling with the following jupyter notebook:

`07_1_Quant.ipynb <https://mgh-vic.github.io/07_1_Quant.html>`_

`07_1_Quant.ipynb <https://mgh-vic.github.io/07_1_Quant.html>`_
