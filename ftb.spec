Summary:	Fault Tolerance Backplance library
Summary(pl.UTF-8):	Biblioteka Fault Tolerance Backplance
Name:		ftb
Version:	0.6.2
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: http://www.mcs.anl.gov/research/cifts/downloads/index.php
Source0:	http://www.mcs.anl.gov/research/cifts/software/%{name}-%{version}.tgz
# Source0-md5:	d79b3dbcfdbfadb372cd4e47811d3048
Patch0:		%{name}-destdir.patch
URL:		http://www.mcs.anl.gov/research/cifts/
BuildRequires:	autoconf >= 2.59
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fault Tolerance Backplance library.

%description -l pl.UTF-8
Biblioteka Fault Tolerance Backplance.

%package devel
Summary:	Header files for FTB library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FTB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FTB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FTB.

%package static
Summary:	Static FTB library
Summary(pl.UTF-8):	Statyczna biblioteka FTB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FTB library.

%description static -l pl.UTF-8
Statyczna biblioteka FTB.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%{__autoheader}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README docs/chapters/{01_FTB_on_Linux.txt,02_TroubleShooting.txt} misc/license.BSD
%attr(755,root,root) %{_sbindir}/ftb_agent
%attr(755,root,root) %{_sbindir}/ftb_database_server
%attr(755,root,root) %{_libdir}/libftb.so

%files devel
%defattr(644,root,root,755)
%doc docs/ftb_developers_guide.pdf
%{_includedir}/libftb.h
%{_includedir}/ftb_*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libftb.a
