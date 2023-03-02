Name:           perl-MogileFS-Plugin-Migrate
Version:        0.04
Release:        1%{?dist}
Summary:        Migrate plugin for MogileFS
License:        GPL or Artistic
Group:          Development/Libraries
URL:            https://github.com/shutterstock/MogileFS-Plugin-Migrate
Source0:        MogileFS-Plugin-Migrate-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-MogileFS-Client
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Migrate plugin for the MogileFS distributed storage system

%prep
%setup -q -n MogileFS-Plugin-Migrate-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/*
