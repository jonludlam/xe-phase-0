V=20040811

PATCHES=getopt-install

NAME=getopt-$(V)
PACKAGE=$(NAME).tar.gz
URL=http://www.eleves.ens.fr/home/frisch/info/$(PACKAGE)

SRC=$(OBJDIR)/$(NAME)

$(DOWNLOADED):
	echo $(SRC_DIR)
	@mkdir -p $(SRC_DIR)
	bash -c 'if [ ! -e $(SRC_DIR)/$(PACKAGE) ]; then if [ -e $(DISTFILES)/$(PACKAGE) ]; then cp $(DISTFILES)/$(PACKAGE) $(SRC_DIR); else wget $(URL) --output-document=$(SRC_DIR)/$(PACKAGE); fi; fi'
	@touch $@

$(EXTRACTED): $(DOWNLOADED)
	cd $(OBJDIR) && tar -zxf $(SRC_DIR)/$(PACKAGE)
	mv $(OBJDIR)/getopt $(OBJDIR)/$(NAME)
	@touch $@

$(CONFIGURED): $(PATCHED)
	@touch $@

$(BUILT): $(CONFIGURED)
	$(MAKE) -C $(SRC) all allopt
	@touch $@

$(FAKED): $(BUILT)
	$(MAKE) -C $(SRC) install
	@touch $@

$(SOURCES):
	echo ocaml gpl file $(DISTFILES)/$(PACKAGE) > $@
	
clean::
	rm -rf $(SRC)
