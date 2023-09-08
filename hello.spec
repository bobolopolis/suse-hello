# norootforbuild

Name: suse-hello
BuildRequires: gcc
BuildRequires: make
BuildRequires: elfutils-libelf-devel
BuildRequires: kmodtool
BuildRequires: kernel-rpm-macros

# Required to support secure-boot: Include sles-release in order to determine
# service-pack version
License: GPL-2.0-only
Group: System/Kernel
Summary: Sample Kernel Module Package
Version: 1.0
Release: 0
Source0: main.c
Source1: Kbuild
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%kernel_module_package

%description
This package contains the hello.ko module.

%prep
%setup
# Required to support secure-boot: Copy the signing key to the build area
%if 0%{?sle_version} > 112
cp %_sourcedir/signing_key.* .
21 Kernel Module Packages Manual
%endif
set -- *

mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %flavors_to_build; do
rm -rf obj/$flavor
cp -r source obj/$flavor
make -C %{kernel_source $flavor} modules M=$PWD/obj/$flavor
done

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
	# Required to support secure-boot: By default, kernel modules are not
	# signed by make. The CONFIG_MODULE_SIG_ALL=y setting overrides this for
	# flavors with module signing enabled.
	unset CONFIG_MODULE_SIG_ALL
	if grep '^CONFIG_MODULE_SIG=y' %{kernel_source $flavor}/.config; then
		export CONFIG_MODULE_SIG_ALL=y
	fi
	make -C %{kernel_source $flavor} modules_install M=$PWD/obj/$flavor
done

%changelog
* Fri Apr 27 2017 – andavis@suse.com
- Typo fixes; remove excluded flavors from kernel_module_package macro line
* Wed Apr 24 2013 - mmarek@suse.cz
- Sign the module by a supplied keypair.
* Tue Dec 22 2008 - andavis@suse.com
- Updated to reflect CODE 11 changes and LF standard spec file work.
* Sat Jan 28 2006 - agruen@suse.de
- Initial package.
