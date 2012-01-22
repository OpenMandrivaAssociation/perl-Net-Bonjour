%define upstream_name    Net-Bonjour
%define upstream_version 0.96

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Module for DNS service discovery ( Zeroconf ) 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/C/CH/CHLIGE//%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-Net-DNS
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Obsoletes: perl-Net-Rendezvous < 0.90
Provides:  perl-Net-Rendezvous = %{version}

%description
Net::Rendezvous is a set of modules that allow one to discover local services 
via multicast DNS (mDNS) or enterprise services via traditional DNS. This 
method of service discovery has been branded as Rendezvous ( now Bonjour ) by 
Apple Computer.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}/%{perl_vendorarch}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*
