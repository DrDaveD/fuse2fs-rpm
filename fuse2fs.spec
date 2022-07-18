Name: fuse2fs
Version: 1.46.5
Release: 6%{?dist}
Summary: FUSE file system client for ext2/ext3/ext4 file systems
# License explanation from the e2fsprogs NOTICE file:
#  This package, the EXT2 filesystem utilities, are made available under
#  the GNU Public License version 2, with the exception of the lib/ext2fs
#  and lib/e2p libraries, which are made available under the GNU Library
#  General Public License Version 2, the lib/uuid library which is made
#  available under a BSD-style license and the lib/et and lib/ss
#  libraries which are made available under an MIT-style license.  Please
#  see lib/uuid/COPYING for more details for the license for the files
#  comprising the libuuid library, and the source file headers of the
#  libet and libss libraries for more information.
License: GPLv2 and LGPLv2 and BSD and MIT
URL: http://e2fsprogs.sourceforge.net
Source0: https://github.com/tytso/e2fsprogs/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: fuse-devel
BuildRequires: gcc

%description
fuse2fs is a FUSE file system client for ext2/ext3/ext4 file systems.
It is a standard component in the e2fsprogs package but the version
of the package on RHEL7 is too old, so this packages just the fuse2fs
command from a more recent e2fsprogs.

%prep
%setup -q -n e2fsprogs-%{version}

%build
%configure
%make_build SUBDIRS=misc
cp -p lib/uuid/COPYING libuuid.COPYING

%check
%make_build SUBDIRS=misc fullcheck

%install
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_mandir}/man1
cp -p misc/%{name} %{buildroot}%{_sbindir}/
cp -p misc/%{name}.1 %{buildroot}%{_mandir}/man1

%files
%doc README
%{!?_licensedir:%global license %%doc}
%license NOTICE
%license libuuid.COPYING
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Jul 18 2022 Dave Dykstra <dwd@fnal.gov> 1.46.5-6
- Mark libuuid.COPYING as a license

* Fri Jul 15 2022 Dave Dykstra <dwd@fnal.gov> 1.46.5-5
- Add description of multiple licenses
- Remove Requires: fuse-libs
- Make use of percent in changelog use double percent

* Wed Jul 13 2022 Dave Dykstra <dwd@fnal.gov> 1.46.5-4
- Remove _smp_flags macro from make_build

* Tue Jul 12 2022 Dave Dykstra <dwd@fnal.gov> 1.46.5-3
- Add using %%make_build, overlooked from first round

* Tue Jul 12 2022 Dave Dykstra <dwd@fnal.gov> 1.46.5-2
- Respond to first round of review comments

* Wed Jul  6 2022 Dave Dykstra <dwd@fnal.gov> 1.46.5-1
- Build from upstream e2fsprogs-1.46.5
