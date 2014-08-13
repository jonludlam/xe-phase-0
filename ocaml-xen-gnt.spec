%define debug_package %{nil}

Name:           ocaml-xen-gnt
Version:        1.0.2
Release:        1%{?extrarelease}
Summary:        OCaml bindings to the Xen grant tables libraries
License:        ISC
URL:            https://github.com/mirage/ocaml-gnt
Source0:        https://github.com/mirage/ocaml-gnt/archive/v%{version}/ocaml-gnt-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-findlib

%description
Xen grant table bindings for OCaml.

These are used to create Xen device driver "backends" (servers) and "frontends" (clients).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}
Requires:       ocaml-io-page-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-gnt-%{version}

%build
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
make

%install
rm -rf %{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/xen-gnt
%exclude %{_libdir}/ocaml/xen-gnt/*.a
%exclude %{_libdir}/ocaml/xen-gnt/*.cmxa
%exclude %{_libdir}/ocaml/xen-gnt/*.cmx
%exclude %{_libdir}/ocaml/xen-gnt/*.mli

%files devel
%{_libdir}/ocaml/xen-gnt/*.a
%{_libdir}/ocaml/xen-gnt/*.cmx
%{_libdir}/ocaml/xen-gnt/*.cmxa
%{_libdir}/ocaml/xen-gnt/*.mli

%changelog
* Wed Aug 13 2014 John Else <john.else@citrix.com> - 1.0.1-1
- Initial package
