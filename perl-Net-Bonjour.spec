%define realname   Net-Bonjour

Name:		perl-%{realname}
Version:    0.95
Release: %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Module for DNS service discovery ( Zeroconf ) 
Source0:    http://search.cpan.org/CPAN/authors/id/C/CH/CHLIGE//%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRequires:	perl-devel
BuildRequires:  perl-Net-DNS
BuildArch:      noarch
Obsoletes: perl-Net-Rendezvous < 0.90
Provides: perl-Net-Rendezvous = %version

%description
Net::Rendezvous is a set of modules that allow one to discover local services 
via multicast DNS (mDNS) or enterprise services via traditional DNS. This 
method of service discovery has been branded as Rendezvous ( now Bonjour ) by 
Apple Computer.

%prep
%setup -q -n %{realname}-%{version}

%build
yes y | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# it seems the number of server changed, and therefore, 
# the test is not working as zeronf.org return more entries than
# planned
perl -pi -e "s/ == 2/ == 11/" t/3-enterprise.t
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

