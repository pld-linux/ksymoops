# TODO:
# - finish and send to builder (not every 2.6 kernel has oops decoding...)
#
# Conditional build:
%bcond_without	static		# link dynamically with libbfd
#
Summary:	Kernel Oops decoder
Summary(es.UTF-8):	Un utilitario para extraer mensajes oops del núcleo y transformarlos en texto
Summary(pl.UTF-8):	Dekoder Oopsów kernela
Summary(pt_BR.UTF-8):	Um utilitário para extrair mensagens oops do kernel e transformar em texto
Summary(ru.UTF-8):	Утилита для расшифровки oops'ов ядра Linux
Summary(uk.UTF-8):	Утиліта для розшифровки oops'ів ядра Linux
Name:		ksymoops
Version:	2.4.11
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/kernel/ksymoops/v2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	4a8249e182a5dbc75e566d162e9f3314
Patch0:		%{name}-ksyms-2.6.patch
BuildRequires:	binutils-devel
# NOTE: binutils-static >= 2.11.90.0.19 has E=2
%{?with_static:BuildRequires:	binutils-static >= 1:2.10.1.0.4}
Obsoletes:	kernel-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ksymoops extracts kernel Oops reports from the Oops.file and uses
various sources of symbol information to convert the addresses and
code to meaningful text. Reporting a kernel Oops is meaningless on its
own because other people do not know what your kernel looks like, you
need to feed the Oops text through ksymoops then send the ksymoops
output as part of your bug report.

%description -l es.UTF-8
ksymoops extrae mensajes de oops del núcleo y usa varias fuentes de
informaciones de símbolos para convertir las direcciones y códigos en
texto.

%description -l pl.UTF-8
ksymoops jest narzędziem służącym do dekodownia informacji jakie
zrzuca kernel w momencie wystąpienia Oopsa na postać zawierającą
więcej informacji, w skład których wchodzi dekodowanie kodu na
mnemoniki instrukcji asemblerowych oraz zamiana adresów na symbole.
Jest to narzędzie przydatne do zgłaszania raportów o błędach w jądrze
Linuksa.

%description -l pt_BR.UTF-8
ksymoops extraí mensagens de oops do kernel e usa várias fontes de
informações de símbolos para converter os endereços e código em texto.

%description -l ru.UTF-8
ksymoops извлекает отчеты ядра о происшедших Oops'ах из текстового
файла и использует разнообразные источники информации о символах для
преобразования адресов и кода в осмысленный текст. Само по себе
сообщение об Oops'е ядра бессмысленно, т.к. другие не знают как
выглядит ваше ядро; вы должны пропустить текст Oops'а через ksymoops и
послать вывод ksymoops как часть вашего сообщения об ошибке.

%description -l uk.UTF-8
ksymoops видобуває звіти ядра про Oops'и, які мали місце, з текстового
файлу і використовує різноманітні джерела інформації про символи для
перетворення адрес та кодів в зрозумілий текст. Саме по собі
повідомлення про Oops ядра не має сенсу, тому що інші не знають як
виглядає ваше ядро; ви повинні пропустити текст Oops'у через ksymoops
та надіслати вивод ksymoops як частину вашого повідомлення про
помилку.

%prep
%setup -q
%patch0 -p1

sed -i -e 's#-lbfd -liberty#-lbfd -liberty -lz#g' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags}" \
	DEF_MAP=\\\"/boot/System.map-*r\\\" \
	%{?!with_static:DYNAMIC="" STATIC=""}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install ksymoops $RPM_BUILD_ROOT%{_sbindir}/ksymoops
install ksymoops.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.XFree86 Changelog
%attr(755,root,root) %{_sbindir}/ksymoops
%{_mandir}/man8/ksymoops.8*
