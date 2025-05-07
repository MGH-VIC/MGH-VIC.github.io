.. miaaim documentation master file, created by
   sphinx-quickstart on Wed May  5 10:42:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


MIAAIM: multi-modal image alignment and analysis by information manifolds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: twocol

   .. container:: leftside

      .. figure:: images/2025_Figure1.png
         :width: 80%

   .. container:: rightside

      MIAAIM is a software to align and analyze multi-omics tissue imaging data.
      The workflow includes high-dimensional image compression and preprocessing,
      image registration,
      tissue state modeling, and domain transfer.

      MIAAIM was developed by
      `Joshua Hess <https://github.com/JoshuaHess12>`_ at
      the `Vaccine and Immunotherapy Center at MGB <http://advancingcures.org>`_
      in the labs of `Dr. Ruxandra Sîrbulescu <http://advancingcures.org/sirbulescu-lab/>`_
      and `Dr. Patrick Reeves <http://advancingcures.org/reeves-lab/>`_.

      Before using this software, please read the relevant background for each
      workflow in the pipeline in the :ref:`Workflows <Workflows to Workflows>` section.
      For a complete description of the project, check our preprint.


.. toctree::
   :maxdepth: 3
   :caption: User Guide / Tutorials

   installation
   quick_start
   directory
   workflows
   parameters
   contributing

.. toctree::
   :maxdepth: 2
   :caption: Quick Start Notebooks

   01_HDI_IMC_Preprocessing
   02_1_MSI_ExportHDF5
   02_2_HDI_MSI_Preprocess
   03_HE_preprocess_TIFF
   04_ilastikTraining
   05_ilastikHeadless
   06_HDI_Registration
   07_HDI_Segmentation
   08_Quant

.. toctree::
   :maxdepth: 2
   :caption: MIAAIM in Python

   python
   python-workflows

.. toctree::
   :maxdepth: 2
   :caption: Background on MIAAIM

   elastix

.. toctree::
   :maxdepth: 2
   :caption: Contributing

   contributing

.. toctree::
   :maxdepth: 2
   :caption: Contact

   contact

.. toctree::
   :maxdepth: 2
   :caption: Funding

   funding

.. toctree::
   :maxdepth: 2
   :caption: License

   license

.. toctree::
   :maxdepth: 2
   :caption: Acknowledgements

   acknowledgements


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
