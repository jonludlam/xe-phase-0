Version:        0.9.1
Release:        1

%global debug_package %{nil}

Name:           ocaml-libvhd
Summary:        VHD manipulation via libvhd
License:        BSD3
URL:            https://github.com/xapi-project/libvhd
Source0:        https://github.com/xapi-project/libvhd/archive/libvhd-0.9.1.tar.gz
BuildRequires:  libuuid-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  xen-devel
BuildRequires:  blktap-devel

%description
Simple C bindings which allow .vhd files to be manipulated.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libuuid-devel%{?_isa}
Requires:       xen-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n libvhd-%{version}

%build
ocaml setup.ml -configure
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install

%files
%doc ChangeLog
%doc README.md
%{_libdir}/ocaml/vhdlib
%exclude %{_libdir}/ocaml/vhdlib/*.a
%exclude %{_libdir}/ocaml/vhdlib/*.cmxa
%exclude %{_libdir}/ocaml/vhdlib/*.cmx
%exclude %{_libdir}/ocaml/vhdlib/*.mli
%{_libdir}/ocaml/stublibs/dllvhdlib_stubs.so
%{_libdir}/ocaml/stublibs/dllvhdlib_stubs.so.owner

%files devel
%{_libdir}/ocaml/vhdlib/*.a
%{_libdir}/ocaml/vhdlib/*.cmx
%{_libdir}/ocaml/vhdlib/*.cmxa
%{_libdir}/ocaml/vhdlib/*.mli

%changelog
* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.1-3
- Remove dependency on xen-missing-headers

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.1-2
- Split files correctly between base and devel packages

* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Initial package

