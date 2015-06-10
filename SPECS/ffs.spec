Name:           ffs
Version:        0.11
Release:        1%{?dist}
Summary:        Simple flat file storage manager for the xapi toolstack
License:        LGPL
URL:            https://github.com/xapi-project/ffs
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       redhat-lsb-core

%description
Simple flat file storage manager for the xapi toolstack.

%prep
%setup -q

%build

%install
DESTDIR=%{buildroot} SCRIPTDIR=%{_libexecdir}/xapi-storage-script/ PYTHONDIR=%{python_sitelib}/xapi make install

%files
%doc README.md LICENSE MAINTAINERS
%{_libexecdir}/xapi-storage-script/volume/org.xen.xcp.storage.ffs/*
%{_libexecdir}/xapi-storage-script/volume/org.xen.xcp.storage.btrfs/*
%{_libexecdir}/xapi-storage-script/datapath/raw+file/*
%{python_sitelib}/xapi/*.py*

%changelog
* Tue Jun 9 2015 David Scott <dave.scott@citrix.com> - 0.11-1
- Update to 0.11

* Thu Oct 2 2014 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Thu Oct 2 2014 David Scott <dave.scott@citrix.com> - 0.9.25-1
- Update to 0.9.25

* Thu Jan 16 2014 Euan Harris <euan.harris@citrix.com> - 0.9.24-1
- Update to 0.9.24, with VDI.clone fix

* Thu Oct 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.23-1
- Update to 0.9.23, with VDI.copy fix

* Wed Oct 30 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.22, with VDI.clone and VDI.snapshot fixes

* Mon Oct 28 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.21, with minimal storage motion support

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.20
- Detect a parallel install of blktap and use that

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.18

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.17

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.4

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

