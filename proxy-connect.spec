

Name: proxy-connect
Version:	100
Release:	1
Summary: Establish TCP connection using SOCKS4/5 and HTTP tunnel
URL: https://www.taiyo.co.jp/~gotoh/ssh/connect.html
Group: Networking/Other
License: GPL
Source0: connect.c
Source1: connect.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
connect-proxy is a simple relaying command to make TCP network connection
via SOCKS or https proxies.
It is mainly intended to be used as proxy command of OpenSSH.

%prep
rm -rf %name
mkdir %name
cd %name
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
cd %name
gcc -o %name connect.c

%install
cd %name
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
cp proxy-connect ${RPM_BUILD_ROOT}%{_bindir}
chmod 0755 ${RPM_BUILD_ROOT}%{_bindir}/%name

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc proxy-connect/connect.html
%{_bindir}/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.95-5mdv2010.0
+ Revision: 430808
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.95-4mdv2009.0
+ Revision: 259297
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.95-3mdv2009.0
+ Revision: 247225
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.95-1mdv2008.1
+ Revision: 140737
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 27 2007 Pascal Terjan <pterjan@mandriva.org> 1.95-1mdv2008.0
+ Revision: 31653
- Import proxy-connect



* Mon Oct 31 2005 Pascal Terjan <pterjan@zarb.org> 1.95-1mdk
- first Mandriva version (description and name comme from Debian)
