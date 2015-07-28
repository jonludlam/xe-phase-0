Name:           xenvm
Version:        0.2.0
Release:        2%{?dist}
Summary:        A compatible replace for LVM supporting thinly provisioned volumes
License:        LGPL
URL:            https://github.com/xapi-project/xenvm
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        refresh-demo
Source2:        resize-demo
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-block-unix-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-camldm-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-mirage-clock-unix-devel
BuildRequires:  ocaml-mirage-block-volume-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-shared-block-ring-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  device-mapper-devel
BuildRequires:  libffi-devel
BuildRequires:  oasis

%description
A compatible replacement for LVM supporting thinly provisioned volumes.

%prep
%setup -q -n xenvm-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
install xenvmd.native %{buildroot}/%{_sbindir}/xenvmd
mkdir -p %{buildroot}/%{_bindir}
install xenvm.native %{buildroot}/%{_bindir}/xenvm
install local_allocator.native %{buildroot}/%{_bindir}/xenvm-local-allocator
mkdir -p %{buildroot}/opt/xensource/sm
cp %{SOURCE1} %{buildroot}/opt/xensource/sm
cp %{SOURCE2} %{buildroot}/opt/xensource/sm
mkdir -p %{buildroot}/etc/xenvm.d
mkdir -p %{buildroot}/var/lib/xenvmd

%files
%doc README.md 
%{_sbindir}/xenvmd
%{_bindir}/xenvm
%{_bindir}/xenvm-local-allocator
/etc/xenvm.d
/opt/xensource/sm/refresh-demo
/opt/xensource/sm/resize-demo
/var/lib/xenvmd

%changelog
* Mon Jul 27 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.2.0-3
- Create /var/lib/xenvmd

* Fri May 15 2015 David Scott <dave.scott@citrix.com> - 0.2.0-2
- Create /etc/xenvm.d

* Tue Apr 28 2015 David Scott <dave.scott@citrix.com> - 0.2.0-1
- Update to 0.2.0-1

* Thu Apr 23 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.1.0-3
- Add local allocator

* Wed Apr 22 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.1.0-2
- Add xenvm CLI

* Mon Apr 20 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.1.0-1
- Initial package

