#
# spec file for package ocaml-camlzip (Version 1.04)
# this code base is under development
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:          ocaml-camlzip
%define upstreamname camlzip
Version:       1.05
Release:       1
License:       LGPL-2.1+
Summary:       OCaml ZIP interface
URL:           http://forge.ocamlcore.org/projects/camlzip/
Group:         Development/Libraries/Other
Source0:       http://forge.ocamlcore.org/projects/camlzip/%{upstreamname}-%{version}.tar.gz
Patch:         camlzip_nolocalldconf.patch
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: zlib-devel
Requires:      ocaml
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This OCaml library provides easy access to compressed files in ZIP
and GZIP format, as well as to Java JAR files. It provides functions
for reading from and writing to compressed files in these formats.

%package devel
Summary: Devel files for OCaml ZIP
Group:         Development/Libraries/Other
Requires: ocaml-camlzip = %{version}

%description devel
Development file for the OCaml ZIP interface

%prep
%setup -q -n %{upstreamname}-%{version}
%patch

%build
%{__make} ZLIB_LIBDIR=%{_libdir} ZLIB_INCLUDE=%{_includedir} INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/zip
%{__make} allopt ZLIB_LIBDIR=%{_libdir} ZLIB_INCLUDE=%{_includedir} INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/zip

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
%{__make} install-findlib INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/zip DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig %{_libdir}/ocaml/zip

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{_libdir}/ocaml/zip/META
%{_libdir}/ocaml/stublibs/dllcamlzip.so
%{_libdir}/ocaml/stublibs/dllcamlzip.so.owner
%{_libdir}/ocaml/zip/gzip.cmi
%{_libdir}/ocaml/zip/zlib.cmi
%{_libdir}/ocaml/zip/zip.cma
%{_libdir}/ocaml/zip/zip.cmi
%dir %{_libdir}/ocaml/zip

%files devel
%defattr(-,root,root,-)
%{_libdir}/ocaml/zip/libcamlzip.a
%{_libdir}/ocaml/zip/gzip.mli
%{_libdir}/ocaml/zip/zlib.mli
%{_libdir}/ocaml/zip/zip.a
%{_libdir}/ocaml/zip/zip.cmxa
%{_libdir}/ocaml/zip/zip.mli


%changelog
* Mon Nov 18 2013 jonathan.ludlam@eu.citrix.com
- New upstream release
- Upstream contains META files, so remove the related patches
* Thu May 31 2012 rschweikert@suse.com
- Add META file to make package ocaml-findlib friendly
- Fixup Makefile
* Tue May 22 2012 rschweikert@suse.com
- Initial build
