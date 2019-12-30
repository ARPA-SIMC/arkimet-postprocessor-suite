#!/bin/bash
set -ex

image=$1

if [[ $image =~ ^centos:7 ]]
then
    pkgcmd="yum"
    builddep="yum-builddep"
    sed -i '/^tsflags=/d' /etc/yum.conf
    yum install -y epel-release
    yum install -y @buildsys-build
    yum install -y yum-utils
    yum install -y yum-plugin-copr
    yum install -y git
    yum copr enable -y simc/stable epel-7
elif [[ $image =~ ^fedora: || $image =~ ^centos: ]]
then
    pkgcmd="dnf"
    builddep="dnf builddep"
    sed -i '/^tsflags=/d' /etc/dnf/dnf.conf
    if [[ $image =~ ^centos: ]]
    then
        dnf install -y rpm-build make
    else
        dnf install --allowerasing -y @buildsys-build
    fi
    dnf install -y 'dnf-command(builddep)'
    dnf install -y git
    dnf copr enable -y simc/stable
fi

$builddep -y fedora/SPECS/arkimet-postprocessor-suite.spec

if [[ $image =~ ^fedora: || $image =~ ^centos: ]]
then
    pkgname=arkimet-postprocessor-suite-master
    mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
    cp fedora/SPECS/arkimet-postprocessor-suite.spec ~/rpmbuild/SPECS/arkimet-postprocessor-suite.spec
    git archive --prefix=$pkgname/ --format=tar HEAD | gzip -c > ~/rpmbuild/SOURCES/$pkgname.tar.gz
    rpmbuild -ba --define "srcarchivename $pkgname" ~/rpmbuild/SPECS/arkimet-postprocessor-suite.spec
else
    autoreconf -ifv
    ./configure
    make check
fi
