FROM centos:7

RUN yum clean all
RUN yum -y install \
    yum-plugin-fastestmirror \
    deltarpm
#RUN yum -y update
RUN yum -y install \
    rpm-build \
    wget \
    openssl \
    libpcre \
    openssl-devel \
    zlib-devel \
    pcre-devel \
    vim-enhanced

RUN yum -y groupinstall 'Development Tools'
