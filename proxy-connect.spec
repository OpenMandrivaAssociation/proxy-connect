%define name proxy-connect
%define version 1.95
%define release %mkrel 4

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Establish TCP connection using SOCKS4/5 and HTTP tunnel
URL: http://www.taiyo.co.jp/~gotoh/ssh/connect.html
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
