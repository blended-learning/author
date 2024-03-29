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
# Scala kernel
#
# @TODO: should move up next to Kotlin kernel
RUN curl -Lo /usr/bin/coursier https://git.io/coursier-cli && chmod +x /usr/bin/coursier
ENV ALMOND_VERSION="0.10.3"
ENV SCALA_VERSION=2.12.12
RUN mkdir -p /usr/share/coursier/cache
ENV COURSIER_CACHE=/usr/share/coursier/cache
RUN coursier launch \
          --fork almond:${ALMOND_VERSION} \
          --scala ${SCALA_VERSION} \
          -- --install --jupyter-path /opt/miniconda3/share/jupyter/kernels
RUN chmod -R a+rx /usr/share/coursier
RUN chmod -R a+rx /opt/miniconda3/share/jupyter/kernels

#
# @TODO: fix timezone
#
RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && \
    dpkg-reconfigure -f noniterative tzdata
ENV TZ="America/New_York"

#
# @TODO: lightning
#
RUN pip install lightning
RUN apt-get install -yq jq

RUN pip install ortools
RUN apt-get update && apt-get install -yq postgresql-client
RUN pip install psycopg2-binary asyncpg

# Tools
COPY ./bash.bashrc /etc/
COPY ./profile /etc/
COPY ./tmux.conf /etc/tmux.conf

