%global debug_package %{nil}
%global releaseno 2
# Note: define _srcarchivename in Travis build only.
%{!?srcarchivename: %global srcarchivename %{name}-%{version}-%{releaseno}}

Name:           arkimet-postprocessor-suite
Version:        0.1
Release:        %{releaseno}%{?dist}
Summary:        arkimet postprocessor suite
License:        GPLv2+
URL:            https://github.com/arpa-simc/%{name}
Source0:        https://github.com/arpa-simc/%{name}/archive/v%{version}-%{releaseno}.tar.gz#/%{srcarchivename}.tar.gz
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  arkimet
BuildRequires:  meteo-vm2-utils
BuildRequires:  dballe
BuildRequires:  libsim
BuildRequires:  bufr2json
BuildRequires:  asciidoc
BuildRequires:  dba_qcfilter
Requires:       arkimet
Requires:       meteo-vm2
Requires:       dballe
Requires:       libsim
Requires:       bufr2json
Requires:       dba_qcfilter

%description
Arkimet postrprocessor suite


%prep
%setup -q -n %{srcarchivename}


%build
autoreconf -ifv
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%defattr(-,root,root,-)
%doc %{_mandir}/man7/*
%doc %{_docdir}/%{name}/*
%{_libdir}/arkimet/*
%{_libexecdir}/%{name}/*

%changelog
* Fri Mar 20 2020 Emanuele Di Giacomo <edigiacomo@arpae.it> - 0.1-2
- Updated requirements

* Thu Jun  7 2018 Emanuele Di Giacomo <edigiacomo@arpae.it> - 0.1-1
- First release
