# Use the docker-matlab-runtime module
# FROM spacetimeanalytics/docker-matlab-runtime. 

# Will have to specify own MCR as run_groupica uses 9.0.1 not 9.1
# Following is copied from docker-matlab-runtime, with R2016b replaced by R2016a
FROM alectolytic/scipy

RUN apk add --update --no-cache g++ gcc libxslt-dev

# FROM python:3.6

ADD requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir /tmp/mcr_installer && \
    cd /tmp/mcr_installer && \
    wget http://ssd.mathworks.com/supportfiles/downloads/R2016a/deployment_files/R2016a/installers/glnxa64/MCR_R2016a_glnxa64_installer.zip && \
    unzip MCR_R2016a_glnxa64_installer.zip && \
    ./install -mode silent -agreeToLicense yes && \
    rm -Rf /tmp/mcr_installer
ENV MCRROOT=/usr/local/MATLAB/MATLAB_Runtime/v901 MCR_CACHE_ROOT=/tmp
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/MATLAB/MATLAB_Runtime/v901/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v901/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v901/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v901/sys/opengl/lib/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v901/sys/java/jre/glnxa64/jre/lib/amd64/native_threads:/usr/local/MATLAB/MATLAB_Runtime/v901/sys/java/jre/glnxa64/jre/lib/amd64/server:/usr/local/MATLAB/MATLAB_Runtime/v901/sys/java/jre/glnxa64/jre/lib/amd64

# Set the working directory
WORKDIR /app

# copy current directory to container
COPY . /app



COPY ./groupicatv4.0b/icatb/nipype-0.10.0/nipype/interfaces/gift /usr/local/lib/python3.6/site-packages/nipype/interfaces/

# Run groupica script
# ./run_groupica.sh /mathworks/home/application/v901
#CMD ["/bin/bash", "run_groupica.sh", "/usr/local/MATLAB/MATLAB_Runtime/v901"]
# CMD ["/bin/bash", "run_groupica.sh", "/usr/local/MATLAB/MATLAB_Runtime/v901"]
