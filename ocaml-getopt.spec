%define XEN_RELEASE %(test -z "${XEN_RELEASE}" && echo unknown || echo $XEN_RELEASE)

Name:           ocaml-getopt
Version:        20040811
Release:        1%{?extrarelease}
Summary:        Command line parsing a la GNU getopt
License:        MIT-like
Group:          Development/Other
URL:            http://alain.frisch.fr/soft#Getopt
Source0:        http://alain.frisch.fr/info/getopt-20040811.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib, ocaml, ocaml-ocamldoc

%description
The OCaml distribution comes with the module Arg specialized in
command-line parsing. However, it doesn't support the well known
features of GNU getopt and getopt_long.

The module Getopt is an alternative; it supports GNU syntax, but from the
programmer point of view, it is close to the spirit of Arg: the programmer
gives to the general parsing function a list of possible options, together
with the behaviour of these options.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n getopt

%build
make all allopt
make doc

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/getopt
make install
cp getopt.mli $OCAMLFIND_DESTDIR/getopt

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING Changes README
%dir %{_libdir}/ocaml/getopt
%{_libdir}/ocaml/getopt/META
%{_libdir}/ocaml/getopt/*.cma
%{_libdir}/ocaml/getopt/*.cmi

%files devel
%defattr(-,root,root)
%doc doc
%doc sample.ml
%{_libdir}/ocaml/getopt/*.a
%{_libdir}/ocaml/getopt/*.cmxa
%{_libdir}/ocaml/getopt/*.mli
%{_libdir}/ocaml/getopt/*.o



%changelog
* Fri May 14 2010 David Scott <dave.scott@eu.citrix.com>
- Customise for XCP

* Fri Sep 11 2009 Florent Monnier <blue_prawn@mandriva.org> 20040811-1mdv2010.0
+ Revision: 438504
- import ocaml-getopt

