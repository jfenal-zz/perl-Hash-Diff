Name:           perl-Hash-Diff
Version:        0.003
Release:        1%{?dist}
Summary:        Return difference between to hashes as a hash
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Hash-Diff/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BO/BOLAV/Hash-Diff-0.003.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Test::use::ok)

%{?perl_default_filter}

%description
Hash::Diff returns the difference between to hashes as a hash.

%prep
%setup -q -n Hash-Diff-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{perl_vendorlib}/Hash/Diff.pm
%{_mandir}/man3/Hash::Diff.3pm*

%changelog
* Wed Jul 14 2010 Jerome Fenal <jfenal@free.fr> 0.003-1
- Specfile autogenerated by cpanspec 1.78.
- Modified Requires and BuildRequires from perl(ok) to perl(Test::use::ok)
- added perl_default_filter
- Remove unnecessary Hash::Merge Require
- Fixed typo in description (from original Description pod)
- Removed directories from spec manifest, as there are other Hash::
  modules already packaged.
