# TODO: kernel module (-DAJANTV2_DISABLE_DRIVER=OFF)
Summary:	Open-source library for AJA Video Systems desktop I/O cards
Summary(pl.UTF-8):	Biblioteka o otwartych źródłach do kart we/wy AJA Video Systems
Name:		libajantv2
Version:	17.0.0
%define	gitref	ntv2_%(echo %{version} | tr . _)
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/aja-video/libajantv2/releases
Source0:	https://github.com/aja-video/libajantv2/archive/%{gitref}/%{name}-%{version}.tar.gz
# Source0-md5:	57f7074c8a0653d5df267f55a37d748c
URL:		https://github.com/aja-video/libajantv2
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	cmake >= 3.15
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the open-source SDK for discovering, interrogating and
controlling NTV2 professional video I/O devices from AJA Video
Systems, Inc.

%description -l pl.UTF-8
Ten pakiet zawiera mające otwarte źródła SDK do wykrywania,
badania i sterowania profesjonalnymi urządzeniami wideo NTV2 firmy
AJA Video Systems, Inc.

%package devel
Summary:	Header files for AJA NTV2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AJA NTV2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for AJA NTV2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AJA NTV2.

%prep
%setup -q -n %{name}-%{gitref}

%build
%cmake -B build \
	-DAJA_INSTALL_CMAKE=OFF \
	-DAJA_INSTALL_MISC=OFF \
	-DAJANTV2_BUILD_SHARED=ON \
	-DAJANTV2_DISABLE_DRIVER=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
%{__mv} $RPM_BUILD_ROOT%{_prefix}/libajantv2 $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/logreader
%attr(755,root,root) %{_bindir}/ntv2*
%attr(755,root,root) %{_bindir}/pciwhacker
%attr(755,root,root) %{_bindir}/regio
%attr(755,root,root) %{_bindir}/supportlog
%attr(755,root,root) %{_libdir}/libajantv2.so.17.0.0.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libajantv2.so
%{_includedir}/libajantv2
