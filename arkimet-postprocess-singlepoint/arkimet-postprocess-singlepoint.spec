Name:           arkimet-postprocess-singlepoint
Version:        0.3
Release:        2%{?dist}
Summary:        Singlepoint postprocessor for arkimet
Group:          Applications/Meteo
License:        GPL
URL:            https://github.com/ARPA-SIMC/arkimet-postprocessor-suite
Vendor:         Emanuele Di Giacomo <edigiacomo@arpa.emr.it>
Packager:       Daniele Branchini <dbranchini@arpa.emr.it>
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  arkimet libsim asciidoc bufr2json
Requires:       arkimet libsim bufr2json
BuildArch:      noarch

%description
Singlepoint postprocessor for arkimet


%prep
rm -rf %{buildroot}
%setup -q


%build
%configure
make %{?_smp_mflags}

%check
make check

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/arkimet/singlepoint


%package doc
Summary:        Documentation for arkimet-postprocess-singlepoint

%description doc
Documentation for arkimet-postprocess-singlepoint

%files doc
%doc %{_mandir}/man7/*
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/*

%changelog
* Tue Nov 24 2014 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.3-2%{dist}
- Documentation files
* Wed Feb 19 2014 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.3-1%{dist}
- BUFR, CREX and JSON formats
- nearest point and bilinear interpolation
