%define XEN_RELEASE %(test -z "${XEN_RELEASE}" && echo unknown || echo $XEN_RELEASE)

Name:           ocaml-type-conv
Version:        1.6.8
Release:        %{XEN_RELEASE}
Summary:        OCaml base library for type conversion

Group:          Development/Other
License:        LGPLv2+ with exceptions and BSD
URL:            http://www.ocaml.info/home/ocaml_sources.html#type-conv
Source0:        http://hg.ocaml.info/release/type-conv/archive/type-conv-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/type-conv/archive/release-%{version}.tar.bz2 > type-conv-release-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-camlp4

%description
The type-conv mini library factors out functionality needed by
different preprocessors that generate code from type specifications,
because this functionality cannot be duplicated without losing the
ability to use these preprocessors simultaneously.

%prep
%setup -q -n type-conv-release-%{version}
#dos2unix LICENSE.Tywith

%build
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE LICENSE.Tywith COPYRIGHT README.txt
%{_libdir}/ocaml/type-conv



%changelog
* Fri May 14 2010 David Scott <dave.scott@eu.citrix.com>
- Customised for XCP

* Wed Jan 07 2009 Florent Monnier <blue_prawn@mandriva.org> 1.6.5-1mdv2009.1
+ Revision: 326698
- corrected group
- import ocaml-type-conv


* Sat Dec 20 2008 Florent Monnier <fmonnier@linux-nantes.org> 1.6.5-1mdv
- Initial RPM release made from the fedora rpm .spec file (revision 1.9) by Richard W.M. Jones
# found there: http://cvs.fedoraproject.org/viewvc/devel/ocaml-type-conv/ocaml-type-conv.spec
