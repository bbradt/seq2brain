FROM bvlc/caffe:gpu
RUN apt-get update  
RUN apt-get install -y python-tk python-dev
RUN git clone https://github.com/bbradt/caffe.git
RUN cd caffe && git checkout recurrent