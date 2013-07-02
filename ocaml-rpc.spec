Name:           ocaml-rpc
Version:        1.4.1
Release:        0
Summary:        An RPC library for OCaml
License:        LGPL
Group:          Development/Other
URL:            https://github.com/samoht/ocaml-rpc/archive/1.4.1.tar.gz
Source0:        ocaml-rpc-1.4.1.tar.gz
Patch0:         ocaml-rpc-1-remove-js_of_ocaml-dep
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-type-conv ocaml-xmlm-devel ocaml-camlp4-devel
Requires:       ocaml ocaml-findlib ocaml-type-conv ocaml-camlp4-devel

%description
An RPC library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-rpc-%{version}
%patch0 -p1 -b ~ocaml-rpc-1-remove-js_of_ocaml-dep

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc README.md
%{_libdir}/ocaml/rpclib/*

%changelog
* Fri Jun 28 2013 Si Beaumont <simon.beaumont@ctirix.com>
- Patch out js_of_ocaml bits for XenServer build env

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

