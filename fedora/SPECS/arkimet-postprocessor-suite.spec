Name:           arkimet-postprocessor-suite
Version:        0.1
Release:        1%{?dist}
Summary:        Suite of Arkimet postprocessors
Group:          Applications/Meteo
License:        GPL
URL:            https://github.com/ARPA-SIMC/arkimet-postprocessor-suite
Source:         https://github.com/arpa-simc/%{name}/archive/v%{version}-%{release}.tar.gz#/%{name}-%{version}-%{release}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  arkimet libsim pandoc
BuildArch:      noarch

%description
Suite of Arkimet postprocessors

* subarea
* singlepoint


%prep
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


%package subarea
Summary: Crop a subarea of a GRIB file
Requires: arkimet libsim


%description subarea
Crop a subarea of a GRIB file


%files subarea
%defattr(-,root,root,-)
%{_libdir}/arkimet/subarea
%dir %{_datadir}/doc/%{name}
%doc %{_mandir}/man7/arkimet-postprocess-subarea.7.gz
%doc %{_datadir}/doc/%{name}/arkimet-postprocess-subarea.7.md
%doc %{_datadir}/doc/%{name}/arkimet-postprocess-subarea.7.html


%package singlepoint
Summary: Extract a single point from a GRIB file
Requires: arkimet libsim bufr2json


%description singlepoint
Extract a single point from a GRIB file in various formats

%files singlepoint
%{_libdir}/arkimet/singlepoint
%dir %{_datadir}/doc/%{name}
%doc %{_mandir}/man7/arkimet-postprocess-singlepoint.7.gz
%doc %{_datadir}/doc/%{name}/arkimet-postprocess-singlepoint.7.md
%doc %{_datadir}/doc/%{name}/arkimet-postprocess-singlepoint.7.html

%changelog
* Fri Nov 13 2015 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.1-1
- First package
