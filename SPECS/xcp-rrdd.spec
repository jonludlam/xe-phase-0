Name:           xcp-rrdd
Version:        0.10.0
Release:        1%{?dist}
Summary:        Statistics gathering daemon for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/xcp-rrdd
Source0:        https://github.com/xapi-project/xcp-rrdd/archive/v%{version}/xcp-rrdd-%{version}.tar.gz
Source1:        xcp-rrdd-init
Source2:	xcp-rrdd-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-oclock-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xcp-inventory-devel
BuildRequires:  ocaml-xenops-devel
BuildRequires:  ocaml-rrd-transport-devel
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  xen-ocaml-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  forkexecd-devel
BuildRequires:  xen-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-libs-devel
BuildRequires:  blktap-devel
#Requires:       redhat-lsb-core

%description
Statistics gathering daemon for the xapi toolstack.

%prep
%setup -q
cp %{SOURCE1} xcp-rrdd-init
cp %{SOURCE2} xcp-rrdd-conf

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
make install DESTDIR=%{buildroot} SBINDIR=%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xcp-rrdd-init %{buildroot}%{_sysconfdir}/init.d/xcp-rrdd
install -m 0644 xcp-rrdd-conf %{buildroot}/etc/xcp-rrdd.conf

%files
%doc README.markdown LICENSE
%{_sbindir}/xcp-rrdd
%{_sysconfdir}/init.d/xcp-rrdd
/etc/xcp-rrdd.conf

%post
/sbin/chkconfig --add xcp-rrdd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xcp-rrdd stop > /dev/null 2>&1
  /sbin/chkconfig --del xcp-rrdd
fi

%changelog
* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.7-2
- Remove xen-missing-headers dependency 

* Wed Jun 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.7-1
- Update to 0.9.7
- Create new subpackage for the devel libraries now installed

* Fri May  9 2014 David Scott <dave.scott@citrix.com> - 0.9.5-1
- Update to 0.9.5, now will start without xen

* Sat Apr 26 2014 David Scott <dave.scott@eu.citrix.com> - 0.9.4-1
- Update to 0.9.4, now depends on rrdd-transport

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

