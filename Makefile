ifdef B_BASE
include $(B_BASE)/common.mk
include $(B_BASE)/rpmbuild.mk
REPO=$(call hg_loc,xen-dist-ocaml)
DIST=$(CARBON_DISTFILES)/ocaml
else
MY_OUTPUT_DIR ?= $(CURDIR)/output
MY_OBJ_DIR ?= $(CURDIR)/obj
REPO ?= $(CURDIR)

RPM?=rpm
RPM_SPECSDIR?=$(shell rpm --eval='%_specdir')
RPM_SRPMSDIR?=$(shell rpm --eval='%_srcrpmdir')
RPM_RPMSDIR?=$(shell rpm --eval='%_rpmdir')
RPM_SOURCESDIR?=$(shell rpm --eval='%_sourcedir')
RPMBUILD?=rpmbuild

DIST?=/data

DOMAIN0_ARCH_OPTIMIZED?=i686

%/.dirstamp:
	@mkdir -p $*
	@touch $@
endif

COMPONENTS=ocaml findlib omake xmlm getopt type-conv ocaml-ounit
PREFIX=/opt/xensource
XEN_RELEASE?=unknown

OCAML_VERSION=3.12.1.ocamlspotter
FINDLIB_VERSION=1.2.6
OMAKE_VERSION=0.9.8.6-r13252
XMLM_VERSION=1.0.2
GETOPT_VERSION=20040811
TYPECONV_VERSION=3.0.1
OCAML_OUNIT_VERSION=1.1.0
LIBEV_VERSION=4.04
REACT_VERSION=0.9.2
LWT_VERSION=2.3.1
OBUS_VERSION=1.1.3
TEXT_VERSION=0.5
BITSTRING_VERSION=2.0.3

RPM_BINDIR=$(RPM_RPMSDIR)/$(DOMAIN0_ARCH_OPTIMIZED)

.PHONY: build
build: srpm $(MY_SOURCES)/MANIFEST
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/ocaml.spec
	$(RPM) -ihv $(RPM_BINDIR)/{ocaml-3*.rpm,ocaml-camlp4*.rpm} || echo ocaml is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/findlib.spec
	$(RPM) -ihv $(RPM_BINDIR)/ocaml-findlib*.rpm || echo ocaml-findlib is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/omake.spec
	$(RPM) -ihv $(RPM_BINDIR)/omake* || echo omake is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/xmlm.spec $(RPM_SPECSDIR)/getopt.spec $(RPM_SPECSDIR)/type-conv.spec
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-xmlm*.rpm || echo ocaml-xmlm is already installed
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-getopt*.rpm || echo ocaml-getopt is already installed
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-type-conv*.rpm || echo ocaml-type-conv is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/ocaml-ounit.spec
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-ounit-*.rpm || echo ocaml-ounit is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/libev.spec
	$(RPM) -ivh $(RPM_BINDIR)/libev*.rpm || echo libev is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/ocaml-react.spec
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-react*.rpm || echo ocaml-react is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/ocaml-text.spec
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-text*.rpm || echo ocaml-text is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/ocaml-lwt.spec
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-lwt*.rpm || echo ocaml-lwt is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/ocaml-obus.spec
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-obus*.rpm || echo ocaml-obus is already installed
	$(RPMBUILD) --target $(DOMAIN0_ARCH_OPTIMIZED) -bb $(RPM_SPECSDIR)/ocaml-bitstring.spec
	$(RPM) -ivh $(RPM_BINDIR)/ocaml-bitstring*.rpm || echo ocaml-bitstring is already installed

.PHONY: srpm
srpm:
	mkdir -p $(RPM_SRPMSDIR) $(RPM_SPECSDIR) $(RPM_SOURCESDIR) $(RPM_RPMSDIR)
	install {ocaml,findlib,omake,xmlm,getopt,type-conv,ocaml-ounit,libev,ocaml-react,ocaml-text,ocaml-lwt,ocaml-obus,ocaml-bitstring}.spec $(RPM_SPECSDIR)
	cp $(DIST)/ocaml-${OCAML_VERSION}.tar.bz2 $(RPM_SOURCESDIR)/
	cp $(DIST)/findlib-${FINDLIB_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/omake-${OMAKE_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/xmlm-${XMLM_VERSION}.tbz $(RPM_SOURCESDIR)/
	cp $(DIST)/getopt-${GETOPT_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/type-conv-${TYPECONV_VERSION}.tar.bz2 patches/type-conv-META.patch $(RPM_SOURCESDIR)/
	cp $(DIST)/ounit-${OCAML_OUNIT_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/libev-${LIBEV_VERSION}.tar.gz libev.pc.in $(RPM_SOURCESDIR)/
	cp $(DIST)/react-${REACT_VERSION}.tbz react-LICENSE $(RPM_SOURCESDIR)/
	cp $(DIST)/ocaml-text-${TEXT_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/lwt-${LWT_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/obus-${OBUS_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/ocaml-bitstring-${BITSTRING_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/ocaml.spec
	cp patches/xmlm-do-not-display-none-dtd-on-output $(RPM_SOURCESDIR)/
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/findlib.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/omake.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/xmlm.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/getopt.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/type-conv.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/ocaml-ounit.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/libev.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/ocaml-react.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/ocaml-text.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/ocaml-lwt.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/ocaml-obus.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/ocaml-bitstring.spec


$(MY_SOURCES)/MANIFEST: $(MY_SOURCES_DIRSTAMP)
	rm -f $@
	@for srpm in "$(/bin/ls -1 ${MY_OUTPUT_DIR})"; do \
		path=$(MY_OUTPUT_DIR)/SRPMS/${srpm}; \
		echo "$(${RPM} --qf "%{name}" -qp ${path}) $(${RPM} --qf "%{License}" -qp ${path}) ${path}" >>$@; \
	done


.PHONY: clean
clean::
	rm -rf $(RPM_SRPMSDIR) $(RPM_SPECSDIR) $(RPM_SOURCESDIR) $(RPM_RPMSDIR)
