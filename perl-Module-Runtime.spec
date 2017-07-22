#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Runtime
Version  : 0.015
Release  : 13
URL      : https://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Module-Runtime-0.015.tar.gz
Source0  : https://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Module-Runtime-0.015.tar.gz
Summary  : 'runtime module handling'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Runtime-doc
BuildRequires : perl-Module-Build

%description
NAME
Module::Runtime - runtime module handling
DESCRIPTION
The functions exported by this module deal with runtime handling of
Perl modules, which are normally handled at compile time.  This module
avoids using any other modules, so that it can be used in low-level
infrastructure.

%package doc
Summary: doc components for the perl-Module-Runtime package.
Group: Documentation

%description doc
doc components for the perl-Module-Runtime package.


%prep
%setup -q -n Module-Runtime-0.015

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/Module/Runtime.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
