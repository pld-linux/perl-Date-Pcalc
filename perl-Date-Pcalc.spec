#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Pcalc
Summary:	Date::Pcalc Perl module - Gregorian calendar date calculations
Summary(pl):	Modu³ Perla Date::Pcalc - obliczenia na datach wg kalendarza gregoriañskiego
Name:		perl-Date-Pcalc
Version:	1.2
Release:	2
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c09a09337c7d2e18a17898ca577c644
URL:		http://catcode.com/date/pcalc.html
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
This package consists of a Perl module for all kinds of date
calculations based on the Gregorian calendar (the one used in all
western countries today), thereby complying with all relevant norms
and standards: ISO/R 2015-1971, DIN 1355 and, to some extent, ISO 8601
(where applicable).

%description -l pl
Ten pakiet zawiera modu³ Perla do wszystkich rodzajów obliczeñ na
datach opartych na kalendarzu gregoriañskim (u¿ywanym aktualnie we
wszystkich pañstwach zachodnich) w sposób zgodny z odpowiednimi
normami i standardami: ISO/R 2015-1971, DIN 1355 i, w pewnym zakresie,
ISO 8601.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt EXAMPLES.txt pcalc.html
%{perl_sitelib}/Date/Pcalc.pm
%{_mandir}/man3/*
