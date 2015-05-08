Name:           ocaml-pci
Version:        0.1.1
Release:        1%{?dist}
Summary:        OCaml bindings to libpci
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/simonjbeaumont/ocaml-pci
Source0:        https://github.com/simonjbeaumont/ocaml-pci/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libffi-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  pciutils-devel

%description
OCaml bindings to libpci.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libffi%{?_isa}
Requires:       ocaml-ctypes-devel%{?_isa}
Requires:       pciutils-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc README.md
%doc LICENSE
%{_libdir}/ocaml/pci
%{_libdir}/ocaml/stublibs/dllpci_stubs.so
%{_libdir}/ocaml/stublibs/dllpci_stubs.so.owner
%exclude %{_libdir}/ocaml/pci/*.a
%exclude %{_libdir}/ocaml/pci/*.cmxa
%exclude %{_libdir}/ocaml/pci/*.mli

%files devel
%{_libdir}/ocaml/pci/*.a
%{_libdir}/ocaml/pci/*.cmxa
%{_libdir}/ocaml/pci/*.mli

%changelog
* Fri May  8 2015 Si Beaumont <simon.beaumont@citrix.com> - 0.1.1-1
- Update to 0.1.1

* Fri May  1 2015 Si Beaumont <simon.beaumont@citrix.com> - 0.1.0-1
- Initial package
