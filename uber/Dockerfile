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
    'xlrd'

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
# Quarto
#
RUN pip install --upgrade nbconvert==7.2.1 mistune==2.0.4
RUN pip install jupyterlab-quarto
RUN pip install jupyter-server-proxy && jupyter serverextension enable --sys-prefix jupyter_server_proxy
# @TODO
RUN pip install gitpython 
RUN pip install jupyterlab-mathjax3
RUN quarto install tinytex

#
# @TODO: fix timezone
#
RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && \
    dpkg-reconfigure -f noniterative tzdata
ENV TZ="America/New_York"

# Tools
COPY ./bash.bashrc /etc/
COPY ./profile /etc/
COPY ./repos.json /etc/repos.json
COPY ./github_setup.py /bin/github_setup
