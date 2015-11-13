Name:           arkimet-postprocessor-suite
Version:        0.1
Release:        1%{?dist}
Summary:        Suite of Arkimet postprocessors
Group:          Applications/Meteo
License:        GPL
URL:            https://github.com/ARPA-SIMC/arkimet-postprocessor-suite
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  arkimet libsim pandoc
Requires:       arkimet libsim
BuildArch:      noarch

%description
Suite of Arkimet postprocessors

* subarea


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
%{_libdir}/arkimet/subarea

%files
%doc %{_mandir}/man7/arkimet-postprocess-subarea.7.gz
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/arkimet-postprocess-subarea.7.md
%doc %{_datadir}/doc/%{name}/arkimet-postprocess-subarea.7.html

%changelog
* Fri Nov 13 2015 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.1-1
- First package
