srpm:
	dnf -y install kernel-rpm-macros rpkg
	ls -lah .
	ls -lah $(spec)/
	ls -lah $(outdir)/
	tar -czf files.tar.gz Kbuild main.c
	cp files.tar.gz $(outdir)
	cp Kbuild $(outdir)/
	cp main.c $(outdir)/
	rpkg srpm --outdir=$(outdir)/ --spec=$(spec)/hello.spec
