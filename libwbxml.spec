%define major 1
%define libname %mklibname wbxml %{major}
%define develname %mklibname wbxml -d

Summary:	WBXML parser and compiler library
Name:		libwbxml
Version:	0.11.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libwbxml.opensync.org
Source0:	http://downloads.sourceforge.net/project/libwbxml/libwbxml/%{version}/%{name}-%{version}.tar.gz
Requires:	expat >= 2.0.1
BuildRequires:	cmake
BuildRequires:	expat-devel >= 2.0.1
BuildRequires:	popt-devel
BuildRequires:	zlib-devel

%description
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce bandwidth
in mobile communications. 

%package -n %{libname}
Group:		System/Libraries
License:	LGPLv2+
Summary:	Library for parsing WAP Binary XML
Obsoletes:  %mklibname wbxml2_ 0

%description -n %libname
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce bandwidth
in mobile communications. 

This package contains just the library for use by other applications.

%package -n %{develname}
Group:		Development/C
License:	LGPLv2+
Summary:	Library for developing applications that parse WAP Binary XML
Requires:	%{libname} = %{version}-%{release}
Provides:   wbxml-devel = %{version}-%{release}
Obsoletes:  %mklibname wbxml2_ -d 0

%description -n %{develname}
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce bandwidth
in mobile communications. 

This package contains the headers and other development files required to
compile applications that need to parse WBXML.

%prep
%setup -q

%build
%cmake
%make

%install
cd build
%makeinstall_std

%files
%doc ChangeLog AUTHORS
%{_bindir}/*

%files -n %libname
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README References TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libwbxml2.pc


%changelog
* Tue May 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.11.0-1
+ Revision: 797337
- version update 0.11.0

* Thu Feb 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.9-1
+ Revision: 638132
- 0.10.9

* Mon Aug 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.8-1mdv2011.0
+ Revision: 570417
- 0.10.8

* Tue May 19 2009 Oden Eriksson <oeriksson@mandriva.com> 0.10.7-1mdv2010.0
+ Revision: 377670
- 0.10.7

* Tue Mar 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.4-4mdv2009.1
+ Revision: 360802
- provides arch-independant devel virtual package

* Mon Mar 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.4-3mdv2009.1
+ Revision: 360760
- obsoletes previous lib package correctly also

* Mon Mar 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.4-2mdv2009.1
+ Revision: 360750
- obsoletes previous devel package correctly

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.4-1mdv2009.1
+ Revision: 358172
- package renaming
- package renaming
- new version
- new name
- drop all patches, merged
- drop static package

* Sun Jul 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.2-4mdv2009.0
+ Revision: 239109
- add patch from libsyncml team

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jun 30 2007 Emmanuel Andry <eandry@mandriva.org> 0.9.2-3mdv2008.0
+ Revision: 46180
- buildrequires automake
- add patches 0 and 1 from synce project

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.2-2mdv2008.0
+ Revision: 38636
- rebuild for expat
- spec file clean
- Import wbxml2

