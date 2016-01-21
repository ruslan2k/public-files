FROM centos:7

RUN yum clean all
RUN yum -y install \
    yum-plugin-fastestmirror \
    deltarpm
#RUN yum -y update
RUN yum -y install rpm-build
