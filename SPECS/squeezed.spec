Name:           squeezed
Version:        0.11.0
Release:        1%{?dist}
Summary:        Memory ballooning daemon for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/squeezed
Source0:        https://github.com/xapi-project/squeezed/archive/v%{version}/squeezed-%{version}.tar.gz
Source1:        squeezed-init
Source2:        squeezed-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  xen-ocaml-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  xen-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-dom0-libs
BuildRequires:  xen-libs-devel
BuildRequires:  xen-libs
#Requires:       redhat-lsb-core
Requires:       message-switch

%description
Memory ballooning daemon for the xapi toolstack.

%prep
%setup -q
cp %{SOURCE1} squeezed-init
cp %{SOURCE2} squeezed-conf

%build
./configure --prefix %{_prefix} --destdir %{buildroot}
make

%install
install -D -m 0755 squeezed.native %{buildroot}%{_sbindir}/squeezed
install -D -m 0755 squeezed-init %{buildroot}%{_sysconfdir}/init.d/squeezed
install -D -m 0644 squeezed-conf %{buildroot}%{_sysconfdir}/squeezed.conf


%files
%doc README.md 
%doc LICENSE 
%doc MAINTAINERS
%{_sbindir}/squeezed
%{_sysconfdir}/init.d/squeezed
%config %{_sysconfdir}/squeezed.conf

%post
/sbin/chkconfig --add squeezed

%preun
if [ $1 -eq 0 ]; then
  /sbin/service squeezed stop > /dev/null 2>&1
  /sbin/chkconfig --del squeezed
fi

%changelog
* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.10.6-2
- Remove dependency on xen-missing-headers

* Fri Jun  6 2014 Jonathan Ludlam <jonathan.ludlam@citrix.com> - 0.10.6-1
- Update to 0.10.6

* Fri Apr 11 2014 Euan Harris <euan.harris@citrix.com> - 0.10.5-1
- Switch build from obuild to oasis

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.4-1
- Update to 0.10.4

* Fri Sep 20 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.3-1
- Update to allow minimal operation without xen

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.2-1
- Update to new xenstore interface in v1.2.3

* Wed Sep 04 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.1-1
- Add get_domain_zero_palicy call required for domain 0 ballooning

* Mon Sep  2 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.0-1
- Update to 0.10.0, with support for domain 0 ballooning

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

