%define debug_package %{nil}

Name:           ocaml-gnt
Version:        1.0.0
Release:        2%{?dist}
Summary:        OCaml bindings for userspace Xen grant table controls
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/ocaml-gnt/
Source0:        https://github.com/xapi-project/ocaml-gnt/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  xen-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-dom0-libs
Requires:       ocaml
Requires:       ocaml-findlib
Requires:       xen-dom0-libs

%description
These APIs allow programs running in userspace to share memory with other
domains on the same host. This can be used to (for example) implement disk
or network backends.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-io-page-devel
Requires:       xen-devel
Requires:       xen-dom0-libs-devel
Requires:       xen-dom0-libs

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
ocaml setup.ml -install

%files
%doc LICENSE
%doc ChangeLog README.md
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
* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.0-2
- Remove dependency on xen-missing-headers

* Sat Apr 26 2014 David Scott <dave.scott@citrix.com> - 1.0.0-1
- Initial package
