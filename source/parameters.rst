.. _Parameter Reference to Parameter Reference:

Parameter Reference
===================
Here we provide parameter options for each workflow in MIAAIM. Commands are added
in the

.. note::
      For up-to-date references of parameters for each workflow, visit the
      :ref:`Workflow GitHub Repositories <Workflow GitHub Repositories to Workflow GitHub Repositories>`

.. _HDIprep to hdiprep parameters:

HDIprep
-------
Here we list the optional input parameters that can be supplied to the HDIprep
workflow through the YAML parameter file. These parameters are passed to both
the fixed and moving images with separate YAML files.

.. csv-table:: --fixed-pars and --moving-pars
      :header: YAML Step / Flag, Description, Options

      Step : :code:`ImportOptions`, options for reading image data, ""
      :code:`flatten:`, flatten pixels for dimension reduction, "| Options:
      | :code:`True` if compressing images
      | :code:`False` if histology processing"

      :code:`subsample:`, subsample image for compression, "| Options:
      | :code:`True` if subsampling pixels
      | :code:`False` if no subsampling"

      :code:`method:`, subsampling method , "| Options:
      | :code:`'grid'` for uniform grid sampling
      | :code:`'random'` for random coordinate sampling
      | :code:`'pseudo_random'` for random sampling
      | initalized by uniform grids"

      :code:`grid_spacing:`, x and y grid spacing for sampling, "| Options:
      | Example : :code:`(5,5)`"

      :code:`n:`, :code:`random` / :code:`pseudo_random` sampling fraction , "| Options:
      | Ex. : :code:`0.15`"

      :code:`masks:`, TIFF mask to compress image portion, "| Options:
      | Ex. : :code:`'moving-mask.tiff'`"

      :code:`save_mem:`, reduce memory footprint, "| Options:
      | :code:`True` for large image compression
      | :code:`False` if interactive Python code"

      Step : :code:`ProcessingSteps`, steps to process images, ""

      :code:`- RunOptimalUMAP`, steady-state compression, "| Options:
      | :code:`n_neighbors` nearest neighbors (Ex. :code:`15`)
      | :code:`landmarks` spectral centroids (Ex. :code:`3000`)
      | :code:`metric` UMAP metric (Ex. :code:`euclidean`)
      | :code:`random_state` seed (Ex. :code:`1`)
      | :code:`dim_range` range of dimensionalities (Ex. :code:`(1,10)`)
      | :code:`**kwargs` kwargs passed to `UMAP <https://github.com/lmcinnes/umap>`_"

      :code:`- RunUMAP`, UMAP compression , ":code:`**kwargs` passed to `UMAP <https://github.com/lmcinnes/umap>`_"

      :code:`- RunOptimalParametricUMAP`, neural network steady state UMAP, "| Options:
      | :code:`n_neighbors` nearest neighbors (Ex. :code:`15`)
      | :code:`landmarks` spectral centroids (Ex. :code:`3000`)
      | :code:`metric` UMAP metric (Ex. :code:`euclidean`)
      | :code:`random_state` seed (Ex. :code:`1`)
      | :code:`dim_range` range of dimensionalities (Ex. :code:`(1,10)`)
      | :code:`**kwargs` kwargs passed to `UMAP <https://github.com/lmcinnes/umap>`_"

      :code:`- RunParametricUMAP`, neural network UMAP compression, ":code:`**kwargs` passed to `UMAP <https://github.com/lmcinnes/umap>`_"

      :code:`- SpatiallyMapUMAP`, reconstruct compressed image, ""

      :code:`- ApplyManualMask`, apply manual mask, "| Options:
      | mask accessed from :code:`ImportOptions`"

      :code:`- MedianFilter`, median filter (remove salt and pepper noise), "| Options:
      | :code:`filter_size` filter disk size (Ex. :code:`15`)
      | :code:`parallel` use parallel processing (:code:`True` or :code:`False`)"

      :code:`- Threshold`, create mask by thresholding , "| Options:
      | :code:`type` threshold type (:code:`'manual' or 'otsu'`)
      | :code:`thresh_value` manual threshold value (Ex. :code:`1.0`)
      | :code:`correction` multiply threshold for stringent results (Ex. :code:`1.2`)"

      :code:`- Open`, morphological closing on mask, "| Options:
      | :code:`disk_size` filter disk size (Ex. :code:`15`)
      | :code:`parallel` use parallel processing (:code:`True` or :code:`False`)"

      :code:`- Close`, resume workflow with cached results, "| Options:
      | :code:`disk_size` filter disk size (Ex. :code:`15`)
      | :code:`parallel` use parallel processing (:code:`True` or :code:`False`)"

      :code:`- Fill`, Fill holes in mask, ""

      :code:`- ApplyMask`, apply mask to image for final processing step, ""

      :code:`- NonzeroBox`, extract image bounding box (for controlled padding), ""

      Step : :code:`ExportNifti1`, export in the NIfTI format, "| Options:
      | :code:`padding` pad to add to images image (Ex. :code:`(50,50)`)
      | :code:`target_size` resize image before padding (Ex. :code:`(1000,1050)`)"

.. _HDIreg to hdireg parameters:

HDIreg
------

.. csv-table:: ---elastix-pars
      :header: Flag, Description, Options

      :code:`--p`, parameter file(s) for registration, ":code:`*.txt`"
      :code:`--mp`, moving image landmark points, ":code:`*.txt`"
      :code:`--fp`, fixed image landmark points, ":code:`*.txt`"
      :code:`--fMask`, fixed image mask, ":code:`*.tif`"

.. tip::
      You can chain together multiple elastix parameter files by
      supplying multiple inputs. For example, an affine registration followed
      by a nonlinear one can be implemented as :code:`--p affine.txt nonlinear.txt` where
      :code:`affine.txt` and :code:`nonlinear.txt` are your parameter files.


.. csv-table:: ---transformix-pars
      :header: Flag, Description, Options

      :code:`--tps`, transformation parameter file(s), ":code:`*.txt`"
      :code:`--target_size`, resize image before padding, "(Ex. :code:`(1000,1050)`)"
      :code:`--pad`, pad to add to images image, "(Ex. :code:`(50,50)`)"
      :code:`--trim`, number of pixels to trim off edges, "(Ex. :code:`50`)"
      :code:`--out_ext`, aligned image final file format, "| :code:`.ome.tiff`
      | :code:`.ome.tif`
      | :code:`.tiff`
      | :code:`.hdf5`
      | :code:`.h5`
      | :code:`.nii`"

.. tip::
      If you use multiple registration parameter files in elastix, then you
      should add both sets of transformation parameters to the transformix command
      to receive final results. From the above example, two transformation parameter
      files would be exported -- :code:`TransformationParameters.0.txt` for the
      affine registration and :code:`TransformationParameters.1.txt` for nonlinear.
      Your transformix call should be :code:`--tps TransformationParameters.0.txt TransformationParameters.1.txt`
