Name: suse-hello
Version: 0.0.0
Release: 0
Summary: Sample Kernel Module Package

Group: System/Kernel
License: GPL-2.0-only
Source0: main.c
Source1: Kbuild
#BuildRoot: %%{_tmppath}/%%{name}-%%{version}-build

BuildRequires: kernel-rpm-macros

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
* Tue Sep 12 2023 - Robert Joslyn <robert_joslyn@selinc.com> 0.0.0
- Initial spec file
