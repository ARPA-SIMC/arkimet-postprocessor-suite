Name:           arkimet-postprocessor-suite
Version:        0.1
Release:        1
Summary:        Suite of Arkimet postprocessors
Group:          Applications/Meteo
License:        GPL
URL:            https://github.com/ARPA-SIMC/arkimet-postprocessor-suite
Source:         https://github.com/arpa-simc/%{name}/archive/v%{version}-%{release}.tar.gz#/%{name}-%{version}-%{release}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  arkimet libsim dballe meteo-vm2-utils bufr2json
Requires:       arkimet libsim dballe meteo-vm2-utils bufr2json
BuildArch:      noarch

%description
Suite of Arkimet postprocessors

* subarea
* singlepoint
* bufr


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

%files subarea
%defattr(-,root,root,-)
%{_libdir}/arkimet/subarea
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/subarea.md

%{_libdir}/arkimet/singlepoint
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/singlepoint.md

%{_libdir}/arkimet/bufr
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/bufr.md


%changelog
* Fri Nov 13 2015 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.1-1
- First package
