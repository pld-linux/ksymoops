Summary:	Kernel Oops decoder
Summary(es):	Un utilitario para extraer mensajes oops del n�cleo y transformarlos en texto
Summary(pl):	Dekoder Opp-�w kernela
Summary(pt_BR):	Um utilit�rio para extrair mensagens oops do kernel e transformar em texto
Summary(ru):	������� ��� ����������� oops'�� ���� Linux
Summary(uk):	���̦�� ��� ����������� oops'�� ���� Linux
Name:		ksymoops
Version:	2.4.6
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.4/%{name}-%{version}.tar.bz2
BuildRequires:	binutils-static >= 2.10.1.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kernel-utils

%description
ksymoops extracts kernel Oops reports from the Oops.file and uses
various sources of symbol information to convert the addresses and
code to meaningful text. Reporting a kernel Oops is meaningless on its
own because other people do not know what your kernel looks like, you
need to feed the Oops text through ksymoops then send the ksymoops
output as part of your bug report.

%description -l es
ksymoops extrae mensajes de oops del n�cleo y usa varias fuentes de
informaciones de s�mbolos para convertir las direcciones y c�digos en
texto.

%description -l pl
ksymoops jest narz�dziem s�u��cym do dekodownia informacji jakie
zrzuca kernel w momencie wyst�pienia Oppa na posta� zawieraj�c� wi�cej
informacji w sk�ad kt�rych wchodzi dekodowanie kodu na mnemoniki
instrukcji assemblerowych, a tak�e posta� owa zawiera pozamieniane
adresy na symbole kernela.

%description -l pt_BR
ksymoops extra� mensagens de oops do kernel e usa v�rias fontes de
informa��es de s�mbolos para converter os endere�os e c�digo em texto.

%description -l ru
ksymoops ��������� ������ ���� � ����������� Oops'�� �� ����������
����� � ���������� ������������� ��������� ���������� � �������� ���
�������������� ������� � ���� � ����������� �����. ���� �� ����
��������� �� Oops'� ���� ������������, �.�. ������ �� ����� ���
�������� ���� ����; �� ������ ���������� ����� Oops'� ����� ksymoops �
������� ����� ksymoops ��� ����� ������ ��������� �� ������.

%description -l uk
ksymoops ��������� �צ�� ���� ��� Oops'�, �˦ ���� ͦ���, � ����������
����� � ����������դ Ҧ�����Φ�Φ ������� �������æ� ��� ������� ���
������������ ����� �� ��Ħ� � �����ͦ��� �����. ���� �� ��¦
��צ�������� ��� Oops ���� �� ��� �����, ���� �� ��ۦ �� ������ ��
�������� ���� ����; �� �����Φ ���������� ����� Oops'� ����� ksymoops
�� ��Ħ����� ����� ksymoops �� ������� ������ ��צ�������� ���
�������.

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
