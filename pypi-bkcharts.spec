#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-bkcharts
Version  : 0.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/8f/bf/f4975a10ce859da55e17c16fff45159f224344a6220e79c528ab288d0720/bkcharts-0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/8f/bf/f4975a10ce859da55e17c16fff45159f224344a6220e79c528ab288d0720/bkcharts-0.2.tar.gz
Summary  : High level chart types built on top of Bokeh
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-bkcharts-license = %{version}-%{release}
Requires: pypi-bkcharts-python = %{version}-%{release}
Requires: pypi-bkcharts-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
BuildRequires : pypi(six)

%description
No detailed description available

%package license
Summary: license components for the pypi-bkcharts package.
Group: Default

%description license
license components for the pypi-bkcharts package.


%package python
Summary: python components for the pypi-bkcharts package.
Group: Default
Requires: pypi-bkcharts-python3 = %{version}-%{release}

%description python
python components for the pypi-bkcharts package.


%package python3
Summary: python3 components for the pypi-bkcharts package.
Group: Default
Requires: python3-core
Provides: pypi(bkcharts)
Requires: pypi(numpy)
Requires: pypi(six)

%description python3
python3 components for the pypi-bkcharts package.


%prep
%setup -q -n bkcharts-0.2
cd %{_builddir}/bkcharts-0.2
pushd ..
cp -a bkcharts-0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361398
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bkcharts
cp %{_builddir}/bkcharts-0.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-bkcharts/6b22af92424fc948d99a21b8a99a5306fe67ce1b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bkcharts/6b22af92424fc948d99a21b8a99a5306fe67ce1b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
