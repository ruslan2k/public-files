FROM ubuntu:16.04
MAINTAINER Ruslan Karachun <free.changer@gmail.com>

RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN mkdir /root/.ssh
ADD https://raw.githubusercontent.com/ruslan2k/public-files/master/docker/centos-ssh/id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 0700 /root/.ssh
RUN chmod 0600 /root/.ssh/authorized_keys

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
