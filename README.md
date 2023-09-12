Experiments using python stack with taichi and tensorstore / brainmaps / DVID sources.

### Setup

Base conda with python 3.10
```
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
conda install -c conda-forge jupyterlab
conda install ipykernel
# conda install pytorch from website
pip install tensorstore
pip install taichi
```

### Env variables

Set the following environment variables:

`GRAYSCALE_BUCKET` to reflect a valid tensorstore reference, e.g., a GCS bucket like `gs:my-bucket-name`.

`GOOGLE_APPLICATION_CREDENTIALS` to the GCP credentials JSON file if using Google services.