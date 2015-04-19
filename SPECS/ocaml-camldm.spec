Name:           ocaml-camldm
Version:        0.9.1
Release:        1%{?dist}
Summary:        OCaml bindings to device mapper
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            http://github.com/xapi-project/camldm
Source0:        https://github.com/xapi-project/camldm/archive/v%{version}/camldm-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpc-devel
BuildRequires:  device-mapper
BuildRequires:  device-mapper-devel
BuildRequires:  ocaml-camlp4-devel
Requires:       ocaml
Requires:       ocaml-findlib
Requires:       device-mapper

%description
OCaml bindings to libdevicemapper.
These are the userspace libraries that talk to the kernel 
device-mapper module

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n camldm-%{version}

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files
%doc ChangeLog README.md
%{_libdir}/ocaml/camldm
%exclude %{_libdir}/ocaml/camldm/*.a
%exclude %{_libdir}/ocaml/camldm/*.cmxa
%exclude %{_libdir}/ocaml/camldm/*.cmx
%exclude %{_libdir}/ocaml/camldm/*.mli
%{_libdir}/ocaml/stublibs/dllcamldm_stubs.so
%{_libdir}/ocaml/stublibs/dllcamldm_stubs.so.owner

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/camldm/*.a
%{_libdir}/ocaml/camldm/*.cmx
%{_libdir}/ocaml/camldm/camldm.cmxa
%{_libdir}/ocaml/camldm/camldm.mli




%changelog
* Sat Apr 18 2015 Jon Ludlam <jonathan.ludlam@citrix.com>
- Layout fixes

* Mon Nov 18 2013 Jon Ludlam <jonathan.ludlam@eu.citrix.com>
- Initial package

