Summary:	Kernel Oops decoder
Summary(pl):	Dekoder Opp-ów kernela
Name:		ksymoops
Version:	0.7c
Release:	8
Copyright:	GNU
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.ocs.com.au/pub/%{name}-%{version}.tar.gz
BuildRequires:	binutils = 2.9.5.0.29
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
make DEBUG="$RPM_OPT_FLAGS"

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
