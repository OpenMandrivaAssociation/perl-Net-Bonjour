%define upstream_name    Net-Bonjour
%define upstream_version 0.96

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Module for DNS service discovery ( Zeroconf ) 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHLIGE//%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Net-DNS
BuildRequires:	perl-devel
BuildArch:  noarch

Obsoletes:	perl-Net-Rendezvous < 0.90
Provides:	perl-Net-Rendezvous = %{version}

%description
Net::Rendezvous is a set of modules that allow one to discover local services 
via multicast DNS (mDNS) or enterprise services via traditional DNS. This 
method of service discovery has been branded as Rendezvous ( now Bonjour ) by 
Apple Computer.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.960.0-4mdv2012.0
+ Revision: 765520
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.960.0-2
+ Revision: 667267
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.960.0-1mdv2011.0
+ Revision: 407813
- rebuild using %%perl_convert_version

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.96-1mdv2010.0
+ Revision: 372111
- update to new version 0.96

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.95-4mdv2009.0
+ Revision: 257952
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.95-3mdv2009.0
+ Revision: 246004
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.95-1mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.95-1mdv2008.0
+ Revision: 25203
- Import perl-Net-Bonjour

