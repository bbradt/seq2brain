FROM continuumio/miniconda

RUN apt-get install -y git build-essential

WORKDIR /app

RUN git clone https://github.com/scopeInfinity/Video2Description.git btp_VideoCaption
RUN git clone 'https://github.com/tylin/coco-caption.git' cococaption
RUN apt-get install -y yasm
RUN git clone 'https://github.com/FFmpeg/FFmpeg.git' && \
    cd FFmpeg && \
    ./configure --prefix=~/V2D_local/ --enable-shared && \
    make && \
    make install

RUN export PATH=/home/gagan.cs14/V2D_local/bin:$PATH
RUN export LD_LIBRARY_PATH=$/home/gagan.cs14/V2D_local/lib/:$LD_LIBRARY_PATH

RUN cd btp_VideoCaption && conda env create -f environment.yml

RUN conda install opencv -c conda-forge