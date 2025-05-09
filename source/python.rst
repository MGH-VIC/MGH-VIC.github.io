.. _Python to Python:

Installation
============
MIAAIM's workflows can also be run in Python to allow for more user flexibility with
custom workflow creation. To install `MIAAIM in Python
<https://github.com/JoshuaHess12/miaaim-python>`_, follow these steps:

You can install MIAAIM in Python using either the miaaim-python Docker container,
which could allow for complete workflow
reproducibility, or you can install the package into your environment with pip.

Dependencies
^^^^^^^^^^^^
MIAAIM utilizes the `Elastix <https://elastix.lumc.nl>`_ library for image
registration computations, which is written in the C++ language.
For this reason, we recommend running your workflows with the MIAAIM Python
package inside of a Docker container, which we have created to automatically
include Elastix. You can still run MIAAIM, however, if you would rather stick
with installing packages via pip, you will just need to install Elastix separately.
These two options for installing MIAAIM are outlined below:

Usage without Docker / Install with Pip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are unable to use Docker on your machine, then you can still use MIAAIM:

1. `download <https://github.com/SuperElastix/elastix/releases/tag/5.0.1>`_ the latest version of Elastix.

2. Make Elastix accessible to your `$PATH` environment (Ex. on a Mac, access your
:code:`.bash_profile` and add :code:`export PATH=~/elastix-latest/bin:$PATH` and
:code:`export DYLD_LIBRARY_PATH=~/elastix-latest/lib:$DYLD_LIBRARY_PATH`)

3. Run the following command to install MIAAIM on your machine:

::

   pip install miaaim-python  # install miaaim


Reproducibility with Pip
^^^^^^^^^^^^^^^^^^^^^^^^
If you are using pip to install MIAAIM, you can reconstruct your working environment easily using
pip as follows:

1. Use pip-freeze to create documentation of installed packages on your machine.
::

   pip freeze > requirements.txt  # create documentation of installed packages

This will create a text file called :code:`requirements.txt` that indicates the
specific packages that you are using. You can then
install the specific packages that were exported into another environment with:

2. Install produced list of packages in another environment.
::

   pip install -r requirements.txt

We have included a :code:`requirements.txt` file in this repository to use for our convenience.

Docker
^^^^^^
MIAAIM's Python implementation is containerized using Docker to enable a reproducible
environment. Inside of this container,
the Python distribution of MIAAIM is already installed.
It is therefore set up so that users can copy scripts and data into it in
order to run analyses that they need.

To get started with MIAAIM using Docker:

1. `Install Docker <https://docs.docker.com/get-docker/>`_.

2. Ensure that Docker is available to your system using the command :code:`docker images`.

3. Pull the miaaim-python docker container :code:`docker pull joshuahess/miaaim-python:latest`
where :code:`latest` is the version number. This step has taken ~1 minute to complete
on a workstation with the following specifications:

* Processor: Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20 GHz, 2201 Mhz, 10 cores(s), Logical Processor(s)
* Memory: 64 GB RAM

.. note::
   If you are using MIAAIM with Docker, we recommend having a concrete file
   structure for data and code with relative paths so that your script doesn't
   rely on absolute file paths outside of the Docker container.

You can mount your custom scripts and data into the virtual environment as follows:

4. Mount your data and scripts into Docker from your local path (:code:`src-path`)
::

   docker run -it -v /path/to/data:/data joshuahess/miaaim-python:latest bash    # mount data in the "dest-path" folder

Here, we assumed that the folder :code:`data` contains your new script and your input data that goes with it.

5. Run your script (named here :code:`script.py`) from the data folder:
::

   python ./data/scipt.py

.. note::
   Any additional packages that you use to process your data that
   are not included in the docker image will not be found!


HDI Utility Functions (hdi-utils)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The hdi-utils toolbox serves as a base library for MIAAIM to read and write
images to various file formats.
