FROM kenpu/base:latest

#
# Data Science
#
RUN mamba install --quiet --yes \
    'altair' \
    'beautifulsoup4' \
    'bokeh' \
    'bottleneck' \
    'cloudpickle' \
    'conda-forge::blas=*=openblas' \
    'cython' \
    'dask' \
    'dill' \
    'h5py' \
    'ipympl'\
    'ipywidgets' \
    'matplotlib-base' \
    'numba' \
    'numexpr' \
    'pandas' \
    'patsy' \
    'protobuf' \
    'pytables' \
    'scikit-image' \
    'scikit-learn' \
    'scipy' \
    'seaborn' \
    'sqlalchemy' \
    'statsmodels' \
    'sympy' \
    'widgetsnbextension'\
    'xlrd' && \
    mamba clean --all -f -y

#
# Java
#
RUN apt-get update \
    && apt-get install -yq openjdk-8-jdk-headless

#
# Clojure Kernel
#
RUN wget -q https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \
    && mv ./lein /bin/lein \
    && chmod a+x /bin/lein

RUN cd /tmp \
    && curl -O https://download.clojure.org/install/linux-install-1.11.1.1273.sh \
    && chmod +x linux-install-1.11.1.1273.sh \
    && ./linux-install-1.11.1.1273.sh

ENV LC_ALL en_US.UTF-8

RUN cd /tmp/ \
    && git clone https://github.com/clojupyter/clojupyter.git \
    && cd clojupyter \
    && make install
    
RUN mv ~/.local/share/jupyter/kernels/clojupyter* /opt/miniconda3/share/jupyter/kernels/clojupyter
COPY clojure.kernel.json /opt/miniconda3/share/jupyter/kernels/clojupyter/kernel.json

#
# Kotlin
#
RUN cd /tmp \
    && wget -q https://github.com/JetBrains/kotlin/releases/download/v1.6.21/kotlin-compiler-1.6.21.zip \
    && unzip kotlin-compiler-1.6.21.zip \
    && mv kotlinc /opt/kotlinc
ENV PATH=${PATH}:/opt/kotlinc/bin
RUN pip install kotlin-jupyter-kernel

#
# Quarto
#
RUN cd /tmp \
    && wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.340/quarto-1.3.340-linux-amd64.tar.gz \
    && tar -C /opt -xzf quarto-1.3.340-linux-amd64.tar.gz \
    && ln -s /opt/quarto-1.3.340/bin/quarto /bin/quarto

#
# Pytorch
#
RUN pip install torch
RUN pip install torchaudio torchtext torchvision torchmetrics
RUN pip install transformers
RUN pip install pytorch-lightning

#
# PATH
#
RUN echo 'export PATH=/opt/miniconda3/bin:$PATH' >> /etc/bash.bashrc

# @TODO
RUN pip install --upgrade nbconvert==7.2.1 mistune==2.0.4
RUN pip install jupyterlab-quarto
RUN pip install jupyter-server-proxy && jupyter serverextension enable --sys-prefix jupyter_server_proxy

