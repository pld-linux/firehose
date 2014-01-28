Summary:	Easy data transfer over parallel network devices
Summary(pl.UTF-8):	Narzędzie do łatwego przesyłania danych po równoległych urządzeniach sieciowych
Name:		firehose
Version:	0.6.0
Release:	3
License:	LGPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/heroines/%{name}-%{version}-src.tar.bz2
# Source0-md5:	04b846adb6f90df2756d297ab02cce21
Patch0:		%{name}-sh.patch
Patch1:		%{name}-page.patch
URL:		http://heroines.sourceforge.net/firehose.php3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
At the heart of firehose is a library which allows any program wishing
to stream data over striped ethernet to do so. There are several
utilities which demonstrate use of the library. firerecv is a threaded
server and firesend is a client. firepipe allows you to send data over
parallel network devices using pipes.

%description -l pl.UTF-8
Podstawą firehose jest biblioteka pozwalająca programom przesyłać
strumienie danych po wielu równoległych połączeniach sieciowych naraz.
Pakiet zawiera kilka narzędzi demonstrujących użycie tej biblioteki:
firerecv to wielowątkowy serwer, firesend to klient, a firepipe
pozwala na wysyłanie danych przy użyciu rurek.

%package devel
Summary:	Firehose header files and static library
Summary(pl.UTF-8):	Pliki nagłówkowe i statyczna biblioteka firehose
Group:		Development/Libraries
# does not depend on base (no shared library)

%description devel
Firehose header files and static library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i statyczna biblioteka firehose.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	GCC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	TARGET=pld

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}

install pld/{firerecv,firesend,firepipe,dateserve,dateget,bottom,extract} $RPM_BUILD_ROOT%{_bindir}
install pld/libfirehose.a $RPM_BUILD_ROOT%{_libdir}
install firehose*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/*.h
