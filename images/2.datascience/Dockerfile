FROM kenpu/base:latest

#
# Data Science
#
RUN pip install \
    'altair' \
    'beautifulsoup4' \
    'bokeh' \
    'bottleneck' \
    'cloudpickle' \
    'cython' \
    'dask' \
    'dill' \
    'h5py' \
    'ipympl'\
    'ipywidgets' \
    'matplotlib' \
    'numba' \
    'numexpr' \
    'pandas' \
    'scikit-image' \
    'scikit-learn' \
    'scipy' \
    'seaborn' \
    'sqlalchemy' \
    'statsmodels' \
    'sympy' \
    'widgetsnbextension'\
    'xlrd' \
    ortools \
    psycopg2-binary \
    asyncpg

#
# OpenCV
#
RUN conda install -y -c menpo opencv
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
