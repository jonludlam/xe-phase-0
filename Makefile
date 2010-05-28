ifdef B_BASE
include $(B_BASE)/common.mk
REPO=$(call hg_loc,xen-dist-ocaml)
else
MY_OUTPUT_DIR ?= $(CURDIR)/output
MY_OBJ_DIR ?= $(CURDIR)/obj
REPO ?= $(CURDIR)

RPM_SPECSDIR?=/usr/src/redhat/SPECS
RPM_SRPMSDIR?=/usr/src/redhat/SRPMS
RPM_SOURCEDIR?=/usr/src/redhat/SOURCES
XEN_RELEASE?=unknown

CARBON_DISTFILES ?= /data

%/.dirstamp:
	@mkdir -p $*
	@touch $@
endif

COMPONENTS=ocaml findlib omake xmlm getopt type-conv
PREFIX=/opt/xensource

.PHONY: build
build: $(MY_OUTPUT_DIR)/ocaml-libs.tar.gz $(MY_SOURCES)/MANIFEST
	@ :

OCAML_VERSION=3.11.0
FINDLIB_VERSION=1.1.2pl1
OMAKE_VERSION=0.9.8.5-3
XMLM_VERSION=1.0.2
GETOPT_VERSION=20040811

.PHONY: srpm
srpm:
	cp $(CARBON_DISTFILES)/ocaml-${OCAML_VERSION}.tar.bz2 $(RPM_SOURCEDIR)/
	cp $(CARBON_DISTFILES)/findlib-${FINDLIB_VERSION}.tar.gz $(RPM_SOURCEDIR)/
	cp $(CARBON_DISTFILES)/omake-${OMAKE_VERSION}.tar.gz $(RPM_SOURCEDIR)/
	cp patches/omake-no-sync $(RPM_SOURCEDIR)/
	cp $(CARBON_DISTFILES)/xmlm-${XMLM_VERSION}.tbz $(RPM_SOURCEDIR)/
	cp $(CARBON_DISTFILES)/getopt-${GETOPT_VERSION}.tar.gz $(RPM_SOURCEDIR)/
	rpmbuild -bs ocaml.spec
	cp patches/xmlm-do-not-display-none-dtd-on-output $(RPM_SOURCEDIR)/
	rpmbuild --nodeps -bs findlib.spec
	rpmbuild --nodeps -bs omake.spec
	rpmbuild --nodeps -bs xmlm.spec
	rpmbuild --nodeps -bs getopt.spec

$(MY_OUTPUT_DIR)/ocaml-libs.tar.gz: $(MY_OUTPUT_DIR)/.dirstamp
	$(MAKE) $(foreach c,$(COMPONENTS),install-$(c))
	rm -rf $(MY_OBJ_DIR)/restage
	mkdir $(MY_OBJ_DIR)/restage
	for i in $(COMPONENTS); do tar -C $(MY_OBJ_DIR)/restage \
	  -zxf $(MY_OUTPUT_DIR)/$$i.tar.gz; done
	tar -C $(MY_OBJ_DIR)/restage -zcf $@ .

$(MY_SOURCES)/MANIFEST: $(MY_SOURCES_DIRSTAMP) $(MY_OUTPUT_DIR)/ocaml-libs.tar.gz
	rm -f $@
	for i in $(COMPONENTS); do \
	  cat $(MY_OBJ_DIR)/$$i/.sources >> $@; done
	# assemble patch list
	$(call mkdir_clean,$(MY_OUTPUT_DIR)/patches)
	$(MAKE) --no-print-directory patchlist >> $@

define comp_template

$(1)_BUILT=$(MY_OBJ_DIR)/$(1)/.built
$(1)_DOWNLOADED=$(MY_OBJ_DIR)/$(1)/.downloaded
$(1)_EXTRACTED=$(MY_OBJ_DIR)/$(1)/.extracted
$(1)_CONFIGURED=$(MY_OBJ_DIR)/$(1)/.configured
$(1)_PATCHED=$(MY_OBJ_DIR)/$(1)/.patched
$(1)_FAKED=$(MY_OBJ_DIR)/$(1)/.faked
$(1)_SOURCES=$(MY_OBJ_DIR)/$(1)/.sources

.PHONY: $(1)-%
$(1)-%:
	@mkdir -p $(MY_OBJ_DIR)/$(1)
	@$(MAKE) -f $(1).mk MAKEFILES=common.mk OBJDIR=$(MY_OBJ_DIR)/$(1) \
		DESTDIR=$(MY_OBJ_DIR)/$(1)-staging \
		COMPONENT=$(1) SRC_DIR=$(CURDIR)/distfiles/$(1) \
		DISTFILES=$(CARBON_DISTFILES)/ocaml PREFIX=$(PREFIX) \
		BUILT=$$($(1)_BUILT) FAKED=$$($(1)_FAKED) PATCHED=$$($(1)_PATCHED) \
		DOWNLOADED=$$($(1)_DOWNLOADED) EXTRACTED=$$($(1)_EXTRACTED) CONFIGURED=$$($(1)_CONFIGURED) \
		SOURCES=$$($(1)_SOURCES) $$*

$(MY_OBJ_DIR)/$(1)/.downloaded:
	$(MAKE) $(1)-download
	@touch $$@

$(MY_OBJ_DIR)/$(1)/.built:
	rm -rf $(MY_OBJ_DIR)/$(1)
	mkdir -p $(MY_OBJ_DIR)/$(1)
	$(MAKE) $(1)-build
	@touch $$@

$(MY_OBJ_DIR)/$(1)/.faked:
	rm -rf $(MY_OBJ_DIR)/$(1)-staging
	mkdir -p $(MY_OBJ_DIR)/$(1)-staging
	$(MAKE) $(1)-fake
	@touch $$@

$(MY_OUTPUT_DIR)/$(1).tar.gz: $(MY_OBJ_DIR)/$(1)/.faked
	tar -C $(MY_OBJ_DIR)/$(1)-staging -zcf $$@ .

.PHONY: install-$(1)
install-$(1): $(MY_OUTPUT_DIR)/$(1).tar.gz
	tar -C / -zxf $$<

endef

$(foreach c,$(COMPONENTS),$(eval $(call comp_template,$(c))))

.PHONY: patchlist
patchlist:
	@$(call mkdir_clean,$(MY_OUTPUT_DIR)/patches)
	@mkdir -p $(MY_OUTPUT_DIR)/patches
	@for c in $(COMPONENTS); do \
	  for p in `$(MAKE) --no-print-directory $$c-patchlist`; do \
	    echo $$c gpl file $(MY_OUTPUT_DIR)/patches/$$p; \
	    cp $(REPO)/patches/$$p $(MY_OUTPUT_DIR)/patches/$$p; \
	  done; \
	done

.PHONY: clean
clean::
	rm -rf $(foreach c,$(COMPONENTS),$(MY_OBJ_DIR)/$(c) $(MY_OBJ_DIR)/$(c)-staging)
	mkdir -p $(foreach c,$(COMPONENTS),$(MY_OBJ_DIR)/$(c) $(MY_OBJ_DIR)/$(c)-staging)
	rm -f $(foreach c,$(COMPONENTS),$(MY_OUTPUT_DIR)/$(c).tar.gz)
	rm -rf $(MY_OBJ_DIR)/restage
	rm -f $(MY_OUTPUT_DIR)/ocaml-libs.tar.gz
