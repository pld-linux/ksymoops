#
# Conditional build:
# _without_static - link dynamically with libbfd
#
Summary:	Kernel Oops decoder
Summary(es):	Un utilitario para extraer mensajes oops del nЗcleo y transformarlos en texto
Summary(pl):	Dekoder OopsСw kernela
Summary(pt_BR):	Um utilitАrio para extrair mensagens oops do kernel e transformar em texto
Summary(ru):	Утилита для расшифровки oops'ов ядра Linux
Summary(uk):	Утил╕та для розшифровки oops'╕в ядра Linux
Name:		ksymoops
Version:	2.4.9
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	231b6ea3afbc318c129ec770d10f8ec8
%{!?_without_static:BuildRequires:	binutils-static >= 2.10.1.0.4}
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
ksymoops extrae mensajes de oops del nЗcleo y usa varias fuentes de
informaciones de sМmbolos para convertir las direcciones y cСdigos en
texto.

%description -l pl
ksymoops jest narzЙdziem sЁu©╠cym do dekodownia informacji jakie
zrzuca kernel w momencie wyst╠pienia Oopsa na postaФ zawieraj╠c╠
wiЙcej informacji, w skЁad ktСrych wchodzi dekodowanie kodu na
mnemoniki instrukcji asemblerowych oraz zamiana adresСw na symbole.
Jest to narzЙdzie przydatne do zgЁaszania raportСw o bЁЙdach w j╠drze
Linuksa.

%description -l pt_BR
ksymoops extraМ mensagens de oops do kernel e usa vАrias fontes de
informaГУes de sМmbolos para converter os endereГos e cСdigo em texto.

%description -l ru
ksymoops извлекает отчеты ядра о происшедших Oops'ах из текстового
файла и использует разнообразные источники информации о символах для
преобразования адресов и кода в осмысленный текст. Само по себе
сообщение об Oops'е ядра бессмысленно, т.к. другие не знают как
выглядит ваше ядро; вы должны пропустить текст Oops'а через ksymoops и
послать вывод ksymoops как часть вашего сообщения об ошибке.

%description -l uk
ksymoops видобува╓ зв╕ти ядра про Oops'и, як╕ мали м╕сце, з текстового
файлу ╕ використову╓ р╕зноман╕тн╕ джерела ╕нформац╕╖ про символи для
перетворення адрес та код╕в в зрозум╕лий текст. Саме по соб╕
пов╕домлення про Oops ядра не ма╓ сенсу, тому що ╕нш╕ не знають як
вигляда╓ ваше ядро; ви повинн╕ пропустити текст Oops'у через ksymoops
та над╕слати вивод ksymoops як частину вашого пов╕домлення про
помилку.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  README README.XFree86 Changelog
%attr(755,root,root) %{_sbindir}/ksymoops
%attr(644,root,root) %{_mandir}/man8/ksymoops.8*
