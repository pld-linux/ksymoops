Summary:	Kernel Oops decoder
Summary(pl):	Dekoder Opp-ów kernela
Name:		ksymoops
Version:	2.3.4
Release:	1
License:	GNU
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://ftp.ocs.com.au/pub/%{name}/v2.3/%{name}-%{version}.tar.gz
BuildRequires:	binutils = 2.9.5.0.46
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kernel-utils

%description
Read a kernel Oops file and make the best stab at converting the code to
instructions and mapping stack values to kernel symbols.

%description -l pl
ksymoops jest narzêdziem s³u¿±cym do dekodownia informacji jakie zrzuca
kernel w momencie wyst±pienia Oppa na postaæ zawieraj±c± wiêcej informacji
w sk³ad których wchodzi dekodowanie kodu na mnemoniki instrukcji
assemblerowych, a tak¿e postaæ owa zawiera pozamieniane adresy na symbole
kernela.

%prep
%setup -q

%build
%{__make} DEBUG="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install -s ksymoops $RPM_BUILD_ROOT%{_sbindir}/ksymoops

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_sbindir}/ksymoops
