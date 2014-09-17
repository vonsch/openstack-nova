owner = gooddata
project = openstack-nova
commit = $(shell sed -n 's/%global release_number\s*//p' $(project).spec)

tarball:
	curl -Lf -s https://github.com/$(owner)/$(project)/archive/$(commit)/$(project)-$(commit).tar.gz > openstack-nova.tar.gz

clean:
	rm -f openstack-nova.tar.gz
