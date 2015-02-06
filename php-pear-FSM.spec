%define		_class		FSM
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.3.1
Release:	6
Summary:	Finite State Machine
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/FSM/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The FSM package provides a simple class that implements a Finite State
Machine.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3mdv2012.0
+ Revision: 741945
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-2
+ Revision: 679314
- mass rebuild

* Thu Feb 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-1
+ Revision: 638144
- 1.3.1

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-5mdv2011.0
+ Revision: 613654
- the mass rebuild of 2010.1 packages

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-4mdv2010.1
+ Revision: 478675
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-3mdv2010.0
+ Revision: 441079
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2009.1
+ Revision: 321967
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1mdv2009.0
+ Revision: 278916
- update to new version 1.3.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-3mdv2009.0
+ Revision: 236832
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.2.4-2mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Nov 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-2mdv2007.0
+ Revision: 83322
- rebuild

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdv2007.0
+ Revision: 81568
- Import php-pear-FSM

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdk
- 1.2.4

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1mdk
- 1.2.3
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdk
- initial Mandriva package (PLD import)

