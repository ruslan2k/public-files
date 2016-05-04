FROM debian:7
MAINTAINER Ruslan Karachun <free.changer@gmail.com>

RUN apt-get update
RUN apt-get install -y python sudo
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN mkdir /root/.ssh
ADD id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 0700 /root/.ssh
RUN chmod 0600 /root/.ssh/authorized_keys

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
