%include	/usr/lib/rpm/macros.perl

Summary:	A C++ interface to ATK
Name:		atkmm
Version:	2.22.7
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/atkmm/2.22/%{name}-%{version}.tar.xz
# Source0-md5:	fec7db3fc47ba2e0c95d130ec865a236
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	atk-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ interface for ATK library.

%package devel
Summary:	A C++ interface for atk library - header files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
A C++ interface for ATK library - header files.

%package apidocs
Summary:	ATKmm API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
ATKmm API documentation.

%prep
%setup -q

%build
mm-common-prepare
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install	\
	DESTDIR=$RPM_BUILD_ROOT	\
	libdocdir=%{_gtkdocdir}/atkmm-1.6

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libatkmm*.so.?
%attr(755,root,root) %{_libdir}/libatkmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm*.so
%{_includedir}/atkmm-1.6
%{_libdir}/atkmm-1.6
%{_pkgconfigdir}/atkmm*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-1.6

