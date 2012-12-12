Name:           opam-repository
Version:        2012.12.12
Release:        1
Summary:        Repository used by opam

Group:          Development/Libraries
License:        Unknown
URL:            https://github.com/xen-org/opam-repository
Source0:        http://www.uk.xensource.com/distfiles/ocaml/opam-repository-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

%description
See opam docs at ocamlpro site.

%prep
%setup -n opam-repository

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/opam-repository
cp -a * $RPM_BUILD_ROOT/usr/local/opam-repository/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/local/opam-repository
