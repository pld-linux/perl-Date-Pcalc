#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Pcalc
Summary:	Date::Pcalc Perl module - Gregorian calendar date calculations
Summary(pl.UTF-8):	Moduł Perla Date::Pcalc - obliczenia na datach wg kalendarza gregoriańskiego
Name:		perl-Date-Pcalc
Version:	6.1
Release:	15
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6a719d8fe10ac673be5d09e003130aa8
Patch0:		build.patch
Patch1:		Date-Pcalc-6.1-century.patch
URL:		http://catcode.com/date/pcalc.html
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Bit-Vector >= 7.1
BuildRequires:	perl-Carp-Clan >= 5.3
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
This package consists of a Perl module for all kinds of date
calculations based on the Gregorian calendar (the one used in all
western countries today), thereby complying with all relevant norms
and standards: ISO/R 2015-1971, DIN 1355 and, to some extent, ISO 8601
(where applicable).

%description -l pl.UTF-8
Ten pakiet zawiera moduł Perla do wszystkich rodzajów obliczeń na
datach opartych na kalendarzu gregoriańskim (używanym aktualnie we
wszystkich państwach zachodnich) w sposób zgodny z odpowiednimi
normami i standardami: ISO/R 2015-1971, DIN 1355 i, w pewnym zakresie,
ISO 8601.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%{__rm} t/f035.t

%build
echo c | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a tools $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt INSTALL.txt README.txt EXAMPLES.txt
%dir %{perl_vendorarch}/Date
%{perl_vendorarch}/Date/Pcalc.pm
%dir %{perl_vendorarch}/Date/Pcalc
%{perl_vendorarch}/Date/Pcalc/Object.pm
%{perl_vendorarch}/Date/Pcalendar.pm
%dir %{perl_vendorarch}/Date/Pcalendar
%{perl_vendorarch}/Date/Pcalendar/*.pm
%dir %{perl_vendorarch}/auto/Date
%dir %{perl_vendorarch}/auto/Date/Pcalc
%attr(755,root,root) %{perl_vendorarch}/auto/Date/Pcalc/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
