srpm:
	dnf -y install kernel-rpm-macros rpkg
	ls -lah .
	ls -lah $(spec)/
	ls -lah $(outdir)/
	cp Kbuild $(outdir)/
	cp main.c $(outdir)/
	rpkg srpm --outdir=$(outdir)/ --spec=$(spec)/hello.spec
