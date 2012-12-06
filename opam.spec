Name:           ocaml-opam
Version:        0.8.2
Release:        1
Summary:        Objective CAML package manager

Group:          Development/Libraries
License:        GPLv3
URL:            http://opam.ocamlpro.com/
Source0:        https://github.com/OCamlPro/opam/archive/opam-%{version}.tar.gz
Source1:	https://gforge.inria.fr/frs/download.php/31543/cudf-0.6.3.tar.gz
Source2:	http://ocaml-extlib.googlecode.com/files/extlib-1.5.3.tar.gz
Source3:	https://gforge.inria.fr/frs/download.php/31595/dose3-3.1.2.tar.gz
Source4:	http://www.ocamlpro.com/pub/ocaml-arg.0.3.tar.gz
Source5:	http://ocamlgraph.lri.fr/download/ocamlgraph-1.8.1.tar.gz
Source6:	http://www.ocamlpro.com/pub/ocaml-re.1.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ocaml

%description
Objective CAML package manager.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n opam-%{version} -b 0
cp -p %SOURCE1 src_ext/
cp -p %SOURCE2 src_ext/
cp -p %SOURCE3 src_ext/
cp -p %SOURCE4 src_ext/
cp -p %SOURCE5 src_ext/
cp -p %SOURCE6 src_ext/

%build
ocamlc -version
ocamlc -where
./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/usr/lib/ocaml
mkdir -p $OCAMLFIND_DESTDIR
export DESTDIR=%{buildroot}
echo DESTDIR=$DESTDIR
make install 
make libinstall
mkdir -p $DESTDIR/usr/share/doc/ocaml-opam-%{version}
cp LICENSE $DESTDIR/usr/share/doc/ocaml-opam-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/opam-mk-repo
/usr/bin/opam
/usr/share/doc/ocaml-opam-0.8.2
/usr/share/doc/ocaml-opam-0.8.2/LICENSE
/usr/share/man/man1/opam-remote.1.gz
/usr/share/man/man1/opam-pin.1.gz
/usr/share/man/man1/opam-install.1.gz
/usr/share/man/man1/opam-update.1.gz
/usr/share/man/man1/opam-list.1.gz
/usr/share/man/man1/opam-info.1.gz
/usr/share/man/man1/opam-switch.1.gz
/usr/share/man/man1/opam-config.1.gz
/usr/share/man/man1/opam-init.1.gz
/usr/share/man/man1/opam-remove.1.gz
/usr/share/man/man1/opam-upgrade.1.gz
/usr/share/man/man1/opam-upload.1.gz
/usr/share/man/man1/opam-reinstall.1.gz
/usr/share/man/man1/opam-search.1.gz
/usr/share/man/man1/opam.1.gz

%files devel
/usr/lib/ocaml/opam/META
/usr/lib/ocaml/opam/opam-core.a
/usr/lib/ocaml/opam/opam-core.cma
/usr/lib/ocaml/opam/opam-core.cmxa
/usr/lib/ocaml/opam/opamCompiler.cmi
/usr/lib/ocaml/opam/opamFile.cmi
/usr/lib/ocaml/opam/opamFilename.cmi
/usr/lib/ocaml/opam/opamFormat.cmi
/usr/lib/ocaml/opam/opamFormula.cmi
/usr/lib/ocaml/opam/opamGlobals.cmi
/usr/lib/ocaml/opam/opamMisc.cmi
/usr/lib/ocaml/opam/opamPackage.cmi
/usr/lib/ocaml/opam/opamParallel.cmi
/usr/lib/ocaml/opam/opamPath.cmi
/usr/lib/ocaml/opam/opamProcess.cmi
/usr/lib/ocaml/opam/opamRepository.cmi
/usr/lib/ocaml/opam/opamRepositoryName.cmi
/usr/lib/ocaml/opam/opamSwitch.cmi
/usr/lib/ocaml/opam/opamSystem.cmi
/usr/lib/ocaml/opam/opamTypes.cmi
/usr/lib/ocaml/opam/opamVariable.cmi
/usr/lib/ocaml/opam/opamVersion.cmi

%changelog
* Tue Dec 4 2012 Jon Ludlam <jonathan.ludlam@eu.citrix.com>
- First release

