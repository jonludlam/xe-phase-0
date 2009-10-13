V=1.6.8

NAME=type-conv-$(V)
FILENAME=type-conv-release-$(V)
ARCHIVE=release-$(V).tar.bz2
PACKAGE=$(NAME).tar.bz2
URL=http://hg.ocaml.info/release/type-conv/archive/$(ARCHIVE)

SRC=$(OBJDIR)/$(FILENAME)

$(DOWNLOADED):
	echo $(SRC_DIR)
	@mkdir -p $(SRC_DIR)
	bash -c 'if [ ! -e $(SRC_DIR)/$(PACKAGE) ]; then if [ -e $(DISTFILES)/$(PACKAGE) ]; then cp $(DISTFILES)/$(PACKAGE) $(SRC_DIR); else wget $(URL) --output-document=$(SRC_DIR)/$(PACKAGE); fi; fi'
	@touch $@

$(EXTRACTED): $(DOWNLOADED)
	cd $(OBJDIR) && tar -jxf $(SRC_DIR)/$(PACKAGE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC)
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) PREFIX=$(DESTDIR)$(PREFIX) install
	@touch $@

$(SOURCES):
	echo ocaml gpl file $(DISTFILES)/$(PACKAGE) > $@

clean::
	rm -rf $(SRC)
