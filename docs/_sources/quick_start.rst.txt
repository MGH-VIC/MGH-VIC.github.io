.. _quick start to quick start:

Quick Start
===========

After you have :ref:`installed Nextflow <install to install>` you can
download the latest version of MIAAIM directly from GitHub by typing::

  git clone https://github.com/JoshuaHess12/miaaim.git  # clone MIAAIM repository

If you have already cloned MIAAIM from GitHub, ensure that you have
the latest version by entering the directory where you are storing MIAAIM and typing
:code:`git pull`

MIAAIM currently contains one prototype use case with pre-configured parameters for
multi-modal image registration.


TMA013
^^^^^^^^^^^^^

TMA013 is a coupled MALDI-TOF mass spectrometry imaging (MSI) and Imaging Mass Cytometry (IMC) data
set from a prostate tumor biopsy. In this example, the MSI dataset is
considered the "moving" image, and the IMC data set is the "fixed" image.
Run through this example workflow by following the following steps.

.. warning::
    Executing all steps for TMA013 will require you to have ~5GB of free
    space on your computer.

Download Data
-------------

1. Go to the link below to download the data and place the contents to your current working
directory. You should be able to inspect the contents of the :code:`input` folder
to confirm that the download was successful.

::

https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YU6V7E

.. note::
    If you are using a larger workstation consider checking out the
    :ref:`Configuration <Configs to Configs>` to allocate more
    resources for your computations. With the preset files, you can
    add :code:`-profile medium_multi` to the following steps to use more computing
    resources.

Image Preprocessing
-------------------

2. The first step of the pipeline is processing each image so that they can
be aligned later in the pipeline. To process the images for TMA013,
reference and run the following jupyter notebooks:

::

01_HDI_Preprocessing.ipynb

02_1_MSI_ExportHDF5.ipynb

02_2_HDI_MSI_Preprocess.ipynb

03_HE_preprocess_TIFF.ipynb

Manual Image Registration
------------------
3. If manual image registration is necessary, follow the following steps using ImageJ
to create a csv file containing landmark points

- Load images to register into ImageJ
- Use the Multi-Point Tool (7th icon from the left in a standard install of ImageJ that contains 5 crosshairs) to select landmarks between images
- One image at a time, create a summary of the point selections with *ctrl + m* and export these points as a .csv file


Image Registration
------------------
4. After processing each of the images, use the following jupyter notebooks/python scripts to register
the moving image to the fixed image:

::

04_1_ilastikTraining.ipynb

04_2_ilastikHeadless.ipynb

05_HDI_Registration.py

Image Segmentation
------------------
5. After registering the images, perform nuclei and membrane-based segmentation and quantile scaling with the following jupyter notebook:

::

06_HDI_Segmentation.ipynb

07_1_Quant.ipynb
