%define debug_package %{nil}

Name:           ocaml-rrdd-plugin
Version:        0.7.0
Release:        1%{?dist}
Summary:        Plugin library for the XenServer RRD daemon
License:        LGPL2.1 + OCaml linking exception
Group:          Development/Other
URL:            https://github.com/xapi-project/ocaml-rrdd-plugin/
Source0:        https://github.com/xapi-project/ocaml-rrdd-plugin/archive/v0.7.0/ocaml-rrdd-plugin-0.7.0.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-rrd-transport-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-ocamldoc

%description
Plugin library for the XenServer RRD daemon.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       forkexecd-devel%{?_isa}
Requires:       ocaml-stdext-devel%{?_isa}
Requires:       ocaml-xcp-idl-devel%{?_isa}
Requires:       ocaml-xcp-rrd-devel%{?_isa}
Requires:       ocaml-rrd-transport-devel%{?_isa}

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
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/ocaml/rrdd-plugin
%exclude %{_libdir}/ocaml/rrdd-plugin/*.a
%exclude %{_libdir}/ocaml/rrdd-plugin/*.cmx
%exclude %{_libdir}/ocaml/rrdd-plugin/*.cmxa
%exclude %{_libdir}/ocaml/rrdd-plugin/*.mli

%files devel
%defattr(-,root,root)
%doc ChangeLog
%doc README.md
%{_libdir}/ocaml/rrdd-plugin/*.a
%{_libdir}/ocaml/rrdd-plugin/*.cmx
%{_libdir}/ocaml/rrdd-plugin/*.cmxa
%{_libdir}/ocaml/rrdd-plugin/*.mli

%changelog
* Tue Jul 8 2014 John Else <john.else@citrix.com> - 0.5.0-1
- Initial package
