Summary:	Kernel Oops decoder
Summary(pl):	Dekoder Opp-ów kernela
Name:		ksymoops
Version:	2.4.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.4/%{name}-%{version}.tar.bz2
BuildRequires:	binutils-static >= 2.10.1.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kernel-utils

%description
Read a kernel Oops file and make the best stab at converting the code
to instructions and mapping stack values to kernel symbols.

%description -l pl
ksymoops jest narzêdziem s³u¿±cym do dekodownia informacji jakie
zrzuca kernel w momencie wyst±pienia Oppa na postaæ zawieraj±c± wiêcej
informacji w sk³ad których wchodzi dekodowanie kodu na mnemoniki
instrukcji assemblerowych, a tak¿e postaæ owa zawiera pozamieniane
adresy na symbole kernela.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags}" \
	DEF_MAP=\\\"/boot/System.map-*r\\\" \
	%{?_without_static:DYNAMIC="" STATIC=""}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install ksymoops $RPM_BUILD_ROOT%{_sbindir}/ksymoops
install ksymoops.8 $RPM_BUILD_ROOT%{_mandir}/man8/

gzip -9nf README README.XFree86 Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/ksymoops
%attr(644,root,root) %{_mandir}/man8/ksymoops.8*
