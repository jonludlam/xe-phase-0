V=0.9.6.9
SUBV=1

PATCHES=omake-64bit-build-fixes omake-no-sync

NAME=omake-$(V)
PACKAGE=$(NAME)-$(SUBV).tar.gz
URL=http://omake.metaprl.org/downloads/$(PACKAGE)

SRC=$(OBJDIR)/$(NAME)

$(DOWNLOADED):
	echo $(SRC_DIR)
	@mkdir -p $(SRC_DIR)
	bash -c 'if [ ! -e $(SRC_DIR)/$(PACKAGE) ]; then if [ -e $(DISTFILES)/$(PACKAGE) ]; then cp $(DISTFILES)/$(PACKAGE) $(SRC_DIR); else wget $(URL) --output-document=$(SRC_DIR)/$(PACKAGE); fi; fi'
	@touch $@

$(EXTRACTED): $(DOWNLOADED)
	cd $(OBJDIR) && tar -zxf $(SRC_DIR)/$(PACKAGE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	# this will fail because of bad dependencies
	-$(MAKE) -C $(SRC) PREFIX=$(PREFIX) boot
	rm -f $(SRC)/boot/Makefile.dep
	$(MAKE) -C $(SRC)/boot Makefile.dep
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) PREFIX=$(PREFIX) all
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) PREFIX=$(DESTDIR)$(PREFIX) install
	@touch $@

$(SOURCES):
	@touch $@

clean::
	rm -rf $(SRC)
