FROM kenpu/base:latest

ENV LC_ALL en_US.UTF-8
RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && \
    dpkg-reconfigure -f noniterative tzdata
ENV TZ="America/New_York"
RUN apt-get install -yq jq

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

RUN apt-get update && apt-get install -yq postgresql-client

#
# Quarto
#
RUN cd /tmp \
    && wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.340/quarto-1.3.340-linux-amd64.tar.gz \
    && tar -C /opt -xzf quarto-1.3.340-linux-amd64.tar.gz \
    && ln -s /opt/quarto-1.3.340/bin/quarto /bin/quarto

RUN pip install --upgrade nbconvert==7.2.1 mistune==2.0.4
RUN pip install jupyterlab-quarto
RUN pip install jupyter-server-proxy && jupyter serverextension enable --sys-prefix jupyter_server_proxy
RUN pip install gitpython 
RUN quarto install tinytex


#
# Pytorch
#
RUN pip install torch
RUN pip install torchaudio torchtext torchvision torchmetrics
RUN pip install lightning
RUN pip install -q -U bitsandbytes
RUN pip install -q -U git+https://github.com/huggingface/transformers.git
RUN pip install -q -U git+https://github.com/huggingface/peft.git
RUN pip install -q -U git+https://github.com/huggingface/accelerate.git

# Tools
COPY ./bash.bashrc /etc/
COPY ./profile /etc/
COPY ./tmux.conf /etc/tmux.conf

