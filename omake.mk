V=0.9.6.9
SUBV=1

SRC=$(OBJDIR)/omake-$(V)
PATCHES=omake-64bit-build-fixes omake-no-sync

$(EXTRACTED):
	cd $(OBJDIR) && tar -zxf $(DISTFILES)/omake-$(V)-$(SUBV).tar.gz
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
