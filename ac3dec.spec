Summary:	A free AC-3 stream decoder
Summary(pl):	Darmowy dekoder strumieni AC-3
Name:		ac3dec
Version:	0.6.1
Release:	8
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://gusnet.cx/aaron/codecs/ac3/tarballs/%{name}-%{version}.tar.gz
# Source0-md5:	92b8d3af8d0d06318bb2bb04b8093eef
Patch0:		%{name}-make.patch
Patch1:		%{name}-am_fix.patch
Patch2:		%{name}-ppc.patch
Patch3:		%{name}-fixbuild.patch
URL:		http://gusnet.cx/aaron/codecs/ac3/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
ExcludeArch:	amd64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ac3dec is a free AC-3 stream decoder.

%description -l pl
ac3dec jest darmowym dekoderem strumieni AC-3.

%package devel
Summary:	Header file required to build programs using ac3dec library
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce ac3dec
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files required to build programs using ac3dec library

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
biblioteki ac3dec.

%package static
Summary:	Static ac3dec library
Summary(pl):	Statyczna biblioteka ac3dec
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static ac3dec library.

%description static -l pl
Statyczna biblioteka ac3dec.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
cp -f /usr/share/automake/config.sub .
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
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
%doc TODO README Change*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ac3

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
