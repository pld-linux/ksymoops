Summary:	Kernel Oops decoder
Summary(pl):	Dekoder Opp-ów kernela
Name:		ksymoops
Version:	2.4.1
Release:	2
License:	GNU
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.4/%{name}-%{version}.tar.bz2
Patch0:		%{name}-shared.patch
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
%patch0 -p1

%build
%{?!_without_static:%{__make} DEBUG="%{rpmcflags}"} DEF_MAP=\\\"/boot/System.map-*r\\\"
%{?_without_static:%{__make} ksymoops.shared DEBUG="%{rpmcflags}"} DEF_MAP=\\\"/boot/System.map-*r\\\"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{?!_without_static:install ksymoops $RPM_BUILD_ROOT%{_sbindir}/ksymoops}
%{?_without_static:install ksymoops.shared $RPM_BUILD_ROOT%{_sbindir}/ksymoops}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_sbindir}/ksymoops
