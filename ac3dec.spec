Summary:	a free AC-3 stream decoder
Summary(pl):	darmowy dekoder strumieni AC-3
Name:		ac3dec
Version:	0.6.1
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://gusnet.cx/aaron/codecs/tarballs/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-am_fix.patch
URL:		http://gusnet.cx/aaron/codecs/ac3dec.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A free AC-3 stream decoder.

%description -l pl
Darmowy dekoder strumieni AC-3.

%package devel
Summary:	Header file required to build programs using ac3dec library
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce ac3dec
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files required to build programs using ac3dec library

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
biblioteki ac3dec.

%package static
Summary:	Static ac3dec library.
Summary(pl):	Statyczna biblioteka ac3dec.
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static ac3dec library.

%description static -l pl
Statyczna biblioteka ac3dec.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm missing
libtoolize --copy --force
aclocal
autoheader
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf TODO README Change*

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/ac3

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
