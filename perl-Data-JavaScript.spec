#
# Conditional build:
%bcond_without	tests		# perform "make test" (require Internet connection)
#
%define	pdir	Data
%define	pnam	JavaScript
Summary:	Data::JavaScript - dump perl data structures into JavaScript code 
Summary(pl.UTF-8):	Data::JavaScript - konwersja struktur danych Perla do kodu JavaScript
Name:		perl-Data-JavaScript
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JP/JPIERCE/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	14a2e422d2a22d34749e762614b4736f
URL:		http://search.cpan.org/dist/Data-JavaScript/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is mainly intended for CGI programming, when a perl
script generates a page with client side JavaScript code that needs
access to structures created on the server.

%description -l pl.UTF-8
Ten moduł jest przeznaczony główne do programowania CGI, kiedy
skrypt perlowy generuje stronę z kodem JavaScript, który korzysta
z danych utworzonych przez serwer.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__cp} -a example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} -f $RPM_BUILD_ROOT%{perl_vendorlib}/Data/example.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Data/JavaScript.pm
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
