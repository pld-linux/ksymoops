Summary:	Kernel Oops decoder
Summary(pl):	Dekoder Opp-�w kernela
Name:		ksymoops
Version:	0.6
Release:	2
Copyright:	GNU
Group:		Utilities/System
Group(pl):	narz�dzia/System
Source:		ftp://ftp.ocs.com.au/pub/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Read a kernel Oops file and make the best stab at converting the code to
instructions and mapping stack values to kernel symbols.

%description -l pl
ksymoops jest narz�dziem s�u��cym do dekodownia informacji jakie zrzuca
kernel w momencie wyst�pienia Oppa na posta� zawieraj�c� wi�cej informacji w
sk�ad kt�rych wchodzi dekodowanie kodu na mnemoniki instrukcji
assemblerowych, a tak�e posta� owa zawiera pozamieniane adresy na symbole
kernela.

%prep
%setup -q

%build
make DEBUG="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install -s ksymoops $RPM_BUILD_ROOT%{_sbindir}/ksymoops

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_sbindir}/ksymoops

%changelog
* Wed Apr  7 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.6-2]
- added gzipping %doc,
- added pl translation.

* Wed Nov 18 1998 Maciej W. Rozycki <macro@ds2.pg.gda.pl>
- initial build for ksymoops 0.6
