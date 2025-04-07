#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v23
# autospec commit: a88ffdc
#
Name     : perl-Module-Runtime
Version  : 0.017
Release  : 44
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Module-Runtime-0.017.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Module-Runtime-0.017.tar.gz
Summary  : 'runtime module handling'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Runtime-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl-Module-Build
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Module::Runtime - runtime module handling
SYNOPSIS
use Module::Runtime qw(
$module_name_rx is_module_name check_module_name
module_notional_filename require_module);

%package dev
Summary: dev components for the perl-Module-Runtime package.
Group: Development
Provides: perl-Module-Runtime-devel = %{version}-%{release}
Requires: perl-Module-Runtime = %{version}-%{release}

%description dev
dev components for the perl-Module-Runtime package.


%package perl
Summary: perl components for the perl-Module-Runtime package.
Group: Default
Requires: perl-Module-Runtime = %{version}-%{release}

%description perl
perl components for the perl-Module-Runtime package.


%prep
%setup -q -n Module-Runtime-0.017
cd %{_builddir}/Module-Runtime-0.017

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Runtime.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
