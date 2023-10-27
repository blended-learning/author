FROM ubuntu:22.04

#
# Core UNIX
#
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive TZ=America/New_York apt-get install -y tzdata
RUN apt-get update && apt-get install -yq \
    build-essential \
    openssh-server openssh-client \
    git \
    htop \
    tree \
    less \
    vim \
    wget \
    curl \
    unzip \
    tmux \
    sudo \
    jq \
    postgresql-client

# set locale to support UTF-8 codebase of Clojupyter
RUN apt-get install -yq locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen

ENV LC_ALL en_US.UTF-8
RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && \
    dpkg-reconfigure -f noniterative tzdata
ENV TZ="America/New_York"

#
# Core Python
#
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash ./Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -s -b
ENV PATH=/opt/miniconda3/bin:$PATH
RUN rm -f /Miniconda3-latest-Linux-x86_64.sh

#
# Jupyter
#

RUN pip install jupyterlab==3.6.3 jupyterhub==3.1.1
RUN cd /tmp && \
    wget -q https://nodejs.org/dist/v14.18.1/node-v14.18.1-linux-x64.tar.xz && \
    tar xvf ./node-v14.18.1-linux-x64.tar.xz && \
    mv node-v14.18.1-linux-x64 /opt/node-v14.18.1-linux-x64

ENV PATH=${PATH}:/opt/node-v14.18.1-linux-x64/bin
RUN npm install -g configurable-http-proxy

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

# Customization
COPY ./start.sh /bin
COPY ./createuser.sh /bin
COPY ./createusers /bin
COPY ./users.default /etc/
COPY ./jupyterhub_config.py /etc/
COPY ./bash.bashrc /etc/
COPY ./profile /etc/
COPY ./tmux.conf /etc/tmux.conf

CMD /bin/start.sh
