%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-text
Version:        0.5
Release:        3%{?dist}
Summary:        OCaml-Text is a library for dealing with ``text'', i.e. sequence of unicode characters, in a convenient way.

Group:          Development/Libraries
License:        BSD
URL:            http://forge.ocamlcore.org/projects/ocaml-text
Source0:        http://forge.ocamlcore.org/frs/download.php/641/ocaml-text-0.5.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4

%define _use_internal_dependency_generator 0


%description
OCaml-Text is a library for dealing with ``text'', i.e. sequence of
unicode characters, in a convenient way.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ocaml-text-%{version}
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
%{_libdir}/ocaml/text
%if %opt
%exclude %{_libdir}/ocaml/text/*.a
%exclude %{_libdir}/ocaml/text/*.cmxa
%endif
%exclude %{_libdir}/ocaml/text/*.mli


%files devel
%defattr(-,root,root,-)
%doc /usr/share/doc/ocaml-text/*
%if %opt
%{_libdir}/ocaml/text/*.a
%{_libdir}/ocaml/text/*.cmxa
%endif
%{_libdir}/ocaml/text/*.cma
%{_libdir}/ocaml/text/*.mli
%{_libdir}/ocaml/stublibs/dll*
%changelog
