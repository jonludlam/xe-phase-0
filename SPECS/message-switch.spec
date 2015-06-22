Name:           message-switch
Version:        0.11.0
Release:        3%{?dist}
Summary:        A store and forward message switch
License:        FreeBSD
URL:            https://github.com/djs55/message-switch
Source0:        https://github.com/djs55/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        message-switch-init
Source2:        message-switch-conf
Patch0:         message-switch-7a385e7487d2d7a4fd8731891a3b93c8f8ca7382.patch
Patch1:         message-switch-785f2fdeaaa71aabc5cd4769bf89be73c20195f0
Patch2:         message-switch-0229af6a9880c7ae1461ae2315490b22e60f9842
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires: ocaml-cohttp-devel
BuildRequires: ocaml-rpc-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-rpc-devel
BuildRequires: ocaml-async-devel
BuildRequires: ocaml-shared-block-ring-devel
BuildRequires: ocaml-mtime-devel
# Not available in the build chroot
#Requires:      redhat-lsb-core
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts

%description
A store and forward message switch for OCaml.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp %{SOURCE1} message-switch-init
cp %{SOURCE2} message-switch-conf

%build
ocaml setup.ml -configure
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install
mkdir -p %{buildroot}/%{_sbindir}
install switch_main.native %{buildroot}/%{_sbindir}/message-switch
install main.native %{buildroot}/%{_sbindir}/message-cli
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 0755 message-switch-init %{buildroot}%{_sysconfdir}/init.d/message-switch
install -m 0644 message-switch-conf %{buildroot}/etc/message-switch.conf

%files
%{_sbindir}/message-switch
%{_sbindir}/message-cli
%{_sysconfdir}/init.d/message-switch
%config(noreplace) /etc/message-switch.conf

%post
/sbin/chkconfig --add message-switch

%preun
if [ $1 -eq 0 ]; then
  /sbin/service message-switch stop > /dev/null 2>&1
  /sbin/chkconfig --del message-switch
fi

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cohttp-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-rpc-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE README.md CHANGES
%{_libdir}/ocaml/message_switch/*

%changelog
* Mon Jun 15 2015 David Scott <dave.scott@citrix.com> - 0.11.0-3
- Add blocking fix.

* Fri Jun 12 2015 David Scott <dave.scott@citrix.com> - 0.11.0-2
- Add tail-recursion fix

* Thu Apr 23 2015 David Scott <dave.scott@citrix.com> - 0.11.0-1
- Update to 0.11.0

* Sun Apr 19 2015 David Scott <dave.scott@citrix.com> - 0.10.5.1-2
- Fix for bug exposed by cohttp upgrade

* Thu Apr  2 2015 David Scott <dave.scott@citrix.com> - 0.10.5.1-1
- Update to 0.10.5.1

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 0.10.4-1
- Update to 0.10.4, enable core/async

* Thu Jun 19 2014 David Scott <dave.scott@citrix.com> - 0.10.3-1
- Update to 0.10.3

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.10.2-1
- Update to 0.10.2

* Fri Oct 18 2013 David Scott <dave.scott@eu.citrix.com> - 0.10.1-1
- Update to 0.10.1 which is more tolerant of startup orderings

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

