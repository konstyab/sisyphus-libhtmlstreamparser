Name: libhtmlstreamparser
Version: git.2016.12.04.19.31
Release: alt1

Summary: Simple, low memory usage, HTML stream parser library

License: GPLv3
Group: Text tools
Url: https://github.com/arjunc77/htmlstreamparser

Packager: Sample Maintainer <samplemaintainer@altlinux.org>
#BuildPreReq: 
Source: %name-%version.tar


%package doc
Summary: Documentation files for libhtmlstreamparser
Group: Text tools
BuildArch: noarch
Provides: libhtmlstreamparser-doc = %version-%release


%package -n libhtmlstreamparser-devel
Summary: Development files for libhtmlstreamparser
Group: Development/C
Requires: libhtmlstreamparser = %version-%release


%package -n libhtmlstreamparser-devel-static
Summary: Static library version for libhtmlstreamparser
Group: Development/C
Requires: libhtmlstreamparser = %version-%release
Requires: libhtmlstreamparser-devel = %version-%release


%description
It is simple, low memory usage, HTML stream parser library.
Originally written for embedded devices.
Parsing HTML stream char by char.
Not building HTML tree.
Supports invalid HTML code


%description -n libhtmlstreamparser-devel
Development files for libhtmlstreamparser

%description -n libhtmlstreamparser-devel-static
Static library version for libhtmlstreamparser

%description doc
Documentation files for libhtmlstreamparser


%prep
%setup

%build
%configure
make clean
make

%install
%makeinstall_std



%files doc
%doc AUTHORS ChangeLog COPYING INSTALL LICENSE NEWS README README.md


%files
%_libdir/libhtmlstreamparser.so.*


%files -n libhtmlstreamparser-devel
%_libdir/libhtmlstreamparser.so
%_includedir/htmlstreamparser.h

%files -n libhtmlstreamparser-devel-static
%_libdir/libhtmlstreamparser.a

%changelog
* Sun Dec 04 2016 Sample Maintainer <samplemaintainer@altlinux.org> git.2016.12.04.19.31-alt1
- initial build

