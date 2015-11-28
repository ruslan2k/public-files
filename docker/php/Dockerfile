FROM fedora

RUN dnf install -y composer

RUN dnf -y install \
    screen \
    tmux \
    make \
    vim

RUN dnf -y install \
    php-pecl-yaml \
    php-mysqlnd \
    php-mcrypt
