Name:           arkimet-postprocess-subarea
Version:        0.2
Release:        2%{?dist}
Summary:        Subarea postprocessor for arkimet
Group:          Applications/Meteo
License:        GPL
URL:            http://www.arpa.emr.it/
Vendor:         Emanuele Di Giacomo <edigiacomo@arpa.emr.it>
Packager:       Daniele Branchini <dbranchini@arpa.emr.it>
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  arkimet libsim asciidoc
Requires:       arkimet libsim
BuildArch:      noarch

%description
Subarea postprocessor for arkimet


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

%package doc
Summary:        Documentation for arkimet-postprocess-subarea

%description doc
Documentation for arkimet-postprocess-subarea

%files doc
%doc %{_mandir}/man7/arkimet-postprocess-subarea.7.gz
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/arkimet-postprocess-subarea.7.txt
%doc %{_datadir}/doc/%{name}/arkimet-postprocess-subarea.7.html

%changelog
* Mon Sep 23 2013 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.2-2%{dist}
- Improved postprocessor
