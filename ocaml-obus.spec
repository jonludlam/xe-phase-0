%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-obus
Version:        1.1.3
Release:        3%{?dist}
Summary:        OBus is a pure ocaml implementation of DBus. It aims to provide a clean and easy way for ocaml programmers to access and provide dbus services.

Group:          Development/Libraries
License:        BSD
URL:            http://forge.ocamlcore.org/projects/obus/
Source0:        http://forge.ocamlcore.org/frs/download.php/666/obus-1.1.3.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4


%description
OBus is a pure ocaml implementation of DBus. It aims to provide a clean and easy way for ocaml programmers to access and provide dbus services.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n obus-%{version}
ocaml setup.ml -configure --destdir $RPM_BUILD_ROOT --prefix /usr

%build
ocaml setup.ml -build
ocaml setup.ml -doc

%install
rm -rf $RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install

# Remove this, reinstall it properly with a %%doc rule below.
rm -rf $RPM_BUILD_ROOT/usr/local/share/doc


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/ocaml/obus
%if %opt
%exclude %{_libdir}/ocaml/obus/*.a
%exclude %{_libdir}/ocaml/obus/*.cmxa
%endif
%exclude %{_libdir}/ocaml/obus/*.mli


%files devel
%defattr(-,root,root,-)
%doc LICENSE README
%doc /usr/share/doc/obus/*
%doc /usr/share/man/man1/*
%if %opt
%{_libdir}/ocaml/obus/*.a
%{_libdir}/ocaml/obus/*.cmxa
%endif
%{_libdir}/ocaml/obus/*.mli
%{_bindir}/obus-dump
%{_bindir}/obus-gen-client
%{_bindir}/obus-gen-interface
%{_bindir}/obus-gen-server
%{_bindir}/obus-idl2xml
%{_bindir}/obus-introspect
%{_bindir}/obus-xml2idl

%changelog
