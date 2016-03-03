Name:           arkimet-postprocess-json
Version:        0.12
Release:        1%{?dist}
Summary:        JSON post processor for arkimet

License:        GPLv2+
URL:            https://github.com/ARPA-SIMC/arkimet-postprocessor-suite
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  arkimet
BuildRequires:  libsim
BuildRequires:  meteo-vm2-utils
BuildRequires:  asciidoc source-highlight html2text wget
BuildRequires:  bufr2json
Requires:       arkimet
Requires:       libsim
Requires:       meteo-vm2-utils
Requires:       bufr2json

%description
JSON post processor for arkimet. It supports GRIB1, GRIB2, BUFR and VM2 formats.


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
%dir %{_libexecdir}/%{name}
%{_libdir}/arkimet/json
%{_libexecdir}/%{name}/bufr2chunks
%doc %{_mandir}/man7/*
%doc %{_datadir}/doc/*
%attr(0755,root,root) %{_libexecdir}/%{name}
%attr(0755,root,root) %{_libdir}/arkimet
%attr(0755,root,root) %{_docdir}/%{name}
%attr(0444,root,root) %{_docdir}/%{name}/*

%changelog
* Thu Mar 03 2016 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.12-1
- Do report when converting from VM2 
* Mon Nov 23 2015 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.11-1
- DB-All.e JSON format and optional qcfilter
* Mon Nov 23 2015 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.10-1
- dba_qcfilter
* Tue Jan 29 2014 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.9-2
- noarch
* Mon Apr 22 2013 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.9-1
- bufr2json dependency
* Wed Mar 13 2013 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.8-1
- Options removed
* Mon Mar 04 2013 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.7-1
- Postprocessor options with double dash
* Thu Feb 21 2013 Emanuele Di Giacomo <edigiacomo@arpa.emr.it> - 0.6-2
- Changed attribute names
