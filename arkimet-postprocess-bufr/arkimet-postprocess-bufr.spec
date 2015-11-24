Name:           arkimet-postprocess-bufr
Version:        0.1
Release:        1%{?dist}
Summary:        BUFR postprocessor for arkimet

License:        GPLv2+
URL:            https://github.com/ARPA-SIMC/arkimet-postprocessor-suite
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  arkimet
BuildRequires:  meteo-vm2-utils
BuildRequires:  dballe
BuildRequires:  asciidoc source-highlight html2text wget
Requires:       arkimet
Requires:       meteo-vm2-utils
Requires:       dballe

%description
BUFR post processor for arkimet. It supports VM2 format.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/arkimet/bufr
%doc %{_mandir}/man7/*
%doc %{_datadir}/doc/*
%attr(0755,root,root) %{_libdir}/arkimet
%attr(0755,root,root) %{_docdir}/%{name}
%attr(0444,root,root) %{_docdir}/%{name}/*

%changelog
* Thu Feb 05 2015 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.1-1
- First version
