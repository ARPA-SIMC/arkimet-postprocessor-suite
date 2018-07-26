%global debug_package %{nil}
%global releaseno 1
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
BuildRequires:  automake
BuildRequires:  arkimet
BuildRequires:  meteo-vm2-utils
BuildRequires:  dballe
BuildRequires:  libsim >= 6.2.0
BuildRequires:  bufr2json
BuildRequires:  asciidoc
Requires:       arkimet
Requires:       meteo-vm2
Requires:       dballe
Requires:       libsim >= 6.2.0
Requires:       bufr2json

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
* Thu Jun  7 2018 Emanuele Di Giacomo <edigiacomo@arpae.it> - 0.1-1
- First release
