FROM kenpu/datascience:latest

#
# Torch
#
RUN conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia


#
# Transformers
#
RUN apt-get install -yq git-lfs
RUN pip install \
    transformers==4.27.1 \
    datasets==2.9.0 \
    accelerate==0.17.1 \
    evaluate==0.4.0 \
    tensorboard
RUN pip install peft==0.3.0

# bitsandbytes
RUN pip install bitsandbytes==0.37.1
RUN mkdir -p /usr/local/cuda/lib64 \
    && ln -s /opt/miniconda3/lib/libcudart.so.11.0 /usr/local/cuda/lib64/libcudart.so

# torchtext
RUN pip install torchtext==0.15.2

# lightning
RUN pip install lightning==2.0.1
