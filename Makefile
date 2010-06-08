ifdef B_BASE
include $(B_BASE)/common.mk
include $(B_BASE)/rpmbuild.mk
REPO=$(call hg_loc,xen-dist-ocaml)
DIST=$(CARBON_DISTFILES)/ocaml
else
MY_OUTPUT_DIR ?= $(CURDIR)/output
MY_OBJ_DIR ?= $(CURDIR)/obj
REPO ?= $(CURDIR)

RPM_SPECSDIR?=/usr/src/redhat/SPECS
RPM_SRPMSDIR?=/usr/src/redhat/SRPMS
RPM_RPMSDIR?=/usr/src/redhat/RPMS
RPM_SOURCESDIR?=/usr/src/redhat/SOURCES
RPMBUILD?=rpmbuild

DIST?=/data

DOMAIN0_ARCH_OPTIMIZED?=i686

%/.dirstamp:
	@mkdir -p $*
	@touch $@
endif

COMPONENTS=ocaml findlib omake xmlm getopt type-conv
PREFIX=/opt/xensource
XEN_RELEASE?=unknown

OCAML_VERSION=3.11.0
FINDLIB_VERSION=1.1.2pl1
OMAKE_VERSION=0.9.8.5-3
XMLM_VERSION=1.0.2
GETOPT_VERSION=20040811
TYPECONV_VERSION=1.6.8

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

.PHONY: srpm
srpm:
	mkdir -p $(RPM_SRPMSDIR) $(RPM_SPECSDIR) $(RPM_SOURCESDIR) $(RPM_RPMSDIR)
	install -g root -o root {ocaml,findlib,omake,xmlm,getopt,type-conv}.spec $(RPM_SPECSDIR)
	cp $(DIST)/ocaml-${OCAML_VERSION}.tar.bz2 $(RPM_SOURCESDIR)/
	cp $(DIST)/findlib-${FINDLIB_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/omake-${OMAKE_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp patches/omake-no-sync $(RPM_SOURCESDIR)/
	cp patches/omake-stdin-stdout $(RPM_SOURCESDIR)/
	cp $(DIST)/xmlm-${XMLM_VERSION}.tbz $(RPM_SOURCESDIR)/
	cp $(DIST)/getopt-${GETOPT_VERSION}.tar.gz $(RPM_SOURCESDIR)/
	cp $(DIST)/type-conv-${TYPECONV_VERSION}.tar.bz2 $(RPM_SOURCESDIR)/
	$(RPMBUILD) -bs $(RPM_SPECSDIR)/ocaml.spec
	cp patches/xmlm-do-not-display-none-dtd-on-output $(RPM_SOURCESDIR)/
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/findlib.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/omake.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/xmlm.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/getopt.spec
	$(RPMBUILD) --nodeps -bs $(RPM_SPECSDIR)/type-conv.spec

$(MY_SOURCES)/MANIFEST: $(MY_SOURCES_DIRSTAMP)
	rm -f $@
	@for srpm in "$(/bin/ls -1 ${MY_OUTPUT_DIR})"; do \
		path=$(MY_OUTPUT_DIR)/SRPMS/${srpm}; \
		echo "$(${RPM} --qf "%{name}" -qp ${path}) $(${RPM} --qf "%{License}" -qp ${path}) ${path}" >>$@; \
	done


.PHONY: clean
clean::
	rm -rf *.rpm
