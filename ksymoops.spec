Summary:	Kernel Oops decoder
Summary(pl):	Dekoder Opp-ów kernela
Name:		ksymoops
Version:	2.4.0
Release:	1
License:	GNU
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.3/%{name}-%{version}.tar.bz2
Patch0:		%{name}-shared.patch
BuildRequires:	binutils-static >= 2.10.0.33
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
%{?!bcond_off_static:%{__make} DEBUG="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"}
%{?bcond_off_static:%{__make} ksymoops.shared DEBUG="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{?!bcond_off_static:install ksymoops $RPM_BUILD_ROOT%{_sbindir}/ksymoops}
%{?bcond_off_static:install ksymoops.shared $RPM_BUILD_ROOT%{_sbindir}/ksymoops}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_sbindir}/ksymoops
