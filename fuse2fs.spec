Name: fuse2fs
Version: 1.46.5
Release: 1%{?dist}
Summary: FUSE file system client for ext2/ext3/ext4 file systems
License: GPLv2
Group: System Environment/Base
# download with:
# $ curl -o %{name}-%{version}.tar.gz \
#    https://codeload.github.com/tytso/e2fsprogs/tar.gz/v%{version}
Source0: %{name}-%{version}.tar.gz

BuildRequires: fuse-devel
BuildRequires: gcc

Requires: fuse-libs

%description
fuse2fs is a FUSE file system client for ext2/ext3/ext4 file systems.
It is a standard component in the e2fsprogs package but the version
of the package on RHEL7 is too old, so this packages just the fuse2fs
command from a more recent e2fsprogs.

%prep
%setup -q -n e2fsprogs-%{version}

%build
./configure
make %{?_smp_mflags}

%check
make SUBDIRS=misc fullcheck

%install
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_mandir}/man1
cp misc/%{name} %{buildroot}%{_sbindir}/
cp misc/%{name}.1 %{buildroot}%{_mandir}/man1

%files
%license NOTICE
%{!?_licensedir:%global license %%doc}
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Jul  6 2022 Dave Dykstra <dwd@fnal.gov> 1.46.5-1
- Build from upstream e2fsprogs-1.46.5
