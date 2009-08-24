V=3.11.0

NAME=ocaml-$(V)
PACKAGE=$(NAME).tar.bz2
URL=http://caml.inria.fr/pub/distrib/ocaml-3.11/$(PACKAGE)

SRC=$(OBJDIR)/$(NAME)

$(DOWNLOADED):
	echo $(SRC_DIR)
	@mkdir -p $(SRC_DIR)
	bash -c 'if [ ! -e $(SRC_DIR)/$(PACKAGE) ]; then if [ -e $(DISTFILES)/$(PACKAGE) ]; then cp $(DISTFILES)/$(PACKAGE) $(SRC_DIR); else wget $(URL) --output-document=$(SRC_DIR)/$(PACKAGE); fi; fi'
	@touch $@

$(EXTRACTED): $(DOWNLOADED)
	cd $(OBJDIR) && tar -jxf $(SRC_DIR)/$(PACKAGE)
	@touch $@

$(CONFIGURED): $(PATCHED)
	cd $(SRC) && ./configure -prefix $(PREFIX)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) world.opt
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) PREFIX=$(DESTDIR)$(PREFIX) install
	@touch $@

$(SOURCES):
	echo ocaml gpl file $(DISTFILES)$(PACKAGE) > $@

clean::
	rm -rf $(SRC)
