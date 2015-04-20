include $(B_BASE)/common.mk

.PHONY: build buildrpms ocaml

DIST?=.el7.centos
MOCK=planex-cache --mock-exe /usr/bin/mock --cachedirs=/rpmcache
FETCH_EXTRA_FLAGS=--mirror file:///distfiles/ocaml2

ocaml: build

build: $(MY_SOURCES)/MANIFEST

buildrpms: rpms
	cp -r _build/RPMS $(MY_OUTPUT_DIR)
	rm -rf $(MY_OUTPUT_DIR)/RPMS/repodata
	cp -r _build/SRPMS $(MY_OUTPUT_DIR)

include /usr/share/planex/Makefile.rules

#### Build-system boilerplate below ####

$(MY_SOURCES)/MANIFEST: $(MY_SOURCES_DIRSTAMP) buildrpms
	@for i in $(shell /bin/ls -1 ${RPM_SRPMSDIR}); do \
		path=$(MY_OUTPUT_DIR)/SRPMS/$${i}; \
		echo -n "ocaml "; \
		$(RPM) --qf %{License} -qp $${path} | sed -e 's/ /_/g'; \
		echo " file $${path}"; \
	done > $@.tmp
	mv -f $@.tmp $@

.PHONY: clean
clean:
	rm -rf ./planex-build-root

