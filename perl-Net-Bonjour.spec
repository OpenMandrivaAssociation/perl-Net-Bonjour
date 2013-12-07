%define modname	Net-Bonjour
%define modver	0.96

Summary:	Module for DNS service discovery ( Zeroconf ) 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHLIGE//%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-devel
Obsoletes:	perl-Net-Rendezvous < 0.90
Provides:	perl-Net-Rendezvous = %{version}

%description
Net::Rendezvous is a set of modules that allow one to discover local services 
via multicast DNS (mDNS) or enterprise services via traditional DNS. This 
method of service discovery has been branded as Rendezvous ( now Bonjour ) by 
Apple Computer.

%prep
%setup -qn %{modname}-%{modver}

%build
yes y | %__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# it seems the number of server changed, and therefore, 
# the test is not working as zeronf.org return more entries than
# planned
#
# disable all tests as they fail at ABF
# perl -pi -e "s/ == 2/ == 11/" t/3-enterprise.t
# make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

