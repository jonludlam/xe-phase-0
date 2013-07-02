Name:           optcomp
Version:        1.4
Release:        0
Summary:        Optional compilation with cpp-like directives
License:        BSD3
Group:          Development/Other
URL:            https://forge.ocamlcore.org/frs/download.php/1011/optcomp-1.4.tar.gz
Source0:        optcomp-1.4.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-ocamldoc ocaml-camlp4 ocaml-camlp4-devel
Requires:       ocaml

%description
Optional compilation with cpp-like directives.

%prep
%setup -q -n optcomp-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}/%{_libdir}/ocaml/usr/local/bin/optcomp-r %{buildroot}/%{_bindir}/
mv %{buildroot}/%{_libdir}/ocaml/usr/local/bin/optcomp-o %{buildroot}/%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_libdir}/ocaml/optcomp/*
%{_bindir}/optcomp-r
%{_bindir}/optcomp-o

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

