ifdef B_BASE
include $(B_BASE)/common.mk
else
MY_OUTPUT_DIR ?= $(CURDIR)/output
MY_OBJ_DIR ?= $(CURDIR)/obj
CARBON_DISTFILES ?= /usr/groups/linux/distfiles

%/.dirstamp:
	@mkdir -p $*
	@touch $@
endif

COMPONENTS=ocaml findlib annot omake xmlm getopt
PREFIX=/opt/xensource
REPO=$(call hg_loc,dist-ocaml)

.PHONY: build
build: $(MY_OUTPUT_DIR)/ocaml-libs.tar.gz $(MY_SOURCES)/MANIFEST
	@ :

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
		COMPONENT=$(1) \
		DISTFILES=$(CARBON_DISTFILES)/ocaml PREFIX=$(PREFIX) \
		BUILT=$$($(1)_BUILT) FAKED=$$($(1)_FAKED) PATCHED=$$($(1)_PATCHED) \
		EXTRACTED=$$($(1)_EXTRACTED) CONFIGURED=$$($(1)_CONFIGURED) \
		SOURCES=$$($(1)_SOURCES) $$*

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
