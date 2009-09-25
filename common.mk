.PHONY: extract
extract: $(EXTRACTED)
	@ : 

.PHONY: patch
patch: $(PATCHED)
	@ :

$(PATCHED): $(EXTRACTED)
	cd $(SRC) && for i in $(PATCHES); do \
	  patch -b -p1 < $(CURDIR)/patches/$$i; \
	done
	@touch $@

.PHONY: configure
configure: $(CONFIGURED)
	@ :

.PHONY: build
build: $(BUILT)
	@ :

.PHONY: fake
fake: $(FAKED) $(SOURCES)
	@ :

.PHONY: all
all: $(FAKED)
	@ :

.PHONY: clean
clean::
	rm -f $(EXTRACTED) $(BUILT) $(CONFIGURED) $(FAKED) $(PATCHED)

.PHONY: patchlist
patchlist:
	@echo $(PATCHES)
