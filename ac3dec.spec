Summary:	a free AC-3 stream decoder
Summary(pl):	darmowy dekoder strumieni AC-3
Name:		ac3dec
Version:	0.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.linuxvideo.org/devel/data/%{name}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.linuxvideo.org/ac3dec/
BuildRequires:	autoconf
BuildRequires:	automake
BuildConflicts:	libao
Conflicts:	libao
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name}

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
Requires:	%{name}-devel

%description static
Static ac3dec library.

%description static -l pl
Statyczna biblioteka ac3dec.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
libtoolize --copy --force
aclocal
autoheader
autoconf
automake -a -c
%configure

%{__make} CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -Ilibac3 -Ilibao"

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
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
