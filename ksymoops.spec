Summary:	Kernel Oops decoder
Name:		ksymoops
Version:	0.6
Release:	1
Copyright:	GNU
Group:		Utilities/System
Group(pl):	narzêdzia/System
Source:		ftp://ftp.ocs.com.au/pub/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Read a kernel Oops file and make the best stab at converting the code to
instructions and mapping stack values to kernel symbols.

%prep
%setup -q

%build
make DEBUG=$RPM_OPT_FLAGS

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/sbin

install -s ksymoops $RPM_BUILD_ROOT/usr/sbin/ksymoops

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) /usr/sbin/ksymoops

%changelog
* Wed Nov 18 1998 Maciej W. Rozycki <macro@ds2.pg.gda.pl>
- initial build for ksymoops 0.6
