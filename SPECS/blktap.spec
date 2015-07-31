Summary: blktap user space utilities
Name: blktap
Version: 3.0.0.xs1110
Release: xs6.6.80
License: GPLv2 or BSD
URL: https://github.com/xapi-project/blktap
Source0: %{name}-%{version}.tar.bz2
Patch1: %{name}-udev-ignore-tapdevs.patch
BuildRequires: e2fsprogs-devel
BuildRequires: libaio-devel
BuildRequires: libuuid-devel
BuildRequires: xen-devel
BuildRequires: kernel-headers
BuildRequires: xen-dom0-libs-devel
BuildRequires: xen-libs-devel

%description
Blktap creates kernel block devices which realize I/O requests to
processes implementing virtual hard disk images entirely in user
space.

Typical disk images may be implemented as files, in memory, or
stored on other hosts across the network. The image drivers included
with tapdisk can map disk I/O to sparse file images accessed through
Linux DIO/AIO and VHD images with snapshot functionality.

This packages includes the control utilities needed to create
destroy and manipulate devices ('tap-ctl'), the 'tapdisk' driver
program to perform tap devices I/O, and a number of image drivers.

%package devel
Summary: BlkTap Development Headers and Libraries
Requires: blktap = %{version}

%description devel
Blktap and VHD development files.

%prep
%setup -q
%patch1 -p1

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_localstatedir}/log/blktap

%files
%defattr(-,root,root,-)
%doc
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_bindir}/vhd-util
%{_bindir}/vhd-update
%{_bindir}/vhd-index
%{_bindir}/tapback
%{_sbindir}/lvm-util
%{_sbindir}/tap-ctl
%{_sbindir}/td-util
%{_sbindir}/td-rated
%{_sbindir}/part-util
%{_sbindir}/vhdpartx
%{_sbindir}/thinprovd
%{_sbindir}/thin-cli
%{_sbindir}/xlvhd-resize
%{_sbindir}/xlvhd-refresh
%{_libexecdir}/tapdisk
%{_sysconfdir}/udev/rules.d/blktap.rules
%{_sysconfdir}/rc.d/init.d/tapback
%{_sysconfdir}/logrotate.d/blktap
%{_sysconfdir}/xensource/bugtool/tapdisk-logs.xml
%{_sysconfdir}/xensource/bugtool/tapdisk-logs/description.xml
%{_sysconfdir}/rc.d/init.d/thinprovd
%{_localstatedir}/log/blktap

%files devel
%defattr(-,root,root,-)
%doc
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/vhd/*
%{_includedir}/blktap/*

%post
[ ! -x /sbin/chkconfig ] || chkconfig --add tapback
[ ! -x /sbin/chkconfig ] || chkconfig --add thinprovd

%changelog
* Mon Jul 27 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 3.0.0.xs1110-xs6.6.80
- Create /var/lib/xenvmd
