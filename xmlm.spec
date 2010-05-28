Name:           ocaml-xmlm
Version:        1.0.2
Release:        %mkrel 1
Summary:        Streaming XML input/output for OCaml
License:        new-BSD
Group:          Development/Other
URL:            http://erratique.ch/software/xmlm
Source0:        http://erratique.ch/software/xmlm/releases/xmlm-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
Requires:       ocaml

%description
Xmlm is an OCaml module providing streaming XML input/output. It aims at
making XML processing robust and painless. The streaming interface can
process documents without building an in-memory representation. It lets
the programmer translate its data structures to XML documents and
vice-versa. Functions are provided to easily transform arborescent data
structures to/from XML documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xmlm-%{version}

%build
./build module
./build doc

%install
rm -rf %{buildroot}
export INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/xmlm
./build install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/ocaml/xmlm/META
%{_libdir}/ocaml/xmlm/xmlm.cmi
%{_libdir}/ocaml/xmlm/xmlm.cmo

%files devel
%defattr(-,root,root)
%doc test doc CHANGES
%{_libdir}/ocaml/xmlm/xmlm.cmx
%{_libdir}/ocaml/xmlm/xmlm.o
%{_libdir}/ocaml/xmlm/xmlm.mli
%{_libdir}/ocaml/xmlm/xmlm.ml



%changelog
* Wed Mar 17 2010 Florent Monnier <blue_prawn@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 522813
- update to new version 1.0.2

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-2mdv2010.0
+ Revision: 390087
- rebuild

* Thu Feb 19 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0.1-1mdv2009.1
+ Revision: 342935
- ocaml required to build
- * Thu Feb 19 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0.1-1mdv
- Initial RPM release (please care that the upstream doc tells this software is designed to be used included)


