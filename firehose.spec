Summary:	Easy data transfer over parallel network devices
Summary(pl):	Narzêdzie do ³atwego przesy³ania danych po równoleg³ych urz±dzeniach sieciowych
Name:		firehose
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Networking/Utilities
Source0:	http://heroines.sourceforge.net/%{name}-%{version}.tar.gz
URL:		http://heroines.sourceforge.net/firehose.php3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
At the heart of firehose is a library which allows any program wishing
to stream data over striped ethernet to do so. There are several
utilities which demonstrate use of the library. firerecv is a threaded
server and firesend is a client. firepipe allows you to send data over
parallel network devices using pipes.

%description -l pl
Podstaw± firehose jest biblioteka pozwalaj±ca programom przesy³aæ
strumienie danych po wielu równoleg³ych po³±czeniach sieciowych naraz.
Pakiet zawiera kilka narzêdzi demonstruj±cych u¿ycie tej biblioteki:
firerecv to wielow±tkowy serwer, firesend to klient, a firepipe
pozwala na wysy³anie danych przy u¿yciu rurek.

%package devel
Summary:	Firehose header files and static library
Summary(pl):	Pliki nag³ówkowe i statyczna biblioteka firehose
Group:		Development/Libraries
# doesn not depend on base (no shared library)

%description devel
Firehose header files and static library.

%description devel -l pl
Pliki nag³ówkowe i statyczna biblioteka firehose.

%prep
%setup -q -n %{name}

%build
%{__make} \
	GCC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}

install firerecv firesend firepipe $RPM_BUILD_ROOT%{_bindir}
install libfirehose.a $RPM_BUILD_ROOT%{_libdir}
install firehose*.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/*.h
