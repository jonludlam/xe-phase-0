
%define XEN_RELEASE %(test -z "${XEN_RELEASE}" && echo unknown || echo $XEN_RELEASE)

%define major 3.12

Summary: Objective Caml
Name: ocaml
Version: %{major}.1.ocamlspotter
Release: %{XEN_RELEASE}
License: QPL/LGPL
Group: Development/Languages
URL: http://caml.inria.fr/

Packager: David Scott <dave.scott@eu.citrix.com>
Vendor: http://www.xen.org/

Source0: http://caml.inria.fr/distrib/ocaml-%{major}/ocaml-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Objective Caml is the latest implementation of the Caml dialect of ML. It
has full support for objects and classes combined with ML-style type
reconstruction, a powerful module calculus in the style of Standard ML (but
retaining separate compilation), a high-performance native code compiler (in
addition to a Caml Light-style bytecode compiler), and labeled arguments
with possible default value.

%package camlp4
Group: Development/Languages
Summary: Pre-Processor-Pretty-Printer for OCaml
Requires: ocaml = %{version}-%{release}
Obsoletes: camlp4 <= %{version}-%{release}

%description camlp4
Camlp4 is a Pre-Processor-Pretty-Printer for OCaml, parsing a source
file and printing some result on standard output.

%prep
%setup -T -b 0

%build
./configure \
    -cc "%{__cc} %{optflags}" \
    -bindir "%{_bindir}" \
    -libdir "%{_libdir}/ocaml" \
    -mandir "%{_mandir}" \
    -prefix "%{_prefix}" \
    -verbose \
    -with-pthread
%{__make} core coreboot
./build/mixed-boot.sh
cp boot/myocamlbuild boot/myocamlbuild.boot
%{__make} world opt opt.opt

%install
%{__rm} -rf %{buildroot}
%{__make} install BINDIR="%{buildroot}%{_bindir}" LIBDIR="%{buildroot}%{_libdir}/ocaml" MANDIR="%{buildroot}%{_mandir}"
%{__perl} -pi.orig -e 's|^%{buildroot}||' %{buildroot}%{_libdir}/ocaml/ld.conf
mkdir -p %{buildroot}%{_libdir}/ocaml/compiler-libs/utils
cp -r utils/*.{cmo,cmi,spit,spot} %{buildroot}%{_libdir}/ocaml/compiler-libs/utils/
mkdir -p %{buildroot}%{_libdir}/ocaml/compiler-libs/typing
cp -r typing/*.{cmo,cmi,spit,spot} %{buildroot}%{_libdir}/ocaml/compiler-libs/typing/
mkdir -p %{buildroot}%{_libdir}/ocaml/compiler-libs/parsing
cp -r parsing/*.{cmo,cmi,spit,spot} %{buildroot}%{_libdir}/ocaml/compiler-libs/parsing/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE README
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3*
%{_bindir}/*
%{_libdir}/ocaml/
%{_libdir}/ocaml/compiler-libs/

%files camlp4
%defattr(-, root, root, 0755)
%{_bindir}/camlp4*
%{_bindir}/mkcamlp4
%dir %{_libdir}/ocaml/
%{_libdir}/ocaml/camlp4/

%changelog
* Tue Sep 27 2011 David Scott <dave.scott@eu.citrix.com>
- Updated to 3.12.1

* Sat Nov 27 2010 Mike McClurg <mike.mcclurg@citrix.com>
- Updated to OCaml Spotter, a patched 3.12.0 OCaml compiler that provides enhanced typing annotation files.

* Wed Nov 24 2010 Mike McClurg <mike.mcclurg@citrix.com>
- Updated to release 3.12.0.

* Fri May 14 2010 David Scott <dave.scott@eu.citrix.com>
- Customise for use in XCP build

* Sun May  4 2008 Dries Verachtert <dries@ulyssis.org> - 3.11.0-1 - 6690/cmr
- Updated to release 3.11.0.

* Sun May  4 2008 Dries Verachtert <dries@ulyssis.org> - 3.10.2-1
- Updated to release 3.10.2.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 3.10-1
- Updated to release 3.10.

* Wed Jan 04 2006 Dries Verachtert <dries@ulyssis.org> - 3.09.1-1
- Updated to release 3.09.1.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 3.08.4-1
- Updated to release 3.08.4.

* Tue Aug 09 2005 Dag Wieers <dag@wieers.com> - 3.08.3-2
- Cleanup and fixes to build on x86_64.
- Added subpackages and obsoletes for FE.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 3.08.3-1
- Update to release 3.08.3.

* Thu Mar 03 2005 Dries Verachtert <dries@ulyssis.org> - 3.08.2-2
- Added the documentation, thanks to David Aspinall for informing me
  about the missing documentation.

* Thu Dec 09 2004 Dries Verachtert <dries@ulyssis.org> - 3.08.2
- Initial package.
