#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Pcalc
Summary:	Perl module Date::Pcalc
Summary(pl):	Modu³ perla Date::Pcalc
Name:		perl-Date-Pcalc
Version:	1.2
Release:	1
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c09a09337c7d2e18a17898ca577c644
URL:		http://catcode.com/date/pcalc.html
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
This package consists of a Perl module for all kinds of date
calculations based on the Gregorian calendar (the one used in all
western countries today), thereby complying with all relevant norms
and standards: ISO/R 2015-1971, DIN 1355 and, to some extent, ISO 8601
(where applicable).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

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
%{perl_vendorlib}/Date/Pcalc.pm
%{_mandir}/man3/*
